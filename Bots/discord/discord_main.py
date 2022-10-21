import discord
import openai
 
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        f = open("openai.key")
        lines = f.read()
        openai.api_key = lines
        f.close()

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
 
        if message.content[0] == '?':
            response = openai.Completion.create(
                engine="text-davinci-001",
                prompt="Human:" + message.content[1:] + "\nAI:",
                temperature=1,
                max_tokens=200,
                top_p=1,
                best_of=1,
                frequency_penalty=0,
                presence_penalty=0,
                stop=["Human: ", "AI: "]
            )
            # clean the response
            caption: str = response.choices[0].text.strip()
            await message.channel.send(caption)

client = MyClient(intents=discord.Intents.default())
f = open("discord/discord.key")
lines = f.read()
TOKEN = lines
f.close()
client.run(TOKEN)

