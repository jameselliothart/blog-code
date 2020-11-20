from pathlib import Path

class Greeter():
    def __init__(self, path):
        self._path = Path(path)

    def get_greetings(self):
        path = Path.joinpath(self._path, 'greetings.txt')
        return Path.read_text(path).split('\n')

    @staticmethod
    def greet_planet(greetings):
        return [f'{greeting} mars!' for greeting in greetings]

    def run(self):
        greetings = self.greet_planet(self.get_greetings())
        path = Path.joinpath(self._path, 'planet_greetings.txt')
        Path.write_text(path, '\n'.join(greetings))
