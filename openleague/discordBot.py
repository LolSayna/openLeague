import discord
import logging
from interpreter import parse_Cmd

# Implementing the discord Client Class
class myClient(discord.Client):

    # debugging on startup
    async def on_ready(self):
        logging.info(f"Bot online as: {self.user}, Id: {self.user.id}")

    # replying to message and parsing them
    async def on_message(self, msg):
        if msg.author != self.user:
            
            logging.warning(f"Message: {msg.clean_content}, by: {msg.author}")

            if str(self.user.id) in msg.content:
                cmd = msg.clean_content.split()
                logging.warning(f"Parsing: {cmd}")

                if cmd[1] == "status":
                    await msg.channel.send(f"Online")
                
                elif cmd[1] == "exe":
                    await msg.channel.send(f"Execute Order 66!")

                elif cmd[1] == "emb":
                    print("dsa")    
                    embed = discord.Embed(title="hallo", description="welt", url="https://euw.op.gg/summoner/userName=uffsayna")
                    await msg.channel.send(embed=embed)

                else:
                    await msg.channel.send(parse_Cmd(cmd))

                    
    


        
# to start the bot
def runBot(token):
    # disable not important logging from the package
    logging.getLogger("discord").setLevel(logging.ERROR)

    myClient().run(token)