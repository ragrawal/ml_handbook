.PHONY: help book clean serve

help:
	@echo "Please use 'make <target>' where <target> is one of:"
	@echo "  install     to install the necessary dependencies for jupyter-book to build"
	@echo "  book        to convert the content/ folder into Jekyll markdown in _build/"
	@echo "  clean       to clean out site build files"
	@echo "  runall      to run all notebooks in-place, capturing outputs with the notebook"
	@echo "  serve       to serve the repository locally with Jekyll"
	@echo "  build       to build the site HTML locally with Jekyll and store in _site/"


install:
	# Check to see whether bundler is already installed. If not, install it.
	if [ hash bundler 2>/dev/null ]; then \
	gem install bundler;\
	fi
	bundle install

book:
	jupyter-book build ./

runall:
	jupyter-book run ./content

clean:
	python scripts/clean.py

serve:
	bundle exec guard

build:
	bundle exec jekyll build
	touch _site/.nojekyll

sitemap:
	python scripts/sitemap_generator.py
	s3cmd put -P _site/sitemap.txt s3://mlcompanion

ship:
	make clean
	make book
	python scripts/post_build_process.py
	make build
	cp _site/intro.html _site/index.html
	s3cmd put -P _site/*.html s3://mlcompanion
	make sitemap

