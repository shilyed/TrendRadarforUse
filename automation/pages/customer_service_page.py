from __future__ import annotations

from automation.pages.base_page import BasePage


class CustomerServicePage(BasePage):
    def open_customer_service(self) -> None:
        self.tap("customer_service.entry")

    def send_message(self, message: str) -> None:
        self.type_text("customer_service.message_input", message)
        self.tap("customer_service.send_button")
