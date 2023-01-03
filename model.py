import pydantic as pd
from typing import List


class UserData(pd.BaseModel):
    name: str
    age: int


class UsersInfo(pd.BaseModel):

    all_users: List[UserData]

    def get_user(self, user_name: str) -> UserData:
        for i in self.all_users:
            if i.name == user_name:
                return i
        raise KeyError(user_name)

    def delet_user(self, user_name: str) -> None:
        for i in self.all_users:
            if i.name == user_name:
                del i
        raise KeyError(user_name)

    def add_user(self, user_name: str, user_age: int) -> None:
        self.all_users.append(UserData(name=user_name, age=user_age))
