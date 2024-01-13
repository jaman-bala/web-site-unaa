from sqladmin import ModelView

from auth.models import User
from news.models import News
from informations.models import Information


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.email, User.username, User.is_active]
    column_details_exclude_list = [User.hashed_password]
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"
    category = "Сотрудники"


class NewsAdmin(ModelView, model=News):
    column_list = [News.id, News.title, News.publication_date]
    name = "Новости"
    name_plural = "Новости"
    icon = "fa-solid fa-newspaper"
    category = "Новости"


class InformationAdmin(ModelView, model=Information):
    column_list = [Information.id, Information.paragraph, Information.title, Information.money]
    name = "Информация"
    name_plural = "Информация"
    icon = "fa-solid fa-info-circle"
    category = "Информация"