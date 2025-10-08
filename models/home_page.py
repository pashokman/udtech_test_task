from models.login_page import LoginPage


class HomePage:
    def __init__(self, page):
        self.page = page
        self.url = "https://events.shooters.global/"
        self.build_for_free_btn = page.get_by_role("button", name="Build for free").first

    def navigate(self):
        self.page.goto(self.url)

    def build_for_free_btn_click(self):
        self.build_for_free_btn.click()
        return LoginPage(self.page)
