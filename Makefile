

teste:
	@echo "testando"
	@source virtual/bin/activate ; virtual/bin/python app/teste_geral.py $(file)

teste-verso:
	@clear
	@echo "Rodando bateria de testes"
	@source virtual/bin/activate ; virtual/bin/python app/teste_geral.py 04-V.jpeg
	@source virtual/bin/activate ; virtual/bin/python app/teste_geral.py 03-V.jpeg
	@source virtual/bin/activate ; virtual/bin/python app/teste_geral.py 02-V.jpeg
	@source virtual/bin/activate ; virtual/bin/python app/teste_geral.py 01-V.jpeg
	@source virtual/bin/activate ; virtual/bin/python app/teste_geral.py photo_5118776271898258939_y.jpg

install: 
	rm -rf virtual;
	virtualenv virtual && source virtual/bin/activate && pip install -r requirements.txt; \
	
run:
	clear;
	#@source virtual/bin/activate ; virtual/bin/python app/detecta_cor.py
	#@source virtual/bin/activate ; virtual/bin/python app/teste.py
	@source virtual/bin/activate ; virtual/bin/python app/extract.py

help:
	clear;
	@echo "Comandos disponíveis \n"
	@echo "Executando o teste em um arquivo único: "
	@echo "make teste file=04-V.jpeg"
	@echo "\n"
	@echo "Executando o teste em todas a imagens disponíveis"
	@echo "make teste-verso"
	@echo "\n"



