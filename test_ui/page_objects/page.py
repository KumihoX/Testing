from test_ui.page_objects.element import BasePageElement
from test_ui.page_objects.locators import MainPageLocators


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    def input_data_in_text_fields(self, height, width, matrix_data):
        height_text_element = self.driver.find_element(*MainPageLocators.INPUT_TEXT_HEIGHT)
        width_text_element = self.driver.find_element(*MainPageLocators.INPUT_TEXT_WIDTH)
        matrix_data_text_element = self.driver.find_element(*MainPageLocators.INPUT_TEXT_MATRIX_DATA)

        height_text_element.send_keys(height)
        width_text_element.send_keys(width)
        matrix_data_text_element.send_keys(matrix_data)

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""

        return "Longest Increasing Path In a Matrix" in self.driver.title

    def is_header_h1_matches(self):
        header = self.driver.find_element(*MainPageLocators.HEADER)
        return "Longest Increasing Path In a Matrix" in header.text

    def is_header_height_matches(self):
        header = self.driver.find_element(*MainPageLocators.HEADER_HEIGHT)
        return "Введите высоту матрицы" in header.text

    def is_header_width_matches(self):
        header = self.driver.find_element(*MainPageLocators.HEADER_WIDTH)
        return "Введите ширину матрицы" in header.text

    def is_header_matrix_data_matches(self):
        header = self.driver.find_element(*MainPageLocators.HEADER_MATRIX_DATA)
        return "Введите содержимое матрицы через пробел" in header.text

    def click_go_button(self):
        """Triggers the search"""

        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()


class CheckResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "Bad Request" not in self.driver.page_source