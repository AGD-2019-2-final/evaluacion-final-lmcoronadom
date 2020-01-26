import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":

	curkey=None
	suma=None
	cont=None

	for line in sys.stdin:
		key,val=line.split("\t")
		val=float(val)
		
		if key==curkey:
			suma+=val
			cont+=1

		else:
			if curkey is not None:
				sys.stdout.write("{}\t{}\t{}\n".format(curkey,suma,(suma/cont)))

			curkey=key
			suma=val
			cont=1
	sys.stdout.write("{}\t{}\t{}\n".format(curkey,suma,(suma/cont)))