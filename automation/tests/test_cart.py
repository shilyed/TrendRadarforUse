from __future__ import annotations

from automation.core.base_test import MobileTestCase
from automation.core.case import case
from automation.pages.cart_page import CartPage


class CartTests(MobileTestCase):
    def setUp(self) -> None:
        self.page = CartPage(self.driver, self.settings)
        self.page.open_cart()

    @case("TC-CART-01", "购物车-商品数量增加", "P0")
    def test_tc_cart_01_increase_quantity(self) -> None:
        self.page.increase_first_item()

    @case("TC-CART-02", "购物车-商品数量减少至1", "P0")
    def test_tc_cart_02_reduce_quantity_to_one(self) -> None:
        self.page.decrease_first_item()

    @case("TC-CART-03", "购物车-商品数量减少至0（删除逻辑）", "P0")
    def test_tc_cart_03_reduce_quantity_to_zero(self) -> None:
        self.page.decrease_first_item()

    @case("TC-CART-04", "购物车-批量删除", "P1")
    def test_tc_cart_04_batch_delete(self) -> None:
        self.page.open_manage_mode()
        self.page.delete_selected()

    @case("TC-CART-05", "购物车-库存不足/失效商品展示", "P1")
    def test_tc_cart_05_invalid_product_state(self) -> None:
        self.page.clear_invalid_items()

    @case("TC-CART-06", "购物车-金额精度计算", "P1")
    def test_tc_cart_06_price_precision(self) -> None:
        self.page.wait_for_visible("cart.total_price")
