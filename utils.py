import random #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
import time #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
import math #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
import os #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
from vars import CREDIT #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
from pyrogram.errors import FloodWait #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
from datetime import datetime,timedelta #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®

class Timer: #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
    def __init__(self, time_between=5): #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
        self.start_time = time.time() #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
        self.time_between = time_between #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®

    def can_send(self): #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
        if time.time() > (self.start_time + self.time_between): #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
            self.start_time = time.time() #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
            return True #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
        return False #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®

#lets do calculations #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
def hrb(value, digits= 2, delim= "", postfix=""): #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
    """Return a human-readable file size. #NIKHIL SAINI BOTS
    """ #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
    if value is None: #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
        return None #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
    chosen_unit = "B" #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
    for unit in ("KB", "MB", "GB", "TB"): #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
        if value > 1000: #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
            value /= 1024 #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
            chosen_unit = unit #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
        else: #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
            break #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
    return f"{value:.{digits}f}" + delim + chosen_unit + postfix #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®

def hrt(seconds, precision = 0): #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
    """Return a human-readable time delta as a string. #NIKHIL SAINI BOTS
    """ #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
    pieces = [] #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
    value = timedelta(seconds=seconds) #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®

    if value.days: #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
        pieces.append(f"{value.days}day") #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®

    seconds = value.seconds #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®

    if seconds >= 3600: #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
        hours = int(seconds / 3600) #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
        pieces.append(f"{hours}hr") #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
        seconds -= hours * 3600 #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®

    if seconds >= 60: #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
        minutes = int(seconds / 60) #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
        pieces.append(f"{minutes}min") #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
        seconds -= minutes * 60 #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®

    if seconds > 0 or not pieces: #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
        pieces.append(f"{seconds}sec") #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®

    if not precision: #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
        return "".join(pieces) #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®

    return "".join(pieces[:precision]) #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®

timer = Timer() #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®

async def progress_bar(current, total, reply, start): #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
    if timer.can_send(): #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
        now = time.time() #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
        diff = now - start #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
        if diff < 1: #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
            return #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
        else: #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
            perc = f"{current * 100 / total:.1f}%" #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
            elapsed_time = round(diff) #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
            speed = current / elapsed_time #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
            remaining_bytes = total - current #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
            if speed > 0: #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
                eta_seconds = remaining_bytes / speed #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
                eta = hrt(eta_seconds, precision=1) #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
            else: #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
                eta = "-" #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
            sp = str(hrb(speed)) + "/s" #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
            tot = hrb(total) #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
            cur = hrb(current) #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
            bar_length = 10 #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
            completed_length = int(current * bar_length / total) #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
            remaining_length = bar_length - completed_length #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®

            symbol_pairs = [ #N𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
                ("▬", "▭"), #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
                ("✅", "☑️"), #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
                ("🐬", "🦈"), #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
                ("💚", "💛"), #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
                ("🌟", "⭐"), #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
                ("▰", "▱") #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
            ] #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
            chosen_pair = random.choice(symbol_pairs) #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
            completed_symbol, remaining_symbol = chosen_pair #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®

            progress_bar = completed_symbol * completed_length + remaining_symbol * remaining_length #NIKHIL SAINI BOTS

            try: #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
                await reply.edit(f'`╭──⌯═════𝐔𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠══════⌯──╮\n├⚡ {progress_bar}\n├⚙️ Progress ➤ | {perc} |\n├🚀 Speed ➤ | {sp} |\n├📟 Processed ➤ | {cur} |\n├🧲 Size ➤ | {tot} |\n├🕑 ETA ➤ | {eta} |\n╰─═══✨🦋{CREDIT}🦋✨═══─╯`') 
                #await reply.edit(f'`╭──⌯═════𝐁𝐨𝐭 𝐒𝐭𝐚𝐭𝐢𝐜𝐬══════⌯──╮\n├⚡ {progress_bar}\n├⚙️ Progress ➤ | {perc} |\n├🚀 Speed ➤ | {sp} |\n├📟 Processed ➤ | {cur} |\n├🧲 Size ➤ | {tot} |\n├🕑 ETA ➤ | {eta} |\n╰─═══✨🦋𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®🦋✨═══─╯`') 
            except FloodWait as e: #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
                time.sleep(e.x) #𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®
