.PHONY: build analyze run stop

build:
		sudo docker build -t dbot .
analyze:
		sudo docker run --rm -it dbot flake8 /app
run:
		sudo docker run --rm -d --name dbot dbot
stop:
		sudo docker container stop dbot
