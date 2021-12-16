class importer:
  def __init__(module, file, name):
    module.path = module.os_path()
    module.system = module.sys_path()
    module.file = file
    module.name = name

  def os_path(module):
    import os
    current_dir = os.getcwd()
    up = os.path.dirname(current_dir)
    utilspath = os.path.dirname(up)
    return utilspath

  def sys_path(module):
    import sys
    sys.path.append(module.path)
    return sys.path

  def get_statement(module):
    statement = f'from utilities.{module.file} import {module.name}'
    return statement
