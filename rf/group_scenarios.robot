*** Settings ***
Library  Collections
Library  rf.AddressBook
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures






*** Test Cases ***

Add new group
    ${old_list}=  Get Group List
    ${group}=  New Group  name1  header1  footer1
    Create Group  ${group}
    ${new_list}=  Get Group List
    Append To List  ${old_list}  ${group}
    Group Lists Should Be Equal  ${new_list}  ${old_list}


Delete group
    ${old_list}=  Get Group List
    ${len}=  get length  ${old_list}
    ${index}=  evaluate  random.randrange(${len})  random
    ${group}=  get from list  ${old_list}  ${index}
    Delete Group  ${group}
    ${new_list}=  Get Group List
    Remove Values From List  ${old_list}  ${group}
    Group Lists Should Be Equal  ${new_list}  ${old_list}


Add new address
    ${old_list}=  Get Address List
    ${address}=  New Address  name1  lmane1
    Create Address  ${address}
    ${new_list}=  Get Address List
    Append To List  ${old_list}  ${address}
    Address Lists Should Be Equal  ${new_list}  ${old_list}
