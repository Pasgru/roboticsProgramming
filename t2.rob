*** Settings ***
Documentation     Check for text in page
Library           SeleniumLibrary

*** Variables ***
${URL}            http://localhost:8080
${BROWSER}        Chrome

*** Test Cases ***
Keywords
    OBTHP
    Page Should Contain    Credit App
    [Teardown]    Close Browser

*** Keywords ***
OBTHP
    Open Browser    ${URL}    ${BROWSER}