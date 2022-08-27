package main

import "fmt"

func main() {
	temperatures := []int{73, 74, 75, 71, 69, 72, 76, 73}
	fmt.Println(dailyTemperatures(temperatures))
}

type Mem struct {
	val   int
	index int
}

func dailyTemperatures(temperatures []int) []int {
	stack := make([]Mem, 0)
	res := make([]int, len(temperatures))

	for i, v := range temperatures {
		for len(stack) > 0 && v > stack[len(stack)-1].val {
			res[stack[len(stack)-1].index] = i - stack[len(stack)-1].index
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, Mem{val: v, index: i})
	}
	return res
}
