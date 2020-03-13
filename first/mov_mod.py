
#nested list
movies = ["Black Widow",2020,"Scarlett Johansson","Florence Pugh",["David Harbour","Rachel Weisz","William Hurt",["Cate Shortland","Stan Lee"]]]


def marvel(the_actors):
    for actors in the_actors:
        if isinstance(actors,list):
            marvel(actors)
        else:
            print(actors)