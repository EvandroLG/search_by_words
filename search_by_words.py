import re

def search_by_words(text, *keywords):
    sentences = re.split('\w+\.[\s|\n]', text)
    result = []

    for sentence in sentences:
        is_valid = any(re.search('%s%s' % (word, '(\s|\.|\`|s)'), sentence, flags=re.IGNORECASE)\
                   for word in keywords)

        if is_valid: 
            result.append(sentence.strip())

    return result
