from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from helper.database import madflixbotz

def get_shortlink(link):
    shor = f'https://publicearn.com/api?api=8b263022657dc3aa0dfba63347185dc365c04d6c&url={link}'
    response = requests.get(shor, headers={'Connection': 'close'})
    js = json.loads(response.content)
    print(response.content)
    sh = js['shortenedUrl']
    return sh

def is_token_valid(mid, token):

    tstr=datetime.now()
    ox=open(f"verify.txt",'r')
    prt= ox.read().splitlines()
    ox.close()
    os.system(f"sed -i '/{token}/d' verify.txt")
    if token in prt:
        result=datetime.now() + timedelta(hours=12)
        print(result)
        os.system(f'echo "{result.strftime("%Y:%m:%d:%H:%M")}" > {mid}.txt')
        return True


def time_checker(yearx,monthx,dayx,hourx,mintx):
    tchk=datetime.now()
    y=tchk.strftime("%Y")
    m=tchk.strftime("%m")
    d=tchk.strftime("%d")
    h=tchk.strftime("%H")
    mi=tchk.strftime("%M")
    kk=datetime(int(y),int(m),int(d),int(h),int(mi))
    ik=datetime(int(yearx),int(monthx),int(dayx),int(hourx), int(mintx))
    if ik > kk:
        return True
    else:
        return False

@Client.on_message(filters.private & filters.command("autorename"))
async def auto_rename_command(client, message):
    user_id = message.from_user.id
    mid=message.chat.id
    try:
        o=open(f'{message.chat.id}.txt','r')
        s=o.read().split(":")
        print('->',s[4].strip('\n'))
        o.close()
    except:
         token=  ''.join(random.choices(string.ascii_letters + string.digits, k=10))
#      print(token)
         urlx=get_shortlink(f'https://telegram.me/autorename_proxbot?start={token}')
         await message.reply_text('Your Ads token is expired, refresh your token and try again.\n\nToken Timeout: 12 hours \nWhat is the token?\n\nThis is an ads token. If you pass 1 ad, you can use the bot for 12 Hour after passing the ad.' ,reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("Click here", url=urlx)],
                    [InlineKeyboardButton('>> HOW TO TAKE FREE TOKEN Tutorial ', url='t.me/japanese_live_actionz/18')]
                ]  ))
         tym=datetime.now()
         os.system(f'echo "{token}" >> verify.txt')


#         return False
    tf=time_checker(s[0],s[1],s[2],s[3],s[4])
    print(tf)
    if not tf :
        
        return 


    # Extract the format from the command
    format_template = message.text.split("/autorename", 1)[1].strip()

    # Save the format template to the database
    await madflixbotz.set_format_template(user_id, format_template)

    await message.reply_text("**Auto Rename Format Updated Successfully! ✅**")

@Client.on_message(filters.private & filters.command("setmedia"))
async def set_media_command(client, message):
    mid=message.chat.id
    try:
        o=open(f'{message.chat.id}.txt','r')
        s=o.read().split(":")
        print('->',s[4].strip('\n'))
        o.close()
    except:
         token=  ''.join(random.choices(string.ascii_letters + string.digits, k=10))
#      print(token)
         urlx=get_shortlink(f'https://telegram.me/autorename_proxbot?start={token}')
         await message.reply_text('Your Ads token is expired, refresh your token and try again.\n\nToken Timeout: 12 hours \nWhat is the token?\n\nThis is an ads token. If you pass 1 ad, you can use the bot for 12 Hour after passing the ad.' ,reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("Click here", url=urlx)],
                    [InlineKeyboardButton('>> HOW TO TAKE FREE TOKEN Tutorial ', url='t.me/japanese_live_actionz/18')]
                ]  ))
         tym=datetime.now()
         os.system(f'echo "{token}" >> verify_{tym.strftime("%y")}_{tym.strftime("%m")}_{tym.strftime("%d")}.txt')


#         return False
    tf=time_checker(s[0],s[1],s[2],s[3],s[4])
    print(tf)
    if not tf :
        
        return 
    user_id = message.from_user.id    
    media_type = message.text.split("/setmedia", 1)[1].strip().lower()

    # Save the preferred media type to the database
    await madflixbotz.set_media_preference(user_id, media_type)

    await message.reply_text(f"**Media Preference Set To :** {media_type} ✅")






# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Developer @JishuDeveloper
