# ======================
# XPath LOCATORS (25)
# ======================

xpath_locators = [

    "//button[text()='Sign up']",
    "//button[text()='Sign in']",
    "//h1[text()='Hillel Qauto']",
    "//input[@name='name']",
    "//input[@name='lastName']",
    "//input[@name='email']",
    "//input[@name='password']",
    "//input[@id='signupName']",
    "//input[@id='signupLastName']",
    "//input[@id='signupEmail']",
    "//input[@id='signupPassword']",
    "//div[@class='modal-content']",
    "//button[@class='btn btn-primary']",
    "//button[contains(@class,'btn')]",
    "//a[@href='/contacts']",
    "//a[text()='Contacts']",
    "//a[text()='About']",
    "//a[text()='Home']",
    "//div[@class='hero-descriptor']",
    "//div[contains(@class,'hero')]",
    "//img[@class='hero-img']",
    "//header//button[text()='Sign in']",
    "//footer//a[contains(@href,'facebook')]",
    "//footer//a[contains(@href,'telegram')]",
    "//footer//a[contains(@href,'youtube')]"
]


# ======================
# CSS LOCATORS (25)
# ======================

css_locators = [

    "button.btn-primary",
    "button.btn-outline-white",
    "h1.hero-title",
    "input[name='name']",
    "input[name='lastName']",
    "input[name='email']",
    "input[name='password']",
    "#signupName",
    "#signupLastName",
    "#signupEmail",
    "#signupPassword",
    ".modal-content",
    ".btn.btn-primary",
    ".btn.btn-outline-white",
    "a[href='/contacts']",
    "a.nav-link",
    "header .btn-outline-white",
    "header button.btn",
    "footer a[href*='facebook']",
    "footer a[href*='telegram']",
    "footer a[href*='youtube']",
    "div.hero-descriptor",
    "div.hero-img",
    "div.container h1",
    "header nav a"
]


# просто для перевірки
if __name__ == "__main__":
    print("XPath count:", len(xpath_locators))
    print("CSS count:", len(css_locators))