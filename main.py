from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from quantiles import generate_problem

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todos los orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos
    allow_headers=["*"],  # Permitir todos los encabezados
)


@app.get("/")
def generate_quantile_problem(cuartil: bool = Query(None), decil: bool = Query(None), percentil: bool = Query(None)):
    if cuartil or decil or percentil:
        return generate_problem([cuartil, decil, percentil])
    return generate_problem([True, True, True])
