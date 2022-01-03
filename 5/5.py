"""
5. Створіть за допомогою класів та продемонструйте свою реалізацію шкільної бібліотеки(включіть фантазію).
"""
from librare_book import Librare


def menu():
    while True:
        try:
            print("<-------------------------------------------->")
            print("<< you went to the library >>\n"
                  "<< the library consists of 50 books >>\n")
            in_put = input("1. book search.\n"
                           "2. add book to library.\n"
                           "3. exit\n"
                           "make a choice -> ")
            print("<-------------------------------------------->")
            lib_book = Librare()
            if in_put == "1":
                print("<-------------------------------------------->")
                print("<< you can find your book by <<author>> by <<book title>> and <<year of publication>> >>")
                print("<<SEARCH FOR PRIZVODITS ON KIRILLITS EXAMPLE (author -> Николай Гоголь )\n"
                      "(book title -> Мёртвые души)>>")
                print("<-------------------------------------------->")
                if input("if you know the author press y/n -> ").lower() in ("y", "н"):
                    in_author = input("enter author -> ")
                    lib_book.get_book_search(author=in_author or None)
                if input("if you know the book title press y/n -> ").lower() in ("y", "н"):
                    in_name_book = input("enter book title -> ")
                    lib_book.get_book_search(name_book=in_name_book or None)
                if input("if you know the year of publication press y/n -> ").lower() in ("y", "н"):
                    in_year_book = input("enter year of publication -> ")
                    lib_book.get_book_search(year_book=in_year_book or None)
                if input("want to borrow a book from the library y/n -> ").lower() in ("y", "н"):
                    in_giv_author = input("author -> ")
                    in_giv_book_title = input("book title -> ")
                    in_giv_number_of_copies = input("number_of_copies -> ")
                    if in_giv_author.isalpha() and in_giv_book_title.isalpha() and (in_giv_number_of_copies == int):
                        lib_book.give_book_from_library(author=in_giv_author,
                                                        name_book=in_giv_book_title,
                                                        number_of_copies=int(in_giv_number_of_copies))
                    else:
                        print("<< entering an invalid value >>")

                print("<---------------------------------------------->")
            if in_put == "2":
                print("<< add book to library >>")
                in_add_author = input("add author -> ")
                in_add_book_title = input("add book title -> ")
                in_add_year = input("add year of publication -> ")
                in_add_number_of_copies = input("add number_of_copies -> ")
                if in_add_author.isalpha() and in_add_book_title.isalpha() and in_add_year.isalpha() and (
                        in_add_number_of_copies == int):
                    lib_book.add_book_to_library(author=in_add_author,
                                                 name_book=in_add_book_title,
                                                 year_book=in_add_year,
                                                 number_of_copies=int(in_add_number_of_copies))
                    lib_book.get_book_search()
                else:
                    print("<< entering an invalid value >>")
            elif in_put == "3":
                exit()

        except Exception as err:
            print(f"<< error -> {err} >>")


if __name__ in "__main__":
    menu()
