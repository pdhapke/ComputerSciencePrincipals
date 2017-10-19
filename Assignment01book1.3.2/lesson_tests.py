class unittests132(unittest.TestCase):
    def test_mean1(self):
        msg = "your mean(a, b, c) failed because there was a problem with the syntax or there was a problem with your math"

        self.assertEquals(mean(6, 6, 6), 6)
        self.assertEquals(mean(9, 10, 11), 10)

    def test_mean2(self):
        msg = "your mean(a, b, c) failed because you named your variables incorrectly"

        self.assertEquals(mean(b=6, c=6, a=6), 6)
        self.assertEquals(mean(c=9, a=10, b=11), 10)

    def test_perimeter1(self):
        msg = "Your perimeter(base, height) failed because your syntax is wrong or your math is wrong"

        self.assertEquals(perimeter(10, 5), 30)
        self.assertEquals(perimeter(20, 20), 80)


    def test_perimeter2(self):

        msg = "# Failure message:\n your perimeter failed because you named the variables incorrectly"

        self.assertEquals(perimeter(height=10, base=5), 30)
        self.assertEquals(perimeter(height=20, base=20), 80)


    def test_hyp1(self):
        msg = "Your hyp(leg1, leg2) failed because your syntax is wrong or your math is wrong"

        self.assertEquals(hyp(3, 4), 5)
        self.assertEquals(hyp(5, 12), 13)


    def test_hyp2(self):
        msg = "The test failed, it looks like your variables are named incorrectly"

        self.assertEquals(hyp(leg1=3, leg2=4), 5)
        self.assertEquals(hyp(leg1=5, leg2=12), 13)



    def test_add_tip1(self):
        msg = "Your add_tip(total, percent) failed to run correctly. either there is a problem with your code or a problem with your math."

        self.assertEquals(add_tip(100, 0.10), 110)



    def test_add_tip2(self):
        msg = "The test failed, it looks like your variables are named incorrectly"

        self.assertEquals(add_tip(percent=0.1, total=100), 110)



