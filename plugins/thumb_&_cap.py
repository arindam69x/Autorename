from pyrogram import Client, filters 
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
@Client.on_message(filters.private & filters.command('set_caption'))
async def add_caption(client, message):
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
        
        return False
    if len(message.command) == 1:
       return await message.reply_text("**Give The Caption\n\nExample :- `/set_caption 📕Name ➠ : {filename} \n\n🔗 Size ➠ : {filesize} \n\n⏰ Duration ➠ : {duration}`**")
    caption = message.text.split(" ", 1)[1]
    await madflixbotz.set_caption(message.from_user.id, caption=caption)
    await message.reply_text("**Your Caption Successfully Added ✅**")
   
@Client.on_message(filters.private & filters.command('del_caption'))
async def delete_caption(client, message):
    caption = await madflixbotz.get_caption(message.from_user.id)  
    if not caption:
       return await message.reply_text("**You Don't Have Any Caption ❌**")
    await madflixbotz.set_caption(message.from_user.id, caption=None)
    await message.reply_text("**Your Caption Successfully Deleted 🗑️**")
                                       
@Client.on_message(filters.private & filters.command(['see_caption', 'view_caption']))
async def see_caption(client, message):
    caption = await madflixbotz.get_caption(message.from_user.id)  
    if caption:
       await message.reply_text(f"**Your Caption :**\n\n`{caption}`")
    else:
       await message.reply_text("**You Don't Have Any Caption ❌**")


@Client.on_message(filters.private & filters.command(['view_thumb', 'viewthumb']))
async def viewthumb(client, message):    
    thumb = await madflixbotz.get_thumbnail(message.from_user.id)
    if thumb:
       await client.send_photo(chat_id=message.chat.id, photo=thumb)
    else:
        await message.reply_text("**You Don't Have Any Thumbnail ❌**") 
		
@Client.on_message(filters.private & filters.command(['del_thumb', 'delthumb']))
async def removethumb(client, message):
    await madflixbotz.set_thumbnail(message.from_user.id, file_id=None)
    await message.reply_text("**Thumbnail Deleted Successfully 🗑️**")
	
@Client.on_message(filters.private & filters.photo)
async def addthumbs(client, message):
    mkn = await message.reply_text("Please Wait ...")
    await madflixbotz.set_thumbnail(message.from_user.id, file_id=message.photo.file_id)                
    await mkn.edit("**Thumbnail Saved Successfully ✅️**")





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Developer @JishuDeveloper
