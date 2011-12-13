srcdir = '.'
blddir = 'build'
VERSION = '0.3.5'

def set_options(opt):
  opt.tool_options('compiler_cxx')

def configure(conf):
  conf.check_tool('compiler_cxx')
  conf.check_tool('node_addon')
  conf.env.append_value('CCFLAGS', ['-Ofast'])
  conf.env.append_value('CXXFLAGS', ['-Ofast'])
  
def build(bld):
  obj = bld.new_task_gen('cxx', 'shlib', 'node_addon')
  obj.target = 'validation'
  obj.source = 'src/validation.cc'
  obj2 = bld.new_task_gen('cxx', 'shlib', 'node_addon')
  obj2.target = 'bufferutil'
  obj2.source = 'src/bufferutil.cc'
