from fastapi import Depends, HTTPException
from fastapi.responses import HTMLResponse

from sqlalchemy.ext.asyncio import  AsyncSession
from sqlalchemy import select

from .models import User, UserData, Passport
from ..train.models import Train, ticket_to_pass
from ..food.models import Food

from ..database import get_async_session


class UserServices:
    def __init__(self,
                 session: AsyncSession=(Depends(get_async_session))):
        self.session = session
        self.current_user = self.get_user()

    async def _food_refrash(self): pass

    async def get_user(self, user_id): pass

    async def user_create(self): pass