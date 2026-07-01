from __future__ import annotations

from automation.core.base_test import MobileTestCase
from automation.core.case import case
from automation.pages.startup_page import StartupPage


class StartupTests(MobileTestCase):
    def setUp(self) -> None:
        self.page = StartupPage(self.driver, self.settings)

    @case("TC-START-01", "首次安装冷启动-隐私政策弹窗", "P0")
    def test_tc_start_01_first_install_privacy_dialog(self) -> None:
        self.ensure_fresh_install()
        self.page.wait_for_splash_logo()
        self.page.wait_for_privacy_dialog()
        self.page.assert_privacy_actions()

    @case("TC-START-02", "隐私政策不同意流程", "P0")
    def test_tc_start_02_reject_privacy(self) -> None:
        self.ensure_fresh_install()
        self.page.wait_for_privacy_dialog()
        self.page.reject_privacy()

    @case("TC-START-03", "非首次启动-隐私政策不再弹出", "P1")
    def test_tc_start_03_relaunch_without_privacy_dialog(self) -> None:
        self.page.wait_for_privacy_dialog()
        self.page.agree_privacy()
        self.page.wait_for_home_loaded()
        self.relaunch_app()
        self.page.wait_for_home_loaded()
        self.assertFalse(self.page.is_visible("startup.privacy_dialog"), "非首次启动不应再次出现隐私弹窗")
