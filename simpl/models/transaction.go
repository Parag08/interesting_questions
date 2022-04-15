package models

type Transaction struct {
	Amount     int       `json:"amount"` // 1.00 INR = 100 INR
	User       *User     `json:"user"`
	Merchant   *Merchant `json:"merchant"`
	Curreny    string    `json:"currency"`
	OurEarning int       `json:"ourEarning"`
}
