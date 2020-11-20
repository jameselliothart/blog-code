from pathlib import Path

class Greeter():
    def __init__(self, path):
        self._path = Path(path)

    def get_greetings(self):
        path = Path.joinpath(self._path, 'greetings.txt')
        return Path.read_text(path).split('\n')

    def run(self):
        greetings = [f'{greeting} earth!' for greeting in self.get_greetings()]
        path = Path.joinpath(self._path, 'planet_greetings.txt')
        Path.write_text(path, '\n'.join(greetings))
