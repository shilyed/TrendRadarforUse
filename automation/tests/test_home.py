from __future__ import annotations

from automation.core.base_test import MobileTestCase
from automation.core.case import case
from automation.pages.home_page import HomePage


class HomeTests(MobileTestCase):
    def setUp(self) -> None:
        self.page = HomePage(self.driver, self.settings)
        self.page.wait_for_ready()

    @case("TC-HOME-01", "轮播图正常自动轮播", "P1")
    def test_tc_home_01_banner_auto_rotation(self) -> None:
        self.page.wait_for_banner()

    @case("TC-HOME-02", "轮播图点击跳转-商品详情页", "P0")
    def test_tc_home_02_banner_to_product_detail(self) -> None:
        self.page.wait_for_banner()
        self.page.tap_current_banner()

    @case("TC-HOME-03", "轮播图点击跳转-活动专题页", "P0")
    def test_tc_home_03_banner_to_campaign(self) -> None:
        self.page.wait_for_banner()
        self.page.tap_current_banner()

    @case("TC-HOME-04", "轮播图点击跳转-外部链接", "P1")
    def test_tc_home_04_banner_to_external_link(self) -> None:
        self.page.wait_for_banner()
        self.page.tap_current_banner()

    @case("TC-HOME-05", "轮播图加载失败", "P2")
    def test_tc_home_05_banner_fallback_when_offline(self) -> None:
        self.page.pull_to_refresh()
