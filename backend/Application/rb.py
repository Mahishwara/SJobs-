class RBSjobs.backend.lication():
    def __init__(self, id: int | None = None,
                 id_student: int | None = None,
                 id_vacancy: int | None = None,
                 date: str | None = None,
                 status: int | None = None,):
        self.id = id
        self.id_student = id_student
        self.id_vacancy = id_vacancy
        self.date = date
        self.status = status



    def to_dict(self) -> dict:
        data = {'id': self.id,
                'id_student': self.id_student,
                'id_vacancy': self.id_vacancy,
                'date': self.date,
                'status': self.status}
        # Создаем копию словаря, чтобы избежать изменения словаря во время итерации
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data