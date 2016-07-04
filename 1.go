package main
//brunston 2016
import (
	"fmt"
	"math"
)

func main() {
	var sum float64 = 0
	var i float64
	for i = 0; i < 1000; i++ {
		if math.Mod(i, 5) == 0 || math.Mod(i, 3) == 0 {
			sum += i
		}
	}
	fmt.Println(sum)
}
