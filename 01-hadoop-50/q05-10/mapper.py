import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":
	for line in sys.stdin:
		key=line.split('-')[1]
		##col1=line.split(",")[0]
		##col2=line.split(",")[1]

		#sys.stdout.write("{},{},{}\n".format(key,val,val2))
		sys.stdout.write("{}\t1\n".format(key))