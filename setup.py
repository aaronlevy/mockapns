#!/usr/bin/env python                                                                                                                                        
from setuptools import setup, find_packages


setup(
  name='apnsmock',
  version='0.1.0',
  install_requires=[
    'gevent==1.1.2',
    'greenlet==0.4.11'
  ],
  scripts=['apnsmock']                      
)
