class Screen:
	strings = []
	index = 0

	def __init__(self, strings, lcd):
		self.strings = strings
		self.lcd = lcd

	def moveDown(self):
		return

	def moveUp(self):
		return

	def removeString(self, index):
		del self.strings[index]
		return

	def insertString(self, index, string):
		self.strings.insert([index, string])
		return

	def addString(self, string):
		self.strings.append(string);
		return

	def display(self):
		self.lcd.set_cursor(0,0)
		self.lcd.send_string(self.strings[self.index])
		self.lcd.set_cursor(1,0)
		
		second = self.index+1
		if(second >= len(self.strings)):
			second = 0

		self.lcd.send_string(self.strings[second])
		return