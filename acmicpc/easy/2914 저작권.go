package main

import "fmt"

func main() {
	n := make([]int, 2)

	for i := range n {
		_, _ = fmt.Scan(&n[i])
	}

	fmt.Printf("%d", (n[0] * (n[1] - 1)) + 1)
}
