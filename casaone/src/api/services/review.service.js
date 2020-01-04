/* eslint-disable guard-for-in */
const Product = require('../models/product.model');
const Review = require('../models/review.model');

exports.create = async (productId, review) => {
  try {
    product = await Product.findById(productId);
    if (product) {
      if (product.owners.includes(review.user)) {
        review.productId = productId;
        const newReview = new Review(review);
        await newReview.save();
        return newReview;
      } else {
        throw new Error('only user who buy product can create reviews');
      }
    } else {
      throw new Error('product not found');
    }
  } catch (error) {
    throw error;
  }
};

exports.list = async (productId) => {
  try {
    const reviews = await Review.find({productId: productId});
    return reviews;
  } catch (error) {
    throw error;
  }
};

exports.get = async (id) => {
  try {
    const review = await Review.findById(id);
    return review;
  } catch (error) {
    throw error;
  }
};

exports.delete = async (id) => {
  try {
    const review = await Review.findById(id);
    await review.remove();
    return;
  } catch (error) {
    throw error;
  }
};

exports.approve = async (id) => {
  try {
    const review = await Review.findById(id);
    review.approved = true;
    review.save();
    product = await Product.findById(review.productId);
    if (!product.reviews.includes(review._id)) {
      product.reviews.push(review);
    }
    product.save();
    return review;
  } catch (error) {
    throw error;
  }
};

exports.getRating = async (productId) => {
  try {
    const product = await Product.findById(productId);
    if (product) {
      let rating = 0;
      reviews = await Review.find({'_id': {'$in': product.reviews}});
      for (review in reviews) {
        review = reviews[review];
        rating = rating + review.rating;
      }
      return {'rating': rating/reviews.length, 'number': reviews.length};
    } else {
      throw new Error('product not found');
    }
  } catch (error) {
    throw error;
  }
};
