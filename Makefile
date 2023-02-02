build.docker:
	docker build -t dani-server:latest .

run:
	docker run --rm -p 5001:5000 dani-server:latest

test:
	cURL http://127.0.0.1:5001/ping