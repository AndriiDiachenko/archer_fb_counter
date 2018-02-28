import time


# Main page 'https://www.facebook.com/'
class Fb_main_page(object):
    def __init__(self, driver):
        self.driver = driver

    # Page header elements dict
    page_elements = {
        'email_input': 'input[type="email"][id="email"]',
        'pass_input': 'input[type="password"][id="pass"]',
        'login_btn': 'label[id="loginbutton"]'
    }

    # Login form, should receive user{email:email, pass: pass  }
    def set_login_from(self):
        login_form = {
            'email': self.driver.find_element_by_css_selector(self.page_elements['email_input']),
            'pass': self.driver.find_element_by_css_selector(self.page_elements['pass_input']),
            'btn': self.driver.find_element_by_css_selector(self.page_elements['login_btn']),
        }
        return login_form


class Fb_friends_page(object):
    def __init__(self, driver):
        self.driver = driver

    def scroll_the_page(self):
        SCROLL_PAUSE_TIME = 0.5
        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        d = []
        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)
            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                break
            last_height = new_height

    def count_friends(self):
        self.scroll_the_page()

        f = []
        # Select friends container
        container = self.driver.find_elements_by_css_selector('ul[data-pnref="friends"]')
        for friends in container:
            f += friends.find_elements_by_css_selector('li')

        return f
