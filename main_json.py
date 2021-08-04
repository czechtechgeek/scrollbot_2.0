import json


def print_hi(name):
    print(f'Hi, {name}')


def create_json():
    x = '{ "hello": { "scrollbot_text": "hello world", "twitch_chat":"hello world", "role": "all"},}'
    with open('commands.json', 'w') as outfile:
        json.dump(x, outfile)
    print("json was created")

def add_command(cmd_name, scroll_text, twch_text, role):
    with open('commands.json', 'w') as outfile:
        # data = json.load(outfile)
        outfile[cmd_name] = {str(cmd_name): {
            "scrollbot_text": str(scroll_text),
            "twitch_chat": str(twch_text),
            "role": str(role)
        }}
        print(outfile)


def dump_json(file_json):
    with open(file_json) as json_file:
        data = json.load(json_file)
        print(data)


if __name__ == '__main__':
    print_hi('Scrollbot')
    create_json()
    # dump_json('commands.json')
    add_command('pokus','pokus','pokus','pokus')
