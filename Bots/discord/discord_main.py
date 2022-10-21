import discord
import openai
 
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        f = open("openai.key")
        lines = f.read()
        openai.organization = "org-Xrmm6MxA9FkSXTcN88YHLyZ1"
        openai.api_key = lines
        f.close()

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content.startswith('help'):
            await message.channel.send('Start with "Medo, " to chat with me!')

        print('Message from {0.author}: {0.content}'.format(message))
 
        if message.content.startswith('Medo, '):
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

