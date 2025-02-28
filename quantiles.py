from random import randint
from random import sample

class Quantile():
    def __init__(self, name, symbol, inf, sup) -> None:
        self.name = name
        self.symbol = symbol
        self.inf = inf
        self.sup = sup

def generate_quantile(data):
    quantiles = ['cuartil', 'decil', 'percentil']
    possible_quantiles = [quantiles[i] for i, j in enumerate(data) if j]
    
    seed = randint(0, len(possible_quantiles)-1)
    if possible_quantiles[seed] == "cuartil":
        return Quantile("cuartil", "Q", 1, 3)
    elif possible_quantiles[seed] == "decil":
        return Quantile("decil", "D", 1, 9)
    else:
        return Quantile("percentil", "P", 1, 99)
    
def generate_question(quantile):
    num = randint(quantile.inf, quantile.sup)
    return f"Una interpretación del {quantile.name} {num} es...", num

def generate_good_answer(quantile, num):
    n = randint(0, 3)
    left = 100//(quantile.sup+1)*num
    right = 100 - left

    if n == 0:
        return f"El {quantile.name} {num} es mayor o igual que al menos el {left}% de los datos."
    elif n == 1:
        return f"El {quantile.name} {num} es menor o igual que al menos el {right}% de los datos."
    elif n == 2:
        return f"Al menos el {left}% de los datos son menores o iguales al {quantile.name} {num}."
    else:
        return f"Al menos el {right}% de los datos son mayores o iguales al {quantile.name} {num}."
    
def generate_others_answers(quantile, num):
    left = 100//(quantile.sup+1)*num
    right = 100 - left

    if left == right:
        left = 100//(quantile.sup+1)*(num//2)
        right = 100 - left
    
    responses = [
        f"El {quantile.name} {num} es menor o igual que al menos el {left}% de los datos.",
        f"El {quantile.name} {num} es mayor o igual que al menos el {right}% de los datos.",
        f"Al menos el {left}% de los datos son mayores o iguales al {quantile.name} {num}.",
        f"Al menos el {right}% de los datos son menores o iguales al {quantile.name} {num}."
    ]

    return sample(responses, 3)

def generate_problem(data):
    quantile = generate_quantile(data)
    question, num = generate_question(quantile)
    good_answer = generate_good_answer(quantile, num)
    others_answers = generate_others_answers(quantile, num)
    others_answers.append(good_answer)

    return {"question":question, "answer":good_answer, "others":sample(others_answers, 4)}

