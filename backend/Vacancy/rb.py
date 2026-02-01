from datetime import date, datetime


class RBVacancy():
    def __init__(self, id: int | None = None,
                 name: str | None = None,
                 description: str | None = None,
                 publication_date: datetime | None = None,
                 date_begin: date | None = None,
                 date_end: date | None = None,
                 level_skill: int | None = None,
                 salary: str | None = None,
                 id_employer: int | None = None,
                 is_active: bool | None = None):
        self.id = id
        self.name = name
        self.description = description
        self.publication_date = publication_date
        self.date_begin = date_begin
        self.date_end = date_end
        self.level_skill = level_skill
        self.salary = salary
        self.is_active = is_active



    def to_dict(self) -> dict:
        data = {'id': self.id,
                'name': self.name,
                'description': self.description,
                'publication_date': self.publication_date,
                'date_begin': self.date_begin,
                'date_end': self.date_end,
                'level_skill': self.level_skill,
                'salary': self.salary,
                'is_active': self.is_active}
        # Создаем копию словаря, чтобы избежать изменения словаря во время итерации
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data