# Probability Notes: build, check and package posts.
#   make build P=01-debruijn   A4 + screen PDFs in build/01-debruijn/build/
#   make check P=01-debruijn   run the numerical check
#   make tweets P=01-debruijn  weighted tweet lengths
#   make qa P=01-debruijn      build + log scan + fonts + tweets
#   make zip P=01-debruijn     dist/pn_01_debruijn.zip (Overleaf-ready, PDFs in pdf/)
#   make pdfs P=01-debruijn    copy built PDFs into docs/posts/<P>/pdf/
#   make new P=02-sure         start a post from skeleton/new-post
#   make formats P=01-debruijn img/figure-N.png, article.md, notebook.ipynb (executed)
#   make verify P=01-debruijn  check article.md links/conversion and notebook outputs
#   make site                  build site/ (accepted/published posts only); SITE_ALL=1 adds drafts
#   make pages                 commit site/ to the gh-pages branch; PUSH=1 also pushes
#   make all                   qa + verify for every post
P ?=
POSTS := $(notdir $(wildcard docs/posts/[0-9]*))
NUM   = $(firstword $(subst -, ,$(P)))
SLUG  = $(patsubst $(NUM)-%,%,$(P))
B     = build/$(P)

.PHONY: build check tweets qa zip pdfs new formats verify site pages all clean need-p
need-p:
	@test -n "$(P)" || (echo "set P=<post>, one of: $(POSTS)"; exit 1)

build: need-p
	scripts/assemble.sh $(P) >/dev/null
	$(MAKE) -C $(B) >/dev/null

check: need-p
	cd docs/posts/$(P) && python3 code/check.py

tweets: need-p
	python3 scripts/wlen.py docs/posts/$(P)/post.txt docs/posts/$(P)/tweet.txt

qa: build tweets
	@n=$$(grep -hE "Warning|Overfull|Underfull|^!|undefined" $(B)/build/*.log | grep -v infwarerr | wc -l); \
	 echo "log issues: $$n"; test $$n -eq 0
	@n=$$(pdffonts $(B)/build/saim-post.pdf | tail -n +3 | grep -vc "Type 1" || true); \
	 echo "non-Type-1 fonts: $$n"; test $$n -eq 0

pdfs: build
	cp $(B)/build/saim-post.pdf docs/posts/$(P)/pdf/pn-$(NUM)-$(SLUG).pdf
	cp $(B)/build/saim-post-screen.pdf docs/posts/$(P)/pdf/pn-$(NUM)-$(SLUG)-screen.pdf

zip: need-p
	scripts/assemble.sh $(P) >/dev/null
	mkdir -p dist && rm -f dist/pn_$(NUM)_$(SLUG).zip
	cd $(B) && rm -rf build && zip -qr ../../dist/pn_$(NUM)_$(SLUG).zip .
	@echo dist/pn_$(NUM)_$(SLUG).zip

formats: build
	python3 scripts/figures.py $(P)
	python3 scripts/tex2md.py $(P)
	python3 scripts/make_notebook.py $(P) 2>/dev/null

verify: need-p
	python3 scripts/verify_formats.py $(P)

site:
	python3 scripts/build_site.py $(if $(SITE_ALL),--all) $(if $(PAGES_REPO),--repo $(PAGES_REPO))

pages:
	scripts/publish_pages.sh $(if $(PUSH),--push)

new: need-p
	@test ! -e docs/posts/$(P) || (echo "docs/posts/$(P) exists"; exit 1)
	mkdir -p docs/posts/$(P)/pdf
	cp -r skeleton/new-post/. docs/posts/$(P)/
	sed -i.bak 's/"NN"/"$(NUM)"/; s/"SLUG"/"$(SLUG)"/' docs/posts/$(P)/meta.json && rm -f docs/posts/$(P)/meta.json.bak
	@echo "created docs/posts/$(P)"

all:
	@for p in $(POSTS); do echo "== $$p"; $(MAKE) --no-print-directory qa P=$$p && $(MAKE) --no-print-directory verify P=$$p || exit 1; done

clean:
	rm -rf build dist site
