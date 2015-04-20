#!/usr/bin/env python

'''
Created on Apr 14, 2015

@author: kevin
'''

import os

from push_s3 import push_to_s3
import web_get


OUTPUT_DIR = os.getcwd() + '/download_data_files/'

def main():
    # # get data files from cloud
    # # merge data files into one big file
    web_get.get_data_files()

if __name__ == '__main__':
    main()
