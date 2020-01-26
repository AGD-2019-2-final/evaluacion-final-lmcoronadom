import sys
#
#  >>> Escriba el codigo del reducer a partir de este punto <<<
#
if __name__ == '__main__':

    curkey = None
    total = None

    ##
    ## cada linea de texto recibida es una
    ## entrada clave \tabulador valor
    ##
    for line in sys.stdin:
    	key, val = line.split("\t")
    	val = int(val)
    	if total == None: ##primer iteración pq el primero es mayor, no vuelve a entrar
    		total=val
    	if key == curkey:
    	##max_val=max(total,val)
    		total=max(total,val)
    	else:
    		if curkey is not None:
    		##
    		## una vez se han reducido todos los elementos
    		## con la misma clave se imprime el resultado en
    		## el flujo de salida
    		##
    			sys.stdout.write("{}\t{}\n".format(curkey, total))
    		curkey = key
    		total = None
    sys.stdout.write("{}\t{}\n".format(curkey,total))