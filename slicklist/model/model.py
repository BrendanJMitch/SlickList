from dataclasses import dataclass, astuple


@dataclass
class Model:

    def __tuple__(self):
        return astuple(self)