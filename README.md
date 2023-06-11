# My personal cookbook

Currently the content is only in italian.

See it
[live](https://pitrified.github.io/cookbook/)!

# Develop/Deploy

## Setup jekyll

* https://jekyllrb.com/docs/installation/
* https://jekyllrb.com/docs/step-by-step/01-setup/

Add to .bashrc:

```bash
export GEM_HOME=$HOME/.gem
export GEM_PATH=$HOME/.gem
```

```bash
sudo apt install ruby-full
sudo gem install jekyll bundler
cd ghpages
bundle install
bundle add webrick # might be in the Gemfile now
```

## Develop

```bash
cd ghpages
bundle exec jekyll serve --livereload
```

## Deploy

The generate files are in the ghpages folder in the main branch.

To update the site, the modifications must be pushed on the gh-pages branch:

```bash
git subtree push --prefix ghpages origin gh-pages
```
