package main

func removeDuplicates(nums []int) int {
	index := 0
	if len(nums) == 1 {
		return 1
	}
	for range nums {
		if !(index+1 < len(nums)) {
			return index + 1
		}
		if nums[index] == nums[index+1] {
			nums = append(nums[:index], nums[index+1:]...)
			continue
		}
		println(nums[index])
		index++
	}
	if index == 0 {
		return 1
	}
	return index

}

func main() {
	//nums := []int{1, 2}
	nums := []int{-3, -3, -2, -1, -1, 0, 0, 0, 0, 0}
	println(removeDuplicates(nums))

}
