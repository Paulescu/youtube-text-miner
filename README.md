# Youtube text miner

## What is this repo about
This repo contains a useful script to quickly build your own textual dataset from Youtube.

Go checkout my original [blog](http://datamachines.xyz/2021/07/13/how-to-scrape-your-own-nlp-datasets/) and [subscribe](https://datamachines.xyz/subscribe/)
to my newsletter if you want become a better data scientist.

## Setup

You need Python >= 3.7 and a tool to install the exact packages you need for this
code to run as expected.

Two popular tools are virtualenv (a bit old) and [poetry](https://python-poetry.org/) (my favourite).

Instructions for virtualenv:
```
...cd into the root directory...
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Instructions for Poetry:

```
.. install poetry if you haven't
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

.. cd into the root directory of the repo
$ poetry install
```

## Example

```bash
python data.py --keyword "louis ck stand up" --n_samples 10 --output ./example.json
```