from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# routers
from router import RouterPerfil
from router import RouterUsuario
from router import RouterConcepto
from router import RouterAuth
from router import RouterConcatenado
from router import RouterMovimiento
from router import RouterParametro
from router import RouterPlanMovimiento
from router import RouterHistorial
from router import RouterSecuencia

app = FastAPI()

# Agrega middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# router secuencia
app.include_router(RouterSecuencia.GetSecuencia.router)
app.include_router(RouterSecuencia.DeleteSecuencia.router)
app.include_router(RouterSecuencia.UpdateSecuencia.router)
app.include_router(RouterSecuencia.PostSecuencia.router)

# router perfil
app.include_router(RouterPerfil.PostPerfil.router)
app.include_router(RouterPerfil.UpdatePerfil.router)
app.include_router(RouterPerfil.DeletePerfil.router)
app.include_router(RouterPerfil.GetPerfiles.router)

# router usuario
app.include_router(RouterUsuario.UpdateUsuarios.router)
app.include_router(RouterUsuario.PostUsuario.router)
app.include_router(RouterUsuario.GetUsuarios.router)
app.include_router(RouterUsuario.DeleteUsuario.router)

# router Concepto
app.include_router(RouterConcepto.GetConcepto.router)
app.include_router(RouterConcepto.PostConcepto.router)
app.include_router(RouterConcepto.UpdateConcepto.router)
app.include_router(RouterConcepto.GetConcepto.router)

# router Concatenado
app.include_router(RouterConcatenado.DeleteConcatenado.router)
app.include_router(RouterConcatenado.GetConcatenado.router)
app.include_router(RouterConcatenado.UpdateConcatenado.router)
app.include_router(RouterConcatenado.PostConcatenado.router)

# router movimiento
app.include_router(RouterMovimiento.DeleteMovimiento.router)
app.include_router(RouterMovimiento.UpdateMovimiento.router)
app.include_router(RouterMovimiento.PostMovimiento.router)
app.include_router(RouterMovimiento.GetMovimiento.router)

# router parametros
app.include_router(RouterParametro.DeleteParametro.router)
app.include_router(RouterParametro.UpdateParametro.router)
app.include_router(RouterParametro.PostParametro.router)
app.include_router(RouterParametro.GetParametro.router)

# router plan movimiento
app.include_router(RouterPlanMovimiento.PostPlanMovimiento.router)
app.include_router(RouterPlanMovimiento.GetPlanMovimiento.router)
app.include_router(RouterPlanMovimiento.DeletePlanMovimineto.router)
app.include_router(RouterPlanMovimiento.UpdatePlanMovimiento.router)

# router historial
app.include_router(RouterHistorial.GetHistorial.router)
app.include_router(RouterHistorial.PostHistorial.router)

# router auth
app.include_router(RouterAuth.Login.router)
