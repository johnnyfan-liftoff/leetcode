package main

import "fmt"

func main() {
	fmt.Println(generateParenthesis(3))
}

func generateParenthesis(n int) []string {

	stack := make([]string, 0)
	res := make([]string, 0)

	var helper func(left int, rigth int)

	helper = func(left int, right int) {
		if left == n && right == n {
			var tmp string
			for _, v := range stack {
				tmp = tmp + v
			}
			res = append(res, tmp)
		}
		if left < n {
			stack = append(stack, "(")
			helper(left+1, right)
			stack = stack[:len(stack)-1]
		}
		if right < left {
			stack = append(stack, ")")
			helper(left, right+1)
			stack = stack[:len(stack)-1]
		}
	}

	helper(0, 0)
	return res

}
