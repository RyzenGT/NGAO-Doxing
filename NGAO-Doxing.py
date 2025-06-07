# ========================= Ensure Imports =========================

import subprocess
import sys

def EnsureImports():
    required_modules = [
        "os",
        "time",
        "requests",
        "colorama",
        "datetime"
    ]
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", module])


EnsureImports()

# ========================= Modules =========================

import os
import time
import requests
import random
from datetime import datetime
from colorama import *

# ========================= Utilities =========================

def CurrentLocalTime():
    return datetime.now().strftime("%H:%M:%S")

reset = Fore.RESET
white = Fore.WHITE
green = Fore.GREEN
yellow = Fore.YELLOW
red = Fore.RED

start = f"{red}[{white}"
end = f"{red}]"

SUCCESS = lambda: f"{start + CurrentLocalTime() + end} {start}+{end}{white}"
FAILED = lambda: f"{start + CurrentLocalTime() + end} {start}x{end}{white}"
ERROR = lambda: f"{start + CurrentLocalTime() + end} {start}!{end}{white}"
LOADING = lambda: f"{start + CurrentLocalTime() + end} {start}~{end}{white}"
INPUT = lambda: f"{start + CurrentLocalTime() + end} {start}>{end}{white}"
INFORMATION = lambda: f"{start + CurrentLocalTime() + end} {start}?{end}{white}"
CHOICE = lambda: f"{start + CurrentLocalTime() + end} {start}#{end}{white}"

def Clear():
    os.system("cls")

def SetTitle(text):
    os.system(f"title {text}")

def TypeWriterInput(text, delay=0.005):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    return input()

def TypeWriterPrint(text, delay=0.005):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    return print()

def Scroll(text):
    for line in text.split("\n"):
        print(line)
        time.sleep(0.04)
time.sleep(0.5)

def ScrollGradient(text):
    for line in Gradient(text).split("\n"):
        print(line)
        time.sleep(0.04)
time.sleep(0.5)

def Gradient(text):
    start_color = (223, 5, 5)
    end_color = (121, 3, 3)

    num_steps = 15

    colors = []
    for i in range(num_steps):
        r = start_color[0] + (end_color[0] - start_color[0]) * i // (num_steps - 1)
        g = start_color[1] + (end_color[1] - start_color[1]) * i // (num_steps - 1)
        b = start_color[2] + (end_color[2] - start_color[2]) * i // (num_steps - 1)
        colors.append((r, g, b))

    colors += list(reversed(colors[:-1]))

    fancy_chars = "▄█╔╗║╚╝═╠╣╩╦└┌─@%░▒▓"

    def color_text(r, g, b, char):
        return f"\033[38;2;{r};{g};{b}m{char}"

    lines = text.split("\n")
    result = []

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char in fancy_chars:
                color = colors[(i + j) % len(colors)]
                result.append(color_text(*color, char))
            else:
                result.append(char)
        result.append("\033[0m\n")

    return "".join(result)

def InvalidChoice():
    print(f"{FAILED()} Invalid choice, please try again.")
    time.sleep(1)
    NGAODoxingMenu()

# ========================= Doxing =========================

def Doxing():
    Victim          = TypeWriterInput(f"{INPUT()} Victim {red}->{reset} ")
    DoxingDate      = TypeWriterInput(f"{INPUT()} Doxing Date {red}->{reset} ")
    DoxingBy        = TypeWriterInput(f"{INPUT()} Doxing By {red}->{reset} ")
    Reason          = TypeWriterInput(f"{INPUT()} Reason {red}->{reset} ")

    FirstName       = TypeWriterInput(f"\n{INPUT()} First Name {red}->{reset} ")
    LastName        = TypeWriterInput(f"{INPUT()} Last Name {red}->{reset} ")
    Sexe            = TypeWriterInput(f"{INPUT()} Gender {red}->{reset} ")
    Age             = TypeWriterInput(f"{INPUT()} Age {red}->{reset} ")
    Birthday        = TypeWriterInput(f"{INPUT()} Birthday {red}->{reset} ")
    Nationality     = TypeWriterInput(f"{INPUT()} Nationality {red}->{reset} ")

    IpChoice        = TypeWriterInput(f"\n{INPUT()} Public IP? (y/n) {red}->{reset} ").lower()
    if IpChoice in ["y", "yes"]:
        Ip = TypeWriterInput(f"{INPUT()} Public IP {red}->{reset} ")
        try:
            response = requests.get(f"https://ipinfo.io/{Ip}/json")
            data = response.json()
            Country = data.get("country", "")
            City = data.get("city", "")
            PostalCode = data.get("postal", "")
            Address = data.get("region", "")
            loc = data.get("loc", "")
            Latitude, Longitude = loc.split(",") if "," in loc else ("", "")
        except Exception:
            Country = City = PostalCode = Address = Latitude = Longitude = ""
    elif IpChoice in ["n", "no"]:
        Ip = "None"
        Country     = TypeWriterInput(f"{INPUT()} Country {red}->{reset} ")
        City        = TypeWriterInput(f"{INPUT()} City {red}->{reset} ")
        PostalCode  = TypeWriterInput(f"{INPUT()} Postal Code {red}->{reset} ")
        Address     = TypeWriterInput(f"{INPUT()} Address {red}->{reset} ")
        Latitude    = TypeWriterInput(f"{INPUT()} Latitude {red}->{reset} ")
        Longitude   = TypeWriterInput(f"{INPUT()} Longitude {red}->{reset} ")
    else:
        InvalidChoice()

    Phone           = TypeWriterInput(f"\n{INPUT()} Phone Number {red}->{reset} ")
    Email           = TypeWriterInput(f"{INPUT()} Email {red}->{reset} ")

    Job             = TypeWriterInput(f"\n{INPUT()} Job/Occupation {red}->{reset} ")
    School          = TypeWriterInput(f"{INPUT()} School/University {red}->{reset} ")

    Father          = TypeWriterInput(f"\n{INPUT()} Father's Name {red}->{reset} ")
    Fage            = TypeWriterInput(f"{INPUT()} Father's Age {red}->{reset} ")
    Mother          = TypeWriterInput(f"{INPUT()} Mother's Name {red}->{reset} ")
    Mage            = TypeWriterInput(f"{INPUT()} Mother's Age {red}->{reset} ")
    Brother         = TypeWriterInput(f"{INPUT()} Brother(s) Name(s) {red}->{reset} ")
    Bage            = TypeWriterInput(f"{INPUT()} Brother(s) Age {red}->{reset} ")
    Sister          = TypeWriterInput(f"{INPUT()} Sister(s) Name(s) {red}->{reset} ")
    Sage            = TypeWriterInput(f"{INPUT()} Sisters(s) Age {red}->{reset} ")

    DiscordToken = ""
    Username = ""
    DisName = ""
    ProfilePicURL = ""
    BannerURL = ""
    Id = ""
    Pronouns = ""
    Bio = ""
    Nitro = ""
    NitroType = ""
    DEmail = ""
    DPhone = ""
    GiftInventory = ""

    DscChoice = TypeWriterInput(f"\n{INPUT()} Discord Token? (y/n) {red}->{reset} ").lower()
    if DscChoice in ['y', 'yes']:
        DiscordToken = TypeWriterInput(f"{INPUT()} Discord Token {red}->{reset} ")
        headers = {
            "Authorization": DiscordToken,
            "Content-Type": "application/json"
        }
        try:
            user_resp = requests.get("https://discord.com/api/v10/users/@me", headers=headers)
            user_data = user_resp.json()
            Username = user_data.get("username", "")
            DisName = user_data.get("global_name", "")
            Id = user_data.get("id", "")
            Pronouns = user_data.get("pronouns", "")
            Bio = user_data.get("bio", "")
            DEmail = user_data.get("email", "")
            DPhone = user_data.get("phone", "")
            ProfilePic = user_data.get("avatar", "")
            Banner = user_data.get("banner", "")

            if ProfilePic:
                ProfilePicURL = f"https://cdn.discordapp.com/avatars/{Id}/{ProfilePic}.png"
            else:
                ProfilePicURL = ""
            if Banner:
                BannerURL = f"https://cdn.discordapp.com/banners/{Id}/{Banner}.png"
            else:
                BannerURL = ""

            nitro_resp = requests.get("https://discord.com/api/v10/users/@me/billing/subscriptions", headers=headers)
            nitro_data = nitro_resp.json()
            if isinstance(nitro_data, list) and len(nitro_data) > 0:
                Nitro = "Yes"
                plan = nitro_data[0].get("plan", {})
                NitroType = plan.get("name", "Unknown")
            else:
                Nitro = "No"
                NitroType = "None"

            gift_resp = requests.get("https://discord.com/api/v10/users/@me/guilds/premium/subscription-slots", headers=headers)
            GiftInventory = len(gift_resp.json()) if isinstance(gift_resp.json(), list) else 0

        except Exception:
            Username = DisName = Id = Pronouns = Bio = DEmail = DPhone = ProfilePicURL = BannerURL = ""
            Nitro = "Unknown"
            NitroType = "Unknown"
            GiftInventory = "Unknown"
    elif DscChoice in ['n', 'no']:
        Username    = TypeWriterInput(f"{INPUT()} Username {red}->{reset} ")
        DisName     = TypeWriterInput(f"{INPUT()} Display Name {red}->{reset} ")
        ProfilePic  = TypeWriterInput(f"{INPUT()} Profile Picture URL {red}->{reset} ")
        Banner      = TypeWriterInput(f"{INPUT()} Banner URL {red}->{reset} ")
        Id          = TypeWriterInput(f"{INPUT()} ID {red}->{reset} ")
        Pronouns    = TypeWriterInput(f"{INPUT()} Pronouns {red}->{reset} ")
        Bio         = TypeWriterInput(f"{INPUT()} Bio {red}->{reset} ")
        DEmail      = TypeWriterInput(f"{INPUT()} Email {red}->{reset} ")
        DPhone      = TypeWriterInput(f"{INPUT()} Phone Number {red}->{reset} ")
        Nitro       = TypeWriterInput(f"{INPUT()} Nitro {red}->{reset} ")
    else:
        InvalidChoice()

    Instagram       = TypeWriterInput(f"\n{INPUT()} Instagram {red}->{reset} ")
    Facebook        = TypeWriterInput(f"{INPUT()} Facebook {red}->{reset} ")
    Twitter         = TypeWriterInput(f"{INPUT()} Twitter {red}->{reset} ")
    LinkedIn        = TypeWriterInput(f"{INPUT()} LinkedIn {red}->{reset} ")
    Snapchat        = TypeWriterInput(f"{INPUT()} Snapchat {red}->{reset} ")
    TikTok          = TypeWriterInput(f"{INPUT()} TikTok {red}->{reset} ")
    YouTube         = TypeWriterInput(f"{INPUT()} YouTube {red}->{reset} ")
    Github          = TypeWriterInput(f"{INPUT()} Github {red}->{reset} ")

    folder = f"Dox-Created"
    if not os.path.exists(folder):
        os.makedirs(folder)

    filename = f"{Victim}_Dox.txt".replace(" ", "_")
    filepath = os.path.join(folder, filename)

    content = f"""

⠀⣿⠲⠤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣸⡏⠀⠀⠀⠉⠳⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⠀⠀⠀⠀⠀⠀⠀⠉⠲⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⣄⠀⠀⠀⡰⠋⢙⣿⣦⡀⠀⠀⠀⠀⠀
⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣙⣦⣮⣤⡀⣸⣿⣿⣿⣆⠀⠀⠀⠀
⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⠀⣿⢟⣫⠟⠋⠀⠀⠀⠀
⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣷⣷⣿⡁⠀⠀⠀⠀⠀⠀          ██████╗  ██████╗ ██╗  ██╗
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⢸⣿⣿⣧⣿⣿⣆⠙⢆⡀⠀⠀⠀⠀          ██╔══██╗██╔═══██╗╚██╗██╔╝
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⣿⣤⣿⣿⣿⡟⠹⣿⣿⣿⣿⣷⡀⠀⠀          ██║  ██║██║   ██║ ╚███╔╝ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣧⣴⣿⣿⣿⣿⠏⢧⠀⠀          ██║  ██║██║   ██║ ██╔██╗ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠈⢳⡀          ██████╔╝╚██████╔╝██╔╝ ██╗
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡏⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⢳          ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀                            - By RyzenGT
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠸⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⢠⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣼⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠛⠻⠿⣿⣿⣿⡿⠿⠿⠿⠿⠿⢿⣿⣿⠏

════════════════════════════════════════════════════════════════════════════════

 >> General Information

[+] Victim        : {Victim}
[+] Doxing Date   : {DoxingDate}
[+] Doxing By     : {DoxingBy}
[+] Reason        : {Reason}

════════════════════════════════════════════════════════════════════════════════

 >> Identity

[+] Full Name     : {FirstName} {LastName}
[+] Last Name     : {LastName}
[+] First Name    : {FirstName}
[+] Sexe          : {Sexe}
[+] Age           : {Age}
[+] Birthday      : {Birthday}
[+] Nationality   : {Nationality}

════════════════════════════════════════════════════════════════════════════════

 >> Location

[+] IP Address    : {Ip}
[+] Country       : {Country}
[+] City          : {City}
[+] Postal Code   : {PostalCode}
[+] Address       : {Address}
[+] Latitude      : {Latitude}
[+] Longitude     : {Longitude}

════════════════════════════════════════════════════════════════════════════════

 >> Contact

[+] Phone         : {Phone}
[+] Email         : {Email}

════════════════════════════════════════════════════════════════════════════════

 >> Profession / Education

[+] Job           : {Job}
[+] School        : {School}

════════════════════════════════════════════════════════════════════════════════

 >> Family Information

[+] Father        : {Father}
[+] Age           : {Fage}
[+] Mother        : {Mother}
[+] Age           : {Mage}
[+] Brother(s)    : {Brother}
[+] Age           : {Bage}
[+] Sister(s)     : {Sister}
[+] Age           : {Sage}

════════════════════════════════════════════════════════════════════════════════

>> Discord

[+] Token         : {DiscordToken}
[+] Username      : {Username}
[+] Display Name  : {DisName}
[+] Profile Pic   : {ProfilePicURL}
[+] Banner        : {BannerURL}
[+] Id            : {Id}
[+] Pronouns      : {Pronouns}
[+] Bio           : {Bio}
[+] Nitro         : {NitroType}
[+] Email         : {DEmail}
[+] Phone Number  : {DPhone}
[+] Gift Code     : {GiftInventory}


════════════════════════════════════════════════════════════════════════════════

 >> Social Media

[+] Instagram     : {Instagram}
[+] Facebook      : {Facebook}
[+] Twitter       : {Twitter}
[+] LinkedIn      : {LinkedIn}
[+] Snapchat      : {Snapchat}
[+] TikTok        : {TikTok}
[+] YouTube       : {YouTube}
[+] Github        : {Github}

════════════════════════════════════════════════════════════════════════════════

[+] NGAO Doxing"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"\n{LOADING()} Creating File..")
    time.sleep(random.uniform(1, 2))
    print(f"{SUCCESS()} File Created In {red}->{reset} '{filepath}'")
    TypeWriterInput(f"{INPUT()} Press Enter To Continue {red}->{reset} ")
    NGAODoxingMenu()


# ========================= Main Menu =========================

def NGAODoxingMenu():
    Clear()
    SetTitle("NGAO Doxing / By RyzenGT")
    NGAODoxing = f"""
                 ███▄    █   ▄████  ▄▄▄       ▒█████     ▓█████▄  ▒█████  ▒██   ██▒ ██▓ ███▄    █   ▄████ 
                 ██ ▀█   █  ██▒ ▀█▒▒████▄    ▒██▒  ██▒   ▒██▀ ██▌▒██▒  ██▒▒▒ █ █ ▒░▓██▒ ██ ▀█   █  ██▒ ▀█▒
                ▓██  ▀█ ██▒▒██░▄▄▄░▒██  ▀█▄  ▒██░  ██▒   ░██   █▌▒██░  ██▒░░  █   ░▒██▒▓██  ▀█ ██▒▒██░▄▄▄░
                ▓██▒  ▐▌██▒░▓█  ██▓░██▄▄▄▄██ ▒██   ██░   ░▓█▄   ▌▒██   ██░ ░ █ █ ▒ ░██░▓██▒  ▐▌██▒░▓█  ██▓
                ▒██░   ▓██░░▒▓███▀▒ ▓█   ▓██▒░ ████▓▒░   ░▒████▓ ░ ████▓▒░▒██▒ ▒██▒░██░▒██░   ▓██░░▒▓███▀▒
                ░ ▒░   ▒ ▒  ░▒   ▒  ▒▒   ▓▒█░░ ▒░▒░▒░     ▒▒▓  ▒ ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░░▓  ░ ▒░   ▒ ▒  ░▒   ▒ 
                ░ ░░   ░ ▒░  ░   ░   ▒   ▒▒ ░  ░ ▒ ▒░     ░ ▒  ▒   ░ ▒ ▒░ ░░   ░▒ ░ ▒ ░░ ░░   ░ ▒░  ░   ░ 
                   ░   ░ ░ ░ ░   ░   ░   ▒   ░ ░ ░ ▒      ░ ░  ░ ░ ░ ░ ▒   ░    ░   ▒ ░   ░   ░ ░ ░ ░   ░
                         ░       ░       ░  ░    ░ ░        ░        ░ ░   ░    ░   ░           ░       ░ 
                                                          ░    
                                           
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                       {white}V1.0 {red}// {white}github.com/RyzenGT/Doxing-Tool {red}// {white}Made By RyzenGT {red}// {white}Doxing Tool{reset}                       ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝"""
    ScrollGradient(NGAODoxing)
    Doxing()

if __name__ == "__main__":
    NGAODoxingMenu()