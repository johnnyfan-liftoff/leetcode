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

func maxArea(height []int) int {
	l, r := 0, len(height)-1
	maxA := 0
	for l < r {
		maxA = max(maxA, min(height[l], height[r])*(r-l))
		if height[l] > height[r] {
			r--
		} else if height[l] <= height[r] {
			l++
		}
	}
	return maxA
}

func main() {
	height := []int{1, 8, 6, 2, 5, 4, 8, 3, 7}
	fmt.Println(maxArea(height))
}
