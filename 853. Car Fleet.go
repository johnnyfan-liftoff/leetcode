package main

import (
	"fmt"
	"sort"
)

type st struct {
	pos   int
	speed int
	time  float32
}

func carFleet(target int, position []int, speed []int) int {
	a := make([]st, 0)
	for i, _ := range position {
		ti := float32(target-position[i]) / float32(speed[i])
		t := st{pos: position[i], speed: speed[i], time: ti}
		a = append(a, t)
	}

	sort.Slice(a, func(i, j int) bool {
		return a[i].pos > a[j].pos
	})

	fmt.Print(a)

	res := make([]st, 0)
	for _, v := range a {
		if len(res) == 0 {
			res = append(res, v)
		} else {
			if v.time > res[len(res)-1].time {
				res = append(res, v)
			}
		}
	}

	return len(res)
}

func main() {
	target := 12
	position := []int{10, 8, 0, 5, 3}
	speed := []int{2, 4, 1, 1, 3}
	fmt.Println(carFleet(target, position, speed))
}
