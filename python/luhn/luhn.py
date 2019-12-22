class Luhn:
	def __init__(self, card_num):
		self.nums = [char for char in card_num if char is not ' ']

	def valid(self):
		print(self.nums)

		if len(self.nums) <= 1:
			return False

		for num in self.nums:
			if not num.isnumeric():
				return False

		doubled = [2 * int(self.nums[i]) if (2 * int(self.nums[i])) <= 9 else (2 * int(self.nums[i]) - 9)for i in range(len(self.nums)) ]

		print(doubled)
		return sum(doubled)%10 == 0

print(Luhn("055 444 285").valid())
