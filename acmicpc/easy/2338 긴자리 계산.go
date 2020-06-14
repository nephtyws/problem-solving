package main

import (
	"fmt"
	"math/big"
)

func main() {
	n := new(big.Int)
	m := new(big.Int)

	_, _ = fmt.Scan(n)
	_, _ = fmt.Scan(m)

	fmt.Println(new(big.Int).Add(n, m).String())
	fmt.Println(new(big.Int).Sub(n, m).String())
	fmt.Println(new(big.Int).Mul(n, m).String())
}
