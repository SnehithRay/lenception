class Enemy:
	def __init__(self):
		raise NotImplementedError("Do not create raw Enemy objects.")

	def __str__(self):
		return self.name

	def is_alive(self):
		return self.hp > 0



class SmallEnemy(Enemy):
	def __init__(self):
		self.name = "Small Len"
		self.hp = 100
		self.damage = 5
		self.speed = 25


class BigEnemy(Enemy):
	def __init__(self):
		self.name = "Big Enemy"
		self.hp = 200
		self.damage = 10
		self.speed = 5


class Len_Clone(Enemy):
	def __init__(self):
		self.name = "Len Clone"
		self.hp = 500
		self.damage = 25
		self.speed = 50


class Len_Boss(Enemy):
	def __init__(self):
		self.name = "Len Boss"
		self.hp = 1000
		self.damage = 100
		self.speed = 100
