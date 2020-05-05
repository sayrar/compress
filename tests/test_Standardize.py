from numpy.testing import assert_,assert_raises
import numpy as np
from PCA import PCA

class TestStandardize(object):
	def setup(self):
		intDATA = np.arange(10).reshape(5,2)
		
		self.intPCA = PCA(intDATA, 1)

	def testArrayEqual(self):
		testResult = np.array([[-.5,.5],[-.5,.5],[-.5,.5],[-.5,.5],[-.5,.5]])
		np.testing.assert_array_equal(self.intPCA.standardize(), testResult)
        
if __name__ == "__main__" :
    np.testing.run_module_suite()
