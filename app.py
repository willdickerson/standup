from flask import Flask, render_template, request
import random
import openai
import os
from database import create_table, get_database_connection

app = Flask(__name__)
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

def get_team_members():
    conn = get_database_connection()
    cur = conn.cursor()
    cur.execute('SELECT name FROM team_members')
    team_members = [row[0] for row in cur.fetchall()]
    cur.close()
    conn.close()
    return team_members

def delete_member():
    member_to_delete = request.form['member_to_delete']
    conn = get_database_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM team_members WHERE name = %s', (member_to_delete,))
    conn.commit()
    cur.close()
    conn.close()
    return '', 204

def add_member():
    new_member = request.form['new_member']
    conn = get_database_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO team_members (name) VALUES (%s)', (new_member,))
    conn.commit()
    cur.close()
    conn.close()
    return '', 204

def get_random_discussion_topic():
    seed = random.choice(DISCUSSION_SEEDS)
    openai.api_key = os.environ.get('OPENAI_API_KEY')
    prompt = f"Hey ChatGPT, can you give us a random fun question to discuss during our standup tomorrow about {seed}? Something that everyone can answer quickly and easily that will make us laugh and smile. Please provide only the discussion question and no other text."
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
    return completion.choices[0].message.content

discussion_topic = ""

@app.route('/', methods=['GET', 'POST'])
def index():
    global discussion_topic

    if request.method == 'POST':
        action_type = request.form.get('action_type')

        if action_type == 'add_member':
            add_member()
        elif action_type == 'delete_member':
            delete_member()

    team_members = get_team_members()

    if request.form.get('generate_new_order_and_topic') == 'true':
        random.shuffle(team_members)
        discussion_topic = get_random_discussion_topic()

    return render_template('index.html', team_members=team_members, discussion_topic=discussion_topic)

if __name__ == '__main__':
    app.run(debug=True)
