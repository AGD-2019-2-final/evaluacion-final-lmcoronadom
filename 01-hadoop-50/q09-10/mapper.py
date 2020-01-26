import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":

	for line in sys.stdin:
		line = line.strip()
		key,date,val=line.split("   ")

		sys.stdout.write("{},{},{},{}\n".format(str(float(val)/100),key,date,val))
