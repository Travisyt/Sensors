
def fileo(name, contains):
    file = open(name, "w")
    file.truncate()
    file.write(contains)
    file.close()