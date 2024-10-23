*** Settings ***
Library             SeleniumLibrary
Library             mytools.py

*** Variables ***
${url}       https://www.pocket-lint.com/tv/news/148096-james-bond-007-best-movie-viewing-order-chronological-release

*** Test Cases ***
Start Movie List
    Open Browser              ${url}    Chrome
    Page Should Contain       James Bond movies
    Create My File            list.txt

Iterate Through Movies
    ${elements}=    Get WebElements    //h3
    FOR    ${element}    IN    @{elements}
        Append My File    list.txt    ${element.text}
    END
    [Teardown]      Close Browser