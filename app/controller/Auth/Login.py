from fastapi import APIRouter
from app.model.Auth import Auth
from app.schemas.SchemaAuth import UserCredentials

router = APIRouter()
@router.post("/login/")
def login(user_credentials: UserCredentials):

    authenticated_user = Auth.authenticate(user_credentials.username, user_credentials.password)

    if not authenticated_user:
        return "false"
    return "true"

