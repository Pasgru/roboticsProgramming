*** Settings ***
Documentation     Init DB and insert some clients
Library           SeleniumLibrary
Library           mytools.py

*** Variables ***
${LOGIN URL}      http://localhost:8080
${BROWSER}        Chrome

*** Test Cases ***    
Init DB
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Click Link      //a[@href="initdb"]
    Page Should Contain     DB initialized
    
Insert Several Clients
    Insert Client     id=1001         lim=4000
    Insert Client     id=1002         lim=8000
    Insert Client     id=2001 
    Insert Client     id=2002         lim=6000
    [Teardown]      Close Browser

*** Keywords ***
Insert Client
    [Arguments]                ${id}        ${lim}=5000
    Go To                      ${LOGIN URL}
    Click Link                 //a[@href="newclient"]
    Page Should Contain        New Client
    Input Text                 //input[@name="id"]     ${id}
    Input Text                 //input[@name="lim"]    ${lim}
    Click Element              //input[@type="submit"]
    Page Should Contain        Client inserted 