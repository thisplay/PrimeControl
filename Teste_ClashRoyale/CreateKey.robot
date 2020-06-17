*** Settings ***
Documentation     Arquivos com as keywords e variaveis para o Robot.
Library           SeleniumLibrary
Library           OperatingSystem

*** Variables ***
${SERVER}         developer.clashroyale.com  
${SERVER_IP}      https://icanhazip.com/
${BROWSER}        Chrome
${DELAY}          0
${VALID USER}     douglas2012.ribeiro2gmail.com
${VALID PASSWORD}    TestePrime
${SITE URL}       https://${SERVER}
${PATH}           ${CURDIR}/MyKey.txt

*** Keywords ***

Open Browser To Login Page
    Open Browser    ${SITE URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}
    Title Should Be    Clash Royale API
    Click Element By Script    "//a[contains(text(),'Log In')]"
    

Input Username
    [Arguments]    ${username}
    Input Text    email    ${username}

Input Password
    [Arguments]    ${password}
    Input Text    password    ${password}

Submit Credentials
    Click Button    xpath=//*[@type='submit']

Get IpExterno
    Open Browser    ${SERVER_IP}    ${BROWSER}
    Maximize Browser Window
    ${txtIP}      Get Element By Script  "/html/body/pre/text()"
    Log to console   IP_Externo: ${txtIP}
    Close Browser
    [Return]    ${txtIP}

Create Key
    [Arguments]   ${nome}   ${obs}   ${ipExt} 
    Sleep   3s
    Click Element       xpath=//*[@id="content"]/div/div[2]/div/header/div/div/div[3]/div/div/button
    Wait Until Element Is Visible     xpath=//*[@id="content"]/div/div[2]/div/header/div/div/div[3]/div/div/ul/li[1]/a
    Click Element       xpath=//*[@id="content"]/div/div[2]/div/header/div/div/div[3]/div/div/ul/li[1]/a
    Sleep   3s
    Click Element By Script    "//*[@id='content']/div/div[2]/div/div/section[2]/div/div/div[2]/p/a"
    Input Text   name   ${nome}
    Input Text   description   ${obs}
    Input Text   range-0    ${ipExt}
    Click Button    xpath=//*[@type='submit']
    Save Key   ${nome}
    Log to console   Chave salva no arquivo ${PATH}
    
        
Save Key
    [Arguments]  ${nomeCriado}
    Sleep   3s
    Click Element       xpath=//h4[@class='api-key__name' and text()='${nomeCriado}']
    ${txtKey}      Get Element By Script  "//*[@id='content']/div/div[2]/div/div/section/div/div/div[2]/form/div[1]/div/samp/text()"
    Create File   ${PATH}
    Append to File   MyKey.txt   ${txtKey}
    
    
Click Element By Script 
    [Arguments]  ${xpath}
    Execute JavaScript  document.evaluate(${xpath},document.body,null,9,null).singleNodeValue.click();

    
Get Element By Script
    [Arguments]  ${xpath}
    ${text}   Execute JavaScript   return document.evaluate(${xpath},document.body,null,XPathResult.FIRST_ORDERED_NODE_TYPE,null).singleNodeValue.textContent;
    [Return]  ${text}