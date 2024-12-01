*** Settings ***
Library             SeleniumLibrary
Library             Collections
Library             OperatingSystem
Library             mytools.py
Library             predict.py

*** Variables ***
# ${URL}              https://www.willhaben.at/iad/gebrauchtwagen/d/auto/kia-ceed-1-6-1228510375
${URL}              https://www.willhaben.at/iad/gebrauchtwagen/d/auto/kia-stonic-1-2-dpi-isg-titan-p1-adap-p2-titan-759431666/
${OUTPUT_CSV}       car_data.csv
${brand}
${transmission}
${make_year}
${fuel_type}
${km_driven}
${predicted_price}

*** Test Cases ***
Extract Car Data and Save To CSV
    [Documentation]    Extracts car details and saves them to a CSV file.
    
    Open Browser and Navigate
    Handle Popup
    Extract Car Data
    ${predicted_price}=     Load Model And Predict
    Log To Console    The predicted price is: ${predicted_price} Euros


*** Keywords ***
Open Browser and Navigate
    [Documentation]    Opens the given URL and waits for the page to load.
    Open Browser    ${URL}    Chrome
    Maximize Browser Window
    Sleep    1

Handle Popup
    [Documentation]    Wait for the popup and click the button to close it.
    Wait Until Element Is Visible    xpath=/html/body/div[1]/div/div/div/div/div/div[3]/button[2]
    Click Element    xpath=/html/body/div[1]/div/div/div/div/div/div[3]/button[2]

Extract Car Data
    [Documentation]    Extracts brand, transmission, make year, fuel type, engine capacity, and km driven.
    ${brand}=               Get Text    xpath=/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[4]/div/article/section[3]/div/div[1]/div/div[1]/div[1]/h1
    ${transmission}=        Get Text    xpath=//span[contains(text(), 'Getriebeart')]/following::div[1]
    ${make_year}=           Get Text    xpath=//span[contains(text(), 'Erstzulassung')]/following::div[1]
    ${fuel_type}=           Get Text    xpath=//span[contains(text(), 'Treibstoff')]/following::div[1]
    ${km_driven}=           Get Text    xpath=//span[contains(text(), 'Kilometerstand')]/following::div[1]    

    Create My File            output.txt
    Append My File            output.txt     ${brand}
    Append My File            output.txt     ${transmission}
    Append My File            output.txt     ${make_year}
    Append My File            output.txt     ${fuel_type}
    Append My File            output.txt     ${km_driven}
    
