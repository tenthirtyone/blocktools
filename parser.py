#/usr/bin/python

from blocktools import *

with open('1M.dat', 'rb') as blockfile:
		print "Magic Number:\t %8x" % uint4(blockfile)
		print "Blocksize:\t %u" % uint4(blockfile)
	
		"""Block Header"""
		print "Version:\t %d" % uint4(blockfile)
		print "Previous Hash\t %s" % hashStr(hash32(blockfile))
		print "Merkle Root\t %s" % hashStr(hash32(blockfile))
		print "Time\t\t %s" % str(time(blockfile))
		print "Difficulty\t %8x" % uint4(blockfile)
		print "Nonce\t\t %s" % uint4(blockfile)

		print "Tx Count\t %d" % varint(blockfile)
	
		print "Version Number\t %s" % uint4(blockfile)
		print "Inputs\t\t %s" % varint(blockfile)
		print "Previous Tx\t %s" % hashStr(hash32(blockfile))
		print "Prev Index \t %d" % uint4(blockfile)
		script_len = varint(blockfile)
		print "Script Length\t %d" % script_len
		script_sig = blockfile.read(script_len)
		print "ScriptSig\t %s" % hashStr(script_sig)
		print "ScriptSig\t %s" % hashStr(script_sig).decode('hex')
		print "Seq Num\t\t %8x" % uint4(blockfile)

		print "Outputs\t\t %s" % varint(blockfile)
		print "Value\t\t %s" % str((uint8(blockfile)*1.0)/100000000.00)
		script_len = varint(blockfile)
		print "Script Length\t %d" % script_len
		script_pubkey = blockfile.read(script_len)
		print "Script Pub Key\t %s" % hashStr(script_pubkey)
		print "Lock Time %8x" % uint4(blockfile)
		print
