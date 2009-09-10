# Copyright (c) 2008 Simplistix Ltd
# See license.txt for license details.

import os
from setuptools import setup, find_packages

name = 'errorhandler'
package_dir = os.path.join(os.path.dirname(__file__),name)

setup(
    name=name,
    version=file(os.path.join(package_dir,'version.txt')).read().strip(),
    author='Chris Withers',
    author_email='chris@simplistix.co.uk',
    license='MIT',
    description="A logging framework handler that tracks when messages above a certain level have been logged.",
    long_description=open(os.path.join(package_dir,'readme.txt')).read(),
    url='http://www.simplistix.co.uk/software/python/errorhandler',
    classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    ],    
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    )

# to build and upload the eggs, do:
# python setup.py sdist register upload
# ...or...
#  bin/buildout setup setup.py sdist register upload
# ...on a unix box!

# To check how things will show on pypi, install docutils and then:
# bin/buildout -q setup setup.py --long-description | rst2html.py --link-stylesheet --stylesheet=http://www.python.org/styles/styles.css > dist/desc.html
