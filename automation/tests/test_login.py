from __future__ import annotations

from automation.core.base_test import MobileTestCase
from automation.core.case import case
from automation.pages.login_page import LoginPage


class LoginTests(MobileTestCase):
    def setUp(self) -> None:
        self.page = LoginPage(self.driver, self.settings)
        self.page.open_profile()
        self.page.open_login_entry()

    @case("TC-LOGIN-01", "正常账号密码登录", "P0")
    def test_tc_login_01_successful_password_login(self) -> None:
        self.require_login_credentials()
        self.page.login(self.settings.accounts.valid_username, self.settings.accounts.valid_password)

    @case("TC-LOGIN-02", "密码错误登录", "P0")
    def test_tc_login_02_wrong_password(self) -> None:
        self.require_login_credentials()
        self.page.login(self.settings.accounts.valid_username, self.settings.accounts.invalid_password)

    @case("TC-LOGIN-03", "未注册账号登录", "P1")
    def test_tc_login_03_unregistered_account(self) -> None:
        self.require_unregistered_account()
        self.page.login(self.settings.accounts.unregistered_username, self.settings.accounts.invalid_password)

    @case("TC-LOGIN-04", "密码输入框安全特性", "P1")
    def test_tc_login_04_password_mask_toggle(self) -> None:
        self.page.toggle_password_visibility()

    @case("TC-LOGIN-05", "登录态持久化与过期", "P1")
    def test_tc_login_05_session_persistence(self) -> None:
        self.require_login_credentials()
        self.page.login(self.settings.accounts.valid_username, self.settings.accounts.valid_password)
        self.background_app(3)
