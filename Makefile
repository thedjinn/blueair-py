.PHONY: all clean test publish build

all: build

clean:
	rm -rf build/ dist/ __pycache__/ blueair.egg-info/

test:
	flake8
	mypy .

build:
	python setup.py sdist bdist_wheel

publish: build
	git push origin
	git push origin --tags
	$(MAKE) clean build
	twine upload dist/*
	$(MAKE) clean
