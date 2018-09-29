install:
	@docker build -t intercom/take-home:latest .

lint:
	@docker run -v $(shell pwd):/app intercom/take-home:latest make run-lint

test:
	@docker run -v $(shell pwd):/app intercom/take-home:latest make run-test

# below are to be executed in container
run-test:
	make run-clean
	make run-lint
	@pipenv run mypy --ignore-missing-imports src
	@pipenv run py.test --cov=src \
                --cov-report term \
                --disable-pytest-warnings tests

run-lint:
	@pipenv run flake8

run-clean:
	@find . -type f -name '*.pyc' -delete
	@find . -type d -name '__pycache__' -delete

