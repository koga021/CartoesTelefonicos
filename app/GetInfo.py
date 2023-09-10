# -*- coding: utf-8 -*-
import re
import numpy as np
from iteration_utilities import unique_everseen
from iteration_utilities import duplicates

def SearchUnidades (texto):
    #print("Print por dentro da variavel")
    #print(texto)
    t=re.compile(r' [0-9][0-9] ')
    #check=t.findall(texto)
    correspondencias = t.finditer(texto)
    result=[]
    try:
        for c in correspondencias:
            #print(c[0])
            result.append(c[0])
        print(result)
        dup = unique_everseen(duplicates(result))
        #print("Repetidos")
        #print(dup)
        aux=[]
        for i in dup:
            aux.append(i)
            #print("saida: ",i)
        print(aux)
        return(aux[0])
        #saida=ReturnUnidades(result)
    except:
        return([20,30,35,90])
 


