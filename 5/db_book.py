import sqlite3 as database


class Database(object):
    def __init__(self):
        self.db_dump = database.connect("librare_book.db")

    def get_database(self):
        return self.db_dump

    def close_database(self):
        self.db_dump.close()

    def set_database_insert_book(self, author: str = None, name_book: str = None, year_book: str = None, number_of_copies: int = 0):
        cur = self.db_dump.cursor()
        cur.execute(
            f"INSERT INTO list_book_db ('author','name_book','year','number_of_copies') VALUES (?,?,?,?)",
            (author, name_book, year_book, number_of_copies))
        self.db_dump.commit()

    def set_database_update_existed_book(self, author: str = None, name_book: str = None, number_of_copies: int = 0, opearation_flag: str = "add"):
        book_amount_diff: int = 0
        number_of_copy_tmp: int = 0

        if number_of_copies != 0 and number_of_copies > 0:
            cur = self.db_dump.cursor()
            cur.execute(f"SELECT * FROM list_book_db WHERE name_book LIKE \"%{name_book}%\"")
            rows = cur.fetchall()
            for row in rows:
                number_of_copy_tmp = int(row[4])

            if opearation_flag == "rem":
                if number_of_copy_tmp == 0:
                    print(f"No book available: {number_of_copy_tmp}")
                elif number_of_copies > number_of_copy_tmp:
                    print(f"Sorry, we cant give you requested {number_of_copies} amount of books, because available {number_of_copy_tmp}")
                elif number_of_copy_tmp > number_of_copies:
                    book_amount_diff = int(number_of_copy_tmp) - int(number_of_copies)

                    cur.execute(
                        f"UPDATE list_book_db SET number_of_copies = {book_amount_diff} "
                        f"WHERE name_book = \"{name_book}\" AND author = \"{author}\"")
                    self.db_dump.commit()
                else:
                    print("Unknown issue")

            elif opearation_flag == "add":
                book_amount_diff = int(number_of_copy_tmp) + int(number_of_copies)

                cur.execute(
                    f"UPDATE list_book_db SET number_of_copies = {book_amount_diff} "
                    f"WHERE name_book = \"{name_book}\" AND author = \"{author}\"")
                self.db_dump.commit()
        else:
            print(f"Incorrect amount: {number_of_copies}")

    def set_database_delete_book(self, author: str = None, name_book: str = None, number_of_copies: int = 0):
        cur = self.db_dump.cursor()
        cur.execute(
            f"DELETE FROM list_book_db WHERE name_book = \"{name_book}\" AND author = \"{author}\"")
        self.db_dump.commit()

    def get_database_search_book_by_author(self, author: str = None):
        temp_db_list: list = []
        if author is not None:
            cur = self.db_dump.cursor()
            cur.execute(f"SELECT * FROM list_book_db WHERE author LIKE \"{author}\"")
            cursor = cur.fetchall()
            for data in cursor:
                temp_db_list.append(data)
            self.db_dump.commit()
            return temp_db_list
        else:
            print(f"Incorrect request by author: {author}")
            return None

    def get_database_search_book_by_name(self, name: str = None):
        temp_db_list: list = []
        if name is not None:
            cur = self.db_dump.cursor()
            cur.execute(f"SELECT * FROM list_book_db WHERE name_book LIKE \"{name}\"")
            cursor = cur.fetchall()
            for data in cursor:
                temp_db_list.append(data)
            self.db_dump.commit()
            return temp_db_list
        else:
            print(f"Incorrect request by book name: {name}")
            return None

    def get_database_search_book_by_id(self, id_book: int = None):
        temp_db_list: list = []
        if id_book != 0 or id_book is not None:
            cur = self.db_dump.cursor()
            cur.execute(f"SELECT * FROM list_book_db WHERE id LIKE {id_book}")
            cursor = cur.fetchall()
            for data in cursor:
                temp_db_list.append(data[0])
                temp_db_list.append(data[1])
                temp_db_list.append(data[2])
                temp_db_list.append(data[3])
                temp_db_list.append(data[4])
            self.db_dump.commit()
            return temp_db_list
        else:
            return None

    def get_book_list(self):
        cur = self.db_dump.cursor()
        cur.execute(f"SELECT id, author, name_book, year, number_of_copies FROM list_book_db")
        list_book_db: list = []
        result = cur.fetchall()
        for item in result:
            id_book, author, name_book, year_book, number_of_copies = item
            list_book_db.append({'id': id_book,
                      'author': author,
                      'name_book': name_book,
                      'year': year_book,
                      'number_of_copies': number_of_copies})

        return list_book_db

