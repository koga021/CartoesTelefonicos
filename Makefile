
teste:
	@echo "testando"


install: 
	rm -rf virtual;
	virtualenv virtual && source virtual/bin/activate && pip install -r requirements.txt; \
	
run:
	clear;
	@source virtual/bin/activate ; virtual/bin/python app/teste.py