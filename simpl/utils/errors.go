package utils

import "errors"

var (
	ErrDuplicateUser          = errors.New("duplicate user")
	ErrInvalidInput           = errors.New("invalid input")
	ErrUserNotFound           = errors.New("user not found")
	ErrMerchantNotFound       = errors.New("merchant not found")
	ErrUserSpendLimitExceeded = errors.New("user spend limit exceeded")
)
