from __future__ import annotations

from automation.pages.base_page import BasePage


class HomePage(BasePage):
    def wait_for_ready(self) -> None:
        self.wait_for_visible("home.home_tab")

    def wait_for_banner(self) -> None:
        self.wait_for_visible("home.banner")

    def tap_current_banner(self) -> None:
        self.tap("home.banner")

    def open_search(self) -> None:
        self.tap("home.search_entry")

    def open_menu_category(self) -> None:
        self.tap("product.menu_category")
