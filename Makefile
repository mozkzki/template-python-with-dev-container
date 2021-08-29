.PHONY: black flake8 ut start

all: lint ut

lint: flake8 black

black:
	black .

flake8:
	flake8 --max-line-length=100 --ignore=E203,W503 ./main

ut:
	pytest -v --capture=no --cov-config .coveragerc --cov=main --cov-report=xml --cov-report=term-missing .

start:
	python ./main/my/app.py