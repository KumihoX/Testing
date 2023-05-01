import pytest
import requests

from lib.ApiWrapper import *
from parameterized import parameterized


class TestClass:
    def test_get_form_http_status(self):
        assert get_form().status_code == 200

    def test_post_form_is_http_status_200(self):
        form = post_form("2", "2", "1 1 1 1")
        assert form.status_code == 200 and form.text == "1"

    def test_post_empty_form_is_http_status_400(self):
        assert post_form().status_code == 400

    def test_below_left_bound_matrix_length_is_http_status_400(self):
        assert post_form("0", "0").status_code == 400

    def test_equal_left_bound_matrix_length_is_http_status_200(self):
        form = post_form("1", "1", "0")
        assert form.status_code == 200 and form.text == "1"

    def test_higher_left_bound_matrix_length_is_http_status_200(self):
        form = post_form("1", "2", "0 1")
        assert form.status_code == 200 and post_form("1", "2", "0 1").text == "2"

    def test_below_right_bound_matrix_string_length_is_http_status_200(self):
        matrix_string = " ".join([str(i) for i in range(0, 199)])
        form = post_form("1", "199", matrix_string)
        assert form.status_code == 200 and form.text == "199"

    def test_equal_right_bound_matrix_string_length_is_http_status_200(self):
        matrix_string = " ".join([str(i) for i in range(0, 200)])
        form = post_form("1", "200", matrix_string)
        assert form.status_code == 200 and form.text == "200"

    def test_higher_right_bound_matrix_string_length_is_http_status_400(self):
        matrix_string = " ".join([str(i) for i in range(0, 201)])
        assert post_form("1", "201", matrix_string).status_code == 400

    def test_below_left_bound_matrix_value_is_http_status_400(self):
        assert post_form("1", "1", "-1").status_code == 400

    def test_equal_left_bound_matrix_value_is_http_status_200(self):
        form = post_form("1", "1", "0")
        assert form.status_code == 200 and form.text == "1"

    def test_higher_left_bound_matrix_value_is_http_status_200(self):
        form = post_form("1", "1", "1")
        assert form.status_code == 200 and form.text == "1"

    def test_below_right_bound_matrix_value_is_http_status_200(self):
        number = 2 ** 31 - 2
        form = post_form("1", "1", str(number))
        assert form.status_code == 200 and form.text == "1"

    def test_equal_right_bound_matrix_value_is_http_status_200(self):
        number = 2 ** 31 - 1
        form = post_form("1", "1", str(number))
        assert form.status_code == 200 and form.text == "1"

    def test_higher_right_bound_matrix_value_is_http_status_400(self):
        number = 2 ** 31
        assert post_form("1", "1", str(number)).status_code == 400

    def test_do_not_move_diagonally_is_http_status_200(self):
        form = post_form("3", "3", "2 2 4 2 3 2 2 2 2")
        assert form.status_code == 200 and form.text == "2"

    def test_do_not_move_outside_the_boundary_is_http_status_200(self):
        form = post_form("3", "3", "2 2 2 2 2 2 2 1 3")
        assert form.status_code == 200 and form.text == "2"

    @parameterized.expand([
        ("is_float", "1.5", "1", "1"),
        ("is_list", "[1]", "1", "1"),
        ("is_empty", "", "1", "1"),
        ("is_expression", "1 - 1", "3", "1")
    ])
    def test_invalid_data_in_height_field_is_http_status_400(self, height, width, matrix_string, expected):
        form = post_form(height, width, matrix_string)
        assert form.status_code == 400

    @parameterized.expand([
        ("is_float", "1", "1.5", "1"),
        ("is_list", "1", "[1]", "1"),
        ("is_empty", "1", "", "1"),
        ("is_expression", "3", "1 - 1", "1")
    ])
    def test_invalid_data_in_width_field_is_http_status_400(self, height, width, matrix_string, expected):
        form = post_form(height, width, matrix_string)
        assert form.status_code == 400

    @parameterized.expand([
        ("is_string", "1", "1", "it's string"),
        ("is_float", "1", "1", "2.5"),
        ("is_list", "1", "1", "[1, 2, 3]"),
        ("is_empty", "1", "1", ""),
        ("is_expression", "1", "3", "1 + 1")
    ])
    def test_with_invalid_data_instead_of_matrix_data_with_spaces_is_http_status_400(self, _, height, width, matrix_string):
        assert post_form(height, width, matrix_string).status_code == 400

    def test_non_exist_end_point_is_http_status_404(self):
        response = requests.get(BASE_URL + "\dfskdfls;dkfsl;")
        assert response.status_code == 404

    def test_patch_request_is_http_status_405(self):
        response = requests.patch(BASE_URL)
        assert response.status_code == 405

    def test_delete_request_is_http_status_405(self):
        response = requests.delete(BASE_URL)
        assert response.status_code == 405
