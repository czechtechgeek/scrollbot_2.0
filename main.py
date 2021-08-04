import sys
import os
from audioop import add
from nested_lookup import nested_lookup
from nested_lookup import nested_update

import yaml

# https://github.com/russellballestrini/nested-lookup/

# udelat fci pro zmknuti commandu
# ROLE - Admin, geek(uzivatele v chatu), VIP, SUBS

# def change_role_command

# def update_command

# def delete_command


def create_yaml():
    """
    This function will create new YAML file.
    """
    document = """
          - hello: 
              scroll_text: some text for scrollbot
              twitch_text: some text for twitch chat
              role: user role
          - reklama:
              scroll_text: some text for scrollbot  
              twitch_text: some text for twitch chat
              role: user role
    """
    file = open("commands.yaml", "w")
    yaml.dump(document, file)
    file.close()
    # print(yaml.dump(yaml.load(document, Loader=yaml.FullLoader)))


def add_command(path, cmd_name, scroll_text, twch_text, role):
    dictionary = {cmd_name: {'scroll_text': scroll_text, 'twitch_text': twch_text, 'role': role}}
    if not os.path.isfile(path):
        with open(path, "a") as fo:
            fo.write("---\n")
    sdump = "  " + yaml.dump(
        dictionary
        , indent=4
    )
    with open(path, "a") as fo:
        fo.write(sdump)


# def remove_command(path, cmd_name):


def dump_yaml(path):
    with open(path, "r") as r:
        data = list(yaml.load_all(r, Loader=yaml.FullLoader))
        print(data)


def print_command(path, cmd):
    with open(path, "r") as r:
        data = list(yaml.load_all(r, Loader=yaml.FullLoader))
        print(nested_lookup(cmd, data))


def update_command(path, cmd, scroll_text, twch_text, role):
    dictionary = {'scroll_text': scroll_text, 'twitch_text': twch_text, 'role': role}
    with open(path, "r") as r:
        data = list(yaml.load_all(r, Loader=yaml.FullLoader))
        nested_update(data, key=cmd, value=dictionary)
        print(nested_lookup(cmd, data))

if __name__ == '__main__':
    # create_yaml()
    print_command("commands.yaml", "Ahoj")
    # add_command("commands.yaml", "Ahoj", "Ahoj", "Ahoj", "Admin")
    update_command("commands.yaml", "Ahoj", "pokuspokuspokus", "pokuspokuspokus", "Geek")
    # dump_yaml("commands.yaml")

