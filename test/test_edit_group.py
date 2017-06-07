# -*- coding: utf-8 -*-

from model.group import Group


def test_first_edit_group(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    app.group.edit_first_group(Group(name="test edit group", header="edit group", footer="edit footer"))
    app.group.return_to_groups_page()
    app.session.logout()
