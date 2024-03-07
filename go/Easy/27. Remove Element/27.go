package main

func removeElement(nums []int, val int) int {
	index := 0
	for _, number := range nums {
		if number != val {
			nums[index] = number
			index += 1
			println(number)
		}

	}

	return index
}

func main() {
	nums := []int{3, 2, 2, 3}
	val := 3
	println(removeElement(nums, val))

}
