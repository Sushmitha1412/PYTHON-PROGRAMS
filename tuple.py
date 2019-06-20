def cstolot(cs):
    return [ tuple(i.split("=")) for i in cs.split(";")]
