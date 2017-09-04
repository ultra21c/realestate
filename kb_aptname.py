#!/usr/bin/python
#*-* encoding:utf-8 *-*

from optparse import OptionParser
import ConfigParser
import sys
import os

def kb_newline_merge(options):
    '''
    sample) filename c
    "골든/
    안양시 관양동"
    "골든/
    안양시 관양동"
    "골든/
    안양시 관양동"
    "공작(LG)/
    안양시 관양동"
    "공작(부영2차)/
    안양시 관양동"
    '''
    with open('./data/%s'%options["filename"]) as f:
        start = False
        end = True
        empty = False
        data = ""
        buff = ""
        empty_buff = ""
        for line in f.readlines():
            row = line.strip()
            if row.startswith("\""):
                start = True
                end = False
                empty = False
            if row.endswith("\""):
                end = True
                start = False
            if row == "":
                empty = True
                
            if start:
                buff += row
            if end:
                buff += row
                start = False
                end = False
                col = buff.replace("\"", "").split("/")
                addr = col[1].split(" ")
                display = "%s\t%s\t%s"%(addr[0], addr[1], col[0])
                print display
                empty_buff = display
                buff = ""
            if empty:
                print empty_buff

def split_slash(options):
    with open('./data/%s'%options["filename"]) as f:
        for line in f.readlines():
            row = line.strip()
            size = row.split("/")
            print "%s\t%s"%(size[0], size[1])
        
def load_option():
    # config 를 기본 세팅으로
    options = {}
    parser = OptionParser()
    parser.add_option("-f", "--filename", dest="filename", action="store", default="")
    parser.add_option("-j", "--job", dest="jobname", action="store", default="")

    options.update(vars(parser.parse_args()[0]))

    return options

if __name__ == '__main__':
    options = load_option()
    if options["jobname"] and options["filename"]:
        if options["jobname"] == "merge":
            kb_newline_merge(options)
        elif options["jobname"] == "split":
            split_slash(options)
