*** Settings ***
Documentation     Arquivos com as keywords e variaveis para o Robot.
Library           ClashRoyale.py

*** Variables ***
${CLAN_NAME}  The resistance
${CLAN_TAG}   #9V2Y
${CLAN_LOCATION}   Brazil


*** Keywords ***
Iniciar Busca
    BuscarMembros    ${CLAN_NAME}   ${CLAN_TAG}   ${CLAN_LOCATION}
    
    

    




