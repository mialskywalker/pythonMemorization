class DVD:
    MONTHS = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    def __repr__(self):
        result = f"{self.id}: {self.name} ({self.creation_month} {self.creation_year})" \
                 f" has age restriction {self.age_restriction}. "
        if not self.is_rented:
            result += f"Status: not rented"
        else:
            result += f"Status: rented"
        return result

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):

        month = DVD.MONTHS[int(date[3:5])]

        year = int(date[6::])
        return cls(name, id, year, month, age_restriction)
