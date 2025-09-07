from users import User


class Employee(User):

    def __init__(self, name, email, position, id):
        super().__init__(name, email)
        self.position = position
        self.id = id

    def __str__(self):
        base = super().__str__()
        return f"{base} - {self.position}, id: {self.id}"

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "position": self.position,
            "id": self.id
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data["name"],
            email=data["email"],
            position=data["position"],
            id=data["id"]
        )
