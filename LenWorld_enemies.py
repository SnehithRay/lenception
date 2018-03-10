class Enemy:
	def __init__(self):
		raise NotImplementedError("Do not create raw Enemy objects.")

	def __str__(self):
		return self.name

	def is_alive(self):
		return self.hp > 0

	def handle_input(self, verb, noun1, noun2, inventory):
		return [False, None, inventory]


class regularLens(Enemy):
	def __init__(self):
		self.name = "Desi boy equipped with Chappal"
		self.hp = 10
		self.damage = 2


class boilerMakerSerpent(Enemy):
	def __init__(self):
		self.name = "Big mechanical diesel-spitting serpents operating on piston engines "
		self.hp = 30
		self.damage = 10


class seekerLen(Enemy):
	def __init__(self):
		self.name = "Seeker guard Lens armed with Titration tubes"
		self.hp = 100
		self.damage = 4


class bigLenClone(Enemy):
	def __init__(self):
		self.name = "Brute guard Len armed with lethal Chemistry lab-books"
		self.hp = 80
		self.damage = 15

class lenBoss(Enemy):
	def __init__(self):
		self.name = "This needs no description for you shall RUN!! :o o7 "
		self.hp = 150
		self.damage = 25

class pwshLen(Enemy):
	def __init__(self):
		self.name = "Crazy, tired-looking len-clone that will deliver toxic speeches that are quite the lethal "
		self.hp = 15
		self.damage = 20

class purdueCastleDrone(Enemy):
	def __init__(self):
		self.name = "maneuverable drones controlled by the Big Len Clone"
		self.hp = 2
		self.damage = 1
