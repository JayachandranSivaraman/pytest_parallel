from Common.TestBase import TestBase

class Test(TestBase) :

    def test_google(self):
        print("Test Google")
        assert "google" == self.driver.title.lower()

    def test_fb(self):
        print("Test Facebook")
        assert "google" == self.driver.title.lower()

    def test_twitter(self):
        print("Test Twitter")
        assert "google" == self.driver.title.lower()

    def test_linkedin(self):
        print("Test LinkedIn")
        assert "google" == self.driver.title.lower()

    def test_linkedin_1(self):
        print("Test LinkedIn_1")
        assert "google" == self.driver.title.lower()


