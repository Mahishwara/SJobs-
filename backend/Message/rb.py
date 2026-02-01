class RBMessage:
    def __init__(self, id: int | None = None,
                 id_student: str | None = None,
                 id_vacancy: str | None = None,
                 path_type: int | None = None):
        self.id = id
        self.id_student = id_student
        self.id_vacancy = id_vacancy
        self.path_type = path_type


    def to_dict(self) -> dict:
        data = {'id': self.id,
                'id_student': self.id_student,
                'id_vacancy': self.id_vacancy,
                'path_type': self.path_type,}
        # Создаем копию словаря, чтобы избежать изменения словаря во время итерации
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data