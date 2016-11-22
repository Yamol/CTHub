import ast
from distutils.core import setup
from setuptools import setup, find_packages

def get_version(fname):
    with open(fname) as f:
        source = f.read()
    module = ast.parse(source)
    for e in module.body:
        if isinstance(e, ast.Assign) and \
                len(e.targets) == 1 and \
                e.targets[0].id == '__version__' and \
                isinstance(e.value, ast.Str):
            return e.value.s
    raise RuntimeError('__version__ not found')

setup(name = 'CTHub',  
      version = get_version('CTHub/CTHub'),
      keywords = 'Create Track Hub',
      description = 'Create Track Hub', 
      long_description = 'Create Track Hub',
      license = 'GPLv3',
      classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Topic :: Software Development :: Build Tools',
      'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
      'Programming Language :: Python :: 2.7',
      ],
      author = 'Yingxiang Li',  
      author_email = 'xlccalyx@gmail.com', 
      maintainer = 'Yingxiang Li',
      url = 'http://www.calyx.biz/',
      download_url = 'https://pypi.python.org/pypi/CTHub',
#      install_requires = ['numpy>=1.11.0'],
      packages = ['CTHub'],
      package_dir = {'CTHub': 'CTHub'},
      scripts = ['CTHub/CTHub'],
      package_data = {'CTHub': ['configure.txt']}
) 

