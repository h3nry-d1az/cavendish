CXX = g++

.PHONY: default
default: debug

setup:
	mkdir bin
	cp -r lib/* bin/

debug:
	$(CXX) src/* -L lib -lsfml-graphics-2 -lsfml-window-2 -lsfml-system-2 -I include -o bin/cavendish.exe