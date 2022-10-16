# Makefile for rpl maintainer tasks

all: README.md

release:
	tox && \
	git diff --exit-code && \
	rm -rf ./dist && \
	mkdir dist && \
	python3 setup.py sdist bdist_wheel && \
	twine upload dist/* && \
	git tag v$$(python3 setup.py --version) && \
	git push --tags

README.md: rpl README.md.in Makefile
	cp README.md.in README.md
	printf '\n```\n' >> README.md
	./rpl --help >> README.md
	printf '```\n' >> README.md
