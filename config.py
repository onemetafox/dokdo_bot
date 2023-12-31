import toml


class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


config = toml.load('config.toml', AttrDict)
try:
    repos = toml.load('repos.toml', AttrDict)
except FileNotFoundError:
    repos = toml.load('repos.default.toml', AttrDict)
