*** Settings ***
Library  Collections
Library  rf.AddressBook
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures



*** Test Cases ***

Add new address
    ${old_list}=  Get Address List
    ${address}=  New Address  name1  lmane1
    Create Address  ${address}
    ${new_list}=  Get Address List
    Append To List  ${old_list}  ${address}
    Address Lists Should Be Equal  ${new_list}  ${old_list}


Delete Address
    ${old_list}=  Get Address List
    ${len}=  get length  ${old_list}
    ${index}=  evaluate  random.randrange(${len})  random
    ${address}=  get from list  ${old_list}  ${index}
    Delete Address  ${address}
    ${new_list}=  Get Address List
    Remove Values From List  ${old_list}  ${address}
    Address Lists Should Be Equal  ${new_list}  ${old_list}


Modify Address
    ${old_list}=  Get Address List
    ${len}=  get length  ${old_list}
    ${index}=  evaluate  random.randrange(${len})  random
    ${address}=  get from list  ${old_list}  ${index}
    ${new_address}=  New Address  name1  lmane1
    Modify Address  ${new_address}  ${address}
    ${new_list}=  Get Address List
    Address Lists Should Be Equal  ${new_list}  ${old_list}