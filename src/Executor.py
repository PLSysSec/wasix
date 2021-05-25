from pathlib import Path
import subprocess
import shutil

def Execute(test_dir, out_dir, runtimes, os, config):
  for test_name, test_path in get_all_tests(test_dir):
    for runtime in runtimes:
      run_one_test(out_dir, test_name, test_path, runtime, os, config)


def run_one_test(dir, test_name, test_path, runtime, os, config):
  working_dir = setup_environment(dir, test_name, config)
  print("Running {} with {}".format(test_name, runtime["name"]))

  accessible_dir = "."
  cmd = runtime["getCmds"](accessible_dir, test_path)
  p = None
  for cmd in runtime["getCmds"](accessible_dir, test_path):
    p = subprocess.run(cmd, cwd=working_dir,
      universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  collect_after_run_info(working_dir, runtime, os, test_name, config, p)
 

def setup_environment(dir, name, config):
  working_dir = Path("{}/{}".format(dir, name))
  working_dir.mkdir(parents=True, exist_ok=True)

  test_file_dir = Path("{}/test_files".format(Path(__file__).parent))
  working_test_file_dir = Path("{}/test_files".format(working_dir))
  working_test_file_dir.mkdir(parents=True, exist_ok=True)
  for tfile in test_file_dir.iterdir():
    if tfile.suffix == ".txt":
      shutil.copy2(str(tfile), working_test_file_dir)

  print("Prepared {}".format(str(working_dir)))
  return str(working_dir)

def collect_after_run_info(dir, runtime, os, test_name, config, process):
  old_trace = Path("{}/{}.trace".format(dir, test_name))
  if not old_trace.exists(): old_trace.touch()
  new_trace = Path("{}/{}_{}_{}.trace".format(dir, test_name, runtime["name"], os))
  trace = old_trace.rename(new_trace)

  f = open(trace, "a")
  f.write(sep_line("After Run Info"))
  collect_proc_info(config, process, f)
  collect_test_files(config, dir, f)
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

def collect_test_files(config, dir, f):
  f.write(sep_line("test files"))
  tf_dir = Path("{}/test_files".format(dir))
  for file in tf_dir.iterdir():
    if file.is_file():
      stat = file.stat()
      f.write("{}:\n".format(file.name))
      f.write("st_size: {}\n".format(stat.st_size))
      if config["single_os"]:
        f.write("st_mode: {}\n".format(stat.st_mode))
        f.write("st_nlink: {}\n".format(stat.st_nlink))
        f.write("st_uid: {}\n".format(stat.st_uid))
        f.write("st_gid: {}\n".format(stat.st_gid))

def get_all_tests(test_dir):
  names = []
  paths = []
  for child in Path(test_dir).iterdir():
    if(child.suffix == ".wasm"):
      names.append(child.stem)
      paths.append(str(child))
  return zip(names, paths)

def sep_line(s):
  return "********************** {} **********************\n".format(s)
