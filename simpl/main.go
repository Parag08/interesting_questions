package main

import (
	"fmt"

	"github.com/parag08/interesting_questions/simpl/service"
)

func main() {
	driver("createMerchant", "{}")
}

func driver(operation string, payload string) {
	switch operation {
	case "createMerchant":
		service.CreateMerchant(payload)
	case "createUser":
		service.CreateUser(payload)
	case "createTransaction":
		fmt.Println(service.CreateTransactions(payload))
	}
}
