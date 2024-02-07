import time
import json 
import os
import ctypes
try:
    import requests
    import clipboard
    import colorama
    import keyboard
    import pygame
except ModuleNotFoundError:
    moduls = input("You have uninstalled modules! Do you want to install them?(Y/n)")
    if moduls.lower() == "y":
        for module in open("rq.txt", "r").readlines():
            os.system(f"pip install {module}");os.system(f"python -m pip install {module}");os.system(f"py -m pip install {module}")
            os.system("cls" if os.name == "nt" else "clear")
            input("Successfully installed required modules! Reopen the program to continue...")
    else:
        input("If you want to install modules reopen this program. Press enter to exit...")
        exit()
except Exception as e:
    input("You got unknown error! Dm deadlysilence. #7583 to solve it. Press enter to exit...")
    exit()

colorama.init()

red = colorama.Fore.RED
yellow = colorama.Fore.YELLOW
cyan = colorama.Fore.LIGHTCYAN_EX
reset = colorama.Style.RESET_ALL

counter = 1
modes = [" >> ", "    ", "    "]
config = [0.1, 1, 5]
FILE_PATH = "/".join(__file__.split("\\")[:-1]) + "/"

if os.name == "nt":
    try:
        ctypes.windll.kernel32.SetConsoleTitleW("ShoutSniper")
        avin = True
    except:
        avin = False

embed = """
                                                                            by deadlysilence.#7583   
          ██████  ██░ ██  ▒█████   █    ██ ▄▄▄█████▓  ██████  ███▄    █  ██▓ ██▓███  ▓█████  ██▀███  
        ▒██    ▒ ▓██░ ██▒▒██▒  ██▒ ██  ▓██▒▓  ██▒ ▓▒▒██    ▒  ██ ▀█   █ ▓██▒▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒
        ░ ▓██▄   ▒██▀▀██░▒██░  ██▒▓██  ▒██░▒ ▓██░ ▒░░ ▓██▄   ▓██  ▀█ ██▒▒██▒▓██░ ██▓▒▒███   ▓██ ░▄█ ▒
          ▒   ██▒░▓█ ░██ ▒██   ██░▓▓█  ░██░░ ▓██▓ ░   ▒   ██▒▓██▒  ▐▌██▒░██░▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  
        ▒██████▒▒░▓█▒░██▓░ ████▓▒░▒▒█████▓   ▒██▒ ░ ▒██████▒▒▒██░   ▓██░░██░▒██▒ ░  ░░▒████▒░██▓ ▒██▒
        ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░ ▒░▒░▒░ ░▒▓▒ ▒ ▒   ▒ ░░   ▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒ ░▓  ▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
        ░ ░▒  ░ ░ ▒ ░▒░ ░  ░ ▒ ▒░ ░░▒░ ░ ░     ░    ░ ░▒  ░ ░░ ░░   ░ ▒░ ▒ ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░
        ░  ░  ░   ░  ░░ ░░ ░ ░ ▒   ░░░ ░ ░   ░      ░  ░  ░     ░   ░ ░  ▒ ░░░          ░     ░░   ░ 
              ░   ░  ░  ░    ░ ░     ░                    ░           ░  ░              ░  ░   ░     
"""

config_template = {
    "group_id": "PLACE_GROUP_ID"
}

def clear_cmd() -> None:
    os.system("cls" if os.name == "nt" else "clear")

def raise_error(err: str) -> None:
    print(red + f"{err} Closing in 5 seconds..." + reset)
    time.sleep(5)
    exit()

if not os.path.exists('config.json'):
    with open('config.json', 'w') as config_file:
        json.dump(config_template, config_file, indent=4)

def play_sound(sound_path: str) -> None:
    pygame.mixer.init()
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play()

def copy(content: str) -> str:
    try:
        clipboard.copy(content)
    except:
        raise_error("Failed to copy! Try to restart your PC.")

with open('config.json', 'r') as config_file:
    try:
        config = json.load(config_file)
    except json.JSONDecodeError as e:
        raise_error("JSON decode error!")

group_id = config.get("group_id", "")

def start_checking(speed: int, group_id: str) -> None:
    shout = str()
    while True:
        res = requests.get(f"https://groups.roblox.com/v1/groups/33655441")
        if res.status_code == 429:
            print(red + "You got ratelimited! Waiting 30 seconds..." + reset)
            time.sleep(30)
        elif res.status_code == 200:
            data = json.loads(res.content)
            shout_content = data["shout"]["body"].replace("code: ", "").replace("Code:", "").strip()
            username = data["owner"]["username"]
            if shout_content != shout:
                print(colorama.Fore.GREEN + f"Message by {username}:")
                print(f" -- {shout_content}")
                print(reset)
                clipboard.copy(shout_content)
                shout = shout_content
                play_sound("sound.mp3")
        else:
            print(res.content)
            raise_error(f"You got unkown error! ({res.status_code})")
        time.sleep(speed)

def print_modes() -> None:
    print(red + embed + reset)
    print(f"""
            {modes[0]}Speed - use this when the code is dropping in 10 seconds or less
            {modes[1]}Medium - use this when the code is dropping in 1 minute or less
            {modes[2]}Slow - use this when the code is dropping in 5 minutes or less
""")
clear_cmd()
print_modes()

def kbpress(event) -> None:
    global counter, group_id, config, modes
    if event.name in ["w", "up"] and counter >= 2:
        clear_cmd()
        modes[counter - 1] = "    "
        modes[counter - 2] = " >> "
        counter -= 1
        print_modes()
    elif event.name in ["s", "down"] and counter <= len(modes) - 1:
        clear_cmd()
        modes[counter - 1] = "    "
        modes[counter] = " >> "
        counter += 1
        print_modes()
    elif event.name in ["enter", "e"]:
        clear_cmd()
        print(yellow + "Watching...\n" + reset)
        start_checking(0.3, group_id)
        """start_checking = threading.Thread(target=start_checking)
        start_checking.daemon = True
        start_checking.start()
"""
keyboard.on_press(kbpress)

keyboard.wait("q")