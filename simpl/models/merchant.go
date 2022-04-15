package models

type Merchant struct {
	MerchantId  string `json:"merchantId"`
	CutRate     int    `json:"cutRate"` // 1
	TotalPayout int    `json:"totalPayout"`
}
