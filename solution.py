"""
Functions used by the Mad Lib generator.
Running this file will **not** generate the Mad Lib... run the main.py file instead.
Complete each function in this file such that when the main.py file is run, a Mad Lib is generated.
"""


def get_adj():
    """
    Ask the user to enter an adjective.
      :returns: the text entered by the user
    """
    # write your code for this function below this line

    # don't modify the return statement below...
    word = input("Enter an adjective: ")
    return word


def get_verb():
    """
    Ask the user to enter a verb.
      :returns: the text entered by the user
    """
    # write your code for this function below this line

    # don't modify the return statement below... leave it as the last line in this function
    word = input("Enter a verb: ")
    return word


def get_plural_noun():
    """
    Ask the user to enter a plural noun.
      :returns: the text entered by the user
    """
    # write your code for this function below this line

    # don't modify the return statement below... leave it as the last line in this function
    word = input("Enter a plural noun: ")
    return word


def get_proper_noun():
    """
    Ask the user to enter a proper noun (the name of a location, person, or event).
      :returns: the text entered by the user
    """
    # write your code for this function below this line

    # don't modify the return statement below... leave it as the last line in this function
    word = input("Enter a proper noun: ")
    return word


def generate():
    """
    Generates a variation of the Jabberwocky poem in a "Mad Lib" style.
    You can view the text of the original Jaabberwocky poem here: https://en.wikipedia.org/wiki/Jabberwocky

    Uses the functions defined in this file to ask the user for...
    - 2 adjectives
    - 2 verbs
    - 2 plural nouns
    - 2 proper nouns (names of a place, person, or event)

    Then plug these into the Jaberwocky poem according to the given template and print it out.
    """

    # write your code for this function below this line...
    # feel free to modify the given poem code and add any additional code as necessary
    adjective_1 = input("Enter the first adjective: ")
    adjective_2 = input("Enter the second adjective: ")
    verb_1 = input("Enter the first verb: ")
    verb_2 = input("Enter the second verb: ")
    plural_noun_1 = input("Enter the first plural noun : ")
    plural_noun_2 = input("Enter the second plural noun: ")
    proper_noun_1 = input("Enter the first proper noun: ")
    proper_noun_2 = input("Enter the second proper noun: ")

    poem = """
    'Twas {adjective_1}, and the slithy toves
    Did {verb_1} and gimble in the wabe;
    All {adjective_2} were the borogoves,
    And the mome {plural_noun_1} outgrabe.

    "Beware the {proper_noun_1}, my son!
    The jaws that {verb_2}, the {plural_noun_2} that catch!
    Beware the Jubjub bird, and shun
    The frumious {proper_noun_2}!
  """.format(
        adjective_1 = adjective_1,
        adjective_2 = adjective_2,
        verb_1 = verb_1,
        verb_2 = verb_2,
        plural_noun_1 = plural_noun_1,
        plural_noun_2 = plural_noun_2,
        proper_noun_1 = proper_noun_1,
        proper_noun_2 = proper_noun_2
    )

    # don't modify the print statement below... leave it as the last line in this function
    print(poem)
