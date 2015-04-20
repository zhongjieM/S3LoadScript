'''
Created on Apr 14, 2015

@author: kevin
'''

import os

from push_s3 import push_to_s3
import wget


# File path build up BASEs
URL_BASE = 'http://dumps.wikimedia.org/other/pagecounts-raw/{0}/{1}-{2}/{3}'
LOCAL_BASE = os.getcwd() + '/{0}'
FILENAME_BASE = 'pagecounts-{0}{1}{2}-{3}0000.gz'
# File path specifics
YEAR = 2015
MONTH = 1
DAY_START = 5
DAY_END = 11
HOUR_START = 0
HOUR_END = 24

WGET_CMD = 'wget {0}'

def get_data_files():
    files_paths = []
    year = YEAR
    month = MONTH
    for day in range(DAY_START, DAY_END):
        for hour in range(HOUR_START, HOUR_END):
            local_file_path = buildup_local_file_path(year, month, day, hour)
            files_paths.append(local_file_path)
            if os.path.exists(local_file_path) == False:
                webfilepath = buildup_url(year, month, day, hour)
                print 'Downloading {0} to {1}'.format(webfilepath, local_file_path)
                os.system(WGET_CMD.format(webfilepath))
#                 _filename = wget.download(webfilepath)
            push_to_s3(local_file_path);
    return files_paths


def buildup_url(y, m, d, h):
    year = y
    month = roundup_two_digits(m)
    day = roundup_two_digits(d)
    hour = roundup_two_digits(h)
    return URL_BASE.format(year, year, month, buildup_file_name(year, month, day, hour))


def buildup_local_file_path(y, m, d, h):
    year = y
    month = roundup_two_digits(m)
    day = roundup_two_digits(d)
    hour = roundup_two_digits(h)
    return LOCAL_BASE.format(buildup_file_name(year, month, day, hour))


def buildup_file_name(year, month, day, hour):
    return FILENAME_BASE.format(year, month, day, hour);


def roundup_two_digits(v):
    value = str(v)
    if v < 10:
        value = '0' + value
    return value
