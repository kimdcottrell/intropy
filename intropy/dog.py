class Dog:
    """Business requires that we must have more puppers"""

    def __init__(self, name: str):
        self.name = name
        self.tricks = []
        self.owner = ''

    def add_trick(self, trick: str):
        """Add as many tricks as you'd like.

        :param trick: description for trick
        """
        self.tricks.append(trick)

    def add_owner(self, owner: str):
        """Add in the optional owner.

        :param owner: description for owner
        """
        self.owner = owner

    def description(self) -> str:
        """Generate the overall description of the dog.

        :return: description for return
        """
        desc = [f"{self.name} knows {', '.join(self.tricks)}."]
        if self.owner is not None:
            desc.append(f"{self.name.capitalize()}'s owner is {self.owner}.")

        return ' '.join(desc)
