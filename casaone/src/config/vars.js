const path = require('path');


// import .env variables

try {
  require('dotenv-safe').config({
    path: path.join(__dirname, '../../.env'),
    sample: path.join(__dirname, '../../.env.example'),
  });
} catch (error) {
  console.log(error);
  console.log('conuldnot include env files runnning in docker mode');
}


module.exports = {
  env: process.env.NODE_ENV,
  port: process.env.PORT,
  mongo: {
    uri: process.env.NODE_ENV === 'test' ?
      process.env.MONGO_URI_TESTS :
      process.env.MONGO_URI,
  },
  logs: process.env.NODE_ENV === 'production' ? 'combined' : 'dev',
};
