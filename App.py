from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# ALL PROGRAMMING JOKES
programming_jokes = [
    {"setup": "Why do programmers prefer dark mode?", "punchline": "Because light attracts bugs! 🐛"},
    {"setup": "How many programmers does it take to change a light bulb?", "punchline": "None, that's a hardware problem! 💡"},
    {"setup": "Why did the developer go broke?", "punchline": "Because he used up all his cache! 💰"},
    {"setup": "Why do Java developers wear glasses?", "punchline": "Because they don't C#! 👓"},
    {"setup": "What's a programmer's favorite hangout place?", "punchline": "Foo Bar! 🍺"},
    {"setup": "Why did the database admin leave his wife?", "punchline": "She had one-to-many relationships! 💔"},
    {"setup": "How many programmers does it take to fix a bug?", "punchline": "That's not a bug, it's a feature! ✨"},
    {"setup": "Why do programmers mix up Halloween and Christmas?", "punchline": "Because Oct 31 equals Dec 25! 🎃"},
    {"setup": "A SQL query walks into a bar...", "punchline": "'Can I join you?' 🍻"},
    {"setup": "Why did the programmer quit?", "punchline": "Because he didn't get arrays! 📊"},
]

# ALL ROMANTIC JOKES
romantic_jokes = [
    {"setup": "Are you a magician?", "punchline": "Because whenever I look at you, everyone else disappears! ✨💕"},
    {"setup": "Do you believe in love at first sight?", "punchline": "Or should I walk by again? 😘"},
    {"setup": "Are you a parking ticket?", "punchline": "Because you've got FINE written all over you! 💑"},
    {"setup": "If you were a vegetable, you'd be a cute-cumber! 🥒", "punchline": "And I'd love to have you in my salad! 💚"},
    {"setup": "Are you Google?", "punchline": "Because you're everything I've been searching for! 💕"},
    {"setup": "Do you have a map?", "punchline": "Because I just got lost in your eyes! 👀💕"},
    {"setup": "Are you French?", "punchline": "Because Eiffel for you! 🗼❤️"},
    {"setup": "If you were a flower, you'd be a damnnnn-delion! 🌼", "punchline": "Beautiful and dangerously attractive! 😍"},
    {"setup": "Can I follow you home?", "punchline": "Cause my parents always told me to follow my dreams! 💭💕"},
    {"setup": "Do you have any raisins?", "punchline": "No? How about a date? 📅💑"},
    {"setup": "Are you a bank loan?", "punchline": "Because you have my interest! 💰💕"},
    {"setup": "If you were a fruit, you'd be a fine apple! 🍎", "punchline": "And I'd love to bite you! 😋❤️"},
    {"setup": "Is your name Google?", "punchline": "Because you're the answer to all my searches! 🔍💕"},
    {"setup": "Do you believe in destiny?", "punchline": "Because I think we were meant to meet! ✨👫"},
    {"setup": "Are you a Wi-Fi signal?", "punchline": "Because I'm feeling a connection! 📶💕"},
    {"setup": "If you were a tear in my eye...", "punchline": "I would never cry, because I wouldn't ever want to lose you! 😢💕"},
    {"setup": "Do you have a pencil?", "punchline": "Because I want to erase your past and write our future! ✏️💕"},
    {"setup": "Are you the sun?", "punchline": "Because you light up my whole world! ☀️💕"},
    {"setup": "If I were a cat, I'd spend all nine lives with you! 🐱", "punchline": "That's how much I love you! 💕"},
    {"setup": "Do you know what's beautiful?", "punchline": "Read the first word! You are! 😘💕"},
]

# JUMPSCARE MEMES
jumpscare_memes = [
    "https://media.giphy.com/media/l3q2K5jinAlChoCLS/giphy.gif",
    "https://media.giphy.com/media/l0HlDtKCoYt5n8jDo/giphy.gif",
    "https://media.giphy.com/media/3ohzdKdb7CliMnHlRS/giphy.gif",
    "https://media.giphy.com/media/l0IypeKl9NJhFXpIQ/giphy.gif",
]

# NORMAL MEMES
all_memes = [
    "https://i.imgflip.com/1bgw.jpg",
    "https://i.imgflip.com/1ihzfe.jpg",
    "https://i.imgflip.com/30b1gx.jpg",
    "https://i.imgflip.com/3og0u9.jpg",
]

# GLOBAL COUNTERS
prank_count = 0
total_pranks = 0
current_joke_index = 0
joke_type = "Romantic"

@app.route('/')
def index():
    global prank_count, total_pranks, current_joke_index, joke_type
    prank_count = 0
    total_pranks = 0
    current_joke_index = 0
    joke_type = "Romantic"
    
    joke = romantic_jokes[0]
    meme = random.choice(all_memes)
    
    return render_template('index.html', 
                         joke=joke, 
                         meme=meme,
                         joke_index=current_joke_index,
                         total_jokes= len(romantic_jokes),
                         joke_type=joke_type)

@app.route('/next-joke')

def next_joke():
     global current_joke_index

     current_joke_index += 1

     if current_joke_index >= len(romantic_jokes):
         current_joke_index = 0

     joke = romantic_jokes[current_joke_index]

     return jsonify({
        "joke": joke,
        "index": current_joke_index,
        "type": "romantic",
        "total": len(romantic_jokes),
        "progress": f"{current_joke_index + 1} / {len(romantic_jokes)}"
     })
@app.route('/previous-joke')

    
def previous_joke():
     global current_joke_index

     current_joke_index -= 1

     if current_joke_index < 0:
        current_joke_index = len(romantic_jokes) - 1

     joke = romantic_jokes[current_joke_index]

     return jsonify({
        "joke": joke,
        "index": current_joke_index,
        "type": "romantic",
        "total": len(romantic_jokes),
        "progress": f"{current_joke_index + 1} / {len(romantic_jokes)}"
     })
@app.route('/prank-button', methods=['POST'])
def prank_button():
    global prank_count, total_pranks
    prank_count += 1
    total_pranks += 1
    
    responses = [
        "🎪 YOU GOT PRANKED AGAIN! 🎪",
        "😜 FOOLED YOU TWICE! 😜",
        "🎭 YOU'RE TOO EASY! 🎭",
        "🚀 MEGA PRANK! 🚀",
        "💥 PRANK OVERDRIVE! 💥",
    ]
    
    return jsonify({
        "message": random.choice(responses),
        "prank_count": prank_count,
        "total_pranks": total_pranks
    })

@app.route('/jumpscare')
def jumpscare():
    jumpscare_meme = random.choice(jumpscare_memes)
    return jsonify({"jumpscare_url": jumpscare_meme})

@app.route('/get-random-meme')
def get_random_meme():
    meme = random.choice(all_memes)
    return jsonify({"meme_url": meme})

@app.route('/combo-prank', methods=['POST'])
def combo_prank():
    global prank_count, total_pranks
    prank_count += 3
    total_pranks += 3
    
    return jsonify({
        "message": "⚡ TRIPLE COMBO! PRANK MASTER! ⚡",
        "prank_count": prank_count,
        "total_pranks": total_pranks
    })

@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"error": "Page not found!"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
