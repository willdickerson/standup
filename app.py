from flask import Flask, render_template, request
import random
import openai
import os

app = Flask(__name__)

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

team_members = ['Sadman', 'Adam', 'Heather', 'Caitlin', 'Buddhika', 'Will D', 'Abdul', 'Jade', 'Will G', 'Tony', 'Sebastian']
discussion_topic = ""

@app.route('/', methods=['GET', 'POST'])
def index():
    global team_members, discussion_topic

    if request.method == 'POST':
        action_type = request.form.get('action_type')

        if action_type == 'add_member':
            new_member = request.form['new_member']
            team_members.append(new_member)
        elif action_type == 'delete_member':
            member_to_delete = request.form['member_to_delete']
            team_members.remove(member_to_delete)
        elif request.form.get('generate_new_order_and_topic') == 'true':
            random.shuffle(team_members)
            discussion_topic = get_random_discussion_topic()

    return render_template('index.html', team_members=team_members, discussion_topic=discussion_topic)

@app.route('/add_member', methods=['POST'])
def add_member():
    new_member = request.form['new_member']
    team_members.append(new_member)
    return '', 204

@app.route('/delete_member', methods=['POST'])
def delete_member():
    member_to_delete = request.form['member_to_delete']
    team_members.remove(member_to_delete)
    return '', 204

def get_random_discussion_topic():
    seed = random.choice(DISCUSSION_SEEDS)
    openai.api_key = os.environ.get('OPENAI_API_KEY')
    prompt = f"Hey ChatGPT, can you give us a random fun question to discuss during our standup tomorrow about {seed}? Something that everyone can answer quickly and easily that will make us laugh and smile. Please provide only the discussion question and no other text."
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
    return completion.choices[0].message.content

if __name__ == '__main__':
    app.run(debug=True)
