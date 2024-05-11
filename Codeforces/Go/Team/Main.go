/*
One day three best friends Petya, Vasya and Tonya decided to form a team and take part in programming contests. Participants are usually offered several problems during programming contests. Long before the start the friends decided that they will implement a problem if at least two of them are sure about the solution. Otherwise, the friends won't write the problem's solution.

This contest offers n problems to the participants. For each problem we know, which friend is sure about the solution. Help the friends find the number of problems for which they will write a solution.
*/

package main

import (
	"fmt"
)

func main() {
	var size int
	var wins int
	fmt.Scanln(&size)
	for i := 0; i < size; i++ {
		var x int
		var y int
		var z int
		fmt.Scanf("%d %d %d\n", &x, &y, &z)

		if x+y+z > 1 {
			wins += 1
		}

	}
	fmt.Println(wins)

}

/*
package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)

	var p1, p2, p3, count int

	for i := 0; i < n; i++ {
		fmt.Scan(&p1, &p2, &p3)
		if p1+p2+p3 >= 2 {
			count++
		}

	}
	fmt.Println(count)
}
*/
