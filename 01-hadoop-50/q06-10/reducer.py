import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":

	curkey=None
	maxi=None
	mini=None

	for line in sys.stdin:
		key,val=line.split("\t")

		if key==curkey:
			maxi=max(val,maxi)
			mini=min(val,mini)

		else:
			if curkey is not None:
				sys.stdout.write("{}\t{}\t{}\n".format(curkey,maxi,mini))

			curkey=key
			maxi=val
			mini=val
	sys.stdout.write("{}\t{}\t{}\n".format(curkey,maxi,mini))