# Clean python build files
clean-build:
	rm -rf substratum.egg-info
	rm -rf build
	rm -rf dist
	rm -rf .eggs

clean: clean-build
