# -*- coding: utf-8 -*-

from pony.orm import *
from datetime import datetime
from model.group import Group
from model.address import Address
from pymysql.converters import decoders
from pymysql.converters import encoders
from pymysql.converters import convert_mysql_timestamp


class ORMFixture(object):

    db = Database()

    conv = encoders
    conv.update(decoders)
    conv[datetime] = convert_mysql_timestamp

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda :ORMFixture.ORMAddress, table="address_in_groups", column="id", reverse="groups", lazy=True)

    class ORMAddress(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated')
        groups = Set(lambda :ORMFixture.ORMGroup, table="address_in_groups", column="group_id", reverse="contacts", lazy=True)

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=self.conv)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    def convert_contact_to_model(self, addresses):
        def convert(address):
            return Address(id=str(address.id), name=address.firstname, lname=address.lastname)
        return list(map(convert, addresses))

    @db_session
    def get_group_list(self):
        # return list(select(g for g in ORMFixture.ORMGroup))
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    @db_session
    def get_address_list(self):
        # return list(select(g for g in ORMFixture.ORMGroup))
        return self.convert_contact_to_model(select(c for c in ORMFixture.ORMAddress if c.deprecated is None))

    @db_session
    def get_address_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return  self.convert_contact_to_model(orm_group.contacts)

    @db_session
    def get_address_in_group_by_id(self, address_id, group_id):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group_id.id))[0]
        orm_address = select(c for c in ORMFixture.ORMAddress if c.deprecated is None and orm_group in c.groups and c.id == address_id.id)
        return self.convert_contact_to_model(orm_address)

    @db_session
    def get_address_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contact_to_model(
            select(c for c in ORMFixture.ORMAddress if c.deprecated is None and orm_group not in c.groups))



