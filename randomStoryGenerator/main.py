import random

# define some lists of words that we will use to generate our stories
characters = ["Alice", "Bob", "Charlie", "Dave", "Eve"]
settings = ["in a dark forest", "on a deserted island", "in a bustling city", "in a medieval castle"]
plots = ["finds a mysterious object", "goes on a quest to find a lost treasure", "falls in love with a stranger"]

# function to generate a random story
def generate_story():
    # choose a random character, setting, and plot
    character = random.choice(characters)
    setting = random.choice(settings)
    plot = random.choice(plots)

    # generate the story
    story = f"{character} {plot} {setting}."

    # return the story
    return story

story = generate_story()
print(story)
