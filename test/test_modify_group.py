# -*- coding: utf-8 -*-
from random import randrange
import random
import string
import re
import pytest
from model.group import Group
from generator.group import testdata


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_modify_group_name(app, group, db, check_ui):
    if not len(db.get_group_list()):
        app.group.create(group)
    old_groups = db.get_group_list()
    select_group = random.choice(old_groups)
    app.group.modify_group_by_id(group, select_group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

