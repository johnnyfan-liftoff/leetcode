package main

import "fmt"

func main() {
	nums := []int{-1, 0, 3, 5, 9, 12}
	target := 9
	fmt.Println(search(nums, target))
}

func search(nums []int, target int) int {
	l := 0
	r := len(nums) - 1
	for l <= r {
		t := (r-l)/2 + l
		if target == nums[t] {
			return t
		}
		if target > nums[t] {
			l = t + 1
		} else {
			r = t - 1
		}
	}
	return -1
}
