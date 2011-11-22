import os
from os.path import exists
from shutil import copy2 as copy

TARGET = 'nroonga_bindings'
TARGET_FILE = '%s.node' % TARGET
built = 'build/Release/%s' % TARGET_FILE
dest = 'lib/%s' % TARGET_FILE

def set_options(opt):
  opt.tool_options("compiler_cxx")

def configure(conf):
  conf.check_tool("compiler_cxx")
  conf.check_tool("node_addon")
  conf.check(lib='groonga', libpath=['/usr/lib', '/usr/local/lib'])

def build(bld):
  obj = bld.new_task_gen("cxx", "shlib", "node_addon")
  obj.cxxflags = ["-g", "-D_FILE_OFFSET_BITS=64", "-D_LARGEFILE_SOURCE", "-Wall"]
  obj.target = "nroonga_bindings"
  obj.source = "src/nroonga.cc"
  obj.uselib = ["GROONGA"]

  os.system('coffee -o lib/ -c src/')

def shutdown():
  if exists(built):
    copy(built, dest)
