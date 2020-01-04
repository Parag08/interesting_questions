const Joi = require('joi');


module.exports = {
  createReview: {
    body: {
      review: Joi.string().required(),
      rating: Joi.number().min(0).max(5).required(),
      headline: Joi.string().required(),
      user: Joi.string().required(),
    },
  },
};
