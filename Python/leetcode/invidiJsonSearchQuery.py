def search():
    # list of dicts of movies
    matches =()
    data = self._data['items']
    tag = self.query_tag
    # iterate the list of dicts of movies and append to matches
    for i in range(len(data)):
        curr_movie = data[i]
        if tag in curr_movie['tags']:
            matches = matches + (curr_movie,)

    for i in range(len(matches)):
        yield(matches[i])

def first():
    # need to call search and return the first item
    gen = self.search()
    return next(gen)

