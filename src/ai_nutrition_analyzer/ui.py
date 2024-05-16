class Greeter:
    def __init__(self, name="Guest"):
        self.name = name

    def set_name(self, name):
        """Set the name of the user."""
        self.name = name

    def greet(self):
        """Print a greeting message."""
        print(f"Hello, {self.name}!")