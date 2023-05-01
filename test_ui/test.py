from test_ui.page_objects import page


class TestSeleniumBasic:
    def test_main_page_loads_with_expected_title(self, browser):
        browser.get('http://localhost:5000/')
        main_page = page.MainPage(browser)
        assert main_page.is_title_matches()

    def test_main_page_check_longest_increasing_path_in_matrix(self, browser):
        browser.get('http://localhost:5000/')
        main_page = page.MainPage(browser)
        main_page.input_data_in_text_fields("2", "2", "1 1 1 1")
        main_page.click_go_button()
        check_results_page = page.CheckResultsPage(browser)

        assert check_results_page.is_results_found()

    def test_main_page_check_longest_increasing_path_in_matrix_not_found(self, browser):
        browser.get('http://localhost:5000/')
        main_page = page.MainPage(browser)
        main_page.input_data_in_text_fields("1", "0", "1")
        main_page.click_go_button()
        check_results_page = page.CheckResultsPage(browser)

        assert not check_results_page.is_results_found()

    def test_main_page_loads_with_expected_h1_header(self, browser):
        browser.get('http://localhost:5000/')
        main_page = page.MainPage(browser)

        assert main_page.is_header_h1_matches()

    def test_main_page_loads_with_expected_height_header(self, browser):
        browser.get('http://localhost:5000/')
        main_page = page.MainPage(browser)

        assert main_page.is_header_height_matches()

    def test_main_page_loads_with_expected_width_header(self, browser):
        browser.get('http://localhost:5000/')
        main_page = page.MainPage(browser)

        assert main_page.is_header_width_matches()

    def test_main_page_loads_with_expected_matrix_data_header(self, browser):
        browser.get('http://localhost:5000/')
        main_page = page.MainPage(browser)

        assert main_page.is_header_matrix_data_matches()


