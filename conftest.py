import pytest

from playwright.sync_api import sync_playwright
from models.home_page import HomePage


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=True)
        yield browser
        browser.close()


@pytest.fixture
def setup(browser):
    context = browser.new_context(viewport={"width": 1920, "height": 1080}, locale="en-US")
    page = HomePage(context.new_page())
    # page.context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield page
    # page.context.tracing.stop(path="trace.zip")
