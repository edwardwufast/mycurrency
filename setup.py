import glob
from setuptools import setup, find_packages

requires = ['pandas', 'xlwings', 'openpyxl', 'html_table_extractor',
            'requests', 'twder']

setup(name='mycurrency',
      version='1.0',
      packages=find_packages('lib/'),
      package_dir={'': 'lib'},
      scripts=glob.glob('bin/*'),
      install_requires=requires,
      data_files=[('/etc/mycurrency/', ['mycurrency.config'])],
      include_package_data=True
     )
