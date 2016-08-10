package main
//brunston 2016

import (
	"fmt"
	"math"
)

func main() {
	var number int = 600851475143
	var sqrt_aprx float = math.Ceil(math.Sqrt(number))
	
	prime_factors := make([]int, 0)
	primes := make([]int, 1)
	primes[0] = 2
	for i:=2; i < sqrt_aprx; i++ {
		for j:=0; i<len(primes); i++{
			if math.Mod(i,primes[j]) == 0 {
				
			}
		}
	}
}
