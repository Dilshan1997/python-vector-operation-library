
class Vector2D:

	def __init__(self, x, y):
		self.x=x
		self.y=y
		 			

	def add(self,other_vector):
		return f'<{self.x+other_vector.x}, {self.y+other_vector.y}>'

	def sub(self,other_vector):
		return f'<{self.x-other_vector.x}, {self.y-other_vector.y}>'
	
	def dotProduct(self,other_vector):
		return self.x*other_vector.x + self.y*other_vector.y
	
	def crossProduct(self,other_vector):
		return self.x-other_vector.y - other.x-self.y

vector1=Vector2D(1,2)
vector2=Vector2D(3,5)

new_vector=vector1.dotProduct(vector2)
print(new_vector)

class Vector3D:

	def __init__(self, x, y, z):
        	self.x = x
        	self.y = y
        	self.z = z

	def add(self, other_vector):
        	return f"<{self.x + other_vector.x}, {self.y + other_vector.y}, {self.z + other_vector.z}>"

	def sub(self, other_vector):
        	return f"<{self.x - other_vector.x}, {self.y - other_vector.y}, {self.z - other_vector.z}>"

	def dot_product(self, other_vector):
        	return self.x * other_vector.x + self.y * other_vector.y + self.z * other_vector.z

	def cross_product(self, other_vector):
		cross_x = self.y * other_vector.z - self.z * other_vector.y
		cross_y = self.z * other_vector.x - self.x * other_vector.z
		cross_z = self.x * other_vector.y - self.y * other_vector.x
		return f"<{cross_x},{cross_y},{cross_z}>"


v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)


print(v1.add(v2))
print(v1.sub(v2))
print(v1.dot_product(v2))
print(v1.cross_product(v2))

