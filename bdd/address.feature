Scenario Outline: Add new address
    Given a address list
    Given a address with <name>, <lname>
    When I add the address to the list
    Then the new address list is equal to the list with the added address

    Examples:
    | name | lname |
    | name1 | lname2 |
    | name2 | lname3 |

Scenario: Delete a address
    Given a non-empty address list
    Given a random address from the list
    When I delete the address from the list
    Then the new list is equal to the old without the deleted address


Scenario Outline: Modify address
    Given a non-empty address list
    Given a random address from the list
    Given a address with <name>, <lname>
    When I modify the random address
    Then the new address list is equal to the list with the modifyed address

    Examples:
    | name | lname |
    | name1 | lname2 |
    | name2 | lname3 |