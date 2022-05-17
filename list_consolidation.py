#! /usr/bin/env python

"""
  Author:  Jim Hardesty

"""






import sys, getopt
sys.path.append("/afs/btv/data/amslibs/bin/binpy")
import os
import DB2Queries
import types
import csv
import re
import subprocess
from bs4 import BeautifulSoup







def main():


    

    dodata_run_list = open("dodata.run.results", "r")
    #tech_list_contents = tech_list.readlines()     #convert the text file into a list.   Gives newline character at end of each list element
    #tech_list_contents_test = tech_list.read()     #convert the text file into a list.   Gives newline character at end of each list element

    dodata_run__list_contents = [line.rstrip() for line in dodata_run_list]       #convert the text file into a list.  Takes out the newline character and trailing whitespace.


    #print dodata_run_list_contents



    #tech_list_contents = []
    #for line in tech_list:
         #tech_list_contents.append(line.rstrip('\n')) 
         

    master_layer_list = []




    item_iter = iter(dodata_run__list_contents)


    unordered_flag = "not_set"

    for line in item_iter:

         if unordered_flag == "set":

	      if line.rstrip() == "":

	           unordered_flag = "not_set"
		   item_iter.next()

              else:

	           line2 = line.rstrip()     #remove trailing spaces
	           master_layer_list.append(line2)
		   print line2




         if unordered_flag == "not_set":

	      if "Unordered mask levels with data:" in line:

	           unordered_flag = "set"

		   line2 = re.sub(r'Unordered mask levels with data:',"",line)       #leaving just the layer list if not a multiple line list

                   master_layer_list.append(line2)
                   print line2



    consolidated_layer_list = []


    for line in master_layer_list:

         tmp_list = []

         if line != "":

	      tmp_list = list(line.split())

	      for item in tmp_list:
              
                   already_in_list = "false"

	           for layer in consolidated_layer_list:

		        if layer == item:

			     already_in_list = "true"

                   if already_in_list == "false":

		        consolidated_layer_list.append(item)


    print "\n\n"

    print "length of consolidated_layer_list = " + str(len(consolidated_layer_list))


    #print consolidated_layer_list

    #for item in consolidated_layer_list:
         #print item,


    print ""


    for i in range(0,len(consolidated_layer_list), 15):
         print " ".join(consolidated_layer_list[i:i+15])



    dodata_run_list.close()



if __name__ == '__main__':

    main()


