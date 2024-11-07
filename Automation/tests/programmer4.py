from src.automaton import webdriver
from src.automaton.options import DesktopOptions
from appium.webdriver.common.appiumby import AppiumBy
from pywinauto import Application
import psutil
import time

# Set up capabilities
caps = DesktopOptions()
caps.set_capability("app", "C:\\Program Files\\WindowsApps\\InspireSleepSyncProgrammer_11.2.0.2_neutral__jmsm63tvsjw2m\\ClinProgWpf\\ClinProgWpf.exe")
caps.set_capability("automationName", "Windows")
caps.set_capability("newCommandTimeout", 60)

driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4723',
    options=caps
)


# Function to get the process ID by name
def get_process_id_by_name(process_name):
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        if process_name.lower() in proc.info['name'].lower():
            return proc.info['pid']
    return None
##########################################################################

def click_button( driver , btn_value, by_type=AppiumBy.ACCESSIBILITY_ID):
    try:
        # Locate and click the button using the specified attribute type (default: Accessibility ID)
        button = driver.find_element(by_type, btn_value)
        if isinstance(button, dict):
            print("Element retrieved as a dict. Converting to WebElement.")
            button = driver.create_web_element(list(button.values())[0])

        print(f"Is displayed: {button.is_displayed()}")
        print(f"Is enabled: {button.is_enabled()}")
        button.click()
        print(f"Clicked on the button with {by_type} '{btn_value}' successfully.")
    except Exception as e:
        print(f"Failed to perform the click operation: {e}")


###########################################################################

# Retrieve the process ID (replace with correct process name if needed)
process_id = get_process_id_by_name("ClinProgWpf.exe")

if process_id:
    # Connect to the application using pywinauto
    app = Application(backend="uia").connect(process=process_id)
    app_window = app.top_window()
    app_window.maximize()
    print("Application window maximized.")
else:
    print("Process ID for the application could not be found.")
    driver.quit()
    exit()

driver.implicitly_wait(30)

# Locate and click the "Demo" button using the Automation ID
try:
    time.sleep(5)
    #1. Clicking on the demo button
    click_button(driver, "UploadButtonDemo")  # Using Accessibility ID

    #2. Clicking the model of the demo
    click_button(driver, "Inspire V (Model 3150)", AppiumBy.NAME)  # Using Name

    # 3. Clicking on continue on the model
    click_button(driver, "Continue", AppiumBy.NAME)

    # 4. Clicking on the exit button
    time.sleep(10)
    click_button(driver, "btn_exit", AppiumBy.ACCESSIBILITY_ID)

except Exception as e:
    print(f"Failed to perform the click operations: {e}")

# Keep the app open until the user decides to quit
input("Press Enter to close the application and exit the script...")

# Quit the driver after the interaction
driver.quit()
