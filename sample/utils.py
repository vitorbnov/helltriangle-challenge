import numpy


def multiarrays_from_multilist(multilist):
    multiarray = numpy.array(multilist)
    for index in range(len(multiarray)):
        multiarray[index] = numpy.array(multilist[index], dtype=numpy.dtype("uint"))
    return multiarray
