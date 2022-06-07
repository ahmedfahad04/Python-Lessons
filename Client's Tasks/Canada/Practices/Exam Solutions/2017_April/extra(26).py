def buildLibrary(authors, titles):
    library = {}
    for a,t in zip(authors,titles):
        if a not in library.keys():
            library[a] = [t]
        else:
            library[a].append(t)

    return library
