# Проект: Вычислитель отличий

[![Build Status](https://travis-ci.org/AndrewLrrr/python-project-lvl2.svg?branch=master)](https://travis-ci.org/AndrewLrrr/python-project-lvl2)
[![Maintainability](https://api.codeclimate.com/v1/badges/68aae8cdee93e7efcc29/maintainability)](https://codeclimate.com/github/AndrewLrrr/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/68aae8cdee93e7efcc29/test_coverage)](https://codeclimate.com/github/AndrewLrrr/python-project-lvl2/test_coverage)

## Работа с проектом:
### Установка зависимостей:
```
poetry install
```
---
### Тесты:
```
make test
```
---
### Кодстайл:
```
make lint
```

## Сборка и публикация пакета:
### Установка репозитория:
```
poetry config repositories.avatara_gendiff https://test.pypi.org/legacy/
```
---
### Установка доступа к репозиторию:
```
poetry config http-basic.avatara_gendiff {login} {password}
```
---
### Сборка пакета:
```
make build
```
---
### Публикация пакета:
```
make publish
```

## Загрузка опубликованного пакета:
```
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple avatara_gendiff
```

## Примеры использования:
### Установка пакета:
<a href="https://asciinema.org/a/EhhCIpE6ioBEZGWQj8KojHUGA" target="_blank"><img src="https://asciinema.org/a/EhhCIpE6ioBEZGWQj8KojHUGA.svg" /></a>

### Сравнение файлов JSON:
<a href="https://asciinema.org/a/dowlgUZW21MJWM6C2ACiRV1dw" target="_blank"><img src="https://asciinema.org/a/dowlgUZW21MJWM6C2ACiRV1dw.svg" /></a>

### Сравнение файлов YAML:
<a href="https://asciinema.org/a/Df6gBN53ZmFFluuCbV9GXzSPV" target="_blank"><img src="https://asciinema.org/a/Df6gBN53ZmFFluuCbV9GXzSPV.svg" /></a>

### Сравнение файлов JSON --format=linear:
<a href="https://asciinema.org/a/S4QMZa3RmX3mIMOvdmnYfNcXN" target="_blank"><img src="https://asciinema.org/a/S4QMZa3RmX3mIMOvdmnYfNcXN.svg" /></a>

### Сравнение файлов YAML --format=linear:
<a href="https://asciinema.org/a/lwSEpxCx6y94ubcT7dCvB377j" target="_blank"><img src="https://asciinema.org/a/lwSEpxCx6y94ubcT7dCvB377j.svg" /></a>

### Сравнение файлов JSON --format=json:
<a href="https://asciinema.org/a/YQNAVeXopUri9CkSzJEsirR70" target="_blank"><img src="https://asciinema.org/a/YQNAVeXopUri9CkSzJEsirR70.svg" /></a>

### Сравнение файлов YAML --format=json:
<a href="https://asciinema.org/a/lyKbXXbK8hKs3nwmlhEqids6g" target="_blank"><img src="https://asciinema.org/a/lyKbXXbK8hKs3nwmlhEqids6g.svg" /></a> 