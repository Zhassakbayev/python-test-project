import softest


class TestFirst(softest.TestCase):

    def test1(self):
        print("Test № 1")
        self.assertEqual(2 + 2, 4, "not equal")

    def test2(self):
        print("Test № 2")
        self.assertEqual(2 + 2, 5, "not equal")

    def test3(self):
        print("Test № 3")
        self.soft_assert(self.assertEqual, 2 + 2, 4, "not equal")
        self.soft_assert(self.assertEqual, 2 + 2, 5, "not equal")
        self.assert_all()

    def test4(self):
        print("Test № 4")
        self.assertEqual(1 / 0, 1, "not equal")

    def test5(self):
        print("Test № 5")
