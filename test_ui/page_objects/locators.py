from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    GO_BUTTON = (By.ID, 'submit')
    INPUT_TEXT_HEIGHT = (By.ID, 'height')
    INPUT_TEXT_WIDTH = (By.ID, 'width')
    INPUT_TEXT_MATRIX_DATA = (By.ID, 'matrix_data')

    HEADER = (By.ID, 'header')
    HEADER_WIDTH = (By.ID, 'header_width')
    HEADER_HEIGHT = (By.ID, 'header_height')
    HEADER_MATRIX_DATA = (By.ID, 'header_matrix_data')


class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should
    come here"""

    pass