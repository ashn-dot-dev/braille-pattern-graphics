.POSIX:
.PHONY: all main lint format clean

all: main

main:
	python3 main.py

lint:
	python3 -m mypy *.py
	python3 -m flake8 *.py --ignore=E203,E221,E241,W503

format:
	python3 -m black *.py --line-length 79

clean:
	rm -rf __pycache__
	rm -rf .mypy_cache/