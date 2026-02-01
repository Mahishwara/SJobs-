class RBStatus:
    def __init__(self, id: int | None = None,
                 name: str | None = None,
                 description: str | None = None):
        self.id = id
        self.name = name
        self.description = description


    def to_dict(self) -> dict:
        data = {'id': self.id,
                'name': self.name,
                'description': self.description}
        # Создаем копию словаря, чтобы избежать изменения словаря во время итерации
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data