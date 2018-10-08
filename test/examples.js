const { generateDoc } = require('../lib')

const SPEC_DIR = './examples/'
const SPECS = [
  'mini-3.0.0.spec',
  'bulma-0.7.1.spec'
]
SPECS.forEach(spec => generateDoc(`${SPEC_DIR}${spec}`))
