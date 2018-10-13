__author__ = "Cody Swain"

'''Creating custom dict'''
class HashTable:
	def __init__(self):
		self.size = 10
		self.slots = [None] * self.size
		self.data = [None] * self.size

	def hashfunction(self, key, size):
		'''Implementation of the simple remainder method for hashing.'''
		return key%size

	def rehash(self, oldhash, size):
		'''Ideally this rehash computes the next open slot.'''
		return (oldhash+1)%size

	def put(self, key, data):
		'''Inserts key into hash table'''
		hashvalue = self.hashfunction(key, len(self.slots))

		if self.slots[hashvalue] == None:
			self.slots[hashvalue] = key
			self.data[hashvalue] = data
		else:
			if self.slots[hashvalue] == key:
				self.data[hashvalue] = data #replace existing data
			else:
				nextslot = self.rehash(hashvalue, len(self.slots))
				while self.slots[nextslot] != None and \
								self.slots[nextslot] != key:
					nextslots = self.rehash(nextslots, len(self.slots))
				if self.slots[nextslot] == None:
					self.slots[nextslot] = key
					self.data[nextslot] = data
				else:
					self.data[nextslots] = data #replace existing data

	def get(self, key):
		startslot = self.hashfunction(key, len(self.slots))
		data = None
		stop = False
		found = False
		position = startslot
		while self.slots[position] != None and not found and not stop:
			if self.slots[position] == key:
				found = True
				data = self.data[position]
			else:
				position = self.rehash(position, len(self.slots))
				if position == startslot:
					stop = True
		return data

	def __getitem__(self, key):
		return self.get(key)

	def __setitem__(self, key, data):
		self.put(key, data)


