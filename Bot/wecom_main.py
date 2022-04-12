# https://corpwechatbot.gentlecp.com/%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B/callback_configuration/
from corpwechatbot.chatbot import CorpWechatBot
import openai

bot = CorpWechatBot(key='e8c7cdd7-448b-4245-a0be-4907f1bfa6e3')  # 你的机器人key，通过群聊添加机器人获取

def respond(message) -> None:
    """Forward OpenAI messages."""
    response = openai.Completion.create(
        engine="text-davinci-001",
        prompt="Human:" + message + "\nAI:",
        temperature=1,
        max_tokens=1000,
        top_p=1,
        best_of=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n"]
    )
    # clean the response
    caption: str = response.choices[0].text.strip()
    print(caption)
    bot.send_text(content=caption)

def main() -> None:
    f = open("./openai.key")
    lines = f.read()
    openai.api_key = lines
    f.close()
    respond("你好,最近怎么样?请用英文回答")

if __name__ == '__main__':
    main()
