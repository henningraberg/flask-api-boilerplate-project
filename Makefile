.ONESHELL:

.PHONY: clean install tests run all test

install:
	python3.11 -m venv "venv"; \
	. venv/bin/activate; \
	pip install -r requirements.txt;

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

tests:
	. venv/bin/activate; \
	python manage.py test

run:
	. venv/bin/activate; \
	python manage.py run

test:
	echo 'test'; \


all: clean install tests run test