#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Vorlage.py
#  
#  Copyright (C) 2020 by GBS St. Gallen, Inc. All rights reserved.
#  Released under the therms of the GNU General Public License version 3
#  or later.
#  

#Example function:
def printArguments(args):
    print("Number of arguments: ", len(args))
    print("The first argument ist the name of the script: ", args[0])
    print("Here ara the other arguments: ")
    for arg in args[1:]:
        print(arg)

#Main function:
def main(args):
    print("Hello world")
    printArguments(args)
    return 0

#Checks whether this file has been executed directly or imported from 
#another file. Only if the file is executed directly, the main function 
#is called.
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
