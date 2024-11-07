from robot.api.deco import keyword

class CustomLibrary:
    @keyword
    def custom_message(self, message):
        print(f"Custom Message: {message}")
