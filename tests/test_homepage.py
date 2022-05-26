import time
import pytest
from pom.home_page_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_nav_links(self):
        home_page_nav = HomepageNav(self.driver)
        # home_page_nav.driver.delete_cookie('ak_bmsc')
        # cookies = home_page_nav.driver.get_cookies()
        # cookies_names = [cookie['name'] for cookie in cookies]
        # print(cookies)
        # print('------------------------------------------')
        # print(cookies_names)
        for indx in range(12):
            home_page_nav.get_nav_links()[indx].click()
            # home_page_nav.driver.delete_cookie('ak_bmsc')
            # for cookie_name in cookies_names:
            #     home_page_nav.driver.delete_cookie('ak_bmsc')
            #     home_page_nav.driver.refresh()
            #     home_page_nav.is_visible('tag_name', 'h1', cookie_name)
            # time.sleep(1.5)
