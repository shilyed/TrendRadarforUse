from __future__ import annotations

from automation.pages.base_page import BasePage


class LoginPage(BasePage):
    def open_profile(self) -> None:
        self.tap("login.profile_tab")

    def open_login_entry(self) -> None:
        self.tap("login.login_entry")

    def login(self, username: str, password: str) -> None:
        self.type_text("login.username_input", username)
        self.type_text("login.password_input", password)
        self.tap("login.submit_button")

    def toggle_password_visibility(self) -> None:
        self.tap("login.password_toggle")
