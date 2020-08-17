lint:
	poetry run flake8 gendiff

test:
	poetry run pytest --cov .

build:
	poetry build

publish:
	poetry publish -r avatara_gendiff
