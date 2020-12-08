import discord

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))




@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        
    if message.content == '/dog':
        await message.channel.send('わん！')

    if message.content == '/who made?':
        await message.channel.send('はむ')

    if message.content == 'p/forge':
        await message.channel.send('minecraftのverをp/形式で答えてください 例　(p/1.8.9)など 。') 

    if message.content == '/admin':
        await message.channel.send('どうしましたか？')

    if message.content == 'p/1.8.9':
        await message.channel.send('https://files.minecraftforge.net/maven/net/minecraftforge/forge/1.8.9-11.15.1.1722/forge-1.8.9-11.15.1.1722-installer-win.exe')

    if message.content == 'p/1.12.2':
        await message.channel.send('https://files.minecraftforge.net/maven/net/minecraftforge/forge/1.12.2-14.23.5.2854/forge-1.12.2-14.23.5.2854-installer.jar')
    
    if message.content == 'p/1.7.10':
        await message.channel.send('https://files.minecraftforge.net/maven/net/minecraftforge/forge/1.7.10-10.13.4.1558-1.7.10/forge-1.7.10-10.13.4.1558-1.7.10-installer-win.exe')

    if message.content == 'p/help':
        await message.channel.send('対応しているバージョンは　1.12.2 1.8.9 1.7.10 です。希望に応じて増やします。')

    if message.content == '/hamubot/help':
        await message.channel.send('p/forgeでminecraftに使うforgeのURLに簡単に飛べます。')

    if message.content == '/hamubot/help':
        await message.channel.send('p/optiでminecraftに使うoptifineのURLに簡単に飛べます。')

    if message.content == '/hey':
        await message.channel.send('hai!')      

    if message.content == '/google':
        await message.channel.send('https://www.google.co.jp/')   

    if message.content == '/youtube':
        await message.channel.send('https://www.youtube.com/?gl=JP')

    if message.content == '/amazon':
        await message.channel.send('https://www.amazon.co.jp/') 

    if message.content == '/url/minecraft':
        await message.channel.send('https://www.minecraft.net/ja-jp')  

    if message.content == '/url/discord':
        await message.channel.send('https://discord.com/') 
                        


client.run('NzgwNzUxNjQ1NjYyMzgwMDQz.X7zpoQ.fusguV1LTqst2itB_SrgQav6QPg')
