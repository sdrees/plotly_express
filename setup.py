from setuptools import setup, find_packages
from os import path

# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding
# Python 3 only projects can skip this import
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="plotly_express",
    version="0.4.1",  # sync with __version__ !
    description="Plotly Express - a high level wrapper for Plotly.py",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://plotly.express/",
    project_urls={"Github": "https://github.com/plotly/plotly_express/"},
    author="Nicolas Kruchten",
    author_email="nicolas@plot.ly",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Scientific/Engineering :: Visualization",
        "License :: OSI Approved :: MIT License",
    ],
    packages=find_packages(),
    install_requires=[
        "pandas>=0.20.0",
        "plotly>=4.1.0",
        "statsmodels>=0.9.0",
        "scipy>=0.18",
        "patsy>=0.5",
        "numpy>=1.11",
    ],
)
