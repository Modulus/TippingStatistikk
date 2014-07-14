__author__ = 'Modulus'


"""Get the name of the current game beeing displayed"""


def get_game_name(url):
    if url:
        elements = url.split("/")
        page = elements[-1]

        """ Remove prefix and suffix (.htm)"""
        name = page[len("getNumberStatistics"):-4]

        if name:
            return name.strip()
        else:
            return name
    else:
        return None
