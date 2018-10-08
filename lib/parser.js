const fs = require('fs')
const eno = require('enojs')
const { debug, error } = require('loglevel')
const { expandEmmet } = require('./helpers/dom')

function parse (specFile) {
  if (!fs.existsSync(specFile)) {
    error(`The file "${specFile}" doesn't exist. Please check your spec file path.`)
    process.exit(1)
  }

  const input = fs.readFileSync(specFile, 'utf-8')
  const document = eno.parse(input, { reporter: 'terminal' })

  const result = {
    name: document.field('name'),
    title: document.field('title'),
    version: document.field('version'),
    language: document.field('language'),
    author: document.field('author'),
    stylesheet: document.field('stylesheet'),
    homepage: document.field('homepage'),
    description: document.field('description'),
    docTemplate: document.field('doc template'),
    categories: {}
  }

  const categories = document.elements().filter(e => e.instruction.type === 'SECTION')

  for (const category of categories) {
    const categoryName = category.name
    debug(categoryName)

    result.categories[category.name] = {
      name: category.name,
      elements: []
    }

    for (const elem of category._elements) {
      debug('-', elem.name)
      const element = {}
      element.name = elem.name
      element.desc = elem.field('desc')

      // element DOM
      let dom
      try {
        dom = [elem.field('dom')]
      } catch (e) {
        dom = elem.list('dom')
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
        debug(`No modifiers found for ${elem.name}`)
      }

      // element examples
      try {
        const examples = Object.assign(...elem.section('examples').raw().examples)
        const defaultExample = examples.default
        examples.default = expandEmmet(defaultExample)
        const examplesWithModifiers = Object.keys(examples).filter(name => name !== 'default')
        examplesWithModifiers.forEach(name => {
          const description = examples[name]
          const modifiers = element.modifiers[name]
          examples[name] = {
            description,
            code: modifiers.map(mod => expandEmmet(defaultExample.replace(/^([#.\w\d\-_[\]]+)/i, `$1.${mod}`)))
          }
        })
        element.examples = examples
      } catch (e) {
        debug(`No examples found for ${elem.name}`)
      }

      // element parents
      element.parents = elem.list('parents')

      result.categories[category.name].elements.push(element)
    }
  }

  return result
}

function iterateElement (elem, section) {
  const collection = elem.section(section).elements()
  return Object.assign(...collection.map(e => ({ [e.name]: e.items() })))
}

module.exports = {
  parse
}
