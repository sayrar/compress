from numpy.testing import assert_,assert_raises
import numpy as np
from PCA import PCA

class TestCalcCovar(object):
	def setup(self):
		intDATA = np.array([[-2, -1, 0, 1, 2],
							[-3, 3, -1, 0, 1]])


		self.intPCA = PCA(intDATA, 1)

	def testArrayEqualMatMul(self):
		intDATA = np.array([[-2, -1, 0, 1, 2],
							[-3, 3, -1, 0, 1]])
		

		testResult = np.array([[10, 5,],
								[5, 20]])
		
		np.testing.assert_array_equal(np.matmul(intDATA, intDATA.T), testResult)

	def testArrayEqualcalcCovar(self):
		testResult = np.array([7.92893218, 22.071068])

		intDATA = np.array([[-2, -1, 0, 1, 2],
							[-3, 3, -1, 0, 1]])
		np.testing.assert_array_almost_equal(self.intPCA.calc_covar(intDATA)[0], testResult)


		
        
if __name__ == "__main__" :
    np.testing.run_module_suite()
