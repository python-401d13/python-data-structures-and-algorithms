
def repeated_word(lengthy):
    """
    Find the first repeated word in lengthy string.

    Known limitations: Plurals are seen as different words.

    Input:
    lengthy (string): phrase, sentences, paragraphs.

    Output:
    string/None: First repeated word or None otherwise.
    """

    punctation = ',-;:\"\'.!?'
    lengthy = lengthy.lower().replace(punctation, '')
    words = lengthy.split(' ')
    counter = {}

    for word in words:
        if counter.get(word):
            return word
        else:
            counter[word] = 1

    return None
