


def to_latex(text, x, round_digits=4, unit=None, scientific_notation=False):
    if scientific_notation:
        res =  "%.*e" % (round_digits, x)
    else:
        res = "%.*f" % (round_digits, x)
    if unit is not None:
        res += " " + unit
    return r"\text{" + text + "} = " + res
