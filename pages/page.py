
class Page:
    def __init__(self, browser, width=0, height=0):
        self.browser = browser
        self.browser_width = width
        self.browser_height = height

    # Precondition is that the browser is resized the full page size
    def set_browser_to_max_screen_size(self):
        self.browser.maximize_window()
        self.browser_width = self.browser.get_window_size().get("width")
        self.browser_height = self.browser.get_window_size().get("height")

    def set_browser_width_to_half_of_the_screen(self):
        self.browser.set_window_size(self.browser_width / 2, self.browser_height)

    def set_browser_position_to_the_left(self):
        self.browser.set_window_position(0, 0)

    def set_browser_position_to_the_right(self):
        self.browser.set_window_position(self.browser_width / 2, 0)

