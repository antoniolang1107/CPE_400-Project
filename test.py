import numpy as np
import unittest

from project import distance_dict_to_matrix

class Test(unittest.TestCase):
	def test_dict_to_matrix(self):
		test_dict_list = [{0: 0, 1:5, 2:20},
						  {0:5, 1:0, 2:15}, 
						  {0:20, 1:15, 2:0}]
		returned_matrix = distance_dict_to_matrix(test_dict_list)
		
		expected_result = np.array([[0,5,20],
									[5,0,15],
									[20,15,0]])

		np.testing.assert_allclose(returned_matrix, expected_result)
		# self.assertEqual(returned_matrix, expected_result)


if __name__ == '__main__':
	unittest.main()