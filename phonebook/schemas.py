from curses.ascii import isdigit
from multiprocessing import Value
from pydantic import BaseModel, FieldValidationInfo, field_validator
from pydantic_extra_types.phone_numbers import PhoneNumber
from phonebook.constants import FILENAME


class UserInfo(BaseModel):
    last_name: str
    first_name: str
    middle_name: str
    organization: str
    work_phone: PhoneNumber
    personal_phone: PhoneNumber

    @field_validator("last_name", "first_name", "middle_name", "organization")
    @classmethod
    def check_non_int_fields(cls, v: str, info: FieldValidationInfo) -> str:
        if v.isdigit():
            raise ValueError(f"{info.field_name} должен иметь только строчные данные.")
        return v
