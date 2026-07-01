from __future__ import annotations

import unittest
from pathlib import Path

from automation.config.settings import load_settings
from automation.core.driver_factory import create_driver


class MobileTestCase(unittest.TestCase):
    driver = None
    settings = None

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.settings = load_settings()
        if cls.settings.framework.skip_if_example_config and (
            cls.settings.using_example_config or cls.settings.package_is_placeholder
        ):
            raise unittest.SkipTest(
                "请先复制 automation/config/android.example.yaml 为 android.local.yaml，"
                "并补齐真机、包名、Activity、账号和定位信息后再执行。"
            )
        cls.driver = create_driver(cls.settings)

    @classmethod
    def tearDownClass(cls) -> None:
        if cls.driver is not None:
            cls.driver.quit()
            cls.driver = None
        super().tearDownClass()

    def relaunch_app(self) -> None:
        self.driver.terminate_app(self.settings.app.package)
        self.driver.activate_app(self.settings.app.package)

    def background_app(self, seconds: int = 3) -> None:
        self.driver.background_app(seconds)

    def ensure_fresh_install(self) -> None:
        apk_file = self.settings.apk_file
        if not apk_file or not Path(apk_file).exists():
            self.skipTest("当前用例需要可安装 APK，请在 android.local.yaml 中配置 app.apk_path。")
        if self.driver.is_app_installed(self.settings.app.package):
            self.driver.remove_app(self.settings.app.package)
        self.driver.install_app(str(apk_file))
        self.driver.activate_app(self.settings.app.package)

    def require_login_credentials(self) -> None:
        if not self.settings.accounts.valid_username or not self.settings.accounts.valid_password:
            self.skipTest("当前用例需要有效登录账号，请在 android.local.yaml 中补充 accounts 配置。")

    def require_unregistered_account(self) -> None:
        if not self.settings.accounts.unregistered_username:
            self.skipTest("当前用例需要未注册账号，请在 android.local.yaml 中补充 accounts.unregistered_username。")
