import discord
import graph
import os

# TOKEN = config.discord_TOKEN
TOKEN = os.getenv("DISCORD_TOKEN")
print("Starting script...")

class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Bot is up...Logged in as {self.user}")

    async def on_message(self,message):
        author = message.author.name
        if author == str(self.user).split('#')[0]:
            return
        content = message.content
        if str(content)==".twhelp":
            embedDesc = "`.twhelp`\nDisplays the help message\n`.twfetch`\nSyntax : `.twfetch [like/retweet] [username(without @ prefix)]`\n\nWhat the second parameter stands for\n`like` : The graph returned is based on the likes the requested user's tweets have received.\n`retweet` : The graph returned is based on the rewteets the requested user's tweets have received."
            embed = discord.Embed(title = "Helper Commands", colour=0x87CEEB, description = embedDesc)
            embed.set_author(name = "Twarx")
            # await message.channel.send("Use the command `.twfetch <<like/retweet>> <<username(without @)>>`")
            await message.channel.send(embed=embed)
            return
        if content.split()[0]==".twfetch":
            if len(content.split())!=3:
                await message.channel.send(f"Hey there...{author} sent a message that reads {content}. Hit `.twhelp` for valid commands")        
                return
            elif (len(content.split())==3 and content.split()[0]!=".twfetch" ):
                await message.channel.send(f"Hey there...{author} sent a message that reads {content}. Hit `.twhelp` for valid commands")
                return
            elif(len(content.split())==3 and content.split()[0]==".twfetch" and (content.split()[1] not in ["like","retweet"])):
                await message.channel.send(f"Syntax error type in `.twhelp` for syntax")
                return
            elif (len(content.split())==3 and content.split()[0]==".twfetch" and (content.split()[1]=="like" or content.split()[1]=="retweet")):
                graphOutput = graph.plotGraphs(content.split()[2])
                if graphOutput=="User not found":
                    await message.channel.send("User not found")
                else:
                    await message.channel.send(f"The graph you requested has been personally sent to you {author}")
                    if(content.split()[1]=="like"):
                        await message.author.send(file = discord.File("./likes.jpeg"))
                        return
                    else:
                        await message.author.send(file = discord.File("./retweets.jpeg"))
                        return
        else:
            pass

client = MyClient()
client.run(TOKEN)

