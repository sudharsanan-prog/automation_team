from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import Keys
from src.automaton import webdriver
from src.automaton.options import DesktopOptions
import time

# Set up capabilities
caps = DesktopOptions()
caps.set_capability("app", r"C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2409.9.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe")
caps.set_capability("automationName", "Windows")
caps.set_capability("newCommandTimeout", 60)

# Start the driver
driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4723',
    options=caps
)

driver.implicitly_wait(30)

# Locate the Notepad window
notepad_window = driver.find_element(AppiumBy.NAME, "Untitled")  # Adjust this if necessary

# Click on the "File" menu
file_menu = notepad_window.find_element(AppiumBy.NAME, "File")  # Locate the File menu
file_menu.click()

# Wait for the menu to open
time.sleep(1)

# Click on "Save" from the File menu
save_option = notepad_window.find_element(AppiumBy.NAME, "Save")  # Locate the Save option
save_option.click()

# Wait for the Save dialog to appear
time.sleep(2)  # Adjust time as needed to ensure the dialog is ready

# Type the filename to save
notepad_window.send_keys("example.txt")

# Press Enter to save the file
notepad_window.send_keys(Keys.RETURN)

# Optionally, keep the app open until the user decides to quit
input("Press Enter to close the application and exit the script...")

# Quit the driver after the interaction
driver.quit()
