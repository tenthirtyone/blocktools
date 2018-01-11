#!/usr/bin/python
import sys
from blocktools import *
from block import Block, BlockHeader

def parse(blockchain, blkNo):
	print 'Parsing Block Chain block head, transaction etc.'
	continueParsing = True
	counter = 0
	blockchain.seek(0, 2)
	fSize = blockchain.tell() - 80 #Minus last Block header size for partial file
	blockchain.seek(0, 0)
	while continueParsing:	
		block = Block(blockchain)
		continueParsing = block.continueParsing
		if continueParsing:
			block.toString()
		counter+=1
		print "#"*20+"Block counter No. %s"%counter +"#"*20
		if counter >= blkNo and blkNo != 0xFF:
			continueParsing = False

	print ''
	print 'Reached End of Field'
	print "Parsed %d blocks" % counter

def main():
	if len(sys.argv) < 2:
            print 'Usage: sight.py filename'
	else:
		blkNo = 0xFF
		if(len(sys.argv) == 3):
			blkNo = int(sys.argv[2])
			print "Parsing %d blocks" % blkNo

		with open(sys.argv[1], 'rb') as blockchain:
			parse(blockchain,blkNo)



if __name__ == '__main__':
	main()
