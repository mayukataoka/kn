
import random
import pytest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),  ".."))
from pages.header import Header

@pytest.mark.usefixtures("setup_driver")
class TestSignUp:



    def test_get_schedule_summary(self):
        assert 'Khan Academy' in self.driver.title

        header_page = Header(self.driver)
        sign_up_page = header_page.open_sign_up()
        email = "asdf@asdf.com"
        rand_num = str(random.sample(range(1, 10000), 1)[0])
        username = "aiwmndjhr" + rand_num
        password = "aiwmndjhr" + rand_num
        personalize_ka_page = sign_up_page.join_ka('learner', email, username, password)
        assert personalize_ka_page.is_popup_dialog_visible()

