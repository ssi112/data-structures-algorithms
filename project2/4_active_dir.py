"""
4_active_directory.py

In Windows Active Directory, a group can consist of user(s) and group(s) themselves.
We can construct this hierarchy as such. Where User is represented by a string
representing their ids.

Related references:
http://www.omnisecu.com/windows-2003/active-directory/what-is-active-directory-tree.php

https://algorithmtutor.com/Data-Structures/Tree/Binary-Search-Trees/
https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/

***
since groups can subsist of sub-groups do we need to search sub-groups as well?

are we supposed to find out all the groups a user is in or just a specific group?

That is how problem is worded & setup - is user in a specific group

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
    if user in group.get_users():
        return True
    else:
        return False


def find_user(user, group):
    in_groups = []

    if is_user_in_group(user, group):
        in_groups.append(group.get_name())
    # check for sub-groups
    for groupie in group.get_groups():
        if isinstance(groupie, Group):
            groupie_name = groupie.get_name()
            if is_user_in_group(user, groupie):
                in_groups.append(groupie_name)
    return in_groups


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
parent.add_group(sub_child)

local_domain = Group("local_domain")
global_domain = Group("global_domain")
parent.add_group(local_domain)
parent.add_group(global_domain)

"""
print("-"*75)
print("parent - name:",  parent.get_name())
print("parent groups:",  parent.get_groups())
print("parent - users:", parent.get_users())
print("-"*75)
print("child - name:",   child.get_name())
print("child - groups:", child.get_groups())
print("child - users:",  child.get_users())
print("-"*75)
print("sub_child - name:",  sub_child.get_name())
print("sub_child groups: ", sub_child.get_groups())
print("sub_child - users:", sub_child.get_users())
print("-"*75)
"""

child.add_user("Jarmila Fueg")
sub_child.add_user("Tae Ming")
global_domain.add_user("Tae Ming")
sub_child.add_user("Jarmila Fueg")
global_domain.add_user("Erasmuz B Draggin")
sub_child.add_user("Erasmuz B Draggin")
local_domain.add_user("Bertha D Blues")
global_domain.add_user("Bertha D Blues")

user_id = "Jarmila Fueg"
members_of = find_user(user_id, child)
if members_of:
    print("\n'{}' is a member of the following group(s): {}".format(user_id, members_of))
else:
    print("'{}' is not found in any groups".format(user_id))

user_id = "sub_child_user"
members_of = find_user(user_id, sub_child)
if members_of:
    print("\n'{}' is a member of the following group(s): {}".format(user_id, members_of))
else:
    print("\n'{}' is not found in any groups".format(user_id))

user_id = "Samsonite"
members_of = find_user(user_id, sub_child)
if members_of:
    print("\n'{}' is a member of the following group(s): {}".format(user_id, members_of))
else:
    print("\n'{}' is not found in any groups".format(user_id))

user_id = "Erasmuz B Draggin"
members_of = find_user(user_id, parent)
if members_of:
    print("\n'{}' is a member of the following group(s): {}".format(user_id, members_of))
else:
    print("\n'{}' is not found in any groups".format(user_id))


