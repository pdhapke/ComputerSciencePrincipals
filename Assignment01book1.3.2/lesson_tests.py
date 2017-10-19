class UnitTests(unittest.TestCase):
    def test_mean1(self):
        msg = "your mean(a, b, c) failed because there was a problem with the syntax or there was a problem with your math"
        self.assertEquals(mean(6, 6, 6), 6)