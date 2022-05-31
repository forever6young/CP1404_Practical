import wikipedia

search_title = input("Title:")

while search_title != "":
    wikipedia.search(search_title)
    for line in wikipedia.search(search_title):
        print(line[1])


wikipedia.search("Barack")

wikipedia.suggest("Barak Obama")

ny = wikipedia.page("New York")

wikipedia.set_lang("fr")

print wikipedia.summary("Francois Hollande")

