import sys
import operator
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == '__main__':
	#datain=sorted([i.split(",") for i in sys.stdin],key=lambda x: x[2])
	datain = sys.stdin.readlines()
	for line in range(6):
		ide,key,date,val=datain[line].split(",")
		#val=int(val)
		sys.stdout.write("{}\t{}\t{}\n".format(key,date,val))
		##sys.stdout.write(datain[line])