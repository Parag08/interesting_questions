package repositry

import (
	"github.com/parag08/interesting_questions/simpl/models"
	"github.com/parag08/interesting_questions/simpl/utils"
)

var (
	UserMap = make(map[string]*models.User)
)

func CreateUser(user models.User) error {
	if _, ok := UserMap[user.PhoneNumber]; !ok {
		return utils.ErrDuplicateUser
	}
	UserMap[user.PhoneNumber] = &user
	return nil
}

func UpdateUser(user models.User) error {
	return nil
}

func GetUser(phoneNumber string) (*models.User, error) {
	if val, ok := UserMap[phoneNumber]; ok {
		return val, nil
	}
	return nil, utils.ErrUserNotFound
}
