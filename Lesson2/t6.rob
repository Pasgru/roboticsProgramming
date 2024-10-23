*** Settings ***
Documentation     Check new client insert
Library           SeleniumLibrary
Library           mytools.py

*** Variables ***
${LOGIN URL}      http://localhost:8080
${BROWSER}        Chrome
${ID}             1

*** Test Cases ***    
Valid App Start Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Page Should Contain Link    //a[@href="clients"]  
    Page Should Contain Link    //a[@href="newclient"] 
    Page Should Contain Link    //a[@href="initdb"]

Valid Init DB
    Go To           ${LOGIN URL}
    Click Link      //a[@href="initdb"]
    Page Should Contain     DB initialized. 

Valid Insert
    ${LIM}=                 Get New Client Limit
    Go To                   ${LOGIN URL}
    Click Link              //a[@href="newclient"]
    Page Should Contain     New Client
    Input Text              //input[@name="id"]    ${ID}
    Input Text              //input[@name="lim"]   ${LIM}
    Click Element           //input[@type="submit"]
    Page Should Contain     Client inserted 
    Set Global Variable     ${LIM}

Valid Listing
    Go To           ${LOGIN URL}
    Click Link      //a[@href="clients"]
    Page Should Contain     ${ID}
    Page Should Contain     ${LIM}
    [Teardown]      Close Browser