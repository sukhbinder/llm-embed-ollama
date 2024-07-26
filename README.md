# llm-embed-ollama

[![PyPI](https://img.shields.io/pypi/v/llm-embed-ollama.svg)](https://pypi.org/project/llm-embed-ollama/)
[![Changelog](https://img.shields.io/github/v/release/sukhbinder/llm-embed-ollama?include_prereleases&label=changelog)](https://github.com/sukhbinder/llm-embed-ollama/releases)
[![Tests](https://github.com/sukhbinder/llm-embed-ollama/workflows/Test/badge.svg)](https://github.com/sukhbinder/llm-embed-ollama/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/sukhbinder/llm-embed-ollama/blob/main/LICENSE)

Embedding models using Ollama

## Background

Ollama provides Few embedding models. This plugin enables the usage of those models using Ollama.

To utilize these models, you need to have an instance of the Ollama server running.

See also [Embeddings: What they are and why they matter](https://simonillison.net/2023/Oct/23/embeddings/) for background on embeddings and an explanation of the LLM embeddings tool.


## Installation

Install this plugin in the same environment as [LLM](https://llm.datasette.io/).

    llm install llm-embed-ollama

## Usage

This plugin adds support for three new embedding models:

- all-minilm
- nomic-embed-text
- mxbai-embed-large

The models needs to be downloaded. Using `ollama pull <model-name> the first time you try to use them.

See [the LLM documentation](https://llm.datasette.io/en/stable/embeddings/index.html) for everything you can do.

To get started embedding a single string, run the following:

```bash
llm embed -m all-minilm -c 'Hello world'
```
This will output a JSON array of 384 floating point numbers to your terminal.

To calculate and store embeddings for every README in the current directory (try this somewhere with a `node_modules` directory to get lots of READMEs) run this:

```bash
llm embed-multi ollama-readmes \
    -m all-minilm \
    --files . '**/README.md' --store
```
Then you can run searches against them like this:
```bash
llm similar ollama-readmes -c 'utility functions'
```
Add `| jq` to pipe it through [jq](https://jqlang.github.io/jq/) for pretty-printed output, or ` | jq .id` to just see the matching filenames.

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd llm-embed-ollama
python3 -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
llm install -e '.[test]'
```
To run the tests:
```bash
pytest
```
