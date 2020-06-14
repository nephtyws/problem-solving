package main

import "fmt"

func main() {
	n := make([]int, 5)
	answer := 0

	for i := range n {
		_, _ = fmt.Scan(&n[i])
		answer += n[i] * n[i]
	}

	fmt.Printf("%d", answer % 10)
}
