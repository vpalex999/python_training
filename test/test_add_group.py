# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    app.group.open_groups_page()
    app.group.create(Group(name="test group", header="new group", footer="footer"))
    app.group.return_to_groups_page()
    app.group.return_home_page()


def test_add_empty_group(app):
    app.group.open_groups_page()
    app.group.create(Group(name="", header="", footer=""))
    app.group.return_to_groups_page()
    app.group.return_home_page()
