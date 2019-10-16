chemical_property = {
    'A': [1, 1, 1],
    'C': [0, 1, 0],
    'G': [1, 0, 0],
    'T': [0, 0, 1],
    'U': [0, 0, 1],
    '-': [0, 0, 0],
}
import numpy as np
def NCP(fastas, **kw):

    AA = 'ACGT'
    encodings = []

    for i in fastas:
        sequence = i.strip()
        code = []
        for aa in sequence:
            code = code + chemical_property.get(aa, [0, 0, 0])
        encodings.append(code)
    np.savetxt("ncp", encodings)
    return np.array(encodings)