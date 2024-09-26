from fastapi import FastAPI
from quantiles import generate_problem

app = FastAPI()



@app.get("/")
def generate_quantile_problem():
    return generate_problem()
