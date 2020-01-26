import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#

for line in sys.stdin:
		line = line.strip()
		ide,arr=line.split()
		ide=ide.strip()
		arr=arr.strip()

		letters = arr.split(",")
		for letter in letters:
			sys.stdout.write("{}\t{}\t{}\n".format(letter+str(float(ide)/100),letter,ide))
        