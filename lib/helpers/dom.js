const { domIsLike, domAttrsIs } = require('eminent')
const { expand } = require('@emmetio/expand-abbreviation')
// const transform = require('@emmetio/html-transform')

function matchingDOM (html, doms) {
  return doms.map(dom => {
    try {
      // domIsLike(html, dom)
      domAttrsIs(html, dom)
      return true
    } catch (e) {
      return false
    }
  }).reduce((a, b) => a || b)
}

function expandEmmet (emmet) {
  return {
    emmet,
    html: expand(emmet)
  }
}

module.exports = {
  matchingDOM,
  expandEmmet
}
