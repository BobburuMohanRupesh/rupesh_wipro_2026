*** Settings ***
Library    SeleniumLibrary

# Suite-level setup and teardown
Suite Setup       Suite Initialization
Suite Teardown    Suite Cleanup

# Test-level setup and teardown
Test Setup        Test Initialization
Test Teardown     Test Cleanup


*** Variables ***
${URL}      https://tutorialsninja.com/demo/
${BROWSER}  Chrome


*** Keywords ***
Suite Initialization
    Log    ===== SUITE SETUP: TutorialsNinja Test Suite Started =====

Suite Cleanup
    Log    ===== SUITE TEARDOWN: TutorialsNinja Test Suite Finished =====

Test Initialization
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    0.5s

Test Cleanup
    Capture Page Screenshot
    Close Browser


*** Test Cases ***
Verify Home Page Title
    [Tags]    smoke    regression
    Title Should Be    Your Store

Verify Search Box Is Visible
    [Tags]    sanity
    Page Should Contain Element    name=search
