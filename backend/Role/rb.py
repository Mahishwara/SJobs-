class RBRole:
    def __init__(self, id: int | None = None,
                 role_name: str | None = None,
                 role_type: str | None = None,
                 description: str | None = None):
        self.id = id
        self.role_name = role_name
        self.role_type = role_type
        self.description = description

    def to_dict(self) -> dict:
        data = {
            'id': self.id,
            'role_name': self.role_name,
            'role_type': self.role_type,
            'description': self.description,
        }
        # Создаем копию словаря, чтобы избежать изменения словаря во время итерации
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data
