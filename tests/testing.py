import unittest
from src.vector_library import Vector2D, Vector3D


class TestVector2DOperations(unittest.TestCase):

    def setUp(self):
        self.vector1 = Vector2D(1, 2)
        self.vector2 = Vector2D(3, 5)

        print(self.vector1+self.vector2)

    def test_2d_vector_addition(self):
        self.assertEqual((self.vector1+self.vector2).__str__(), "<4, 7>")

    def test_2d_vector_substraction(self):
        self.assertEqual((self.vector1-self.vector2).__str__(), "<-2, -3>")

    def test_2d_vector_dot_product(self):
        self.assertEqual((self.vector1*self.vector2), 13)

    def test_2d_vector_cross_product(self):
        self.assertEqual((self.vector1@self.vector2), -1)


class TestVector3DOperations(unittest.TestCase):

    def setUp(self):
        self.vector1 = Vector3D(1, 2, 3)
        self.vector2 = Vector3D(3, 5, 7)

    def test_2d_vector_addition(self):
        self.assertEqual((self.vector1 + self.vector2).__str__(), "<4, 7, 10>")

    def test_2d_vector_substraction(self):
        self.assertEqual((self.vector1 - self.vector2).__str__(), "<-2, -3, -4>")

    def test_2d_vector_dot_product(self):
        self.assertEqual((self.vector1*self.vector2), 34)

    def test_2d_vector_cross_product(self):
        self.assertEqual((self.vector1@self.vector2).__str__(), "<-1, 2, -1>")


unittest.main()


# print(vector1)
# print(vector1-vector2)
# print(vector1@vector2)

# print(Vector2D.__doc__)
