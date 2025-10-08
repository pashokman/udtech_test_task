from models.workout_editor_page import WorkoutEditorPage


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.email_or_phone_field = self.page.get_by_role("textbox", name="Enter your email or phone")
        self.password_field = self.page.get_by_role("textbox", name="Enter password")
        self.sign_in_button = self.page.get_by_role("button", name="Sign in", exact=True)

    def fill_email_or_phone(self, email_or_phone):
        self.email_or_phone_field.fill(email_or_phone)

    def fill_password(self, password):
        self.password_field.fill(password)

    def sign_in_button_click(self):
        self.sign_in_button.click()

    def login(self, email_or_phone, password):
        self.fill_email_or_phone(email_or_phone)
        self.fill_password(password)
        self.sign_in_button_click()
        return WorkoutEditorPage(self.page)
