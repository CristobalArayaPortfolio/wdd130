import random

def get_determiner(quantity):
    """Return a randomly chosen determiner.

    Args:
        quantity: An integer. If quantity is 1, this function will return a determiner for a single noun.
                    Otherwise this function will return a determiner for a plural noun.

    Returns:
        A randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    return random.choice(words)

def get_noun(quantity):
    """Return a randomly chosen noun.

    Args:
        quantity: An integer that determines if the returned noun is single or plural.

    Returns:
        A randomly chosen noun.
    """
    single_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    if quantity == 1:
        words = single_nouns
    else:
        words = plural_nouns
    return random.choice(words)

def get_verb(quantity, tense):
    """Return a randomly chosen verb.

    Args:
        quantity: An integer that determines if the returned verb is single or plural.
        tense: A string that determines the verb conjugation, either "past", "present" or "future".

    Returns:
        A randomly chosen verb.
    """
    past_verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    present_single_verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    present_plural_verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    future_verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    if tense == "past":
        words = past_verbs
    elif tense == "present":
        if quantity == 1:
            words = present_single_verbs
        else:
            words = present_plural_verbs
    else:
        words = future_verbs
    return random.choice(words)

def get_preposition():
    """Return a randomly chosen preposition.

    Returns:
        A randomly chosen preposition.
    """
    prepositions = ["about", "above", "across", "after", "against", "along", 
                   "among", "around", "at", "before", "behind", "below", 
                   "beside", "between", "by", "despite", "down", "during", 
                   "except", "for", "from", "in", "inside", "into", "like", 
                   "near", "of", "off", "on", "onto", "out", "outside", 
                   "over", "past", "since", "through", "to", "toward", 
                   "under", "underneath", "until", "up", "upon", "with", 
                   "within", "without"]
    return random.choice(prepositions)

def get_prepositional_phrase():
    """Return a randomly chosen prepositional phrase.

    Returns:
        A randomly chosen prepositional phrase.
    """
    preposition = get_preposition()
    determiner = get_determiner(random.randint(1, 2))  # Randomly choose singular or plural
    noun = get_noun(random.randint(1, 2))  # Randomly choose singular or plural
    return f"{preposition} {determiner} {noun}"

def make_sentence(quantity, tense):
    """Build and return a sentence with four parts: 
       a determiner, a noun, a verb, and a prepositional phrase.

    Args:
        quantity: An integer that determines if the returned sentence uses singular or plural nouns and verbs.
        tense: A string that determines the verb conjugation, either "past", "present" or "future".

    Returns:
        A grammatically correct sentence.
    """
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase = get_prepositional_phrase()
    sentence = f"{determiner.capitalize()} {noun} {verb} {prepositional_phrase}." 
    return sentence

def main():
    """Call the make_sentence function to generate and print six sentences with different combinations of quantity and tense."""
    print(make_sentence(1, "past"))
    print(make_sentence(1, "present"))
    print(make_sentence(1, "future"))
    print(make_sentence(2, "past"))
    print(make_sentence(2, "present"))
    print(make_sentence(2, "future"))

if __name__ == "__main__":
    main()