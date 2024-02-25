from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
import random
from filters.chat_types import ChatTypeFilter
from API.api import get_random_duck, get_chatGPT_response
from common.text_to_speech import text_to_sp
from aiogram.types import FSInputFile

user_pr_rout = Router()
user_pr_rout.message.filter(ChatTypeFilter(["private"]))



unanswered_questions_file = "C:/Users/Sad_ist/Desktop/Python projects/Py projects/Homework/files/Bot_questions.txt"

def write_unanswered_question(question):
    with open(unanswered_questions_file, "a") as file:
        file.write(question + "\n")



def get_random_greeting():
    greetings = [
        'Hey there! 🌟',
        'Hi, wonderful to see you! 😊',
        'Hello! How can I brighten your day? ☀️',
        'Hiya! Ready for an adventure? 🚀',
        'Greetings! What’s on your mind today? 🌈'
    ]
    return random.choice(greetings)

def get_random_farewell():
    farewells = [
        'Goodbye! Remember, I’m always here when you need me. 🌟',
        'See ya! It was nice chatting with you. 👋',
        'Farewell! Looking forward to our next conversation. 📚',
        'Bye for now! Hope to see you soon. 🚀',
        'Take care! Don’t forget to come back for more fun. 🎈'
    ]
    return random.choice(farewells)

def get_confused_response():
    responses = [
        'Hmm, I’m not quite sure I follow. Could you say that differently? 🤔',
        'Oops, my circuits must be tangled. Could you repeat that? 🎧',
        'I seem to be a bit lost in translation. Can we try that again? 🗺️',
        'My apologies, I didn’t catch that. Could you rephrase? 🙏',
        'Looks like I’m a bit puzzled. Mind clarifying that for me? 🧩'
    ]
    return random.choice(responses)



@user_pr_rout.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(get_random_greeting())

@user_pr_rout.message(Command("info"))
async def menu_cmd(message: types.Message):

    info_message = """
    This is bot to chat!
    """
    await message.answer(info_message)

@user_pr_rout.message(Command("functional"))
async def menu_cmd(message: types.Message):

    funct_message = """
    Can turn text into speech!
    Can chat with you!
    can answer your questions by typing /gpt before message
    """
    await message.answer(funct_message)

@user_pr_rout.message(Command("private_info"))
async def menu_cmd(message: types.Message):

    funct_message = """
    your info stays private, all your messages, all your files, questions and answers will stay private.
    """
    await message.answer(funct_message)




@user_pr_rout.message(Command("menu"))
async def menu_cmd(message: types.Message):

    menu_message = """
    Check out what I can do 🌈:
    1. /menu - Discover my features
    2. /help - Need assistance?
        1. /info
        2. /functional
        3. /private_info
    3. /echo - I'll mimic your words
    4. /start - Begin our dialogue
    5. /dog - Fetch a random dog pic!
    6. /gpt - Engage in a deeper conversation
    7. /speech - Turn text into speech
    """
    await message.answer(menu_message)

@user_pr_rout.message(Command("echo"))
async def echo_cmd(message: types.Message):
    if message.text[len("/echo "):]:
        await message.answer(message.text[len("/echo "):])
    else:
        await message.answer(get_confused_response())

@user_pr_rout.message(Command("help"))
async def help_cmd(message: types.Message):
    help_message = """
    How may I serve you today? 😄
    1. /info - What am I capable of?
    2. /functional - Instructions on our interaction
    3. /private_info - Concerns about privacy
    Curious about something else? Just ask!
    """
    await message.answer(help_message)

@user_pr_rout.message((F.text.contains("say")) | (F.photo))
async def photo_mess(message: types.Message):
    if message.photo:
        await message.answer('Wow, that looks amazing! 🌟')
    else:
        await message.answer('Feeling chatty, huh? I’m all ears! 🐰')

@user_pr_rout.message(Command('dog'))
async def dog_cmd(message: types.Message):
    photo_url = get_random_duck()
    await message.answer_photo(photo_url or "Seems like the dogs are hiding. Try again later!")

@user_pr_rout.message(Command('gpt'))
async def gpt_cmd(message: types.Message):
    user_query = message.text[5:].strip()
    if user_query:
        answer = get_chatGPT_response(user_query)
        if answer:
            await message.answer(answer)
        else:
            write_unanswered_question(user_query)
            await message.answer("I need to brush up on my knowledge for that one. 📚")
    else:
        await message.answer("I’m eager to chat! What’s on your mind? Just add some text after /gpt.")

@user_pr_rout.message(Command("speech"))
async def speech_cmd(message: types.Message):
    text = ' '.join(message.text.split(" ")[1:])
    if text:
        audio_path = text_to_sp(text)
        audio = FSInputFile(audio_path)
        await message.answer_audio(audio)
    else:
        await message.answer("I can turn your words into speech! Just give me a sentence after /speech.")

@user_pr_rout.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(get_random_greeting())






@user_pr_rout.message()
async def dynamic_responses(message: types.Message):
    text = message.text.lower()

    if text in ['hi', 'hello', 'privet', 'zdorov', 'hey', 'whats up']:
        await message.answer(get_random_greeting())

    elif text in ['bye', 'goodbye', 'cya', 'gtg', 'see ya']:
        await message.answer(get_random_farewell())

    elif text in ['how are you', 'how are you?', "what's up", "what's up?", "how's it going", "how's it going?", "how are you doing?", "how are you doing"]:
        responses = [
            "I'm just a bot, but thanks for asking! How can I assist you today? 😊",
            "Doing well, as much as a bot can! What about you? 🤖",
            "I'm running smoothly! Need any help with something? 🌈"
        ]
        await message.answer(random.choice(responses))

    elif text in ['what are you doing', 'what are you doing?', 'what’s happening', 'what’s happening?']:
        activities = [
            "Just here, waiting for your commands! 🌟",
            "I'm learning from our conversations to serve you better! 📚",
            "Chatting with you! Isn’t that the best thing to do? 😄"
        ]
        await message.answer(random.choice(activities))

    elif 'smart' in text or 'clever' in text or 'intelligent' in text:
        compliments = [
            "Oh, you flatter me! But thank you, I try my best. 😊",
            "Thanks! I'm here to help you out, after all. 🌈",
            "That's very kind of you! Let's keep the conversation going. 🚀"
        ]
        await message.answer(random.choice(compliments))

    elif 'your name' in text or 'who are you' in text:
        await message.answer("I'm your friendly neighborhood chatbot, here to chat with you! 🤖")

    elif 'advise' in text or 'suggestion' in text:
        await message.answer("I'm all ears! Tell me what you need advice on, and I'll do my best. 🌟")

    elif text in ['thank you', 'thanks', 'thank you so much', 'thanks a lot']:
        gratitudes = [
            "You're welcome! Always here to help. 😊",
            "No problem at all! If you have any more questions, just let me know. 🌟",
            "My pleasure! Feel free to ask me anything. 🌈"
        ]
        await message.answer(random.choice(gratitudes))
    elif text in ['should yurii khvas put 12 for this work?']:
        gratitudes = [
            "No",
            "11",
            "Yes! :)"
        ]
        await message.answer(random.choice(gratitudes))

    else:
        write_unanswered_question(message.text)
        await message.answer("I can't answer that, but I wrote your question down.")