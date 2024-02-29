.DEFAULT_GOAL:=help

.EXPORT_ALL_VARIABLES:

ifndef VERBOSE
.SILENT:
endif

# set default shell
SHELL=/usr/bin/env bash -o pipefail -o errexit

APP_VERSION ?= 0.1.0
VERSUIB ?= $(shell cat TAG)
POETRY_HOME ?= ${HOME}/.local/share/pypoetry
POETRY_BINARY ?= ${POETRY_HOME}/venv/bin/poetry
POETRY_VERSION ?= 1.3.2

version := 0.2.0

src.python := $(shell find ./src -type f -name "*.py" || :)
test.python := $(shell find ./tests -type f -name "*.py" || :)
scripts.python := $(shell find ./scripts -type f -name "*.py" || :)

python.pyc := $(shell find . -type f -name "*.pyc")
cache.dir := $(shell find . -type d -name __pycache__)
checkpoint.dir := $(shell find . -type d -name .ipynb_checkpoints)
mypy.cache.dir := $(shell find . -type d -name ".mypy_cache")
pytest.cache.dir := $(shell find . -type d -name ".pytest_cache")

dist.dir := dist
egg.dir := .eggs
build.dir := build
site.dir := site
output.dir := output

###################
# Build & Release #
###################

build.wheel := $(dist.dir) /




help:  ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z0-9_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

.PHONY: show-version
show-version:  ## Display version
	echo -n "${TAG}"


.PHONY: install
install:  ## Install monitoring_models with poetry
	@scripts/install.sh

.PHONY: publish
publish: ## Publish package to local.
	@$(call i, Publishing package .whl to pypi)
	${POETRY_BINARY} publish

## Run checks, test, and build.
release: check build 

$(build.wheel): $(src.python)
	@$(call i, Build the package wheel)
	${POETRY_BINARY} build

build: $(build.wheel) ## Build the distribution wheel.

.PHONY: clean
clean: ## Remove all build artifacts.
	rm -f $(python.pyc)
	rm -rf $(pytest.cache.dir)
	rm -rf $(cache.dir)

.PHONY: test
test: ${test.python} ${src.python} clean ## Run tests in the poetry environment.
	@$(call i, Running tests)
	${POETRY_BINARY} run pytest -c=configs/pytest.ini ${test.python}


