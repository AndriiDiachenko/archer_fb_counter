import unittest

from archer_fb_counter.drivers import startdriver
from archer_fb_counter.pages import fb_friends

# Test user info here
test_user = {
    # 'id': 'dou.jons.5', - set FB id (link)
    # 'email': 'dou.jons@ex.ua', - set Email
    # 'pass': 'Qwert123' - set Password
}

# Starting page info here
start_page = 'https://facebook.com'
f_page = ''


class TestCoundFbFriends(unittest.TestCase, startdriver.StartDriver):
    def setUp(self):
        new_driver = startdriver.StartDriver()
        self.driver = new_driver.start()
        self.driver.get(start_page)

        # In this test login is in SetUp (bad practise)
        signin_frame = fb_friends.Fb_main_page(self.driver).set_login_from()
        signin_frame['email'].send_keys(test_user['email'])
        signin_frame['pass'].send_keys(test_user['pass'])
        signin_frame['btn'].click()

    def tearDown(self):
        self.driver.quit()

    def test_count_friends(self):
        # Open Friends page
        self.driver.get(('https://www.facebook.com/{}/friends').format(test_user['id']))

        # Get friends list
        friends_list = fb_friends.Fb_friends_page(self.driver).count_friends()

        assert len(friends_list) > 0


if __name__ == '__main__':
    unittest.main()
