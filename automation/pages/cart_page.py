from __future__ import annotations

from automation.pages.base_page import BasePage


class CartPage(BasePage):
    def open_cart(self) -> None:
        self.tap("cart.cart_tab")

    def increase_first_item(self) -> None:
        self.tap("cart.first_item_increase")

    def decrease_first_item(self) -> None:
        self.tap("cart.first_item_decrease")

    def open_manage_mode(self) -> None:
        self.tap("cart.manage_button")

    def delete_selected(self) -> None:
        self.tap("cart.delete_button")

    def clear_invalid_items(self) -> None:
        self.tap("cart.clear_invalid_button")
