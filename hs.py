import xlsxwriter
import xlrd


class high_score(object):

    def __init__(self):
        self.default_hs = [['aaa', 20000]]
        self.high_scores =[]
        self.load_hs_info()




    def check_score(self, score):
        self.high_scores.append(['bbb', score])
        l = len(self.high_scores)
        for i in range(0, l):
            for j in range(0, l - i - 1):
                if (self.high_scores[j][1] > self.high_scores[j+1][1]):
                    tempo = self.high_scores[j]
                    self.high_scores[j] = self.high_scores[j+1]
                    self.high_scores[j+1] = tempo

        return self.high_scores[0][1]

    def display_hs():

        pass

    def hs_enter_name():
        pass


    def save_hs_info(self):
        #writing to xlsx files - https://xlsxwriter.readthedocs.io/
        l = len(self.high_scores)
        for i in range(0, l):
            for j in range(0, 1-i-1):
                if (self.high_scores[j][1] == 'bbb'):
                    self.high_scores[j][0] = hs_enter_name()


        hs_workbook = xlsxwriter.Workbook('./data/hsdata.xlsx')
        hs_worksheet = hs_workbook.add_worksheet()

        row = 0
        col = 0

        for hs_p, hs in (self.high_scores):
            hs_worksheet.write(row, col, hs_p)
            hs_worksheet.write(row, col + 1, hs)
        hs_workbook.close()



    def load_hs_info(self):
        #reading xlsx files - https://www.geeksforgeeks.org/reading-excel-file-using-python/
        try:
            xlrd_loc = ('./data/hsdata.xlsx')
            xlrd_wb = xlrd.open_workbook(xlrd_loc)
            xlrd_sheet = xlrd_wb.sheet_by_index(0)
            xlrd_sheet.cell_value(0, 0)
        except FileNotFoundError:
            self.high_scores = self.default_hs
            self.save_hs_info()
            self.load_hs_info()
        else:
            pass

        xlrd_loc = ('./data/hsdata.xlsx')
        xlrd_wb = xlrd.open_workbook(xlrd_loc)
        xlrd_sheet = xlrd_wb.sheet_by_index(0)
        xlrd_sheet.cell_value(0,0)

        tot_num_rows = xlrd_sheet.nrows
        tot_num_col = xlrd_sheet.ncols

        for row in range(tot_num_rows):
            self.high_scores.append(xlrd_sheet.row_values(row))

        if self.high_scores == []:
            self.high_scores = self.default_hs
