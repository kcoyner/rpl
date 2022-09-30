# Makefile for rpl

all: rpl.1 README.md

lint:
	mypy --strict rpl
	pylint --disable=C,fixme,too-many-locals,too-many-branches,too-many-statements rpl

check:
	pytest --exe-clean-output --exe-runner tests/test-runner.sh

release: lint check
	git diff --exit-code && \
	rm -rf ./dist && \
	mkdir dist && \
	python3 setup.py sdist bdist_wheel && \
	twine upload dist/* && \
	git tag v$$(python3 setup.py --version) && \
	git push --tags

clean:
	rm -f rpl.1

rpl.1: Makefile rpl man-include.1
	COLUMNS=999 help2man --locale=C.UTF-8 --no-info --name="replace strings in files" --include man-include.1 ./rpl > rpl.1

README.md: rpl README.md.in Makefile
	cp README.md.in README.md
	printf '\n```\n' >> README.md
	./rpl --help >> README.md
	printf '```\n' >> README.md
