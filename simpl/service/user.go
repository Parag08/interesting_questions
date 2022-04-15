package service

import (
	"encoding/json"

	"github.com/parag08/interesting_questions/simpl/models"
	"github.com/parag08/interesting_questions/simpl/repositry"
	"github.com/parag08/interesting_questions/simpl/utils"
)

func CreateUser(input string) error {
	var (
		user models.User
		err  error
	)
	err = json.Unmarshal([]byte(input), &user)
	if err != nil {
		return utils.ErrInvalidInput
	}
	return repositry.CreateUser(user)
}
