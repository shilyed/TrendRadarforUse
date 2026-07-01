from __future__ import annotations

from automation.pages.base_page import BasePage


class ProductPage(BasePage):
    def wait_for_list_ready(self) -> None:
        self.wait_for_visible("product.product_list")

    def open_first_product(self) -> None:
        self.tap("product.first_product_card")

    def open_quick_add(self) -> None:
        self.tap("product.quick_add_button")

    def add_to_cart_from_detail(self) -> None:
        self.tap("product.add_to_cart_button")

    def choose_color(self, color_name: str) -> None:
        self.type_text("product.color_input", color_name)

    def choose_size(self, size_name: str) -> None:
        self.type_text("product.size_input", size_name)

    def confirm_sku(self) -> None:
        self.tap("product.sku_confirm_button")

    def search(self, keyword: str) -> None:
        self.type_text("product.search_input", keyword)
        self.tap("product.search_submit")
