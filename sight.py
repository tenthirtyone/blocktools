#!/usr/bin/python
import sys
from blocktools import *
from block import Block, BlockHeader

def parse(blockchain):
	print 'print Parsing Block Chain'
	counter = 0
	while True:
		print counter
		block = Block(blockchain)
		block.toString()
		counter+=1

def main():
	if len(sys.argv) < 2:
		print 'Usage: blockparser.py filename'
	else:
		with open(sys.argv[1], 'rb') as blockchain:
			parse(blockchain)



if __name__ == '__main__':
	main()
