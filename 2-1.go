package main
//brunston 2016
import (
	"fmt"
	"math"
)

func main() {
	var fib_sum, previous, pprevious, ret_sum int64 = 0, 1, 1, 0
	for fib_sum < 4000000 {
		if math.Mod(float64(fib_sum), 2) == 0 {
			fmt.Println(ret_sum)
			ret_sum += fib_sum	
		}
		fib_sum = previous + pprevious
		previous = pprevious
		pprevious = fib_sum
	}
	fmt.Println(ret_sum)
}
