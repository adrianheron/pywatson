PyWatson [![Travis CI][travis-badge]][travis] [![Code Health][landscape-badge]][landscape] [![Documentation Status][readthedocs-badge]][readthedocs]
========

A Python adapter for IBM Watson's question and answer API

## Installation

Install the package from PyPI:

    pip install pywatson

## Usage

```python
from pywatson import Watson

# Create a Watson instance with your URL and credentials
# pywatson will use the endpoint `url + '/question'`
watson = Watson(url='https://watson-wdc01.ihost.com/instance/507/deepqa/v1', username='someuser', password='zyXHLz3sCoPt6G')


```

## See also

- [IBM Watson Developer Cloud API Reference](http://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/apis/#!/Question_Answer)


[travis-badge]:      http://img.shields.io/travis/sherlocke/pywatson.svg?style=flat
[travis]:            https://travis-ci.org/sherlocke/pywatson
[landscape-badge]:   https://landscape.io/github/sherlocke/pywatson/master/landscape.png?style=flat
[landscape]:         https://landscape.io/github/sherlocke/pywatson/master
[readthedocs-badge]: https://readthedocs.org/projects/pywatson/badge/?version=latest
[readthedocs]:       https://readthedocs.org/projects/pywatson/?badge=latest
