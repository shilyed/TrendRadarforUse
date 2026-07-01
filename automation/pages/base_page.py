from __future__ import annotations

from functools import lru_cache
from typing import Any, Dict, Tuple

import yaml
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from automation.config.settings import AutomationSettings


class BasePage:
    _locator_alias = {
        "id": AppiumBy.ID,
        "xpath": AppiumBy.XPATH,
        "accessibility_id": AppiumBy.ACCESSIBILITY_ID,
        "class_name": AppiumBy.CLASS_NAME,
        "android_uiautomator": AppiumBy.ANDROID_UIAUTOMATOR,
    }

    def __init__(self, driver, settings: AutomationSettings):
        self.driver = driver
        self.settings = settings
        self.wait = WebDriverWait(driver, settings.framework.explicit_wait_sec)

    @classmethod
    @lru_cache(maxsize=8)
    def load_locators(cls, file_path: str) -> Dict[str, Any]:
        with open(file_path, "r", encoding="utf-8") as handle:
            return yaml.safe_load(handle) or {}

    def locator(self, key: str) -> Tuple[str, str]:
        config = self.load_locators(str(self.settings.locators_path))
        node: Dict[str, Any] = config
        for part in key.split("."):
            node = node[part]
        by = self._locator_alias[node["by"]]
        return by, node["value"]

    def find(self, key: str):
        return self.driver.find_element(*self.locator(key))

    def find_all(self, key: str):
        return self.driver.find_elements(*self.locator(key))

    def wait_for_visible(self, key: str):
        return self.wait.until(EC.visibility_of_element_located(self.locator(key)))

    def wait_for_clickable(self, key: str):
        return self.wait.until(EC.element_to_be_clickable(self.locator(key)))

    def wait_for_invisible(self, key: str):
        return self.wait.until(EC.invisibility_of_element_located(self.locator(key)))

    def tap(self, key: str) -> None:
        self.wait_for_clickable(key).click()

    def type_text(self, key: str, value: str, clear_first: bool = True) -> None:
        element = self.wait_for_visible(key)
        if clear_first:
            element.clear()
        element.send_keys(value)

    def text_of(self, key: str) -> str:
        return self.wait_for_visible(key).text

    def is_visible(self, key: str) -> bool:
        try:
            self.wait_for_visible(key)
            return True
        except Exception:
            return False

    def assert_text_contains(self, key: str, expected: str) -> None:
        actual = self.text_of(key)
        if expected not in actual:
            raise AssertionError(f"元素 {key} 文本不包含预期内容: {expected}，实际为: {actual}")

    def press_back(self) -> None:
        self.driver.back()

    def swipe_up(self, start_ratio: float = 0.8, end_ratio: float = 0.2, anchor_ratio: float = 0.5) -> None:
        size = self.driver.get_window_size()
        anchor_x = int(size["width"] * anchor_ratio)
        start_y = int(size["height"] * start_ratio)
        end_y = int(size["height"] * end_ratio)
        self.driver.swipe(anchor_x, start_y, anchor_x, end_y, 600)

    def pull_to_refresh(self) -> None:
        size = self.driver.get_window_size()
        anchor_x = int(size["width"] * 0.5)
        start_y = int(size["height"] * 0.25)
        end_y = int(size["height"] * 0.7)
        self.driver.swipe(anchor_x, start_y, anchor_x, end_y, 800)
