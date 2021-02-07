# Makefile for rpl

all: rpl.1

check:
	./rpl --version && \
	( ./rpl Lorem L-O-R-E-M < lorem.txt | egrep L-O-R-E-M || exit 1 ) && \
	( ./rpl -iv Lorem L-O-R-E-M < lorem.txt | egrep L-O-R-E-M || exit 1 ) && \
	( ./rpl -mv lorem loReM < lorem.txt | egrep -i lorem  || exit 1 ) && \
	( ./rpl -v 'a[a-z]+' 'coffee' < lorem.txt | egrep -i "coffee elit" || exit 1 )

release:
	rm -rf ./dist
	mkdir dist
	python3 setup.py sdist bdist_wheel
	twine upload dist/*

clean:
	rm -f rpl.1

rpl.1: Makefile rpl man-include.1
	COLUMNS=999 help2man --locale=C.UTF-8 --no-info --name="replace strings in files" --include man-include.1 ./rpl > rpl.1
