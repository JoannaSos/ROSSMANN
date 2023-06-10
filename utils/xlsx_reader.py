import pandas as pd


class Reader:
    @staticmethod
    def readXlsxFile(file_name):
        df = pd.read_excel(file_name, header=1).fillna("")
        return df

