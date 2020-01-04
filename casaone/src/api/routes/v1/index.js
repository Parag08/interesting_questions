const express = require('express');

const router = new express.Router();

const productRoutes = require('./product.routes');
const reviewRoutes = require('./review.routes');

/**
 * GET v1/status
 */
router.get('/status', (req, res) => res.send('OK'));

router.use('/product', productRoutes);
router.use('/review', reviewRoutes);

module.exports = router;
