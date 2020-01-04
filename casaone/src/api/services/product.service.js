const Product = require('../models/product.model');

exports.create = async (product) => {
  try {
    const newProduct = new Product(product);
    await newProduct.save();
    return newProduct;
  } catch (error) {
    throw error;
  }
};

exports.list = async (query) => {
  try {
    const products = await Product.find({});
    return products;
  } catch (error) {
    throw error;
  }
};

exports.get = async (id) => {
  try {
    const product = await Product.findById(id);
    return product;
  } catch (error) {
    throw error;
  }
};

exports.delete = async (id) => {
  try {
    const product = await Product.findById(id);
    await product.remove();
    return;
  } catch (error) {
    throw error;
  }
};
