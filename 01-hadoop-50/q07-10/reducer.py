import sys
import operator
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
'''if __name__ == '__main__':
	datain=sorted(sys.stdin,key=operator.itemgetter(1))
	#datain=sorted(sys.stdin,key=lambda x:(x[2],x[0]))
	

	for line in datain:
		line=line.strip()
		key,date,val=line.split(",")
		#val=

		#sys.stdout.write("{}\t{}\t{}\n".format(key,date,val))
		sys.stdout.write(key+"\t"+date+"\t"+val+"\n")'''

if __name__ == '__main__':

    #sort = sorted(sys.stdin, key=itemgetter(3))
       
    #for line in sort:
    #for line in sys.stdin:
    #    letter, date, value = line.split(",")
    #    value = int(value)
        
    #    sys.stdout.write("{},{},{}\n".format(letter,date,value))
    
    #sys.stdout = sorted(sys.stdout, key=itemgetter(1,3))
    #sys.stdout.write("{},{},{}\n".format(letter,date,value))
    
    for line in sys.stdin:
        code,letter, date, value = line.split(",")
        value = int(value)
        sys.stdout.write("{}\t{}\t{}\n".format(letter,date,value))