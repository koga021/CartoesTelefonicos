# -*- coding: utf-8 -*-
import re
import numpy as np
from iteration_utilities import unique_everseen
from iteration_utilities import duplicates
UNIDADES=[20,30,35,60,90]
def SearchUnidades (texto):
    #print("Print por dentro da variavel")
    #print(texto)
    #t=re.compile(r' [0-9][0-9] ')
    t=re.compile(r'10|20|30|40|50|60|75|90')

    #check=t.findall(texto)
    correspondencias = t.finditer(texto)
    result=[]
    try:
        for c in correspondencias:
            #print(c[0])
            result.append(c[0])
        #print(result)
        dup = unique_everseen(duplicates(result))
        #print("Repetidos")
        #print(dup)
        aux=[]
        for i in dup:
            aux.append(i)
            #print("saida: ",i)
        #print(aux)
        return(aux[0])
        #saida=ReturnUnidades(result)
    except:  
        if not result:
            print("Retornei Array vazio, retornando padrão")
            return("20")
            #return(UNIDADES)
        else:
            print("Retornei mais de um valor")
            #print(len(result))
            return(result[0])
            #return(aux)


 


