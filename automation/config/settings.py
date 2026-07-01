from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional

import yaml


ROOT_DIR = Path(__file__).resolve().parents[2]
DEFAULT_LOCAL_CONFIG = ROOT_DIR / "automation" / "config" / "android.local.yaml"
DEFAULT_EXAMPLE_CONFIG = ROOT_DIR / "automation" / "config" / "android.example.yaml"


@dataclass
class AppiumConfig:
    server_url: str
    automation_name: str = "UiAutomator2"


@dataclass
class DeviceConfig:
    platform_name: str
    device_name: str
    platform_version: str = ""
    udid: str = ""


@dataclass
class AppConfig:
    package: str
    activity: str
    apk_path: str = ""
    no_reset: bool = False
    full_reset: bool = False
    auto_grant_permissions: bool = True


@dataclass
class FrameworkConfig:
    implicit_wait_sec: int = 8
    explicit_wait_sec: int = 20
    screenshot_dir: str = "automation/output"
    locators_file: str = "automation/config/locators.example.yaml"
    skip_if_example_config: bool = True


@dataclass
class AccountConfig:
    valid_username: str = ""
    valid_password: str = ""
    invalid_password: str = "wrong-password"
    unregistered_username: str = ""


@dataclass
class TestDataConfig:
    search_keyword: str = "连衣裙"
    invalid_search_keyword: str = "xyz123"
    suggestion_keyword: str = "牛仔"
    customer_service_message: str = "这件衣服有M码吗"
    product_color: str = "白色"
    product_size: str = "M"


@dataclass
class AutomationSettings:
    appium: AppiumConfig
    device: DeviceConfig
    app: AppConfig
    framework: FrameworkConfig
    accounts: AccountConfig
    test_data: TestDataConfig
    config_path: str
    using_example_config: bool = False

    @property
    def package_is_placeholder(self) -> bool:
        return self.app.package.startswith("com.example") or self.app.activity.startswith(".Example")

    @property
    def locators_path(self) -> Path:
        return _resolve_path(self.framework.locators_file)

    @property
    def screenshot_path(self) -> Path:
        return _resolve_path(self.framework.screenshot_dir)

    @property
    def apk_file(self) -> Optional[Path]:
        if not self.app.apk_path:
            return None
        return _resolve_path(self.app.apk_path)


def _resolve_path(value: str) -> Path:
    path = Path(value)
    if not path.is_absolute():
        path = ROOT_DIR / path
    return path.resolve()


def _load_yaml(file_path: Path) -> Dict[str, Any]:
    with file_path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def _pick_config_path(config_path: Optional[str]) -> Path:
    if config_path:
        return _resolve_path(config_path)
    env_path = os.getenv("ANDROID_AUTOMATION_CONFIG")
    if env_path:
        return _resolve_path(env_path)
    if DEFAULT_LOCAL_CONFIG.exists():
        return DEFAULT_LOCAL_CONFIG
    return DEFAULT_EXAMPLE_CONFIG


def load_settings(config_path: Optional[str] = None) -> AutomationSettings:
    resolved_path = _pick_config_path(config_path)
    raw = _load_yaml(resolved_path)

    framework = FrameworkConfig(**raw.get("framework", {}))
    settings = AutomationSettings(
        appium=AppiumConfig(**raw.get("appium", {})),
        device=DeviceConfig(**raw.get("device", {})),
        app=AppConfig(**raw.get("app", {})),
        framework=framework,
        accounts=AccountConfig(**raw.get("accounts", {})),
        test_data=TestDataConfig(**raw.get("test_data", {})),
        config_path=str(resolved_path),
        using_example_config=resolved_path == DEFAULT_EXAMPLE_CONFIG,
    )
    settings.screenshot_path.mkdir(parents=True, exist_ok=True)
    return settings
