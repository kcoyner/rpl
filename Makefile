# Makefile for rpl

all: rpl.1

clean:
	rm -f rpl.1

rpl.1: Makefile rpl man-include.1
	help2man --locale=C.UTF-8 --no-info --include man-include.1 ./rpl > rpl.1
