# waqi-python
Python wrapper for the World Air Quality Index Project JSON API

[![Build Status](https://travis-ci.com/danoscarmike/waqi-python.svg?branch=master)](https://travis-ci.com/danoscarmike/waqi-python) [![codecov](https://codecov.io/gh/danoscarmike/waqi-python/branch/master/graph/badge.svg)](https://codecov.io/gh/danoscarmike/waqi-python)

# Installation
1. Get an API token from the [World Air Quality Index Project](https://aqicn.org/data-platform/token/#/)
2. Create an environment variable called AQIPY_TOKEN:
`export AQIPY_TOKEN='<your_new_token>'`
3. `pip install waqi-python`

# Usage
```
>>> from waqi_python import client as base
>>> client = base.WaqiClient()
>>> my_station = client.get_local_station()
>>> my_station.city.name
'San Francisco-Arkansas Street, San Francisco, California'
>>> my_station.aqi
46
```
