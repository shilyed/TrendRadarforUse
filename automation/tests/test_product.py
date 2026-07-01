from __future__ import annotations

from automation.core.base_test import MobileTestCase
from automation.core.case import case
from automation.pages.home_page import HomePage
from automation.pages.product_page import ProductPage


class ProductTests(MobileTestCase):
    def setUp(self) -> None:
        self.home_page = HomePage(self.driver, self.settings)
        self.page = ProductPage(self.driver, self.settings)

    @case("TC-PROD-01", "商品列表浏览", "P1")
    def test_tc_prod_01_browse_category_list(self) -> None:
        self.home_page.open_menu_category()
        self.page.wait_for_list_ready()

    @case("TC-PROD-02", "商品列表浏览-上拉加载更多", "P1")
    def test_tc_prod_02_scroll_to_load_more(self) -> None:
        self.home_page.open_menu_category()
        self.page.wait_for_list_ready()
        self.page.swipe_up()

    @case("TC-PROD-03", "商品详情页-SKU选择", "P0")
    def test_tc_prod_03_select_sku_from_detail(self) -> None:
        self.home_page.open_menu_category()
        self.page.open_first_product()
        self.page.add_to_cart_from_detail()
        self.page.choose_color(self.settings.test_data.product_color)
        self.page.choose_size(self.settings.test_data.product_size)
        self.page.confirm_sku()

    @case("TC-PROD-04", "商品详情页-缺货SKU处理", "P1")
    def test_tc_prod_04_out_of_stock_sku(self) -> None:
        self.home_page.open_menu_category()
        self.page.open_first_product()
        self.page.add_to_cart_from_detail()

    @case("TC-PROD-05", "加购全流程-从列表页直接加购", "P0")
    def test_tc_prod_05_quick_add_from_list(self) -> None:
        self.home_page.open_menu_category()
        self.page.wait_for_list_ready()
        self.page.open_quick_add()
        self.page.choose_color(self.settings.test_data.product_color)
        self.page.choose_size(self.settings.test_data.product_size)
        self.page.confirm_sku()

    @case("TC-SEARCH-01", "搜索-关键词正常匹配", "P0")
    def test_tc_search_01_keyword_match(self) -> None:
        self.home_page.open_search()
        self.page.search(self.settings.test_data.search_keyword)

    @case("TC-SEARCH-02", "搜索-无结果处理", "P1")
    def test_tc_search_02_no_result_state(self) -> None:
        self.home_page.open_search()
        self.page.search(self.settings.test_data.invalid_search_keyword)

    @case("TC-SEARCH-03", "搜索-联想词", "P1")
    def test_tc_search_03_search_suggestions(self) -> None:
        self.home_page.open_search()
        self.page.type_text("product.search_input", self.settings.test_data.suggestion_keyword)
