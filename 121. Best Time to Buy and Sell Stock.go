package main

import (
	"fmt"
)

func max(a1 int, a2 int) int {
	if a1 > a2 {
		return a1
	} else {
		return a2
	}
}

func min(a1 int, a2 int) int {
	if a1 > a2 {
		return a2
	} else {
		return a1
	}
}

func maxProfit(prices []int) int {
	l, r := 0, 1
	profit := 0
	for r < len(prices) {
		profit = max(profit, prices[r]-prices[l])
		if prices[r] < prices[l] {
			l = r
		}
		r++
	}
	return profit
}

func main() {
	prices := []int{7, 1, 5, 3, 6, 4}
	fmt.Println(maxProfit(prices))
}
