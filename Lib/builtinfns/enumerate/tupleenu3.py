# enumerate items in tuple

txt=[(15,'apple'),(16,'orange'),(20,'kiwi')]

for i,(price,fruit) in enumerate(txt):
    print(f" index {i},{fruit} cost is {price}")
    