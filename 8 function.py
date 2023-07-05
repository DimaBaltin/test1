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

def get_name (f_name,l_name):
    full_name=f"{f_name} {l_name}"
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("enter 'q' at any time to quit")
    fir_name=input("First name:")
    if fir_name =='q':
        break
    sec_name=input("Second name:")
    if sec_name =='q':
        break
    formatted_name=get_name(fir_name,sec_name)
    print(f"\nHello,{formatted_name}")