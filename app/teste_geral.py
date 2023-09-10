import sys
import GetInfo as g
import GetText as t

 
n = sys.argv
print(n)
# n[0] = nome do arquivo
# n[1] = Primeiro parametro passado como argumento

t.GetTextFromImage(n[1])