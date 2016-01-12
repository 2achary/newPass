import string


class NewPass(object):
    """
    Give the constructor your favorite quote or song lyric
    and then call hackronym() on your instance to get a new password.
    Make sure the phrase you pass in has as many words as you'd like
    your password to have characters.
    """

    def __init__(self, phrase):
        self.phrase = phrase
        self.translate = {'i': '!', 'a': '4', 'b': '8', 'o': '0',
                          'e': '3', 's': '5', 'x': '%', 'g': '9'}

    def hackronym(self):
        """
        Make an acronym of the provided phrase, replacing
        characters with numbers or symbols for certain matches
        """
        ret = ""
        for word in self.phrase.lower().split():
            try:
                ret += self.translate[word[0]]
            except KeyError:
                ret += word[0]
        ret = list(ret)

        for i in range(1, len(self.phrase.split()), 2):
            ret[i] = ret[i].upper()

        if not any([letter in string.punctuation or letter in string.digits
                    for letter in ret]):
            ret.append('!')

        return ''.join(ret)

if __name__ == "__main__":
    user_phrase = input('Phrase to base password off of: ')
    n = NewPass(user_phrase)
    print(n.hackronym())

