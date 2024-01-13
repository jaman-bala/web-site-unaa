from fastapi import FastAPI
from sqladmin import Admin

from auth.base_config import auth_backend, fastapi_users
from auth.schemas import UserRead, UserCreate

from informations.router import router as router_information
from news.router import router as news_router
from database import engine
from admin.views import UserAdmin, NewsAdmin, InformationAdmin

app = FastAPI(
    title="Унаа сайт"
)


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    news_router,
    prefix="/news",
    tags=["News"]
)

app.include_router(
    router_information,
    prefix="/informations",
    tags=["Information"],
)


admin = Admin(app, engine)

admin.add_view(UserAdmin)
admin.add_view(NewsAdmin)
admin.add_view(InformationAdmin)


