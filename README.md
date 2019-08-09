# Plotly Express

Plotly Express is now part of Plotly.py version 4 and so the `plotly_express` module now just re-exports the contents of `plotly.express`

## Installation

If you follow the [`plotly` Getting Started](https://plot.ly/python/getting-started/) instructions for installation, you will get access to `plotly.express`.

However, if you have existing code that imports from `plotly_express` explicitly and you don't wish to change it, you can still install the latest version, which just exposes `plotly.express` under the `plotly_express` namespace.

### Via `pip`

Just running `pip install plotly_express==0.4.1` in your terminal should do it!

### Via `conda`

You'll have to install from the `plotly` channel with `conda install -c plotly plotly_express==0.4.1`

## Getting Help

Please join our [Community Forum](https://community.plot.ly/c/api/python) or file a [Github Issue](https://github.com/plotly/plotly.py/issues/new) if you've found a bug.
