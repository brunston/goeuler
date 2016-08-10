package main
//brunston 2016
import (
	"fmt"
	"math"
)

func main() {
	var fiblast, fibfirst, retsum, fibsum int64 = 1, 2, 3, 0
	for fibsum < 4000000 {
		
		fibsum = fibfirst + fiblast
		fiblast = fibfirst
		fibfirst = fibsum
		
		if math.Mod(float64(fibsum), 2) == 0 {
			retsum += fibsum
		}
		
		if fibsum < 1000 {
			fmt.Println(fibsum)
		}
	}
	fmt.Println(retsum)
}
