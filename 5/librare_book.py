from db_book import Database


class Librare(object):

    def __init__(self):
        db = Database()
        self.__list_book = db.get_book_list()
        self.__db_dump = db.get_database()
        self.__db_update_book = db.set_database_update_existed_book
        self.__db_search_book_by_name = db.get_database_search_book_by_name
        self.__db_inset_book = db.set_database_insert_book
        self.__db_remove_book = db.set_database_delete_book

    def __get_is_book_exist(self, author: str = None, name_book: str = None, year_book: str = None):
        for i in self.__list_book:
            if (not author or author == i.get("author")) and \
                    (not name_book or i.get("name_book").startswith(name_book)) and \
                    (not year_book or year_book == i.get("year")):

                return True
            else:
                return False

    def get_book_search(self, author: str = None, name_book: str = None,
                        year_book: str = None):
        for i in self.__list_book:
            if (not author or author.title() == i.get("author")) and \
                    (not name_book or i.get("name_book").startswith(name_book)) and \
                    (not year_book or year_book == i.get("year")):
                print("*" * 50)
                print(f'id book -> {i.get("id")}\n'
                      f'author -> {i.get("author")}\n'
                      f'name book -> {i.get("name_book")}\n'
                      f'year -> {i.get("year")}\n'
                      f'number_of_copies -> {i.get("number_of_copies")}')
                print("*" * 50)

    def add_book_to_library(self, author: str = None, name_book: str = None, year_book: str = None,
                            number_of_copies: int = 1):
        lib_book = self.__db_dump
        book_already_exist = self.__get_is_book_exist(author=author, name_book=name_book)
        if book_already_exist:
            self.__db_update_book(author, name_book, number_of_copies, "add")
        else:
            self.__db_inset_book(author, name_book, year_book, number_of_copies)

    def give_book_from_library(self, author: str = None, name_book: str = None, number_of_copies: int = 1):
        lib_book = self.__db_dump
        book_already_exist = self.__get_is_book_exist(author=author, name_book=name_book)

        if book_already_exist:
            self.__db_update_book(author, name_book, number_of_copies, "rem")
        else:
            print(f"We don't have book with current name: {name_book} of author {author}")


# l = Librare()
# l.get_book_search()
# # l.get_book_search(name_book=u"Собачье сердце")
# l.get_book_search(author=u'Николай Гоголь')
# # l.add_book_to_library(author=u'Николай Гоголь', name_book=u'Мёртвые души', number_of_copies=10)
# # l.give_book_from_library(author=u'Николай Гоголь', name_book=u'Мёртвые души', number_of_copies=8)
# #l.get_book_search(name_book=u'Мёртвые души')
