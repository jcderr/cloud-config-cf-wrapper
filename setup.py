#!/usr/bin/env python

from setuptools import setup, find_packages
from cloudcfwrapper import version

setup(name='cloud-config-cf-wrapper',
      version=version,
      description='JSON-safe wrapping of cloud-configs for CloudFormation',
      author='Jeremy Derr',
      author_email='jeremy@derr.me',
      url='http://github.com/jcderr/cloud-config-cf-wrapper',
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'cfwrapper = cloudcfwrapper.cli:wrapcmd',
          ]
      }
      )
