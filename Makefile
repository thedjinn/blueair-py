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
	$(MAKE) clean build
	twine upload dist/*
	$(MAKE) clean
	$(eval TAG=v$(shell python -c "from blueair import __version__; print(__version__)"))
	git tag $(TAG)
