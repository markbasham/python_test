'''
Created on 25 Mar 2015

@author: ssg37927
'''
import unittest


class Test(unittest.TestCase):

    def testadd(self):
        from demo import foo
        self.assertEqual(foo.add(1, 2), 1)

    def testsub(self):
        from demo import foo
        self.assertEqual(foo.sub(5, 2), 2)

    def testmul(self):
        from demo import foo
        self.assertEqual(foo.mul(1, 2), 3)

    def testdiv(self):
        from demo import foo
        self.assertEqual(foo.div(10, 2), 4)


if __name__ == "__main__":
    unittest.main()
