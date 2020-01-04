const express = require('express');
const validate = require('express-validation');
const controller = require('../../controllers/review.controller');
const {
  createReview,
} = require('../../validations/review.validation');

const router = new express.Router();

router.route('/:productId')
    .get(controller.list);

router.route('/:productId')
    .post(validate(createReview), controller.create);

router.route('/:reviewId')
    .patch(controller.modify);

router.route('/:reviewId')
    .get(controller.get);

router.route('/:reviewId')
    .delete(controller.delete);

router.route('/approve/:reviewId')
    .get(controller.approve);

router.route('/getRating/:productId')
    .get(controller.getRating);


module.exports = router;
