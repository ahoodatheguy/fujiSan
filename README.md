# fujiSan
A discord bot made to moderate servers

Hello! As an avid Linux(GNU/Linux whatever), I love open source software. Open source browser, open source kernel, open source window manager.

However, one area where I noticed a profound *lack* of open source software is discord bots. Therefore, I made a simple open source python bot for moderation/content creators.

# Feature Wishlist
- [x] !socials to print users social media
- [x] !credits & !aboutme to print bot info
- [ ] Moderation
  - [x] kick users
  - [x] ban/unban users
  - [ ] blacklisted words
  - [ ] profanity filter
  - [ ] Roles
    - [ ] promotions
    - [ ] demotions
- [ ] Server introduction (react to message in welcome channel to allow new users access to server.)



# How to run
I want the end goal of this bot to be a MEE6 type of bot where users can run bots in the cloud via a website with no need to self host. However at the moment it simply just is not possible or feasible. A simple solution is to self host the bot with a cheap computer like a [Raspberry Pi 4](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/).

The steps to do this is quite simple.

- Clone this github repository.
  - `git clone https://github.com/ahoodatheguy/fujiSan`
- Install discord.py
  - Make sure you have python installed
  - `pip3 install discord`
- `cd` into git repo you just cloned.
-  run `python3 bot.py` in your terminal