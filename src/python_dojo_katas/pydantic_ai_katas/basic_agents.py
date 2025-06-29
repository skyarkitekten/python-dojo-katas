class BasicAgent:
    def __init__(self, name: str):
        self.name = name

    def greet(self) -> str:
        return f"Hello, my name is {self.name}."


class AdvancedAgent(BasicAgent):
    def __init__(self, name: str, skill_level: str):
        super().__init__(name)
        self.skill_level = skill_level

    def introduce(self) -> str:
        return f"{self.greet()} I am skilled at {self.skill_level}."
