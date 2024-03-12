
class Vector2D:
	'''
	This class responsible for handle the 2D vectors operations
	'''
	def __init__(self, x, y):
		'''
		2D Vector inititor
		   Args:
				x: Vector x value
				y: Vector y value
		'''
		self.x = x
		self.y = y

	def __add__(self, other_vector):
		''' 
		This function responsible for handle the 2D addition operation
				Args:
					self: Vector that particular instance
					other_vector: Other Vector

				Returns:
					vector1+vector2
		'''
		return Vector2D(self.x+other_vector.x, self.y+other_vector.y)

	def __sub__(self, other_vector):
		''' 
		This function responsible for handle the 2D substraction operation
				Args:
					self: Vector that particular instance
					other_vector: Other Vector
				Returns:
					vector1-vector2
		'''
		return Vector2D(self.x-other_vector.x, self.y-other_vector.y)

	def __mul__(self, other_vector):
		''' 
		This function responsible for handle the 2D dot product operation
			Args:
				self: Vector that particular instance
				other_vector: Other Vector
			Returns:
				vector1*vector2
		'''
		return self.x*other_vector.x + self.y*other_vector.y

	def __matmul__(self, other_vector):
		''' This function responsible for handle the 2D cross product operation
			Args:
				self: Vector that particular instance
				other_vector: Other Vector
			Returns: 
				vector1 X vector2				
		'''
		
		return self.x*other_vector.y - other_vector.x*self.y

	def __str__(self):
		return f"<{self.x}, {self.y}>"

class Vector3D:
	''' 
	This class responsible for handle the 3D vectors operations
	'''
	def __init__(self, x, y, z):
		'''
		3D vector initiator
			Args:
				x: Vector x value
				y: Vector y value
				z: Vector z value
		'''
		self.x = x
		self.y = y
		self.z = z

	def __add__(self, other_vector):
		''' This function responsible for handle the 3D addition operation'''
		return Vector3D(self.x+other_vector.x, self.y+other_vector.y,  self.z + other_vector.z)

	def __sub__(self, other_vector):
		''' This function responsible for handle the 3D substraction operation'''
		return Vector3D(self.x-other_vector.x, self.y-other_vector.y, self.z - other_vector.z)

	def __mul__(self, other_vector):
		''' This function responsible for handle the 3D dot product operation'''
		return self.x * other_vector.x + self.y * other_vector.y + self.z * other_vector.z

	def __matmul__(self, other_vector):
		''' This function responsible for handle the 3D cross product operation'''
		cross_x = self.y * other_vector.z - self.z * other_vector.y
		cross_y = self.z * other_vector.x - self.x * other_vector.z
		cross_z = self.x * other_vector.y - self.y * other_vector.x
		return Vector3D(cross_x, cross_y, cross_z)

	def __str__(self):
		'''This dunder method reponsible for convert objects to string type'''
		return f"<{self.x}, {self.y}, {self.z}>"