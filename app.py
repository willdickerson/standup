from flask import Flask, render_template, request, session
import random
import openai
import os
from database import create_table, get_team_members, add_member, delete_member

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY')
create_table()

DISCUSSION_SEEDS = [
    "food",
    "music",
    "travel",
    "technology",
    "sports",
    "movies",
    "TV shows",
    "books",
    "video games",
    "board games",
    "cartoons",
    "memes",
    "pets",
    "languages",
    "sarcasm",
    "jokes",
    "puns",
    "celebrities",
    "myths",
    "legends",
    "superheroes",
    "villains",
    "robots",
    "aliens",
    "time travel",
    "magic",
    "fantasy",
    "sci-fi",
    "horror",
    "comedy",
    "drama",
    "action",
    "adventure",
    "mystery",
    "history",
    "politics",
    "philosophy",
    "religion",
    "art",
    "design",
    "fashion",
    "architecture",
    "nature",
    "environment",
    "education",
    "career",
    "money",
    "health",
    "fitness"
]

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
OPENAI_MODEL = "gpt-3.5-turbo"

def get_random_discussion_topic():
    seed = random.choice(DISCUSSION_SEEDS)
    openai.api_key = OPENAI_API_KEY
    prompt = f"Hey ChatGPT, can you give us a random fun question to discuss during our standup tomorrow about {seed}? Something that everyone can answer quickly and easily that will make us laugh and smile. Please provide only the discussion question and no other text."
    completion = openai.ChatCompletion.create(model=OPENAI_MODEL, messages=[{"role": "user", "content": prompt}])
    return completion.choices[0].message.content

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        action_type = request.form.get('action_type')

        if action_type == 'add_member':
            add_member(request)
        elif action_type == 'delete_member':
            delete_member(request)

    team_members = get_team_members()

    if request.form.get('generate_new_order_and_topic') == 'true':
        random.shuffle(team_members)
        session['discussion_topic'] = get_random_discussion_topic()

    discussion_topic = session.get('discussion_topic', "")

    return render_template('index.html', team_members=team_members, discussion_topic=discussion_topic)

if __name__ == '__main__':
    app.run(debug=True)
