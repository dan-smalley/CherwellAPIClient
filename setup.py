import os
from setuptools import find_packages, setup
import sys

sys.path.insert(0, os.path.join(os.path.abspath(os.path.curdir), 'src'))
from cherwellapi import __version__, __release__

name = 'CherwellAPIClient'

setup(name=name,
      version=__release__,
      description='Cherwell API client module',
      long_description="""
Python module for interacting with the Cherwell API in an object-oriented way. Tested with API version 10.1.0, no guarantees for earlier versions...

The philosophy here is to use objects to work with everything in the Cherwell API, and to try to normalize the various calls to the different routers. Thus get methods will always return an object, list methods will return data. All methods to add or create start with add, all remove or delete start with delete. As much as possible the methods try to hide the idiosyncrasies of the JSON API, and to do the work for you, for example by letting you use a device name instead of having to provide the full device UID for every call.
""",
      url='none',
      author='Dan Smalley',
      author_email='dan@dansmalley.com',
      license='Apache',
      classifiers=[
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: Apache Software License',
          'Natural Language :: English',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.8',
          'Topic :: System :: CMDB',
      ],
      keywords='Cherwell CMDB api',
      packages=find_packages(where='src'),
      package_dir={'': 'src'},
      zip_safe=False,
      tests_require=[
          'pytest>=3.2.3',
          'pytest-responses>=0.3.0',
      ],
      install_requires=[
          'python-dateutil>=2.6.1',
          'requests>=2.18.1',
      ],
      command_options={
          'build_sphinx': {
              'project': ('setup.py', name),
              'version': ('setup.py', __version__),
              'release': ('setup.py', __release__),
              'source_dir': ('setup.py', 'docs'),
              'build_dir': ('setup.py', 'docs/_build'),
              'config_dir': ('setup.py', 'docs'),
          }
      }
      )
