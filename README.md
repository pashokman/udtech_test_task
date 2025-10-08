# How to setup and run testing

1. Clone repo from GitHub:
```
git clone git@github.com:pashokman/udtech_test_task.git
```

2. Create a virtual environment:
```
python -m venv venv
```

3. Activate virtual environment:
```
.\venv\Scripts\activate
```

4. Install required modules:
```
pip install -r requirements.txt
```

5. Install Playwright:
```
playwright install
```

6. Run tests:
```
python -m pytest
```

# Things I had to solve

1. I needed to refresh my knowledge of Playwright’s logic and syntax, as I hadn’t used it for some time.

2. I investigated why a test passed in headed mode but failed in headless mode using Playwright tracing. The issue was related to the context locale — in headed mode it was set to English, while in headless mode it defaulted to Ukrainian, causing locator mismatches.

3. I increased the timeout to allow more time for the builder to load - fixed test flakiness.