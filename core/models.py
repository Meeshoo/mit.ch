import random
from itemlist.models import Itemlist, Project

projectList = Itemlist()

mitch = Project("mit.ch", "The site wherein which you are located", "mitch.png", "https://mit.ch/blackhole")
spaceCadetPinballLeaderboard = Project("SpaceCadetPinballLeaderboard", "An online leaderboard for the previously offline only Windows pinball", "pinball.png", "https://www.pinball.etrash.pro/")
iac = Project("IAC", "IAC for all of my personal sites using Terraform, Packer, and Ansible", "IAC.png", "LINK TO REPO")
machro4k = Project("Mechro 4K", "A small macro pad with custom PCB and QMK firmware", "mechro4k.png", "LINK TO SOMETHING")
nokiacontroller = Project("Nokia 3310 Input Device", "A custom PCB with QMK firmware that fits inside the Nokia 3310 for use as a keyboard or game controller", "nokia3310.png", "LINK TO SOMETHING")
discordEntryMusicBot = Project("Entry Music Discord Bot", "A bot for Discord that plays music/SFX on user entry.", "entryMusicBot.png", "https://github.com/Meeshoo/announcer-discord-bot")

class core():

    def __init__(self):
        pass

    def randomMessage(self):

        welcomeMessages = ["Online", "The place wherein which I reside", "Log in, coward", "My online home", "Bing", "Bong", "WHO?"]

        return welcomeMessages[random.randint(0, (len(welcomeMessages)-1))]
