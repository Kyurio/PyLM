from fastapi import APIRouter, HTTPException, Request
from app.model.Usuario import Usuarios
from app.schemas.SchemaUsuario import UsuarioResponseModel

router = APIRouter()

<<<<<<< HEAD
@router.put("/UpdateUsuario/")
def actualizar_usuario(request: UsuarioResponseModel):
    try:
=======
>>>>>>> 6edb1d30b1d5325946486eec57836059d7461449

@router.put("/UpdateUsuario/{usuario_id}")
async def actualizar_usuario(id: int, usuario_request: UsuarioCreateModel, request: Request):
    try:
        usuario_data = usuario_request.dict()

        datos = await request.json()

        usuario_data.update(datos)

        success = Usuarios.update(id, **usuario_data)

        if success:
            return {"message": "Usuario actualizado exitosamente"}
        else:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar el Usuario: {str(e)}")
