def mapToInt(bits):
    result = 0
    power = len(bits) - 1  # El bit de mayor valor tiene el mayor exponente
    for bit in bits:
        result += bit * (2 ** power)
        power -= 1
    return result

def get_score_plato_ppal(plato_ppal,f_cal):
    calorias = mapToInt(plato_ppal[:2]) + 1
    gusto = mapToInt(plato_ppal[2:])


    score_calorias = (4-calorias) * 25
    score_gusto = gusto * calorias * 100/124
    score = score_calorias * f_cal + score_gusto * (1-f_cal)
    return score

def get_score_bebida_acom(plato_ppal,f_cal):
    calorias = mapToInt(plato_ppal[:2]) + 1
    gusto = mapToInt(plato_ppal[2:])

    score_calorias = (4-calorias)
    score_gusto = (gusto + calorias)

    score = (score_calorias * f_cal + score_gusto * (1-f_cal)) * 25
    return score