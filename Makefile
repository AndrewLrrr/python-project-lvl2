lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

build:
	poetry build

publish:
	poetry publish -r avatara_gendiff
