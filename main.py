# main file
from tkinter import *


def center_window(win):
    screen_w = win.winfo_screenwidth()
    screen_h = win.winfo_screenheight()
    width = win.winfo_reqwidth()
    height = win.winfo_reqheight()

    x = screen_w / 2 - width / 2
    y = screen_h / 2 - height / 2
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))


def calculations(event):
    acq = float(purchase_price.get()) + float(rehab.get()) + float(closing_costs.get())
    hml = float(arv.get()) * (float(hard_ltv.get()) / 100)
    monthly_cf = float(rent.get()) - float(piti.get())
    annual_cf = monthly_cf * 12

    oop.config(state='normal')
    monthly.config(state='normal')
    annual.config(state='normal')
    coc.config(state='normal')

    oop.delete(0, END)
    monthly.delete(0, END)
    annual.delete(0, END)
    coc.delete(0, END)

    oop.insert(0, acq - hml)
    monthly.insert(0, monthly_cf)
    annual.insert(0, annual_cf)
    coc.insert(0, ((round(annual_cf / (acq - hml), 4) * 100), '%'))

    oop.config(state='readonly')
    monthly.config(state='readonly')
    annual.config(state='readonly')
    coc.config(state='readonly')


root = Tk()
root.title('CashFlow')
center_window(root)
root.geometry('800x275')


# LABELS
pp_label = Label(root, text='Purchase Price:')
rh_label = Label(root, text='Rehab:')
cc_label = Label(root, text='Closing Costs:')
arv_label = Label(root, text='ARV:')
hltv_label = Label(root, text='Hard Money LTV:')
cltv_label = Label(root, text='Conventional LTV:')
piti_label = Label(root, text='PITI:')
rent_label = Label(root, text='Rent:')
oop_label = Label(root, text='Cash OOP:')
monthly_label = Label(root, text='Cashflow (monthly):')
annual_label = Label(root, text='Cashflow (annual):')
coc_label = Label(root, text='Cash-on-Cash Return:')


pp_label.grid(row=0, sticky=E)
rh_label.grid(row=1, sticky=E)
cc_label.grid(row=2, sticky=E)
arv_label.grid(row=3, sticky=E)
hltv_label.grid(row=4, sticky=E)
cltv_label.grid(row=5, sticky=E)
piti_label.grid(row=6, sticky=E)
rent_label.grid(row=7, sticky=E)
oop_label.grid(row=1, column=3, sticky=E)
monthly_label.grid(row=2, column=3, sticky=E)
annual_label.grid(row=3, column=3, sticky=E)
coc_label.grid(row=4, column=3, sticky=E)


# ENTRIES
purchase_price = Entry(root)
rehab = Entry(root)
closing_costs = Entry(root)
arv = Entry(root)
hard_ltv = Entry(root)
conv_ltv = Entry(root)
piti = Entry(root)
rent = Entry(root)
oop = Entry(root, state='readonly')
monthly = Entry(root, state='readonly')
annual = Entry(root, state='readonly')
coc = Entry(root, state='readonly')


purchase_price.grid(row=0, column=1)
rehab.grid(row=1, column=1)
closing_costs.grid(row=2, column=1)
arv.grid(row=3, column=1)
hard_ltv.grid(row=4, column=1)
conv_ltv.grid(row=5, column=1)
piti.grid(row=6, column=1)
rent.grid(row=7, column=1)
oop.grid(row=1, column=4)
monthly.grid(row=2, column=4)
annual.grid(row=3, column=4)
coc.grid(row=4, column=4)


# BUTTON
calc_button = Button(root, text='Calculate', bg="green")
calc_button.grid(row=8, column=2, pady=4)
calc_button.bind('<Button-1>', calculations)

root.mainloop()
