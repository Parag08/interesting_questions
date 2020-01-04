const express = require('express');
const validate = require('express-validation');
const controller = require('../../controllers/product.controller');
const {
  createProduct,
} = require('../../validations/product.validation');

const router = new express.Router();

router.route('/')
    .get(controller.list);

router.route('/')
    .post(validate(createProduct), controller.create);

router.route('/:productId')
    .patch(controller.modify);

router.route('/:productId')
    .get(controller.get);

router.route('/:productId')
    .delete(controller.delete);


module.exports = router;
