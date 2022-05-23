import pytest
from pom.home_page_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_nav_links(self):
        home_page_nav = HomepageNav(self.driver)
        actual_links = home_page_nav.get_nav_links_text()
        expected_links = home_page_nav.NAV_LINK_TEXT
        assert expected_links == actual_links, 'Validating Nav Links text'
