import openpyxl
def test():
    wb = openpyxl.load_workbook("rozklad.xlsx")

    sheet = wb['Лист1']
    a = ''

    #діапазон




    #tuple(sheet[x:y])
    k = 0
    mas = []
    return sheet
#for rowOfCellObjects in sheet[x:y]:
    #for rowOfCellObj in rowOfCellObjects:
            #if(rowOfCellObj.value != None):

            #k = k+1
            #if(k == 3):
        #a = a + ' ' + str(rowOfCellObj.value)

                #else:
                 #   a = a + ' '+ str(rowOfCellObj.value)

                   # print(rowOfCellObj.value)
    #if(a[0] != "N"):
      #  print(a)
      #  a = ''


        #k = 0
       # mas.append(a)
       # a = ''

        #print('the end string')

