import shutil
from pathlib import Path

class File:
  def __init__(self, name, size, flag = None, mod = None):
    self.name = name
    self.size = size
    self.flag = flag
    self.mod  = mod

class Dir:
  def __init__(self, path):
    pass

def PrepEnv(dir, name, config):
  pass

def CollectAfterRunInfo(dir, runtime, os, test_name, config, process):
  pass