#!/usr/bin/python
import sys
import urllib

def query_AS_prefixes(AS):
	""" A simple python code to lookup a list of prefixes
        currently announced via BGP.
        example: if the AS (Autonomus System) of a given ISP 
        is 21003, you just execute this code to know
        all of its announced registred subnets.

        This code communicate with dan website to gather the requried 
        information.
        https://www.dan.me.uk/

	Author Name: Ibrahim Khorwat
	
	root@PC-1:/home#python query_AS_prefixes.py 21003
	'41.208.103.0/24'
	'41.208.64.0/18'
	'41.252.0.0/14'
	'41.252.0.0/18'
	'41.252.128.0/18'
	'41.252.192.0/18'
	'41.252.192.0/19'
	'41.252.64.0/18'
	'41.254.0.0/24'
	'41.254.1.0/24'
	'41.254.15.0/24'
	'41.254.2.0/24'
	'41.254.3.0/24'
	'41.254.31.0/24'
	'41.254.38.0/24'
	'41.254.5.0/24'
	'41.254.6.0/24'
	'41.254.8.0/24'
	'62.240.32.0/19'
	'62.68.32.0/19'
	'62.68.58.0/24'
	'62.68.59.0/24'
	'62.68.60.0/24'
	"""
	try:
		web = urllib.urlopen("https://www.dan.me.uk/bgplookup?asn="+AS)
		#To convert the file into a text file
		page = web.read()
		table = page[page.index('IPv4 Prefixes seen at AS'+AS):]
		#To splite the table into items, each line represent an item in the list
		IPtable = table[:table.index('</table>')].splitlines()
		#un-comment the below print for troubleshooting
		#print IPtable[2].split()[3]
		for i in range(2,len(IPtable)):
			print IPtable[i].split()[3]
	except:
		print "\nPlease Check your Internet connection or your DNS server\n"


if __name__ == '__main__':
        query_AS_prefixes(sys.argv[1])
