const { parse } = require('./parser')
const { generateDoc } = require('./doc')
const { validate } = require('./validation')

module.exports = {
  parse,
  generateDoc,
  validate
}
