/*
"Contestant who earns a score equal to or greater than the k-th place finisher's score will advance to the next round, as long as the contestant earns a positive score..." — an excerpt from contest rules.

A total of n participants took part in the contest (n ≥ k), and you already know their scores. Calculate how many participants will advance to the next round.
*/
package main

import (
	"fmt"
)

func main() {

	var num, scr, count int

	fmt.Scanf("%d %d", &num, &scr)
	var ppl []int
	for i := 0; i < num; i++ {
		var temb int = 0
		fmt.Scan(&temb)
		ppl = append(ppl, temb)
	}
	scr = ppl[scr-1]
	for _, inp := range ppl {
		if inp >= scr && inp > 0 {
			count += 1
		}
	}
	fmt.Print(count)

}

/*
FirstLine = input("")
SecondLine = input("")




def fun(x):
    tempList = []
    num = 0

    temb = ""

    for i in x:
        num += 1
        temb = temb + i
        if (i == " ") or (num > (len(x) - 1)):
            tempList.append(int(temb))
            temb = ""
    return tempList

list1 = fun(FirstLine)
list2 = fun(SecondLine)
n = int(list1[0])
k = int(list1[1])
score = int(list2[k-1])
count = 0




for i in list2:
    if int(i) >= score and int(i) > 0:
        count+=1
'''
8 5
10 9 8 7 7 7 5 5
'''

print(count)
*/
