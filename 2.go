package main
//brunston 2016
import (
	"fmt"
)

func main() {
	var fiblast, fibfirst, retsum, fibsum int64 = 1, 2, 3, 0
	for fibsum < 4000000 {
		
		fibsum = fibfirst + fiblast
		fiblast = fibfirst
		fibfirst = fibsum
		retsum += fibsum
		if fibsum < 1000 {
			fmt.Println(fibsum)
		}
	}
	fmt.Println(retsum)
}
