*** Settings ***
Library    AppiumLibrary
Library    CustomLibrary.py  # This is your custom Python library

*** Variables ***
${REMOTE_URL}    http://127.0.0.1:4723/wd/hub
${PLATFORM_NAME}    Windows
${APP}    C:/Windows/System32/notepad.exe

*** Test Cases ***
Open Notepad and Type Text
    Open Application    ${REMOTE_URL}    platformName=${PLATFORM_NAME}    app=${APP}
    Sleep    2s
    Input Text    name=Text Editor    Hello, this is an automated test in Notepad!
    Sleep    2s
    Close Application

    Custom Message    This is a test using a Python keyword