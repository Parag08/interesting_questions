const mongoose = require('mongoose');

const productSchema = new mongoose.Schema({
  productName: {
    type: String,
    required: true,
  },
  color: {
    type: String,
    required: true,
  },
  finish: {
    type: String,
    required: true,
  },
  purchasePrice: {
    type: String,
    required: true,
  },
  images: [{
    type: String,
  }],
  reviews: [{
    type: mongoose.Schema.Types.ObjectId,
    ref: 'Review',
  }],
  totalQty: {
    type: Number,
    default: 1,
  },
  soldQty: {
    type: Number,
    default: 0,
  },
  owners: [{
    type: String,
    default: 'admin',
  }],
}, {
  timestamps: true,
});

const Product = mongoose.model('Product', productSchema);
module.exports = Product;
