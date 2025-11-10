
import os
import time
from selenium.common.exceptions import WebDriverException
import pytest
from selenium import webdriver
#declaring driver as none as globally for reuse to make use for screenshhot method

def pytest_addoption(parser): #this hook helps to register the new line command arguments
    parser.addoption(
        "--browser_name", action="store", default="firefox", help="Type of browser: chrome or firefox"
    )


@pytest.fixture()
def BrowserSetup(request): #it will take the command line input as request( pytest filename --variable_name chrome/firefox )
     #we activated our driver here
    browser_name = request.config.getoption("browser_name")  #will to get variable name like (chrome or firefox) #getoption itself takes --variable name no need to mention -- again
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    driver.implicitly_wait(10)
    yield driver
    driver.close()


# to capture screenshot and attach to the html when only something is failing in the tests




@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook that runs after each test. Captures screenshot on failure
    and attaches it to pytest-html report.
    """
    # let pytest run the actual test and get its result
    outcome = yield
    report = outcome.get_result()

    # ensure 'extra' attribute exists
    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("BrowserSetup")

        if driver:
            try:
                driver.current_url  # ensure driver session is still active
            except WebDriverException:
                print("⚠️ Cannot capture screenshot — browser already closed.")
                return

            # make screenshots directory
            screenshots_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            # save screenshot
            timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"{item.name}_{timestamp}.png"
            destination_file = os.path.join(screenshots_dir, file_name)

            try:
                driver.save_screenshot(destination_file)
                print(f"📸 Screenshot saved: {destination_file}")
            except WebDriverException:
                print("⚠️ Failed to save screenshot due to WebDriver error.")
                return

            # Attach screenshot to HTML report
            from pytest_html import extras
            extra.append(extras.image(destination_file))

            # ✅ Update report.extra manually
            report.extra = extra
            print("✅ Screenshot attached to pytest-html report.")