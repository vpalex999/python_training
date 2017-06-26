# -*- coding: utf-8 -*-

import re


def test_phones_on_contact_view_page(app):
    address_from_home_page = app.address.get_addresses_list()[0]
    address_from_edit_page = app.address.get_contact_info_from_edit_page(0)
    assert address_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(address_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(address):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [address.phone, address.mobile,address.workphone , address.phone2]))))
