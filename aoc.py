def file_reader(name):
    with open(f"{name}.in") as f:
        text = f.readlines()
    return [x.strip() for x in text]