def greet_user(username):
    print(f"Hello,{username.title()}")
greet_user('jesse')
greet_user('111jesse')

print(f" ")
def favorite_book(name,author):
    print(f"Favorite book is, {name.title()}")
    print(f"Author book is, {author.title()}")
    full_name=f"{name} {author}"
    return full_name.title()
bookname=favorite_book('book1','name1')
favorite_book('11 minutes', 'Koelio')
favorite_book(name='11 11111minutes', author='Koelio')
print(bookname)
print(bookname)print(bookname)

