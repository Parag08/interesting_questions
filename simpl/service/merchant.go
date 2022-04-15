package service

import (
	"encoding/json"

	"github.com/parag08/interesting_questions/simpl/models"
	"github.com/parag08/interesting_questions/simpl/repositry"
	"github.com/parag08/interesting_questions/simpl/utils"
)

func CreateMerchant(input string) error {
	var (
		err      error
		merchant models.Merchant
	)
	err = json.Unmarshal([]byte(input), &merchant)
	if err != nil {
		return utils.ErrInvalidInput
	}
	return repositry.CreateMerchant(merchant)
}
