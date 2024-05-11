/*
Little Petya loves presents. His mum bought him two strings of the same size for his birthday. The strings consist of uppercase and lowercase Latin letters. Now Petya wants to compare those two strings lexicographically. The letters' case does not matter, that is an uppercase letter is considered equivalent to the corresponding lowercase letter. Help Petya perform the comparison.
*/
package main

import (
	"fmt"
	"strings"
)

func main() {
	var lineOne, lineTwo string
	var ans int
	fmt.Scanln(&lineOne)
	fmt.Scanln(&lineTwo)
	lineOne = strings.ToLower(lineOne)
	lineTwo = strings.ToLower(lineTwo)
	if lineOne == lineTwo {
		ans = 0
	} else {
		for pos, _ := range lineOne {
			if lineOne[pos] < lineTwo[pos] && lineOne[pos] != lineTwo[pos] {
				ans = -1
				break
			} else if lineOne[pos] > lineTwo[pos] && lineOne[pos] != lineTwo[pos] {
				ans = 1
				break
			}

		}
	}
	fmt.Print(ans)
}
