# unit test the my_points.py file

import unittest
from my_points import Point

class testPoint(unittest.TestCase):
    # setup runs once for each test, but runs for all tests before any of the test runs
    def setUp(self):
        self.point = Point(3,5)

    # declare each test here - they will be called/ run in the order they're written here

    def testMoveByA(self):
        self.point.moveBy(5,2)
        # make an assertion
        self.assertEqual(self.point.display(), (8,7))
    
    def testMoveByB(self):
        self.point.moveBy(-5,-2)
        # make an assertion
        self.assertEqual(self.point.display(), (-2,3))

    def testMoveByC(self):
        self.point.moveBy(dy=9)
        self.assertEqual(self.point.display(), (3,14))

    def testPointerCounter(self):
        ''' test the instances of Point class'''
        self.assertEqual(Point.points, 6)

    def testHypot(self):
        #self.point.moveBy(0,-1) # x=3, y=4, hypot=5
        r = self.point.hypot()
        #self.assertEqual(r, 5)
        self.assertAlmostEqual(r,5.83,places=2) # x=3, y=5, hypot=5.830951894845301

    def testPosNegHypot(self):
        self.pos_h = Point(3,4)
        self.neg_h = Point(-3,4)
        self.assertEqual(self.pos_h.hypot(), self.neg_h.hypot())
        
    def testExcRaised(self):
        # exception should be raised for non-ints
        with self.assertRaises(TypeError):
            Point('3',4)


if __name__ == '__main__':
    unittest.main()