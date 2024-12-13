import os



def Static(file):
    """STATIC FOR MOJIZA FRAMEWORK """

    is_exits = os.path.exists(file)

    if is_exits == False:
        os.mkdir(file)
    else:
        return f"{str(os.getcwd())}/{file}"
