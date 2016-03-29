#!/usr/bin/python
import sys
from blocktools import *
from block import Block, BlockHeader

def parse(blockchain):
	print 'print Parsing Block Chain'
	counter = 0
	blockchain.seek(0, 2)
	fSize = blockchain.tell() - 80 #Minus last Block header size for partial file
	blockchain.seek(0, 0)
	while True:
		if fSize < blockchain.tell():
			print ''
			print 'End of File reached'
			break
		print counter
		block = Block(blockchain)
		block.toString()
		counter+=1

def main():
	if len(sys.argv) < 2:
            print 'Usage: sight.py filename'
	else:
		with open(sys.argv[1], 'rb') as blockchain:
			parse(blockchain)



if __name__ == '__main__':
	main()
