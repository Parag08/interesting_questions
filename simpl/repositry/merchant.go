package repositry

import (
	"github.com/parag08/interesting_questions/simpl/models"
	"github.com/parag08/interesting_questions/simpl/utils"
)

var (
	merchantId  = 0
	merchantMap = make(map[int]*models.Merchant)
)

func CreateMerchant(merchant models.Merchant) error {
	merchantId = merchantId + 1
	merchantMap[merchantId] = &merchant
	return nil
}

func GetMerchant(merchantId int) (*models.Merchant, error) {
	if val, ok := merchantMap[merchantId]; ok {
		return val, nil
	}
	return nil, utils.ErrMerchantNotFound
}
