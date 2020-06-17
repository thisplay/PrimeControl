*** Settings ***
Documentation     Um Robot para Criar Chave no Site Clash Royale
...
...               Este Robot faz login no Site  Desenvolvedor do Clash Royale
...               Cria uma nova chave e salva em um arquivo txt
Resource          CreateKey.robot
Resource          GetMembers.robot

*** Test Cases ***
Create Key
    ${ipExt}    Get IpExterno
    Open Browser To Login Page
    Input Username    douglas2012.ribeiro@gmail.com
    Input Password    TestePrime
    Submit Credentials
    Create Key       Douglas     Teste Prime   ${ipExt}
    [Teardown]    Close Browser

Save Members
    Iniciar Busca
