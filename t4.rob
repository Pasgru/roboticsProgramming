*** Settings ***
Documentation     Check page for header and link
Library           SeleniumLibrary

*** Variables ***
${LOGIN URL}      http://localhost:8080
${BROWSER}        Chrome

*** Test Cases ***
Headers and Links
    Check Home Page
    [Teardown]    Close Browser

*** Keywords ***
Check Home Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Element Should Contain     //h1    Credit App  
    Element Should Contain     //a     Clients  