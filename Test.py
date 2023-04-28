import unittest
from Solution import Solution
from parameterized import parameterized


class MyTestCase(unittest.TestCase):
    solution: Solution = Solution()

    # Нужен баг репорт
    @parameterized.expand([
        ("is_string", "it's string"),
        ("is_float", 2.5),
        ("is_complex", complex(1, 2)),
        ("is_none", None)
    ])
    def test_matrix_comprises_invalid_data(self, _, matrix: list[list]):
        with self.assertRaises(ValueError):
            self.solution.longest_increasing_path(matrix)

    def test_below_left_bound_matrix_length(self):
        with self.assertRaises(ValueError):
            self.solution.longest_increasing_path([[]])

    def test_equal_left_bound_matrix_length(self):
        self.assertEqual(
            self.solution.longest_increasing_path([[0]]),
            1
        )

    def test_higher_left_bound_matrix_length(self):
        self.assertEqual(
            self.solution.longest_increasing_path([[0], [1]]),
            2
        )

    def test_below_right_bound_matrix_string_length(self):
        self.assertEqual(
            self.solution.longest_increasing_path([[i for i in range(0, 199)]]),
            199
        )

    def test_equal_right_bound_matrix_string_length(self):
        self.assertEqual(
            self.solution.longest_increasing_path([[i for i in range(0, 200)]]),
            200
        )

    # Нужен баг репорт
    def test_higher_right_bound_matrix_string_length(self):
        with self.assertRaises(ValueError):
            self.solution.longest_increasing_path([[i for i in range(0, 201)]])

    def test_below_left_bound_matrix_value(self):
        with self.assertRaises(ValueError):
            self.solution.longest_increasing_path([[-1]])

    def test_equal_left_bound_matrix_value(self):
        self.assertEqual(
            self.solution.longest_increasing_path([[0]]),
            1
        )

    def test_higher_left_bound_matrix_value(self):
        self.assertEqual(
            self.solution.longest_increasing_path([[1]]),
            1
        )

    def test_below_right_bound_matrix_value(self):
        self.assertEqual(
            self.solution.longest_increasing_path([[2 ** 31 - 2]]),
            1
        )

    def test_equal_right_bound_matrix_value(self):
        self.assertEqual(
            self.solution.longest_increasing_path([[2 ** 31 - 1]]),
            1
        )

    def test_higher_right_bound_matrix_value(self):
        with self.assertRaises(ValueError):
            self.solution.longest_increasing_path([[2 ** 31]])

    def test_do_not_move_diagonally(self):
        self.assertEqual(
            self.solution.longest_increasing_path([[2, 2, 4], [2, 3, 2], [2, 2, 2]]),
            2
        )

    def test_do_not_move_outside_the_boundary(self):
        self.assertEqual(
            self.solution.longest_increasing_path([[2, 2, 2], [2, 2, 2], [2, 1, 3]]),
            2
        )

    # Нужен баг репорт
    @parameterized.expand([
        ("is_string", [["it's string"]]),
        ("is_float", [[2.5]]),
        ("is_complex", [[complex(1, 2)]]),
    ])
    def test_matrix_contain_invalid_data(self, _, matrix: list[list]):
        with self.assertRaises(ValueError):
            self.solution.longest_increasing_path(matrix)


if __name__ == '__main__':
    unittest.main()