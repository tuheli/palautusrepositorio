*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  elias
    Set Password  elias1234
    Set Password Confirmation  elias1234
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  e
    Set Password  elias1234
    Set Password Confirmation  elias1234
    Submit Credentials
    Register Should Fail With Message  Username length must be at least 3

Register With Valid Username And Too Short Password
    Set Username  elias
    Set Password  el
    Set Password Confirmation  el
    Submit Credentials
    Register Should Fail With Message  Password length must be at least 3

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
# ...
    Set Username  elias
    Set Password  eliaselias
    Set Password Confirmation  eliaselias
    Submit Credentials
    Register Should Fail With Message  Password must contain at least 1 other symbol than ascii letter

Register With Nonmatching Password And Password Confirmation
    Set Username  elias
    Set Password  elias1234
    Set Password Confirmation  elias12345
    Submit Credentials
    Register Should Fail With Message  Password and password confirmation must match

Register With Username That Is Already In Use
    Create User  elias  password1234
    Set Username  elias
    Set Password  elias1234
    Set Password Confirmation  elias1234
    Submit Credentials
    Register Should Fail With Message  User with username elias already exists

*** Keywords ***
Reset Application And Go To Register Page
    Reset Application
    Go To Register Page

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Credentials
    Click Button  Register

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}