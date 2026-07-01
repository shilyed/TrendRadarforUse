from __future__ import annotations

from automation.pages.base_page import BasePage


class StartupPage(BasePage):
    def wait_for_splash_logo(self) -> None:
        self.wait_for_visible("startup.splash_logo")

    def wait_for_privacy_dialog(self) -> None:
        self.wait_for_visible("startup.privacy_dialog")

    def assert_privacy_actions(self) -> None:
        self.wait_for_visible("startup.privacy_agree_button")
        self.wait_for_visible("startup.privacy_reject_button")

    def agree_privacy(self) -> None:
        self.tap("startup.privacy_agree_button")

    def reject_privacy(self) -> None:
        self.tap("startup.privacy_reject_button")

    def wait_for_home_loaded(self) -> None:
        self.wait_for_visible("home.home_tab")
