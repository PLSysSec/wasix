from difflib import HtmlDiff
from pathlib import Path
from datetime import date, datetime
import filecmp
import Config

from Template import report_template

def Check(dir):
  time = datetime.now()
  reports = []
  for test in Path(dir).iterdir():
    if test.is_dir():
      report = CheckOneTest(test, time)
      reports.append(report)
  return generateReport(reports, dir, time)

def genereateTable(errs):
  table = []

def generateReport(reports, dir, time):
  lines = []
  for report in reports:
    if len(report["htmls"]) == 0:
      pass
      lines.append('<dt class="wasix-clear">{}: clear</dt>'.format(report["name"]))
    else:
      lines.append('<dt class="wasix-error">{}</dt>'.format(report["name"]))

    for err in report["htmls"]:
      # lines.append('  <dd><a href="{}">{}</a></dd>'
      #   .format(err["path"], err["name"]))
      lines.append("<dd>{}</dd>".format(report["table"]))
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
  table = ["<table>"]

  for trace in dir.iterdir():
    if trace.suffix == ".trace":
      names.append(trace.stem.replace("{}_".format(test_name), ""))
      lines = Config.filter_output_before_checking(trace.open().readlines())
      traces.append((trace, lines))
  
  names.sort()
  traces.sort()

  print("names are: {}".format(names))
  table.append("  <tr>")
  table.append("    <th></th>")
  for name in names:
    table.append("    <th>{}</th>".format(name))
  table.append("    </tr>")  

  for i in range(len(traces)):
    table += [
      "  <tr>",
      "    <th>{}</th>".format(names[i]),
    ]
    for j in range(len(traces)):
      if j > i:
        t1, t1_lines = traces[i]
        t2, t2_lines = traces[j]
        if not check_lines(t1_lines, t2_lines):
          cmp_name = "{}_vs_{}".format(names[i], names[j])
          html_name = "{}_{}.html".format(cmp_name, int(datetime.timestamp(time)))
          full_path = "{}/{}".format(dir, html_name)
          rel_path = "{}/{}".format(test_name, html_name)
          f = open(full_path, "w")
          html = HtmlDiff().make_file(t1_lines, t2_lines)
          f.write(html)
          f.close()
          report["htmls"].append({
            "name": cmp_name,
            "path": rel_path 
          })
          table.append('    <td><a href="{}">Link</a></td>'.format(rel_path))
        else:
          table.append("    <td></td>")
      else:
        table.append("    <td></td>")
    table.append("  </tr>")
  table.append("</table>")
  report["table"] = "\n    ".join(table)
  return report

def check_lines(l1, l2):
  if len(l1) != len(l2): return False
  for i in range(len(l1)):
    if l1[i] != l2[i]: return False
  return True