const fs = require('fs')
const pug = require('pug')
const mkdirp = require('mkdirp')
const { warn } = require('loglevel')
const { parse } = require('./parser')

const OUTPUT_DIR = `build/`

function generateDoc (specFile, { template = 'templates/simple.pug' }) {
  const spec = parse(specFile)
  let output
  if (spec.docTemplate) {
    output = pug.render(spec.docTemplate, spec)
  } else {
    if (!fs.existsSync(template)) {
      warn(`The file "${template}" doesn't exist. Please check your template file path.`)
      process.exit(1)
    }
    output = pug.renderFile(template, spec)
  }
  const path = `${OUTPUT_DIR}${spec.name}${spec.version ? `/${spec.version}` : ''}`
  mkdirp.sync(path)
  fs.writeFileSync(`${path}/index.html`, output)
}

module.exports = {
  generateDoc
}
