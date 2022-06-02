import discord

token = "OTgwNzg3Mjk0NTE0NjAyMDE1.GvOMH-.HyQtft7ODDYULtjQm3NGQ7CxP5xPnKraoC_9gk"

client = discord.Client()

@client.event
async def on_ready():
    print(f"Bot logged in {client.user}")

@client.event
async def on_typing(chn, usr, when):
    await chn.send(f"Stop typing!")


@client.event
async def on_message(msg):
    if msg.author != client.user:
        print(f"Author: {msg.author}\nMessage: {msg.content}\n\n")

        if msg.raw_mentions and msg.raw_mentions[0] == client.user.id:
            await msg.channel.send(f"Bot answers")

            msg = msg.content
            print(msg)
        else:
            print(f"not for bot")

        #print(f"{client.user.id}")
        #for a in msg.mentions:
        #    print(a.id)
        #print(f"Mentions: {msg.mentions}")
        #if msg.isMemberMentioned(client.user)
        


client.run(token)
