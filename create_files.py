import xlwt
import xlrd
from datetime import  datetime

def set_user_information():
    font0 = xlwt.Font()
    font0.name ='Times New Roman'
    font0.colour_index = 3
    font0.bold= True

    style0 = xlwt.XFStyle()
    style0.font = font0

    style1 = xlwt.XFStyle()
    style1.num_format_str='DD/MM/YY h:mm:ss'


    wb=xlwt.Workbook()
    ws = wb.add_sheet('User information')

    ws.write(0,0,'chat_id',style0)
    ws.write(0, 1, 'Время запроса', style0)
    ws.write(1, 1, datetime.now(), style1)
    ws.write(2, 0, 1)
    ws.write(2, 1, 1)
    ws.write(2, 2, xlwt.Formula("A3+B3"))

    wb.save('example.xls')
#set_user_information()


