"""
4_active_directory.py

In Windows Active Directory, a group can consist of user(s) and group(s) themselves.
We can construct this hierarchy as such. Where User is represented by a string
representing their ids.

Related references:
http://www.omnisecu.com/windows-2003/active-directory/what-is-active-directory-tree.php

Change from lists to sets
"""

import time

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = set()
        self.users = set()

    def add_group(self, group):
        self.groups.add(group)

    def add_user(self, user):
        self.users.add(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    # print("user {} - group {}".format(user, group.name))

    try:
        if group == "" or group is None:
            msg  = "\nInvalid group (empty or none). Please provide another group to check."
            raise ValueError(msg)
        if not isinstance(group, Group):
            msg = "\nGroup: " + str(group) + " does not exist. Please try again."
            raise ValueError(msg)
        if user == "" or user is None:
            msg = "\nInvalid user provided. Please provide another user name to check."
            raise ValueError(msg)
    except ValueError as err_msg:
        print(err_msg)
        return False

    in_group_flag = False
    # search in the inital group given
    if user in group.get_users():
        in_group_flag = True
    # check if any sub-groups exist
    for groupie in group.get_groups():
        if isinstance(groupie, Group):
            # sub-group, check if user is in it
            if is_user_in_group(user, groupie):
                in_group_flag = True
    return in_group_flag


parent = Group("parent")
child = Group("child")
sub_child = Group("sub_child")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print("Should be True:", is_user_in_group(sub_child_user, parent))

print("Should be False:", is_user_in_group(sub_child_user, None))

print("Should be False:", is_user_in_group("", parent))

print("Should be False:", is_user_in_group("Imogen Heep", "MobyDick"))
