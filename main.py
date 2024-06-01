from calculator import Calculator
from history import History
from pynput import keyboard


class Main:
    def __init__(self):
        self.calculator = Calculator()
        self.history = History()
        self.history_index = -1
        self.calculate = True
        self.last_result = None

    def keyboard_controller(self, key):
        try:
            if key == keyboard.Key.up:
                if self.history_index < -1:
                    self.history_index += 1
                self.show_operation()
            elif key == keyboard.Key.down:
                if self.history_index > -len(self.history.history):
                    self.history_index -= 1
                self.show_operation()
        except Exception as e:
            print(f"Error: {e}")

    def show_operation(self):
        if -len(self.history.history) <= self.history_index < 0:
            print(f"History: {self.history.history[self.history_index]}")

    def run(self):
        print("Operations: +, -, *, /, **, sqrt, %, fac, sin, cos, tan, ctan")
        print("Type 'stop' to stop calculator")
        print("Type 'reset' to restart calculator")

        listener = keyboard.Listener(on_press=self.keyboard_controller)
        listener.start()

        while self.calculate:
            try:
                if self.last_result is not None:
                    user_input = f"{self.last_result} "
                else:
                    user_input = ""

                expression = input(f"{user_input} ==> ")
                if expression.lower() == 'stop':
                    self.calculate = False
                    print("Calculator stopped")
                    break

                elif expression.lower() == 'reset':
                    self.history = History()
                    self.history_index = -1
                    self.last_result = None
                    print("Calculator restarted.")
                    continue

                if self.last_result is not None:
                    expression = f"{self.last_result} {expression}"

                parts = expression.split()
                if len(parts) == 2:
                    operation = parts[0]
                    number1 = float(parts[1])
                    number2 = None
                elif len(parts) == 3:
                    number1 = float(parts[0])
                    operation = parts[1]
                    number2 = float(parts[2])
                else:
                    raise ValueError("Invalid input format")

                if operation in self.calculator.operations:
                    if number2 is not None:
                        result = self.calculator.operations[operation](number1, number2)
                    else:
                        result = self.calculator.operations[operation](number1)
                else:
                    raise ValueError("Unavailable operation Madam/Sir")

                self.history.add(expression, result)
                self.history_index = -1
                self.last_result = result
                print(f"Result: {result}")
                print(f"Last 5 operations: {self.history.last_five()}")

            except Exception as exc:
                print(f"Error: {exc}")


if __name__ == "__main__":
    main = Main()
    main.run()
    main.history.save_to_txt("history.txt")
