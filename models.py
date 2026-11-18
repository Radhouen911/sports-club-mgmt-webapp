from dataclasses import dataclass


@dataclass
class Member:
    id: int
    last_name: str
    first_name: str
    age: int
    phone: str

    @classmethod
    def from_row(cls, row):
        return cls(
            id=row["id"],
            last_name=row["last_name"],
            first_name=row["first_name"],
            age=row["age"],
            phone=row["phone"],
        )


@dataclass
class Activity:
    code: str
    name: str
    monthly_fee: float
    capacity: int

    @classmethod
    def from_row(cls, row):
        return cls(
            code=row["code"],
            name=row["name"],
            monthly_fee=row["monthly_fee"],
            capacity=row["capacity"],
        )


@dataclass
class Registration:
    member_id: int
    activity_code: str
    date: str

    @classmethod
    def from_row(cls, row):
        return cls(
            member_id=row["member_id"],
            activity_code=row["activity_code"],
            date=row["date"],
        )
