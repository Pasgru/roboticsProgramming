*** Settings ***
Library             SeleniumLibrary

*** Test Cases ***
Home Page
    Open Browser            http://localhost:8080    Chrome
    Page Should Contain     Credit App
    [Teardown]              Close Browser