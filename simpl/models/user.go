package models

import "sync"

type User struct {
	Mu           *sync.Mutex
	PhoneNumber  string `json:"phone_number"`
	Verified     bool   `json:"verified"`
	TotalLimit   int    `json:"totalLimit"`
	CurrentUsage int    `json:"currentUsage"`
}
