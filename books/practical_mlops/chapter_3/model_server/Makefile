docker-build:
	@docker build --build-arg VERSION=1.0 -t flask-predict . 

docker-run:
	@docker run -p 5123:5000 -d --name flask-predict flask-predict

predict:
	@python predict.py
