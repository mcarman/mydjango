#!/usr/bin/env python
import os

myfile = __file__
print "This script file is: %r" % myfile

path = os.path.abspath(__file__)
print "The absolute path to %r : %r" % (myfile, path)

script_dir = os.path.dirname(os.path.abspath(__file__))
print "This script is in directory: %r" % script_dir

script_dir_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print "The parent directory of the %r directory: %r" % (script_dir, script_dir_dir)
script_dir_x3 = os.path.dirname(script_dir_dir)
script_dir_x4 = os.path.dirname(script_dir_x3) 
 
print "The settings directory is: %r" % script_dir
print "One directory level up is: %r" % script_dir_dir
print "Two directory levels up is: %r" % script_dir_x3
print "Three directory levels up is: %r" % script_dir_x4
