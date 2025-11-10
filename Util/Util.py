#if u see something is common for all the pages then create one util and make parent for the pages
class BrowserUtil:
    def __init__(self,driver):
        self.driver = driver

    def title(self):
        return self.driver.title







