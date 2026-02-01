class RBUser:
    def __init__(self, student_id: int | None = None,
                 employer_id: int | None = None,
                 ):
        self.student_id = student_id
        self.employer_id = employer_id


    def to_dict(self) -> dict:
        data = {'student_id': self.student_id, 'employer_id': self.employer_id}
        # Создаем копию словаря, чтобы избежать изменения словаря во время итерации
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data

class RBToken:
    def __init__(self, token: str | None = None):
        self.token = token

    def to_dict(self) -> dict:
        data = {'token': self.token}
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data