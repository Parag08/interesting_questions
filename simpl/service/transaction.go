package service

import (
	"encoding/json"

	"github.com/parag08/interesting_questions/simpl/models"
	"github.com/parag08/interesting_questions/simpl/repositry"
	"github.com/parag08/interesting_questions/simpl/utils"
)

type CreatetransactionRequestStruct struct {
	PhoneNumber string `json:"phoneNumber"`
	Amount      int    `json:"amount"`
	MerchantId  int    `json:"merchantId"`
	Currency    string `json:"currency"`
}

func CreateTransactions(input string) (int, error) {
	var (
		err     error
		request CreatetransactionRequestStruct
	)
	err = json.Unmarshal([]byte(input), &request)
	if err != nil {
		return 0, utils.ErrInvalidInput
	}
	// Get user
	if request.PhoneNumber == "" {
		return 0, utils.ErrInvalidInput
	}
	user, err := repositry.GetUser(request.PhoneNumber)
	if err != nil {
		return 0, err
	}
	// Get merchant
	merchant, err := repositry.GetMerchant(request.MerchantId)
	if err != nil {
		return 0, err
	}
	// Create transaction
	if user.TotalLimit-user.CurrentUsage <= request.Amount {
		user.CurrentUsage += request.Amount
		// think back
		ourCut := request.Amount * merchant.CutRate / 100
		merchantEarning := request.Amount - ourCut
		transaction := models.Transaction{
			User:       user,
			Merchant:   merchant,
			Amount:     request.Amount,
			Curreny:    request.Currency,
			OurEarning: ourCut,
		}
		merchant.TotalPayout = merchant.TotalPayout + merchantEarning
		transactionId, err := repositry.CreateTransactions(transaction)
		if err != nil {
			return 0, err
		}
		return transactionId, err
	} else {
		return 0, utils.ErrUserSpendLimitExceeded
	}
}
