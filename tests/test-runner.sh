#!/bin/sh

../../rpl \
	{{rpl_options}} < input.txt \
	1> executable.stdout \
	2> executable.stderr
grep {{grep_options}} "{{grep_pattern}}" {{grep_file}}
