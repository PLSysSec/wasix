from difflib import HtmlDiff
from pathlib import Path
from datetime import date, datetime
import filecmp

from Template import report_template

def Check(dir):
  time = datetime.now()
  reports = []
  for test in Path(dir).iterdir():
    if test.is_dir():
      report = CheckOneTest(test, time)
      reports.append(report)
  return generateReport(reports, dir, time)

def generateReport(reports, dir, time):
  lines = []
  for report in reports:
    if len(report["htmls"]) == 0:
      pass
      lines.append('<dt class="wasix-clear">{}: clear</dt>'.format(report["name"]))
    else:
      lines.append('<dt class="wasix-error">{}</dt>'.format(report["name"]))

    for err in report["htmls"]:
      lines.append('  <dd><a href="{}">{}</a></dd>'
        .format(err["path"], err["name"]))
  html = report_template.format(str(time), "\n  ".join(lines))
  fn = "{}/report_{}.html".format(dir, int(datetime.timestamp(time)))
  f = open(fn, "w")
  f.write(html)
  f.close()
  return fn

def CheckOneTest(dir, time):
  print("  Checking {}".format(dir))
  test_name = dir.stem
  names  = []
  traces = []
  report = {
    "name": test_name,
    "htmls": []
  }

  for trace in dir.iterdir():
    if trace.suffix == ".trace":
      names.append(trace.stem.replace("{}_".format(test_name), ""))
      traces.append(trace)

  for i in range(len(traces)):
    for j in range(i, len(traces)):
      if i != j:
        t1 = traces[i]
        t2 = traces[j]
        if not filecmp.cmp(t1, t2, shallow=False):
          cmp_name = "{}_vs_{}".format(names[i], names[j])
          html_name = "{}/{}_{}.html".format(
            dir, cmp_name, int(datetime.timestamp(time)))
          f = open(html_name, "w")
          html = HtmlDiff().make_file(t1.open().readlines(), t2.open().readlines())
          f.write(html)
          f.close()
          report["htmls"].append({
            "name": cmp_name,
            "path": html_name
          })
  return report
