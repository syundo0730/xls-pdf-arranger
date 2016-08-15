#! c:/Python27/python.exe
# coding:utf-8

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.units import cm
from reportlab.pdfbase.ttfonts import TTFont
import xlrd
import os.path
import sys
import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui
from MainWindowUI import Ui_MainWindow


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kw):
        QtGui.QMainWindow.__init__(self, *args, **kw)
        self.setupUi(self)

        self.modbar.sliderMoved.connect(self.change_mod)
        self.upmarginbar.sliderMoved.connect(self.change_upmargin)
        self.downmarginbar.sliderMoved.connect(self.change_downmargin)
        self.rcsvbtn.clicked.connect(self.read_csv)
        self.wpdfbtn.clicked.connect(self.make_pdf)

        self.modulation = self.modbar.value() / 100.0
        self.upmargin = self.upmarginbar.value()*cm
        self.downmargin = self.downmarginbar.value()*cm
        self.pdfFile = canvas.Canvas("./segaki.pdf", bottomup=False)
        self.pdfFile.saveState()

        self.xsize = 29.7*cm
        self.ysize = 42*cm
        #    A4
        self.pdfFile.setPageSize((self.xsize,self.ysize))

        self.pdfFile.setAuthor("python-izm.com")
        self.pdfFile.setTitle("PDF")
        self.pdfFile.setSubject("sample")

        self.fontname = "AoyagiKouzanFontT"

        pdfmetrics.registerFont(TTFont(self.fontname, "C:\Windows\Fonts\DFJGYOMD.ttc"))
        self.pdfFile.setFont(self.fontname, 10)

    def draw_string(self,string,size,posx,posy):
        self.pdfFile.setFontSize(size)
        str_len = len(string)
        for i in range(str_len):
            self.pdfFile.drawString(posx, posy + i  *size * 0.75, string[i])

    def calc_size(self, str_len, modulation, margin):
        if str_len == 0:
            return 0
        return (self.ysize * modulation - margin) / str_len

    def change_mod(self, val):
        self.modulation = val / 100.0
        print self.modulation

    def change_upmargin(self, val):
        self.upmargin = val * cm
        print self.upmargin

    def change_downmargin(self, val):
        self.downmargin = val * cm
        print self.downmargin

    def read_csv(self):
        filename = unicode( QtGui.QFileDialog.getOpenFileName(self, u'元データ', os.path.expanduser('./')) )
        self.xlsbook = xlrd.open_workbook(filename)
        print filename

    def make_pdf(self):
        #ページ中の左右どちらにあるかを表す．文字の配置にも使っているから数字が大事
        i=3
        for sheet_i in range(self.xlsbook.nsheets):
            sheet = self.xlsbook.sheet_by_index(sheet_i)
            ref_col = 1#文字が書いてある行番号(0から
            for row_i in range(3, sheet.nrows):
                self.pdfFile.setFont(self.fontname,10)
                modulation = self.modulation
                margin0 = self.upmargin
                margin1 = self.downmargin
                xsize = self.xsize
                ysize = self.ysize

                str0 = conv_grade(sheet.cell(row_i, ref_col+1).value)#大，特，特別　を大施食　等々に変換する
                length0 = len(str0)
                size0 = 3.7 * cm
                ylen = size0 * length0 * 1.1
                self.draw_string(str0, size0 / 0.75, xsize / 4 * i - size0 / 2, margin0 + size0)

                str1 = sheet.cell(row_i, ref_col).value
                length1 = len(str1)
                size1 = self.calc_size(length1, 1-modulation, margin1)
                self.draw_string(str1, size1, xsize / 4 * i - size1 / 2, margin1
                + size1 + ysize * modulation)

                if i == 1:
                    self.pdfFile.showPage()
                i = 4 - i
        self.pdfFile.save()

        print 'PDF print finished!'

def conv_grade(str):
    if str == u'大':
        return u'大施食'
    elif str == u'特':
        return u'特大施食'
    elif str== u'特別':
        return u'特別大施食'
    else:
        return str

def main():
    application = QtGui.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    application.exec_()

if __name__ == "__main__":
    main()
