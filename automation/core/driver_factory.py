from __future__ import annotations

from typing import Dict, Any

from appium import webdriver
from appium.options.android import UiAutomator2Options

from automation.config.settings import AutomationSettings


def build_capabilities(settings: AutomationSettings) -> Dict[str, Any]:
    capabilities: Dict[str, Any] = {
        "platformName": settings.device.platform_name,
        "appium:automationName": settings.appium.automation_name,
        "appium:deviceName": settings.device.device_name,
        "appium:appPackage": settings.app.package,
        "appium:appActivity": settings.app.activity,
        "appium:noReset": settings.app.no_reset,
        "appium:fullReset": settings.app.full_reset,
        "appium:autoGrantPermissions": settings.app.auto_grant_permissions,
    }
    if settings.device.platform_version:
        capabilities["appium:platformVersion"] = settings.device.platform_version
    if settings.device.udid:
        capabilities["appium:udid"] = settings.device.udid
    if settings.apk_file:
        capabilities["appium:app"] = str(settings.apk_file)
    return capabilities


def create_driver(settings: AutomationSettings) -> webdriver.Remote:
    options = UiAutomator2Options()
    options.load_capabilities(build_capabilities(settings))
    driver = webdriver.Remote(settings.appium.server_url, options=options)
    driver.implicitly_wait(settings.framework.implicit_wait_sec)
    return driver
