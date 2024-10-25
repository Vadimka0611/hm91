def popular_words (text, words):

    text = text.lower()
    update_split = text.split()

    slovar = dict()
    for word in words:
        slovar[word] = update_split.count(word)

    return slovar

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')

