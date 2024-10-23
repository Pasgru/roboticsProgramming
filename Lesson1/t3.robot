*** Settings ***
Documentation     Check for text in page, expect fail
Library           SeleniumLibrary

*** Variables ***
${URL}            http://localhost:8080
${BROWSER}        Chrome

*** Test Cases ***
Fail
    Open Browser To Home Page
    Page Should Contain    The Credit App
    [Teardown]    Close Browser

*** Keywords ***
Open Browser To Home Page
    Open Browser    ${URL}    ${BROWSER}