
def create_fibonatchi_values(position):
    if int(position) <= 0:
        raise WrongInputError("number must be above 0")

    index = 0
    v = {}
    old = 1
    new = 1
    while True:
        index += 1
        if index == 1:
            v["1"] = "0"

            if int(position) == 1:
                return v

            continue

        elif index == 2:
            v["2"] = "1"

            if int(position) == 2:
                return v

            continue

        res = old + new
        v[str(index)] = str(res)
        old = new
        new = res

        if index >= int(position):
            return v
