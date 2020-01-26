import sys
import operator

#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
if __name__ == '__main__':
	#datain=sorted(sys.stdin,key=operator.itemgetter(2))
	
	curkey=None
	total=None

	for line in sys.stdin:
		key,val=line.split("\t")
		val=int(val)

		if key==curkey:
			total+=val
		else:
			if curkey is not None:
				sys.stdout.write("{},{}\n".format(curkey, total))

			curkey=key
			total=val

	sys.stdout.write("{},{}\n".format(curkey, total))


		
