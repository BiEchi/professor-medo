import discord
import openai
 
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        f = open("openai.key")
        lines = f.read()
        # remember to strip the newline character
        openai.api_key = lines.strip()
        f.close()

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content.startswith('help'):
            await message.channel.send('Start with "Medo, " to chat with me!')
 

        if message.content.startswith('Medo, '):
            await message.channel.send(message.content[6:])
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt="Human:" + message.content[6:] + "\nAI:",
                temperature=0.5,
                max_tokens=256,
                top_p=1,
                best_of=1,
                frequency_penalty=0,
                presence_penalty=0,
                stop=["Human: ", "AI: "]
            )
            # clean the response
            caption: str = response.choices[0].text.strip()
            await message.channel.send(caption)

client = MyClient(intents=discord.Intents.all())
f = open("discord/discord.key")
lines = f.read()
TOKEN = lines
f.close()
client.run(TOKEN)

