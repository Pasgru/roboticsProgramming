*** Settings ***
Documentation     Check page for header and links
Library           SeleniumLibrary

*** Variables ***
${LOGIN URL}      http://localhost:8080/
${BROWSER}        Chrome

*** Test Cases ***
XPath
    Check Home Page
    [Teardown]    Close Browser

*** Keywords ***
Check Home Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Element Should Contain     //h1    Credit App  
    Element Should Contain     //a     Clients  
    Element Should Contain     //a[contains(text(), "Init DB")]     Init DB  