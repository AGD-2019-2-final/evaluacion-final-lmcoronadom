import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == '__main__':
	#datain=sorted(sys.stdin,key=operator.itemgetter(2))
	
	curkey=None
	result=""

	for line in sys.stdin:
		ide,key,val=line.split("\t")
		val=val.replace("\n","")
		if key==curkey:
			result+=","+val
		else:
			if curkey is not None:
				sys.stdout.write("{}\t{}\n".format(curkey, result))

			curkey=key
			result=val

	sys.stdout.write("{}\t{}\n".format(curkey, result))


		

