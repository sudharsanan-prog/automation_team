from src.automaton import webdriver
from src.automaton.options import DesktopOptions

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

# No additional actions, just keep Notepad open
# To prevent the script from exiting immediately, you can add a loop to keep it alive
try:
    input("Press Enter to close Notepad and exit the script...")
finally:
    driver.quit()  # Ensure the driver is closed when done
