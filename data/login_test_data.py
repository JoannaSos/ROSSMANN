from utils.xlsx_reader import Reader


class Credentials:

    def __init__(self, file_name):
        data = Reader.readXlsxFile(file_name)

        for row in data.values:
            test_type, username, password = row[0], row[1], row[2]

            if test_type == "valid":
                self.valid = Data(username, password)
            elif test_type == "too_short_password":
                self.tooShortPassword = Data(username, password)
            elif test_type == "not_existing_login":
                self.notExistingLogin = Data(username, password)
            elif test_type == "too_long_login":
                self.tooLongLogin = Data(username, password)
            elif test_type == "empty_login":
                self.emptyLogin = Data(username, password)
            elif test_type == "empty_login_and_password":
                self.emptyLoginPassword = Data(username, password)


class Data:
    def __init__(self, username, password):
        self.username = username
        self.password = password
