from playwright.sync_api import expect


class WorkoutEditorPage:
    def __init__(self, page):
        self.page = page
        self.tablet_info_window_ok_button = self.page.get_by_role("button", name="Ok")
        self.builder = self.page.locator("iframe").content_frame.locator("#unity-app-canvas")
        self.account_menu = self.page.locator("(//img[@alt='Avatar image'])").first
        self.menu_log_out_button = self.page.locator("//p[text()='Log Out']")
        self.confirm_log_out_button = self.page.get_by_role("button", name="Log Out", exact=True).last

    def tablet_info_window_ok_button_click(self):
        self.tablet_info_window_ok_button.click()

    def check_builder_visibility(self):
        expect(self.builder).to_be_visible(timeout=15000)

    def open_account_menu(self):
        self.account_menu.click()

    def log_out(self):
        self.open_account_menu()
        self.menu_log_out_button.click()
        self.confirm_log_out_button.click()
