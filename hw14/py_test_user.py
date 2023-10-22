"""📌 На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень)
📌 Напишите 3-7 тестов pytest (или unittest на ваш выбор) для данного проекта
📌 ОБЯЗАТЕЛЬНО! Используйте фикстуры
"""

import pytest
from hw14.project_users import *
from hw14.user_errors import *


@pytest.fixture
def Mommy():
    Mommy = User("Mommy", "10", "5")
    return Mommy


@pytest.fixture
def Real_user():
    Real_user = User("Petrov", "1", "5")
    return Real_user


def test_InvalidNameError(Mommy):
    with pytest.raises(InvalidNameError):
        Mommy.name = ''


def test_InvalidIdError(Mommy):
    with pytest.raises(InvalidIdError):
        Mommy.user_id = 'fsdf'


def test_InvalidLevelError(Mommy):
    with pytest.raises(InvalidLevelError):
        Mommy.level = '-5'


def test_LevelError(Real_user):
    new_name = "Dad"
    new_level = '7'
    test = UserWorkshop()
    test.current_user = Real_user
    with pytest.raises(LevelError) as info:
        test.create_user(new_name, new_level)
    assert info.type is LevelError


def test_AccessError(Mommy):

    with pytest.raises(AccessError):
        test = UserWorkshop()
        test.login(Mommy.name, Mommy.user_id)


def test_Access(Real_user):
        test = UserWorkshop()
        assert test.login(Real_user.name, Real_user.user_id) == '5'


def test_CreateUser(Real_user):
    test = UserWorkshop()

    test.login(Real_user.name, Real_user.user_id)
    assert test.create_user("Dad", '2') == '2'


def test_Check_level(Mommy):
    assert Mommy.level == '5'


def test_Check_Id(Mommy):
    assert Mommy.user_id == '10'


if __name__ == '__main__':
    pytest.main(['-v'])


def run():
    pytest.main(['-v'])
