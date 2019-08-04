# Makefile for rpl

rpl.1: rpl man-include.1
	help2man --locale=en_US.UTF-8 --no-info --include man-include.1 ./rpl > rpl.1
