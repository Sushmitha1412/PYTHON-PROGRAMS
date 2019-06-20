def cstolot(cs):
    return [ tuple(i.split("=")) for i in cs.split(";")]
def cstodict(cs):
    D=dict(cstolot(cs))
    return D
