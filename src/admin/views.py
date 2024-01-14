from sqladmin import ModelView, BaseView

from auth.models import User
from news.models import News
from informations.models import Information


class UserAdmin(ModelView, BaseView, model=User):
    def date_format(value):
        return value.strftime("%d.%m.%Y")

    form_columns = "__all__" # Можно сделать чтоб форма открывалось User.username

    column_list = [
        User.id,
        User.email,
        User.username,
        User.role_id,
        User.is_active
    ]
    column_searchable_list = [User.email, User.username]
    column_sortable_list = [User.id]

    column_labels = {
        User.email: "Email",
        User.username: "Пользователь",
        User.role_id: "Роль",
        User.is_active: "Активный"
    }
    column_details_exclude_list = [User.hashed_password]

    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"
    category = "Сотрудники"


class NewsAdmin(ModelView, model=News):
    def date_format(value):
        return value.strftime("%d.%m.%Y")

    column_list = [
        News.id,
        News.title,
        News.img,
        News.file,
        News.publication_date
    ]
    column_searchable_list = [News.title]
    column_labels = {
        News.title: "Наименование",
        News.img: "Изображение",
        News.file: "Файл",
        News.publication_date: "Дата публикации",
        News.description: "Описание"
    }

    name = "Новости"
    name_plural = "Новости"
    icon = "fa-solid fa-newspaper"
    category = "Новости"

    can_create = True
    can_edit = True
    can_delete = False
    can_view_details = True


class InformationAdmin(ModelView, model=Information):

    column_list = "__all__"
    name = "Информация"
    name_plural = "Информация"
    icon = "fa-solid fa-info-circle"
    category = "Информация"

    can_create = True
    can_edit = True
    can_delete = False
    can_view_details = True