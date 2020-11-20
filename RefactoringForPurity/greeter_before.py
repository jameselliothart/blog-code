from pathlib import Path

class Greeter():
    def __init__(self, path):
        self._path = Path(path)

    def get_greetings(self):
        path = Path.joinpath(self._path, 'greetings.txt')
        return path.read_text().split('\n')

    def run(self):
        planet_greetings = [f'{greeting} earth!' for greeting in self.get_greetings()]
        path = Path.joinpath(self._path, 'planet_greetings.txt')
        path.write_text('\n'.join(planet_greetings))
