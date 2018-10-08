# Spec

**Spec** is a CSS Framework specification toolkit.

It can:

- specify a CSS framework requirements
- generate its documentation
- validate a DOM for its spec and guidelines conformance

## Getting started

```shell
# install the spec `cli`:
npm install -g @codename/spec

# generate documentation for a spec
spec doc examples/mini-3.0.0.spec

# generate documentation using a custom template
spec doc examples/bulma-0.7.1.spec -t examples/bulma.pug
```

## Features

### Framework specification

Spec helps specify a CSS framework requirements and usage with the help of a `.spec` file that relies on the [eno](https://eno-lang.org/) notation language, which is quite similar to [TOML](https://github.com/toml-lang/toml) with an easier to apprehend modern syntax.

### Documentation generation

_TBD_

### Validation & conformance

_TBD_
