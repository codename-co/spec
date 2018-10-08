const { matchingDOM } = require('./helpers/dom')

function validate (specFile, uri) {
  const spec = parse(specFile)

  // if (matchingDOM(`<a class="tag"><span>aa</span></a>`, dom)) {
  //   debug(' > MATCHING')
  // }
}

module.exports = {
  validate
}
