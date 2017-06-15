# -*- coding: utf-8 -*-

from model.group import Group

def test_delete_first_group(app):

    app.group.open_groups_page()
    if app.group.count() == 0:
        app.group.create(Group(name="Create group"))
        app.group.return_to_groups_page()
    app.group.delete_first_group()
    app.group.return_home_page()

