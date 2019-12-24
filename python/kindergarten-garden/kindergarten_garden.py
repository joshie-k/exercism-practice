class Garden:
	default = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
	def __init__(self, diagram, students=default):
		self.first_row, self.second_row = diagram.split('\n')
		self.students = sorted(students)
		self.mapping = {'V' : "Violets", 'R': "Radishes", 'C': "Clover", 'G': "Grass"}

	def plants(self, name):
		ans = []
		pos = self.students.index(name)
		pot = pos * 2
		ans.append(self.mapping.get(self.first_row[pot]))
		ans.append(self.mapping.get(self.first_row[pot + 1]))
		ans.append(self.mapping.get(self.second_row[pot]))
		ans.append(self.mapping.get(self.second_row[pot + 1]))
		return ans