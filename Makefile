
teste:
	@echo "testando"


install: 
	rm -rf virtual;
	virtualenv virtual && source virtual/bin/activate && pip install -r requirements.txt; \
	
run:
	clear;
	#@source virtual/bin/activate ; virtual/bin/python app/detecta_cor.py
	#@source virtual/bin/activate ; virtual/bin/python app/teste.py
	@source virtual/bin/activate ; virtual/bin/python app/extract.py
