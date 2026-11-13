LATEXMK := latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error
BUILD := build

.PHONY: all post post-screen clean

all: post post-screen

$(BUILD):
	mkdir -p $(BUILD)

# A4 reading layout (class default).
post: | $(BUILD)
	$(LATEXMK) -outdir=$(BUILD) -jobname=saim-post main.tex

# 160 x 240 mm screen layout.
post-screen: | $(BUILD)
	printf '%s\n' '\PassOptionsToClass{screen}{saim-blog}\input{main.tex}' > $(BUILD)/post-screen-driver.tex
	$(LATEXMK) -outdir=$(BUILD) -jobname=saim-post-screen $(BUILD)/post-screen-driver.tex
	rm -f $(BUILD)/post-screen-driver.tex

clean:
	rm -rf $(BUILD)
