start-mysql:
	#docker run --rm  --name db_cartoes -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_USER=root -e MYSQL_DATABASE=cartoes_telefonicos mysql:latest
	#docker run --rm  --name db_cartoes -p 3306:3306 -e MYSQL_ROOT_PASSWORD=ribas -e MYSQL_USER=ribas -e MYSQL_DATABASE=cartoes_telefonicos mysql:latest
	docker run --rm  --name db_cartoes -p 3306:3306  -e MYSQL_USER="douglas" -e MYSQL_PASSWORD="a7v8xx" -e MYSQL_ROOT_PASSWORD="021dou" -e MYSQL_DATABASE=cartoes_telefonicos mysql:latest
stop-mysql:
	docker stop db_cartoes
	docker rm db_cartoes