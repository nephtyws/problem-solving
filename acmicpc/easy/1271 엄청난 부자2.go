package main

import (
	"fmt"
	"math/big"
)

func main() {
	n := new(big.Int)
	m := new(big.Int)

	_, err := fmt.Scan(n, m)

	if err == nil {
		fmt.Println(new(big.Int).Div(n, m).String())
		fmt.Println(new(big.Int).Mod(n, m).String())
	}
}
