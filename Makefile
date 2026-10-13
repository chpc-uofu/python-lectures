PYTHON ?= python3
VENV ?= .venv
PIP := $(VENV)/bin/pip
JUPYTER := $(VENV)/bin/jupyter
CONTENT_DIR := _lite_content
OUTPUT_DIR := _output
PORT ?= 8000

.DEFAULT_GOAL := build
.PHONY: install prepare build check serve clean distclean

$(JUPYTER): requirements-jupyterlite.txt
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements-jupyterlite.txt

install: $(JUPYTER)

prepare:
	rm -rf $(CONTENT_DIR)
	mkdir -p $(CONTENT_DIR)/notebooks $(CONTENT_DIR)/images
	rsync -a notebooks/ $(CONTENT_DIR)/notebooks/
	rsync -a images/ $(CONTENT_DIR)/images/

build: $(JUPYTER) prepare jupyter_lite_config.json
	$(JUPYTER) lite build

check: build
	test -f $(OUTPUT_DIR)/jupyter-lite.json
	test -f $(OUTPUT_DIR)/api/contents/all.json
	test -f $(OUTPUT_DIR)/files/notebooks/lectures/03_strings.ipynb
	test -f $(OUTPUT_DIR)/files/images/strings.svg
	@printf '%s\n' 'JupyterLite site and course assets verified in $(OUTPUT_DIR)/'

serve: build
	$(VENV)/bin/python -m http.server $(PORT) --directory $(OUTPUT_DIR)

clean:
	rm -rf $(CONTENT_DIR) $(OUTPUT_DIR)

distclean: clean
	rm -rf $(VENV)
