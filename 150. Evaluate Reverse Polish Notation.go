package main

import (
	"fmt"
	"strconv"
)

func evalRPN(tokens []string) int {
	st := make([]string, 0)
	for _, c := range tokens {
		if c == "+" || c == "-" || c == "*" || c == "/" {
			op1, _ := strconv.Atoi(st[len(st)-1])
			op2, _ := strconv.Atoi(st[len(st)-2])
			st = st[:len(st)-2]
			var res int
			switch c {
			case "+":
				res = op1 + op2
			case "-":
				res = op2 - op1
			case "*":
				res = op1 * op2
			case "/":
				res = op2 / op1
			}
			st = append(st, strconv.Itoa(res))
		} else {
			st = append(st, c)
		}
	}
	res, _ := strconv.Atoi(st[len(st)-1])
	return res
}

func main() {
	// tokens := []string{"2", "1", "+", "3", "*"}
	tokens := []string{"4", "13", "5", "/", "+"}
	fmt.Println(evalRPN(tokens))
}
