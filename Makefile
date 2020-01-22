init:
	pip install -e .[dev]

build:
	python setup.py sdist bdist_wheel

publish: build
	twine check dist/*
	twine upload dist/*

# Clean python build files
clean-build:
	rm -rf substratum.egg-info
	rm -rf build
	rm -rf dist
	rm -rf .eggs

clean: clean-build
