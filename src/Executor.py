from pathlib import Path
import subprocess

def GetAllTests(test_dir):
  names = []
  paths = []
  for child in Path(test_dir).iterdir():
    if(child.suffix == ".wasm"):
      names.append(child.stem)
      paths.append(str(child))
  return zip(names, paths) 

def Before(dir, name, config):
  working_dir = Path("{}/{}".format(dir, name))
  working_dir.mkdir(parents=True, exist_ok=True)

  print("Prepared {}".format(str(working_dir)))
  return str(working_dir)

def After(dir, runtime, os, name, process):
  old_trace = Path("{}/{}.trace".format(dir, name))
  if not old_trace.exists(): old_trace.touch()
  new_trace = Path("{}/{}_{}_{}.trace".format(dir, name, runtime, os))
  trace = old_trace.rename(new_trace)

  print("Generated {}".format(trace.name))

def RunOneTest(dir, name, test, runtime, os, config):
  working_dir = Before(dir, name, config)
  permission = "--dir=."
  print("Running {} with {}".format(name, runtime))
  p = subprocess.run([runtime, test, permission], cwd=working_dir,
    universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  After(working_dir, runtime, os, name, p)


def Execute(test_dir, out_dir, runtimes, os, config):
  for name, test in GetAllTests(test_dir):
    for runtime in runtimes:
      RunOneTest(out_dir, name, test, runtime, os, config)
