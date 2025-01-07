def all_variants(text):
    if not text:
        yield ""
    else:
        for i in all_variants(text[1:]):
            yield i
            yield text[0] + i


a = all_variants("abc")
for i in a:
    print(i)