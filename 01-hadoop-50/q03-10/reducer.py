import sys
import operator

#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
if __name__ == '__main__':
	datain=sorted(sys.stdin,key=operator.itemgetter(2))

	for line in datain:
		key,val=line.split(",")

		sys.stdout.write("{},{}\n".format(key, val))


		
