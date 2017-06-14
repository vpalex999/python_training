# -*- coding: utf-8 -*-

from model.group import Group


def test_modify_group_name(app):

    app.group.open_groups_page()
    app.group.modify_first_group(Group(name="New group"))
    app.group.return_to_groups_page()
    app.group.return_home_page()



def test_modify_group_header(app):

    app.group.open_groups_page()
    app.group.modify_first_group(Group(name="New header"))
    app.group.return_to_groups_page()
    app.group.return_home_page()
