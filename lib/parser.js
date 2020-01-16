const fs = require('fs')
const enolib = require('enolib')
const { TerminalReporter } = require('enolib');
const { debug, error } = require('loglevel')
const { expandEmmet } = require('./helpers/dom')

function parse (specFile) {
  if (!fs.existsSync(specFile)) {
    error(`The file "${specFile}" doesn't exist. Please check your spec file path.`)
    process.exit(1)
  }

  const input = fs.readFileSync(specFile, 'utf-8')
  const document = enolib.parse(input, { reporter: TerminalReporter })

  const result = {
    name: document.field('name').requiredStringValue(),
    title: document.field('title').requiredStringValue(),
    version: document.field('version').requiredStringValue(),
    language: document.field('language').requiredStringValue(),
    author: document.field('author').requiredStringValue(),
    stylesheet: document.field('stylesheet').requiredStringValue(),
    homepage: document.field('homepage').requiredStringValue(),
    description: document.field('description').requiredStringValue(),
    docTemplate: document.field('doc template').optionalStringValue(),
    categories: {}
  }

  const categories = document.elements()
                             .filter(element => element.yieldsSection())
                             .map(element => element.toSection())

  for (const category of categories) {
    const categoryName = category.stringKey()
    debug(categoryName)

    result.categories[categoryName] = {
      name: categoryName,
      elements: []
    }

    for (const elem of category.sections()) {
      debug('-', elem.stringKey())
      const element = {}
      element.name = elem.stringKey()
      element.desc = elem.field('desc').optionalStringValue()

      // element DOM
      let dom
      if(elem.element('dom').yieldsField()) {
        dom = [elem.field('dom').requiredStringValue()]
      } else {
        dom = elem.list('dom').requiredStringValues()
      }
      dom = dom.map(expandEmmet)
      element.dom = dom

      // element modifiers
      try {
        element.modifiers = {}
        const modifiers = iterateElement(elem, 'modifiers')
        element.modifiers =
          Object.assign(...Object.keys(modifiers).map(mod => ({ [mod]: modifiers[mod] })))
        element.modifiers = element.modifiers.map(mod => expandEmmet(mod).html)
      } catch (e) {
        debug(`No modifiers found for ${element.name}`)
      }

      // element examples
      if(elem.optionalSection('examples') !== null) {
        const examples =
          elem.section('examples').fields().reduce((obj, field) => ({ ...obj, [field.stringKey()]: field.requiredStringValue() }), {})
        const defaultExample = examples.default
        examples.default = expandEmmet(defaultExample)
        const examplesWithModifiers = Object.keys(examples).filter(name => name !== 'default')
        examplesWithModifiers.forEach(name => {
          const description = examples[name]
          const modifiers = element.modifiers[name]
          examples[name] = {
            description,
            code: modifiers.map(mod => expandEmmet(defaultExample.replace(/^([#.\w\d\-_:]+)/i, `$1.${mod}`)))
          }
        })
        element.examples = examples
      } else {
        debug(`No examples found for ${element.name}`)
      }

      // element parents
      element.parents = elem.list('parents').requiredStringValues()

      result.categories[categoryName].elements.push(element)
    }
  }

  return result
}

function iterateElement (elem, section) {
  const collection = elem.section(section).lists()
  return collection.reduce((obj, list) => ({ ...obj, [list.stringKey()]: list.requiredStringValues() }), {})
}

module.exports = {
  parse
}
