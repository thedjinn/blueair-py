.PHONY: all clean test publish build

all: build

clean:
	rm -rf build/ dist/ __pycache__/ blueair.egg-info/

test:
	flake8
	mypy .

build:
	python setup.py sdist bdist_wheel

release:
	# This is to be run outside of the Docker container
	$(eval TAG=v$(shell python -c "from blueair import __version__; print(__version__)"))
	@if [ $(shell git tag -l $(TAG)) ]; then echo "Tag $(TAG) already exists, did you forget to bump the version?"; exit 1; fi
	git tag -a $(TAG)
	git push --tags
	echo "Version tagged, now run \"make publish\" inside the container to push the image to PyPI."

publish: build
	$(MAKE) clean build
	twine upload dist/*
	$(MAKE) clean
