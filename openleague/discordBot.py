import discord
import logging

class myClient(discord.Client):

    async def on_ready(self):
        logging.info(f"Bot online as: {self.user}")

    async def on_message(self,msg):
        if msg.author != self.user:
            logging.info(f"Author: {msg.author} Message: {msg.content}")

            if msg.raw_mentions and msg.raw_mentions[0] == self.user.id:
                await msg.channel.send(f"Bot answers")

                msg = msg.content
                logging.info(msg)
            else:
                logging.info(f"not for bot")



def runBot(token):
    # disable not important logging from the package
    logging.getLogger("discord").setLevel(logging.ERROR)

    # starting the client
    myClient().run(token)

    
# should remove
if __name__ == "__main__":

    # getting the token for the local test
    from cred import discord_bot_token

    runbot(token=discord_bot_token)
