const logger = require('../../config/logger');
const reviewService = require('../services/review.service');

exports.get = async (req, res, next) => {
  logger.info('review.controller: get: ');
  try {
    reviewId = req.params.reviewId;
    review = await reviewService.get(reviewId);
    res.status(200).json(review);
  } catch (error) {
    logger.error(error);
    next(error);
  }
};

exports.list = async (req, res, next) => {
  logger.info('review.controller: list: ');
  try {
    productId = req.params.productId;
    reviews = await reviewService.list(productId);
    res.status(200).json(reviews);
  } catch (error) {
    logger.error(error);
    next(error);
  }
};

exports.create = async (req, res, next) => {
  logger.info('review.controller: create: ');
  try {
    review = await reviewService.create(req.params.productId, req.body);
    res.status(201).json(review);
  } catch (error) {
    logger.error(error);
    next(error);
  }
};

exports.modify = async (req, res, next) => {
  logger.info('review.controller: modify: ');
  try {
    reviewId = req.params.reviewId;
    review = {'message': 'not yet implemented'};
    res.status(200).json(review);
  } catch (error) {
    logger.error(error);
    next(error);
  }
};

exports.delete = async (req, res, next) => {
  logger.info('review.controller: delete: ');
  try {
    reviewId = req.params.reviewId;
    await reviewService.delete(reviewId);
    res.status(201).json();
  } catch (error) {
    logger.error(error);
    next(error);
  }
};

exports.approve = async (req, res, next) => {
  logger.info('review.controller: approve');
  try {
    reviewId = req.params.reviewId;
    review = await reviewService.approve(reviewId);
    res.status(200).json(review);
  } catch (error) {
    logger.error(error);
    next(error);
  }
};

exports.getRating = async (req, res, next) => {
  logger.info('review.controller: getRatting');
  try {
    productId = req.params.productId;
    response = await reviewService.getRating(productId);
    res.status(200).json(response);
  } catch (error) {
    logger.error(error);
    next(error);
  }
};
