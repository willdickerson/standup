# Space Eggs Standup Randomizer

This is a Flask application that generates a random discussion topic and a new order for team members in a standup meeting. The discussion topics are generated using OpenAI's GPT-3 language model.

## Usage

The application is currently deployed on Heroku, and you can access it by clicking [here](https://standup.herokuapp.com/).

Upon accessing the application, you will see a list of team members and a discussion topic. To generate a new order and topic, simply click on the "Generate order and topic" button. To add a new team member, fill in the "Add new team member" field and click on the "Add" button. To delete a team member, click on the "x" button next to their name.

## Local development

To run the application locally, you will need to have Python and pip installed. First, clone the repository and navigate to the project directory:

```
$ git clone https://github.com/your-username/space-eggs-standup-randomizer.git
$ cd space-eggs-standup-randomizer
```

Next, install the required packages:

```
$ pip install -r requirements.txt
```

To start the Flask development server, run:

```
$ flask run
```

This will start the server on `http://127.0.0.1:5000/`. You can access the application by navigating to this URL in your browser.
