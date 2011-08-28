#!/usr/bin/python

import os, fileinput, re, collections, sys
from pythonExtractor import PythonExtractor
from cExtractor import CstyleExtractor

# Have someone who knows pythong rewrite this !r1


def listFiles(rootDir, suffixes):
    fileList = []
    for root, subFolders, files in os.walk(rootDir):
        for file in files:
            for suffix in suffixes:
                if file.endswith(suffix):
                    fileList.append(os.path.join(root, file))
    return fileList;


extracters = {
    'js': CstyleExtractor,
    'c': CstyleExtractor,
    'c++': CstyleExtractor,
    'c#': CstyleExtractor,
    'py': PythonExtractor
}

languageSuffixes = {

    'python': ['py'],
    'py': ['py'],
    'js': ['js'],
    'c' : ['c', 'h'],
    'cpp' : ['c++','cpp','cxx', 'h'],
}

defaultSymbols = {
    'python' : '!',
    'py' : '!',
    'js' : '#',
    'c' : '##',
    'cpp' : '##',
}

# Main Script

# Create a .bang file that has project info, login info, symbol info etc !r2


#m = re.search('\^(\d)','#foo ^1');
#print m.group(1)
#
#sys.exit(0)

import argparse




parser = argparse.ArgumentParser(description='\n')
parser.add_argument('dirs', metavar='directory', nargs='+',
                    help='Directories to parse')
parser.add_argument('-l', dest='language', action='store',
                    default='js',
                    help='The language type to parse, options are [php,py[thon],pe[rl],ja[va],c[#,++],js')
parser.add_argument('-text', dest='text', action='store_const',const='True',
                    help='Add this to use text only display')
parser.add_argument('-s', dest='symbol', action='store',
                    help='The symbol type to search for, common uses are !,#,~')

args = parser.parse_args()

files = []

for d in args.dirs:
    files.extend(listFiles(d, languageSuffixes[args.language]))



symbol = args.symbol if args.symbol else defaultSymbols[args.language]

extractorType = extracters[args.language]
extractor = extractorType(files, symbol)
categories = extractor.run()

if args.text:
    print '\n\nBANG.\n=====\n\n'

    for k, v in categories.iteritems():
        print k, '\n\t'
        for tag in v:
            print '\t' + str(tag)
        print '\n\n'
    
else:
    pass
    # upload results and return a url !r1