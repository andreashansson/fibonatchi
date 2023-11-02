import json

class WrongInputError(Exception):
    pass

class Fibonatchi:
    def __init__(self, skipped_file):
        self.skipped_file = skipped_file

    def get_fib_val_by_fib_pos(self, fib_pos):
        skipped_vals = get_skipped(self.skipped_file)

        if fib_pos in skipped_vals:
            return {fib_pos: "skipped"}

        all_fib_values = create_fibonatchi_values(fib_pos)
        return {fib_pos: all_fib_values[fib_pos]}

    def get_fib_vals_up_to_fib_pos(self, fib_pos):
        skipped_vals = get_skipped(self.skipped_file)
        res = create_fibonatchi_values(fib_pos)
        for skipped_val in skipped_vals:
            if int(skipped_val) > int(fib_pos):
                continue
            del res[skipped_val]

        return res

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


def get_skipped(file_path):
    with open(file_path, "r") as json_file:
        data = json.load(json_file)

    return data


def add_skipped(val, file_path):
    try:
        int(val)
    except ValueError:
        raise WrongInputError("must be a number")

    data = set(get_skipped(file_path))
    data.add(val)
    data = list(data)
    write_json(file_path, data)


def write_json(file_path, data):
    with open(file_path, "w") as json_file:
        json.dump(data, json_file)
