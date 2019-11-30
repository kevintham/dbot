build:
		sudo docker build -t dbot .
run:
		sudo docker run --rm -d --name dbot dbot
stop:
		sudo docker container stop dbot
