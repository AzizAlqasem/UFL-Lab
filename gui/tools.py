


def to_latex(text, x, round_digits=4, scientific_notation=False):
    if scientific_notation:
        res =  "%.*e" % (round_digits, x)
    else:
        res = "%.*f" % (round_digits, x)
    return f"\text{text} = {res}"
