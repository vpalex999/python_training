# -*- coding: utf-8 -*-

import random
from pytest_bdd import given, when, then
from model.group import Group
from model.address import Address


@given('a group list')
def group_list(db):
    return db.get_group_list()


@given('a group with <name>, <header>, <footer>')
def new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)


@when('I add the group to the list')
def add_new_group(app, new_group):
    app.group.create(new_group)


@then('the new group list is equal to the old list with the added group')
def verify_group_edit(db, group_list, new_group):
    old_groups = group_list
    new_groups = db.get_group_list()
    old_groups.append(new_group)


@given('a non-empty group list')
def non_empty_group_list(app, db):
    if not len(db.get_group_list()):
        app.group.create(Group(name="djhdfjue"))
    return db.get_group_list()

@given('a random group from the list')
def random_group(non_empty_group_list):
    return random.choice(non_empty_group_list)

@when('I delete the group from the list')
def delete_group(app, random_group):
    app.group.delete_group_by_id(random_group.id)


@then('the new list is equal to the old without the deleted group')
def verify_group_deleted(db, non_empty_group_list, random_group, app, check_ui):
    old_groups = non_empty_group_list
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(random_group)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


@given('a address list')
def address_list(db):
    return db.get_address_list()


@given('a address with <name>, <lname>')
def new_address(name, lname):
    return Address(name=name, lname=lname)


@when('I add the address to the list')
def add_new_address(app, new_address):
    app.address.create(new_address)


@then('the new address list is equal to the list with the added address')
def verify_address(app, db, address_list, new_address, check_ui):
    old_address = address_list
    new_address = db.get_address_list()
    old_address.append(new_address)
    assert len(old_address) == len(new_address)
    if check_ui:
        assert sorted(old_address, key=Address.id_or_max) == sorted(app.address.get_addresses_list(), key=Address.id_or_max)


@given('a address list')
def address_list(db):
    return db.get_address_list()


@given('a address with <name>, <lname>')
def new_address(name, lname):
    return Address(name=name,lname=lname)


@when('I add the address to the list')
def add_new_address(app, new_address):
    app.address.create(new_address)


@then('the new address list is equal to the list with the added address')
def verify_address_after_added(db, app, address_list, new_address, check_ui):
    old_addresses = address_list
    old_addresses.append(new_address)
    assert len(old_addresses) == len(db.get_address_list())
    if check_ui:
        assert sorted(old_addresses, key=Address.id_or_max) == sorted(app.address.get_addresses_list(),
                                                                      key=Address.id_or_max)

@given('a non-empty address list')
def non_empty_address_list(app, db):
    if not len(db.get_address_list()):
        app.address.create(Address(name='nametest1', lname="lastnametest1"))
    return db.get_address_list()

@given('a random address from the list')
def random_address(non_empty_address_list):
    return random.choice(non_empty_address_list)

@when('I delete the address from the list')
def delete_address(app, random_address):
    app.address.delete_address_by_id(random_address.id)


@then('the new list is equal to the old without the deleted address')
def verify_address_after_delete(app, db, non_empty_address_list, check_ui):
    assert len(non_empty_address_list) - 1 == app.address.count()
    new_addresses = db.get_address_list()
    if check_ui:
        assert sorted(new_addresses, key=Address.id_or_max) == sorted(app.address.get_addresses_list(),
                                                                      key=Address.id_or_max)

@when('I modify the random address')
def modify_address(app, new_address, random_address):
    app.address.update_address_by_id(new_address, random_address.id)


@then('the new address list is equal to the list with the modifyed address')
def verify_address_after_modifyed(app, db, non_empty_address_list, check_ui):
    assert len(non_empty_address_list) == len(db.get_address_list())
    if check_ui:
        assert sorted(db.get_address_list(), key=Address.id_or_max) == sorted(app.address.get_addresses_list(),
                                                                      key=Address.id_or_max)







