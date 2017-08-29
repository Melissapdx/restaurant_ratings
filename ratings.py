"""Restaurant rating lister."""

restaurants = open("scores.txt")
# put your code here
name = raw_input("Restaurant name: ")
while True:
    score = int(raw_input("Restaurant score: "))
    if score < 0 or score >= 5:
        print "Please enter in a number between 1 and 5: "
    else:
        break


def rating_lister(restaurants):
    ratings = {}
    ratings[name] = score
    for line in restaurants:
        remove = line.rstrip()
        line = remove.split(":")
        for k in line:
            ratings[line[0]] = line[-1]

    for place in sorted(ratings):
        print place, ratings[place]

rating_lister(restaurants)
