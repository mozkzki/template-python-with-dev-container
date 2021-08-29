import time

import pytest
from main.my.app import login


class TestMain:
    def test_login(self):
        result = login("foo", "xxxxx")
        assert result == "done."

    @pytest.mark.slow
    def test_login_slow(self):
        result = login("bar", "xxxxx")
        time.sleep(2)
        assert result == "done."
