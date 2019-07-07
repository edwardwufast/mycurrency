import glob

from distutils.core import setup, Extension

requires = ['pandas', 'xlwings', 'openpyxl', 'html_table_extractor',
            'requests', 'twder']

setup(name='mycurrency',
      version='1.0',
      package_dir={'': 'lib'},
      scripts=glob.glob('bin/*'),
      install_requires=requires,
      data_files=[('/etc/mycurrency/', ['mycurrency.config'])]
     )
