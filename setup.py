import re
import sys
from setuptools import setup
from io import open

VERSION = '1.5.0'

long_description = open('README.rst', 'rt', encoding='utf8').read()

# PyPI can't process links with anchors
long_description = re.sub(r'<(.*)#.*>`_', '<\g<1>>`_', long_description)

if sys.version_info >= (2,7):
    requests_install_requires = 'requests >=2.9.1'
else:
    # Requests 2.20.0+ doesn't support Python 2.6
    requests_install_requires = 'requests >=2.9.1, <2.20.0'


setup(
    name = 'cloudpayments',
    packages = ['cloudpayments'],

    description = 'CloudPayments Python Client Library',
    long_description = long_description,

    version = VERSION,

    author = 'Antida software',
    author_email = 'info@antidasoftware.com',
    license = 'MIT license',

    url = 'https://github.com/antidasoftware/cloudpayments-python-client',
    download_url = 'https://github.com/antidasoftware/cloudpayments-python-client/tarball/%s' % VERSION,

    requires = [
        'requests (>=2.9.1)',
        'pytz (>=2015.7)'
    ],

    install_requires = [
        requests_install_requires,
        'pytz >=2015.7'
    ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Office/Business',
        'Topic :: Office/Business :: Financial',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],

    zip_safe=False
)