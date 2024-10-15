CXX = g++
DEPENDENCIES = \
	sfml-graphics-2\
	sfml-window-2\
	sfml-system-2

.PHONY: default
default: debug

setup:
	mkdir bin
	cp -r lib/* bin/

debug:
	$(CXX) src/*\
		-L lib $(foreach dep, $(DEPENDENCIES), -l$(dep))\
		-I include\
		-o bin/cavendish.exe