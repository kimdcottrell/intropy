# Kim Gets Learnt 2020

## Generating docs

```bash
# this is horrible and I'm sure there's a better way
pip install -U sphinx
pip install sphinx_rtd_theme

# you don't need to run this again, but for docu's sake, init cmd was: 
sphinx-quickstart --ext-autodoc

# do this whenever you add to intropy
cd docs
sphinx-apidoc -f -o source/ ../intropy
make clean && make html
```

## Viewing the docs

```bash
open docs/build/html/index.html
```