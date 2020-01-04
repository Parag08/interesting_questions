const mongoose = require('mongoose');

const reviewSchema = new mongoose.Schema({
  review: {
    type: String,
    required: true,
  },
  rating: {
    type: Number,
    required: true,
  },
  headline: {
    type: String,
    required: true,
  },
  user: {
    type: String,
    required: true,
  },
  productId: {
    type: mongoose.Schema.Types.ObjectId,
  },
  approved: {
    type: Boolean,
    default: false,
  },
  images: [{
    type: String,
  }],
}, {
  timestamps: true,
});

const Review = mongoose.model('Review', reviewSchema);
module.exports = Review;
