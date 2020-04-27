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
cp ../*.md source/ # this prepares all your .md files to show up in sphinx's output
sphinx-apidoc -f -o source/ ../intropy # this prepares all your .py files to show up in sphinx's outputcd .
make clean && make html
```

## Viewing the docs

```bash
open docs/build/html/index.html
```

## Pushing out changes to github pages

```bash
git checkout gh-pages
git pull
git merge master
git subtree push --prefix docs/build/html origin gh-pages
```

# But can we handle markdown?

- that
- is
- a
- *great*
- question

> time to find out

she said.