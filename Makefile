# for building on local machine
install:
	@docker build -t showjackyang/intercom-take-home:latest .

lint:
	@docker run -v $(shell pwd):/pipeline/source showjackyang/intercom-take-home:latest make run-lint

test:
	@docker run -v $(shell pwd):/pipeline/source showjackyang/intercom-take-home:latest make run-test

run:
	@docker run -v $(shell pwd):/pipeline/source showjackyang/intercom-take-home:latest pipenv run python run.py

# to be executed in docker container
run-test:
	make run-clean
	make run-lint
	make run-static-check
	@pipenv run py.test --cov=src \
		--cov-report xml \
                --cov-report term \
                --disable-pytest-warnings tests

run-lint:
	@pipenv run flake8

run-clean:
	@find . -type f -name '*.pyc' -delete
	@find . -type d -name '__pycache__' -delete

run-static-check:
	@pipenv run mypy --ignore-missing-imports src

