const Joi = require('joi');


module.exports = {
  createProduct: {
    body: {
      productName: Joi.string().required(),
      color: Joi.string().required(),
      finish: Joi.string().required(),
      purchasePrice: Joi.string().required(),
      images: Joi.array(),
      totalQty: Joi.number(),
      soldQty: Joi.number(),
      owners: Joi.array(),
    },
  },
};
