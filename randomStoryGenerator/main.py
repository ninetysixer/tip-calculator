import random

# Predefined templates for different parts of the story
templates = {
    'intro': ['Once upon a time, there was a {character} named {name}.',
              'In a land far away, {name} the {character} lived happily.'],
    'conflict': ['One day, {name} encountered a {adjective} {antagonist}.',
                 '{name} faced a great challenge when a {antagonist} appeared.'],
    'resolution': ['With determination and {adjective}, {name} overcame the {antagonist}.',
                   'Through courage and cleverness, {name} defeated the {antagonist}.'],
    'ending': ['And they all lived happily ever after.',
               'From that day on, {name} became a legend in the land.']
}


def generate_story():
    # Randomly choose character, name, antagonist, and adjective
    character = random.choice(['prince', 'princess', 'wizard', 'knight'])
    name = random.choice(['Arthur', 'Eleanor', 'Merlin', 'Lancelot'])
    antagonist = random.choice(['dragon', 'witch', 'giant', 'evil sorcerer'])
    adjective = random.choice(['bravery', 'wisdom', 'perseverance', 'resourcefulness'])

    # Generate the story parts using the templates
    intro = random.choice(templates['intro']).format(character=character, name=name)
    conflict = random.choice(templates['conflict']).format(name=name, adjective=adjective, antagonist=antagonist)
    resolution = random.choice(templates['resolution']).format(name=name, adjective=adjective, antagonist=antagonist)
    ending = random.choice(templates['ending']).format(name=name)

    # Combine the story parts
    story = intro + ' ' + conflict + ' ' + resolution + ' ' + ending
    return story


# Generate and print a story
story = generate_story()
print(story)
