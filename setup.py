#!/usr/bin/env python

from setuptools import setup

setup(name = 'tender',
      version = '0.3',
      author = 'A few different folks on github',
      author_email = 'dan@tracelytics.com',
      url = 'http://github.com/dankosaur/pytender',
      download_url = 'http://github.com/dankosaur/pytender',
      description  = 'Python TenderApp Client',
      packages = ['tender'],
      package_dir = { 'tender' : 'src' },
      license = 'MIT',
      )
