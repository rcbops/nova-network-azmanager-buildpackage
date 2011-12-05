#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

Name='nova-scheduler-azmanager'
Url='https://github.com/rcbops/nova-scheduler-azmanager'
Version='0.1'
License='Apache License 2.0'
# Change as required
Author='OpenStack LLC'
AuthorEmail=''
Maintainer=''
Summary='Per-AZ vlan manager'
ShortDescription=Summary
Description=Summary

setup(
    name=Name,
    version=Version,
    url=Url,
    author=Author,
    author_email=AuthorEmail,
    description=ShortDescription,
    long_description=Description,
    license=License,
    install_requires= [ 'nova' ],
    include_package_data=True,
    packages=find_packages('lib'),
    package_dir = {'': 'lib'},
    namespace_packages=['nova', 'nova.network'],
    py_modules=[]
)
