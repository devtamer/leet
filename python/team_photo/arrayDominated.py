import collections

class Team:
    Player = collections.namedtuple('Player', ('height'))

print(Team.Player)
