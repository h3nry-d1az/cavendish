release:
	pyinstaller main.py -n cavendish --noconsole --optimize 2
	cp -r assets/ dist/cavendish/