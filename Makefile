.PHONY: docs

clean: clean-eggs clean-build
	@find . -iname '*.pyc' -delete
	@find . -iname '*.pyo' -delete
	@find . -iname '*~' -delete
	@find . -iname '*.swp' -delete
	@find . -iname '__pycache__' -delete

clean-eggs:
	@find . -name '*.egg' -print0|xargs -0 rm -rf --
	@rm -rf .eggs/

clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info

setuptools:
	python -m pip install -U --upgrade setuptools wheel

twine:
	python -m pip install -U --upgrade twine

build: test setuptools
	python setup.py sdist bdist_wheel

release: clean build twine
	git rev-parse --abbrev-ref HEAD | grep '^master$$'
	git tag `python setup.py --version`
	git push origin `python setup.py --version`
	python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/* --verbose

lint:
	pre-commit run -a

test:
	pytest tests

pyformat:
	black .