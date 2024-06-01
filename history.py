class History:
    def __init__(self):
        self.history = []

    def add(self, expression, result):
        self.history.append((expression, result))

    def last_five(self):
        return self.history[-5:]

    def save_to_txt(self, filename):
        with open(filename, 'w') as file:
            for expression, result in self.history:
                file.write(f"{expression} = {result}\n")
