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

# Function to recursively print controls
def print_controls(control, indent=""):
    control_name = control.get_attribute("Name") or ''
    control_id = control.get_attribute("AutomationId") or ''
    control_type = control.get_attribute("ControlType") or ''
    rect = control.get_attribute("BoundingRectangle") or ''

    # Print control details
    print(f"{indent}{control_type} - '{control_name}'    {rect}")
    # Print any identifiers associated with the control
    identifiers = control.get_attribute("AutomationId") or ''
    print(f"{indent}{identifiers}")

    # Find child elements
    children = control.find_elements(AppiumBy.XPATH, ".//*")
    for child in children:
        print_controls(child, indent + "   |   ")

try:
    demo_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "UploadButtonDemo")
    demo_button.click()
    print("Clicked on the Demo button successfully.")

    time.sleep(5)  # Wait before next actions

    inspire_button = driver.find_element(AppiumBy.NAME, "Inspire V (Model 3150)")
    inspire_button.click()
    print("Clicked on the Inspire V (Model 3150) button successfully.")

    time.sleep(5)  # Wait before next actions

    continue_button = driver.find_element(AppiumBy.NAME, "Continue")
    continue_button.click()
    print("Clicked on the Continue button successfully.")

    # Wait for the dialog to appear
    time.sleep(5)

    # Now print the controls of the dialog
    dialog = driver.find_element(AppiumBy.XPATH, "//*[contains(@Name, 'Inspire Programmer')]")  # Adjust XPath as necessary
    print_controls(dialog)

except Exception as e:
    print(f"Failed to perform the click operations: {e}")

# Keep the app open until the user decides to quit
input("Press Enter to close the application and exit the script...")

# Quit the driver after the interaction
driver.quit()
