import sys
import GetInfo as g
import GetText as t

 
n = sys.argv
print(n)
# n[0] = nome do arquivo
# n[1] = Primeiro parametro passado como argumento

texto=t.GetTextFromImage(n[1])
#textoOtimizado=t.GetTextFromImageBest(n[1])
#print(texto)
unidades=g.SearchUnidades(texto)
unidades=unidades.strip()
print(unidades)

#print(textoOtimizado)