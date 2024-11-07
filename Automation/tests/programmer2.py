from src.automaton import webdriver
from src.automaton.options import DesktopOptions
from appium.webdriver.common.appiumby import AppiumBy
import time

# Set up capabilities
caps = DesktopOptions()
caps.set_capability("app", "C:\\Program Files\\WindowsApps\\InspireSleepSyncProgrammer_11.2.0.2_neutral__jmsm63tvsjw2m\\ClinProgWpf\\ClinProgWpf.exe")
caps.set_capability("automationName", "Windows")
caps.set_capability("newCommandTimeout", 60)

# Start the driver
driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4723',
    options=caps
)

driver.implicitly_wait(30)

# Locate the "Settings" button using the Automation ID
try:
    settings_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "UploadButtonSettings")  # Try using Automation ID here
    if isinstance(settings_button, dict):
        print("Element retrieved as a dict. Converting to WebElement.")
        settings_button = driver.create_web_element(list(settings_button.values())[0])

    # Wait for the element to be interactable
    time.sleep(5)

    # Check if the element is displayed and enabled
    print("Is displayed:", settings_button.is_displayed())
    print("Is enabled:", settings_button.is_enabled())

    # Click the Settings button
    settings_button.click()
    print("Clicked on the Settings button successfully.")

except Exception as e:
    print(f"Failed to click on the Settings button: {e}")

# Keep the app open until the user decides to quit
input("Press Enter to close the application and exit the script...")

# Quit the driver after the interaction
driver.quit()
