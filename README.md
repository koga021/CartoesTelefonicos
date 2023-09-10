# CartoesTelefonicos
Sistema para Catalogar Cartoes telefonicos utilizando OCR

# Arquivo de Testes

Abaixo vou documentar os scripts e testes efetuados para a compreenção do melhor algoritmo para a detecção de textos no cartão telefônico

* teste.py 

Esse script converte o fundo do cartão amarelo em tons de cinza para que ele possa ter um melhor performance na detcção te texto em uma foto.

# Funções
Descrição de cada função
* GetInfo.SearchUnidades

Essa Função retorna a unidade a quantidade mais provável do cartão, caso encontre algum erro, retornará um array com as unidades mais prováveis.
No caso de não conseguir encontrar o número de unidades do Cartão, será retornado o valor de 20 Unidades, já que seria o mais provável, foi feito também o tratamento de strip para a string.

* getText.GetTextFromImageBest

Essa função retorna o melhor resultado para a extração de texto do cartão, porém não é a melhor versão para a extração de unidades, para a extração das unidades o melhor método é utilizando a imagem em tons de cinza.
