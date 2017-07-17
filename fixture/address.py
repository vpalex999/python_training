# -*- coding: utf-8 -*-

import re
from model.address import Address

class AddressHelper(object):

    def __init__(self, app):
        self.app = app

    def new_address_page(self):
        """Open new address page"""
        wd = self.app.wd
        if not(wd.current_url.endswith("/edit.php")):
            wd.find_element_by_link_text("add new").click()

    def del_first_address(self):
        """Delete first contact"""
        self.del_address_by_index(0)

    def del_address_by_index(self, index):
        """Delete first contact"""
        wd = self.app.wd
        self.return_home_page()
        wd.find_elements_by_name("selected[]")[index].click()
        # submit deletions
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.address_chace = None

    def delete_address_by_id(self, id):
        wd = self.app.wd
        self.return_home_page()
        wd.find_element_by_css_selector("input[value='{}']".format(id)).click()
        # submit deletions
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.address_chace = None

    def del_all_address(self):
        wd = self.app.wd
        self.return_home_page()
        wd.find_element_by_id("MassCB").click()
        wd.find_elements_by_class_name("left")[1].click()
        wd.switch_to_alert().accept()
        self.address_chace = None

    def return_home_page(self):
        """Return home page"""
        wd = self.app.wd
        if not(wd.current_url.endswith("/addressbook/") and wd.find_element_by_name("searchstring")):
            wd.find_element_by_link_text("home").click()

    def create(self, addr):
        """Create new address"""
        wd = self.app.wd
        self.new_address_page()
        self.input_fields(addr)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.address_chace = None

    def update_first_address(self, addr):
        """Update firs address"""
        self.update_address_by_index(addr, 0)

    def update_address_by_index(self, addr, index):
        """Update firs address"""
        wd = self.app.wd
        self.return_home_page()
        self.open_contact_to_edit_by_index(index)
        self.input_fields(addr)
        # submit Update
        wd.find_element_by_name("update").click()
        self.address_chace = None

    def update_address_by_id(self, addr, id):
        wd = self.app.wd
        self.return_home_page()
        self.open_contact_to_view_by_id(id)
        self.input_fields(addr)
        # submit Update
        wd.find_element_by_name("update").click()
        self.address_chace = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.return_home_page()
        wd.find_elements_by_name("entry")[index].find_element_by_xpath("td[8]/a/img").click()

    def open_contact_to_view_by_id(self, id):
        wd = self.app.wd
        self.return_home_page()
        for element in wd.find_elements_by_name("entry"):
            if element.find_element_by_name("selected[]").get_attribute("value") == id:
                element.find_element_by_xpath("td[8]/a/img").click()
                break


    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.return_home_page()
        wd.find_elements_by_name("entry")[index].find_element_by_xpath("td[7]/a/img").click()

    def input_fields(self, addr):
        """Input fields for address"""
        wd = self.app.wd
        if addr.name is not None:
            wd.find_element_by_name("firstname").click()
            wd.find_element_by_name("firstname").clear()
            wd.find_element_by_name("firstname").send_keys(addr.name)
        if addr.mname is not None:
            wd.find_element_by_name("middlename").click()
            wd.find_element_by_name("middlename").clear()
            wd.find_element_by_name("middlename").send_keys(addr.mname)
        if addr.lname is not None:
            wd.find_element_by_name("lastname").click()
            wd.find_element_by_name("lastname").clear()
            wd.find_element_by_name("lastname").send_keys(addr.lname)
        if addr.nickname is not None:
            wd.find_element_by_name("nickname").click()
            wd.find_element_by_name("nickname").clear()
            wd.find_element_by_name("nickname").send_keys(addr.nickname)
        if addr.title is not None:
            wd.find_element_by_name("title").click()
            wd.find_element_by_name("title").clear()
            wd.find_element_by_name("title").send_keys(addr.title)
        if addr.company is not None:
            wd.find_element_by_name("company").click()
            wd.find_element_by_name("company").clear()
            wd.find_element_by_name("company").send_keys(addr.company)
        if addr.address is not None:
            wd.find_element_by_name("address").click()
            wd.find_element_by_name("address").clear()
            wd.find_element_by_name("address").send_keys(addr.address)
        if addr.phone is not None:
            wd.find_element_by_name("home").click()
            wd.find_element_by_name("home").clear()
            wd.find_element_by_name("home").send_keys(addr.phone)
        if addr.mobile is not None:
            wd.find_element_by_name("mobile").click()
            wd.find_element_by_name("mobile").clear()
            wd.find_element_by_name("mobile").send_keys(addr.mobile)
        if addr.workphone is not None:
            wd.find_element_by_name("work").click()
            wd.find_element_by_name("work").clear()
            wd.find_element_by_name("work").send_keys(addr.workphone)
        if addr.fax is not None:
            wd.find_element_by_name("fax").click()
            wd.find_element_by_name("fax").clear()
            wd.find_element_by_name("fax").send_keys(addr.fax)
        if addr.email is not None:
            wd.find_element_by_name("email").click()
            wd.find_element_by_name("email").clear()
            wd.find_element_by_name("email").send_keys(addr.email)
        if addr.email2 is not None:
            wd.find_element_by_name("email2").click()
            wd.find_element_by_name("email2").clear()
            wd.find_element_by_name("email2").send_keys(addr.email2)
        if addr.email3 is not None:
            wd.find_element_by_name("email3").click()
            wd.find_element_by_name("email3").clear()
            wd.find_element_by_name("email3").send_keys(addr.email3)
        if addr.homepage is not None:
            wd.find_element_by_name("homepage").click()
            wd.find_element_by_name("homepage").clear()
            wd.find_element_by_name("homepage").send_keys(addr.homepage)
        # Birthday
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[16]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[16]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[4]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[4]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1991")
        # Anniversary
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[6]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[6]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[3]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("2017")
        # select Group
        # if not wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[1]").is_selected():
        #     wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[1]").click()
        # Secondary
        if addr.address2 is not None:
            wd.find_element_by_name("address2").click()
            wd.find_element_by_name("address2").clear()
            wd.find_element_by_name("address2").send_keys(addr.address2)
        if addr.phone2 is not None:
            wd.find_element_by_name("phone2").click()
            wd.find_element_by_name("phone2").clear()
            wd.find_element_by_name("phone2").send_keys(addr.phone2)
        if addr.notes is not None:
            wd.find_element_by_name("notes").click()
            wd.find_element_by_name("notes").clear()
            wd.find_element_by_name("notes").send_keys(addr.notes)

    def count(self):
        """Check count address"""
        wd = self.app.wd
        self.return_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    address_chace = None

    def get_addresses_list(self):
        """Great list with addresses"""
        if self.address_chace is None:
            wd = self.app.wd
            self.return_home_page()
            self.address_chace = []
            for element in wd.find_elements_by_name("entry"):
                td = element.find_elements_by_tag_name("td")
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_addr = td[3].text
                all_email = td[4].text
                all_phone = td[5].text
                if all_phone:
                    self.address_chace.append(Address(name=td[2].text, lname=td[1].text, id=id,
                                                      all_address_from_home_page=all_addr,
                                                      all_phones_from_home_page=all_phone,
                                                      all_email_from_home_page= all_email))
                else:
                    self.address_chace.append(Address(name=td[2].text, lname=td[1].text, id=id))

        return list(self.address_chace)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.return_home_page()
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")

        return Address(name=firstname, lname=lastname, address=address, email=email, email2=email2, email3=email3,
                       id=id, phone=homephone, workphone=workphone, mobile=mobilephone, phone2=phone2)



    def get_addresse_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)

        return Address(phone=homephone, workphone=workphone, mobile=mobilephone, phone2=phone2)

