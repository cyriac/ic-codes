#! /usr/bin/env python

from StringIO import StringIO
from zipfile import ZipFile
import json
import os
import requests
import toml


def get_data(file_url):
    print "Fetching %s" % (file_url)
    url = requests.get(file_url)
    zipfile = ZipFile(StringIO(url.content))
    zip_names = zipfile.namelist()
    data = {}
    for file_name in zip_names:
        if file_name.endswith(".toml"):
            extracted_file = zipfile.open(file_name)
            d = toml.loads(extracted_file.read())
            data[d['code']] = d
    return data

def get_codes():
    from locations import sic_file, naics_file
    data  = {
        'sic_codes': get_data(sic_file),
        'naics_codes': get_data(naics_file)
    }
    return data

def write_codes(data, location=None):
    if not location:
        location = "."
    path = os.path.join(location, 'industry-codes.json')
    with open(path, 'w') as f:
        json.dump(data, f)

if __name__ == "__main__":
    write_codes(get_codes(), "/tmp/")

