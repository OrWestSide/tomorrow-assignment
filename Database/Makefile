clear:
	yes | docker container prune 

db:
	yes | docker container prune
	docker run -d --name uber2 -p 3306:3306 --env-file ./.env -v ${PWD}:/docker-entrypoint-initdb.d/ mysql:latest --default-authentication-plugin=mysql_native_password

stop:
	docker stop uber2