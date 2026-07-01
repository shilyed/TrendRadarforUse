from __future__ import annotations

from automation.core.base_test import MobileTestCase
from automation.core.case import case
from automation.pages.customer_service_page import CustomerServicePage


class CustomerServiceTests(MobileTestCase):
    def setUp(self) -> None:
        self.page = CustomerServicePage(self.driver, self.settings)

    @case("TC-CS-01", "客服入口可进入", "P0")
    def test_tc_cs_01_open_customer_service(self) -> None:
        self.page.open_customer_service()

    @case("TC-CS-02", "客服消息发送", "P1")
    def test_tc_cs_02_send_message(self) -> None:
        self.page.open_customer_service()
        self.page.send_message(self.settings.test_data.customer_service_message)
