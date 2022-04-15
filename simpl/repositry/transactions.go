package repositry

import (
	"github.com/parag08/interesting_questions/simpl/models"
)

var (
	transactionId  = 0
	transactionMap = make(map[int]*models.Transaction)
)

func CreateTransactions(Transaction models.Transaction) (int, error) {
	transactionId = transactionId + 1
	transactionMap[transactionId] = &Transaction
	return transactionId, nil
}
