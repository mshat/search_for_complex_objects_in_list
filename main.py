class User:
    def __init__(self, name, age, sex, country):
        self._name = name
        self._age = age
        self._sex = sex
        self._country = country

    def match(self, **kwargs):
        return all(getattr(self, key) == val for (key, val) in kwargs.items())

    def __repr__(self):
        return f'{self._name} {self._age} {self._country}'


class UsersStorage:
    def __init__(self, users: list):
        self.__users = users

    def find_all(self, **kwargs):
        return list(self.__iter_person(**kwargs))

    def find_first(self, **kwargs):
        return next(self.__iter_person(**kwargs))

    def __iter_person(self, **kwargs):
        return (user for user in self.__users if user.match(**kwargs))


if __name__ == '__main__':
    users = [
        User('Ivan', 11, 'male', 'Russia'),
        User('Ivan', 10, 'male', 'Russia'),
        User('Lisa', 18, 'female', 'Poland'),
        User('Lisa', 5, 'female', 'Poland'),
        User('Petr', 49, 'male', 'Ukraine'),
        User('Petr', 11, 'male', 'Poland'),
        User('Max', 21, 'male', 'Uzbekistan'),
        User('Ann', 25, 'female', 'USA'),
        User('Ann', 49, 'female', 'Ukraine'),
        User('Ann', 5, 'female', 'Belarus'),
        User('Uvuvwevwevwe Onyetenyevwe Ugwemuhwem Osas', 25, 'male', 'Kenya'),
    ]

    users_store = UsersStorage(users)
    print('All users:', users_store.find_all())
    print('All users named Ann:', users_store.find_all(_name='Ann'))
    print('All Ivans from Russia:', users_store.find_all(_name='Ivan', _country='Russia'))
    print('Country: Ukraine, age: 49:', users_store.find_all(_country='Ukraine', _age=49))

    print('First Max in list:', users_store.find_first(_name='Max'))
    print('First person from Kenya:', users_store.find_first(_country='Kenya'))

