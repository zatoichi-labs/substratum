# Clean python build files
clean-build:
	rm -rf substratum.egg-info
	rm -rf build
	rm -rf dist

clean: clean-build
