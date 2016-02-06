from lcd import LCD

class Screen:
	strings = []
	index = 0

	def __init__(self, strings):
		self.strings = strings

	def moveDown(self):
		return

	def moveUp(self):
		return

	def removeString(self, index):
		del strings[index]
		return

	def insertString(self, index, string):
		self.strings.insert([index, string])
		return

	def addString(self, string):
		self.strings.append(string);
		return

	def display(self):
		lcd.set_cursor(0,0)
		lcd.send_string(self.strings[self.index])
		lcd.set_cursor(1,0)
		
		second = self.index+1
		if(second >= len(self.strings)):
			second = 0

		lcd.send_string(self.strings[second])
		return

screen = new Screen(['poopy', 'is xander'])
screen.removeString(0)
screen.addString("gay?")
screen.display();