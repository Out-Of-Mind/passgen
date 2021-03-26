package main

import (
	"fmt"
	"flag"
	"time"
	"strings"
	"math/rand"
)

var (
	length, chars_length int
	use_upper, use_low, use_special bool
)

const (
	chars_low = "abcdefghijklmnopqrstuvwxyz"
	chars_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	chars_special = "!#$%&*+-./:=?@^_"
)

func init() {
	flag.IntVar(&length, "c", 8, "usage: -c 16 (to set password length to 16)")
	flag.BoolVar(&use_low, "l", false, "usage: -l (to set use lowercase characters)")
	flag.BoolVar(&use_upper, "u", false, "usage: -u (to set use uppercase characters)")
	flag.BoolVar(&use_special, "s", false, "usage: -s (to set use special characters)")
}

func main() {
	flag.Parse()

	var chars string
	rand.Seed(time.Now().UnixNano())

	if !use_low && !use_upper && !use_special {
		chars_length = 68
		chars += chars_low
		chars += chars_upper
		chars += chars_special
	}
	if use_low {
		chars += chars_low
		chars_length += 26
	}
	if use_upper {
		chars += chars_upper
		chars_length += 26
	}
	if use_special {
		chars += chars_special
		chars_length += 16
	}

	password := make([]string, chars_length)
	chars_arr := strings.Split(chars, "")

	for i := 0; i < length; i++ {
		n := rand.Intn(chars_length)
		password[i] = chars_arr[n]
	}
	
	fmt.Println("Your password is: "+strings.Join(password[:], ""))
}