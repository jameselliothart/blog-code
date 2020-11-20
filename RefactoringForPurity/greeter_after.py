from pathlib import Path

class Greeter():
    def __init__(self, path):
        self._path = Path(path)

    def get_greetings(self):
        path = Path.joinpath(self._path, 'greetings.txt')
        return path.read_text().split('\n')

    @staticmethod
    def greet_planet(greetings):
        return [f'{greeting} mars!' for greeting in greetings]

    def run(self):
        greetings = self.get_greetings()
        planet_greetings = self.greet_planet(greetings)
        self.save_greetings(planet_greetings)

    def save_greetings(self, greetings):
        path = Path.joinpath(self._path, 'planet_greetings.txt')
        path.write_text('\n'.join(greetings))
