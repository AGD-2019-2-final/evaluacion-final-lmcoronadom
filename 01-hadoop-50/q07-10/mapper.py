import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":
	'''for line in sys.stdin:
		line=line.strip()
		key,date,val=line.split("   ")
		##col1=line.split(",")[0]
		##col2=line.split(",")[1]

		sys.stdout.write("{},{},{}\n".format(key.strip(),date.strip(),val.strip()))'''

for line in sys.stdin:
        letter = line.split('   ')[0]
        date = line.split('   ')[1]
        value = line.split('   ')[2]
        value = int(value)
        sys.stdout.write("{},{},{},{}\n".format(letter+str(value/100),letter,date,value))