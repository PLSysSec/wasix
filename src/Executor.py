from pathlib import Path
import Config
import subprocess
import shutil
import time
from os import stat

def Execute(test_dir, out_dir, runtimes, os, config):
  for test_name, test_path in get_all_tests(test_dir):
    for runtime in runtimes:
      run_one_test(out_dir, test_name, test_path, runtime, os, config)


def run_one_test(dir, test_name, test_path, runtime, os, config):
  start_CPU_time = time.time()
  test_dir, working_dir = setup_environment(dir, test_name, config)
  print("Running {} with {}".format(test_name, runtime["name"]))

  accessible_dir = "."
  cmd = runtime["getCmds"](accessible_dir, test_path)
  p = None
  for cmd in runtime["getCmds"](accessible_dir, test_path):
    p = subprocess.run(cmd, cwd=working_dir,
      universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("test_path is: " + test_path)
    print("cwd is : " + working_dir)
    print("cmd is : " + " ".join(cmd))
    print("stdout is:")
    print(p.stdout)
    print("stderr is:")
    print(p.stderr)
    print("stderr end")
  collect_after_run_info(test_dir, working_dir, runtime, os, test_name, config, p, start_CPU_time)
  

def setup_environment(dir, name, config):
  test_dir = Path("{}/{}".format(dir, name))
  test_dir.mkdir(parents=True, exist_ok=True)

  working_dir = Path("{}/{}".format(test_dir, "tmp"))
  working_dir.mkdir(parents=True, exist_ok=True)
  clean_dir(working_dir)

  Config.prep_env(working_dir)
  return (str(test_dir), str(working_dir))

def clean_dir(d):
  for p in d.iterdir():
    if p.is_file():
      p.unlink()
    elif p.is_dir():
      clean_dir(p)
      p.rmdir()

def collect_after_run_info(test_dir, working_dir, runtime, os, test_name, config, process, start_CPU_time):
  old_trace = Path("{}/{}.trace".format(working_dir, test_name))
  if not old_trace.exists():
    print("!!! {} was not generated by {}".format(old_trace, runtime["name"]))
    print("Creating old_trace with stderr")
    old_trace.touch()
    f = open(old_trace, "w")
    f.write(process.stderr)
  else:
    s = stat(old_trace)
    print("{} was generated by {}".format(old_trace, runtime["name"]))
    print("Permission for it is: {}".format(s.st_mode))

  new_trace = Path("{}/{}_{}_{}.trace".format(test_dir, test_name, runtime["name"], os))
  trace = old_trace.rename(new_trace)

  f = open(trace, "a")
  f.write(sep_line("After Run Info"))
  Config.process_output(process)
  collect_proc_info(config, process, f)
  f.write(sep_line("Custom Info"))
  custom_info = Config.collect_info(working_dir)
  f.write(custom_info)
  # end_CPU_time = time.time()
  # f.write("$Time(CPU seconds):%f\r\n" % (end_CPU_time - start_CPU_time))
  f.close()

  print("Generated {}".format(trace.name))


def collect_proc_info(config, p, f):
  f.write("return code: {}\n".format(p.returncode))
  if config["stdout"]:
    f.write(sep_line("std out"))
    f.write(p.stdout)
  if config["stderr"]:
    f.write(sep_line("std err"))
    f.write(p.stderr)

def get_all_tests(test_dir):
  names = []
  paths = []
  for child in Path(test_dir).iterdir():
    if(child.suffix == ".wasm" and "veri" not in str(child)):
      names.append(child.stem)
      paths.append(str(child))
  return zip(names, paths)

def sep_line(s):
  return "********************** {} **********************\n".format(s)
