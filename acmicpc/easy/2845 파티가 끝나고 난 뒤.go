package main

import "fmt"

func main() {
	n := make([]int, 2)

	for i := range n {
		_, _ = fmt.Scan(&n[i])
	}

	guess := n[0] * n[1]

	m := make([]int, 5)

	for i := range m {
		_, _ = fmt.Scan(&m[i])
		fmt.Printf("%d ", m[i] - guess)
	}
}
