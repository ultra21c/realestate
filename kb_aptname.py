#!/usr/bin/python
#*-* encoding:utf-8 *-*

def kb_newline_merge():
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
	with open('./data/apt-manan-all.dat') as f:
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

def split_slash():
	with open('./data/slash_manan-all.dat') as f:
		for line in f.readlines():
			row = line.strip()
			size = row.split("/")
			print "%s\t%s"%(size[0], size[1])
		
if __name__ == '__main__':
	kb_newline_merge()
	#split_slash()
	
