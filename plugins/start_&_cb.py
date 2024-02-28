import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery, Message, InputMediaPhoto

from helper.database import madflixbotz
from config import Config, Txt  

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

@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    try:
        token = message.command[1]
        print(token)
        if  is_token_valid(message.chat.id, token):
            await app.send_message(message.chat.id,'BOT TOKEN VERIFIED SUCCESSFULLY')
            return 
 #       else:

#           await bot.reply_text('Invalid Token. Starting bot. THIS IS TERABOX DOWNLOADER BOT. SEND LINK to know usage')
    except  :
        do='tg'


    user = message.from_user
    await madflixbotz.add_user(client, message)                
    button = InlineKeyboardMarkup([[
      InlineKeyboardButton('📢 Updates', url='https://t.me/kxzen_bots'),
      InlineKeyboardButton('💬 Support', url='')
    ],[
      InlineKeyboardButton('⚙️ Help', callback_data='help'),
      InlineKeyboardButton('💙 About', callback_data='about')
    ],[
        InlineKeyboardButton("🧑‍💻 Developer 🧑‍💻", url='https://t.me/kxzen_x')
    ]])
    if Config.START_PIC:
        await message.reply_photo(Config.START_PIC, caption=Txt.START_TXT.format(user.mention), reply_markup=button)       
    else:
        await message.reply_text(text=Txt.START_TXT.format(user.mention), reply_markup=button, disable_web_page_preview=True)   

@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    user_id = query.from_user.id  
    
    if data == "home":
        await query.message.edit_text(
            text=Txt.START_TXT.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton('📢 Updates', url='https://t.me/kxzen_bots'),
                InlineKeyboardButton('💬 Support', url='')
                ],[
                InlineKeyboardButton('⚙️ Help', callback_data='help'),
                InlineKeyboardButton('💙 About', callback_data='about')
                ],[
                InlineKeyboardButton("🧑‍💻 Developer 🧑‍💻", url='https://t.me/kxzen_x')
                ]])
        )
    elif data == "caption":
        await query.message.edit_text(
            text=Txt.CAPTION_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("✖️ Close", callback_data="close"),
                InlineKeyboardButton("🔙 Back", callback_data="help")
            ]])            
        )
    elif data == "help":
        await query.message.edit_text(
            text=Txt.HELP_TXT.format(client.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("⚙️ Setup AutoRename Format ⚙️", callback_data='file_names')
                ],[
                InlineKeyboardButton('🖼️ Thumbnail', callback_data='thumbnail'),
                InlineKeyboardButton('✏️ Caption', callback_data='caption')
                ],[
                InlineKeyboardButton('🏠 Home', callback_data='home'),
                InlineKeyboardButton('💰 Donate', callback_data='donate')
                ]])
        )
    elif data == "donate":
        await query.message.edit_text(
            text=Txt.DONATE_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("✖️ Close", callback_data="close"),
                InlineKeyboardButton("🔙 Back", callback_data="help")
            ]])          
        )
    
    elif data == "file_names":
        format_template = await madflixbotz.get_format_template(user_id)
        await query.message.edit_text(
            text=Txt.FILE_NAME_TXT.format(format_template=format_template),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("✖️ Close", callback_data="close"),
                InlineKeyboardButton("🔙 Back", callback_data="help")
            ]])
        )      
    
    elif data == "thumbnail":
        await query.message.edit_caption(
            caption=Txt.THUMBNAIL_TXT,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("✖️ Close", callback_data="close"),
                InlineKeyboardButton("🔙 Back", callback_data="help"),
            ]]),
        )

    elif data == "about":
        await query.message.edit_text(
            text=Txt.ABOUT_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("✖️ Close", callback_data="close"),
                InlineKeyboardButton("🔙 Back", callback_data="home")
            ]])          
        )
    
    
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
            await query.message.continue_propagation()
        except:
            await query.message.delete()
            await query.message.continue_propagation()






# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Developer @JishuDeveloper
