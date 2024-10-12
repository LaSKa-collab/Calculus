import tkinter as tk
from math import *


def but(x):
    entry.insert(index=len(entry.get()), string=f'{x}')
    entry.focus()


def ctg(x):
    return cos(x) / sin(x)


def arcctg(x):
    return pi/2 - atan(x)


def dele(x=False):
    if x:
        entry.delete(0, last='end')
    else:
        entry.delete(len(entry.get()) - 1)


def dequally():
    x = entry.get()
    x = x.replace('lg', 'log10')
    x = x.replace('arcsin', 'asin')
    x = x.replace('arccos', 'acos')
    x = x.replace('arctan', 'atan')
    x = x.replace('^', '**')
    x = x.replace('π', 'pi')
    try:
        c = eval(x)
    except ZeroDivisionError:
        dele(True)
        but('Не дели на ноль!')
    except SyntaxError:
        pass
    except Exception:
        dele(True)
        but('Ошибка')
    else:
        dele(True)
        if c >= 1000000000:
            x = eval(x)
            x = "{:.2e}".format(x)
            entry.insert(index=len(entry.get()), string=f'{x}')
        else:
            entry.insert(index=len(entry.get()), string=f'{eval(x)}')


window = tk.Tk()
window.geometry('720x700+400+200')
window.columnconfigure([i for i in range(0, 6)], weight=1, minsize=20)
window.rowconfigure([i for i in range(0, 7)], weight=1, minsize=20)

frames = [tk.Frame(master=window) for i in range(35)]

entry = tk.Entry(master=frames[-1], justify='right', font='Calibri 50')
frames[-1].grid(row=0, column=0, columnspan=6, sticky='nsew')

number_0 = tk.Button(master=frames[0], text=f'{0}', command=lambda: but(f'{0}'), bg='dodger blue', fg='white')
number_1 = tk.Button(master=frames[1], text=f'{1}', command=lambda: but(f'{1}'), bg='dodger blue', fg='white')
number_2 = tk.Button(master=frames[2], text=f'{2}', command=lambda: but(f'{2}'), bg='dodger blue', fg='white')
number_3 = tk.Button(master=frames[3], text=f'{3}', command=lambda: but(f'{3}'), bg='dodger blue', fg='white')
number_4 = tk.Button(master=frames[4], text=f'{4}', command=lambda: but(f'{4}'), bg='dodger blue', fg='white')
number_5 = tk.Button(master=frames[5], text=f'{5}', command=lambda: but(f'{5}'), bg='dodger blue', fg='white')
number_6 = tk.Button(master=frames[6], text=f'{6}', command=lambda: but(f'{6}'), bg='dodger blue', fg='white')
number_7 = tk.Button(master=frames[7], text=f'{7}', command=lambda: but(f'{7}'), bg='dodger blue', fg='white')
number_8 = tk.Button(master=frames[8], text=f'{8}', command=lambda: but(f'{8}'), bg='dodger blue', fg='white')
number_9 = tk.Button(master=frames[9], text=f'{9}', command=lambda: but(f'{9}'), bg='dodger blue', fg='white')
buttons_numbers = [number_0, number_1, number_2, number_3, number_4, number_5, number_6, number_7, number_8, number_9]

for i in range(10):
    if i == 0:
        frames[0].grid(row=4, column=1, sticky='nsew')
    else:
        frames[i].grid(row=ceil(i/3), column=(i - 1) % 3, sticky='nsew')
    buttons_numbers[i].pack(expand=True, fill='both')

list_of_rows_1 = (1, 2, 3, 3, 4, 4, 4, 4, 5)
list_of_columns = (3, 3, 4, 5, 4, 5, 0, 2, 4)
operation_e = tk.Button(master=frames[10], text=f'e', command=lambda: but(f'e'))
operation_pi = tk.Button(master=frames[11], text=f'π', command=lambda: but(f'π'))
operation_plus = tk.Button(master=frames[12], text=f'+', command=lambda: but(f'+'))
operation_minus = tk.Button(master=frames[13], text=f'-', command=lambda: but(f'-'))
operation_multy = tk.Button(master=frames[14], text=f'*', command=lambda: but(f'*'))
operation_deli = tk.Button(master=frames[15], text=f'/', command=lambda: but(f'/'))
operation_l = tk.Button(master=frames[16], text=f'(', command=lambda: but(f'('))
operation_r = tk.Button(master=frames[17], text=f')', command=lambda: but(f')'))
operation_dot = tk.Button(master=frames[18], text=f'.', command=lambda: but(f'.'))
list_of_button_1 = [operation_e, operation_pi, operation_plus, operation_minus, operation_multy, operation_deli, operation_l, operation_r, operation_dot]

for i in range(len(list_of_button_1)):
    frames[i + 10].grid(row=list_of_rows_1[i], column=list_of_columns[i], sticky='nsew')
    list_of_button_1[i].pack(expand=True, fill='both')

delete = tk.Button(master=frames[-2], text='C', command=lambda: dele(True))
frames[-2].grid(row=2, column=5, sticky='nsew')

back = tk.Button(master=frames[-3], text='<==', command=lambda: dele())
frames[-3].grid(row=2, column=4, sticky='nsew')

equally = tk.Button(master=frames[-4], text='=', command=dequally, bg='purple3', fg='white')
frames[-4].grid(row=1, column=4, columnspan=2, sticky='nsew')

potentional = tk.Button(master=frames[-5], text=f'x^y', command=lambda: but('^('))
frames[-5].grid(row=5, column=5, sticky='nsew')

logarithm = tk.Button(master=frames[-6], text=f'ln x', command=lambda: but('log('))
frames[-6].grid(row=3, column=3, sticky='nsew')

space = tk.Button(master=frames[-7], text='(____)', command=lambda: but(' '))
frames[-7].grid(row=6, column=4, sticky='nsew', columnspan=2)

sinus = tk.Button(master=frames[-8], text='sin x', command=lambda: but('sin('))
frames[-8].grid(row=5, column=0, sticky='nsew')

cosinus = tk.Button(master=frames[-9], text='cos x', command=lambda: but('cos('))
frames[-9].grid(row=6, column=0, sticky='nsew')

arcsinus = tk.Button(master=frames[-10], text='arcsin x', command=lambda: but('arcsin('))
frames[-10].grid(row=5, column=2, sticky='nsew')

arccosinus = tk.Button(master=frames[-11], text='arccos x', command=lambda: but('arccos('))
frames[-11].grid(row=6, column=2, sticky='nsew')

arctg = tk.Button(master=frames[-12], text='arctg x', command=lambda: but('arctan('))
frames[-12].grid(row=5, column=3, sticky='nsew')

arccotg = tk.Button(master=frames[-13], text='arcctg x', command=lambda: but('arcctg('))
frames[-13].grid(row=6, column=3, sticky='nsew')

tg = tk.Button(master=frames[-14], text='tan x', command=lambda: but('tan('))
frames[-14].grid(row=5, column=1, sticky='nsew')

cotg = tk.Button(master=frames[-15], text='ctg x', command=lambda: but('ctg('))
frames[-15].grid(row=6, column=1, sticky='nsew')

lg = tk.Button(master=frames[-16], text='lg x', command=lambda: but('lg('))
frames[-16].grid(row=4, column=3, sticky='nsew')

list_of_operation_2 = (entry, delete, back, equally, potentional, logarithm, space, sinus, cosinus, arcsinus, arccosinus, arctg, arccotg, tg, cotg, lg)
for i in list_of_operation_2:
    i.pack(expand=True, fill='both')

window.mainloop()
