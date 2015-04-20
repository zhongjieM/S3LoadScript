'''
Created on Apr 19, 2015

@author: kevin
'''
import os


S3_folder = 's3://kevin017-cs6240/cs6240/project/data/input/raw/'
cp_cmd = 'aws s3 cp {0} {1}{2}'
rm_cmd = 'rm {0}'

def push_to_s3(file_path):
    print 'Copy file {0} to {1}{2}'.format(file_path, S3_folder, os.path.basename(file_path))
    os.system(cp_cmd.format(file_path, S3_folder, os.path.basename(file_path)))
    print 'Remove file {0}'.format(file_path)
    os.system(rm_cmd.format(file_path))