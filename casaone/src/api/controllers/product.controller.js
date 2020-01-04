const logger = require('../../config/logger');
const productService = require('../services/product.service');

exports.get = async (req, res, next) => {
  logger.info('product.controller: get: ');
  try {
    productId = req.params.productId;
    product = await productService.get(productId);
    res.status(200).json(product);
  } catch (error) {
    logger.error(error);
    next(error);
  }
};

exports.list = async (req, res, next) => {
  logger.info('product.controller: list: ');
  try {
    products = await productService.list(req.query);
    res.status(200).json(products);
  } catch (error) {
    logger.error(error);
    next(error);
  }
};

exports.create = async (req, res, next) => {
  logger.info('product.controller: create: ');
  try {
    product = await productService.create(req.body);
    res.status(201).json(product);
  } catch (error) {
    logger.error(error);
    next(error);
  }
};

exports.modify = async (req, res, next) => {
  logger.info('product.controller: modify: ');
  try {
    productId = req.params.productId;
    product = {'message': 'not implemented'};
    res.status(200).json(product);
  } catch (error) {
    logger.error(error);
    next(error);
  }
};

exports.delete = async (req, res, next) => {
  logger.info('product.controller: delete: ');
  try {
    productId = req.params.productId;
    await productService.delete(productId);
    res.status(204).json();
  } catch (error) {
    logger.error(error);
    next(error);
  }
};
