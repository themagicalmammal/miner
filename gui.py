from tkinter import *
from tkinter import messagebox

from main import *

root = Tk()
root.title("Stock Analysis")
root.geometry("400x400")
root.iconbitmap("icon/favicon.ico")

# global variables
Date_start_entry = ""
Date_end_entry = ""
currency_var = StringVar()
currency_var.set("INR")
z = IntVar()


def start():
    global Date_start_entry
    global Date_end_entry

    # print("Do you want to input value ?(1 for Yes)")
    response = messagebox.askyesno("Popup", "Do you want to start?")
    inpu = response
    if inpu == 1:
        start_date_label = Label(root, text="Start Date(YYYY-MM-DD) --> ")
        end_date_label = Label(root, text="End Date(YYYY-MM-DD) --> ")

        Date_start_entry = Entry(root)
        Date_end_entry = Entry(root)

        start_date_label.grid(row=1, column=0, sticky="w")
        Date_start_entry.grid(row=1, column=1, pady=3, sticky="w")
        end_date_label.grid(row=2, column=0, sticky="w")
        Date_end_entry.grid(row=2, column=1, sticky="w")

    else:
        root.destroy()
        return

    confirm_btn = Button(root, text="Confirm", command=my_func)
    confirm_btn.grid(row=3, column=0, columnspan=2, pady=3, ipadx=20)


def my_func():
    global currecny_var

    if len(Date_start_entry.get()) < 10 and len(Date_end_entry.get()) < 10:
        messagebox.showwarning("Invalid Dates",
                               "Please enter date in YYYY-MM-DD format")
        start()
        return

    currency_codes = {"INR", "USD", "GBP", "CAD", "CNY"}

    # dropdown for selecting currency code
    drop1 = OptionMenu(root, currency_var, *currency_codes)
    drop1_label = Label(root, text="Select currency code-  ")
    drop1.grid(row=4, column=1, sticky="w")
    drop1_label.grid(row=4, column=0, sticky="w")
    d_confirm_btn = Button(root, text="OK", command=my_func2)
    d_confirm_btn.grid(row=5, column=0, columnspan=2, pady=3)


def my_func2():
    global z
    global Date_start_entry
    global Date_end_entry
    global currency_var
    ds = Date_start_entry.get()
    de = Date_end_entry.get()
    c = currency_var.get()

    company_label = Label(root,
                          text="Company you want to analyze stock of -> ")
    company_label.grid(row=6, column=0, pady=2, sticky="w")
    Radiobutton(
        root,
        text="1. Netflix",
        variable=z,
        value=1,
        command=lambda: miner(ds, de, c, z.get()),
    ).grid(row=7, column=0, sticky="w")
    Radiobutton(
        root,
        text="2. Facebook",
        variable=z,
        value=2,
        command=lambda: miner(ds, de, c, z.get()),
    ).grid(row=8, column=0, sticky="w")
    Radiobutton(
        root,
        text="3. Apple",
        variable=z,
        value=3,
        command=lambda: miner(ds, de, c, z.get()),
    ).grid(row=9, column=0, sticky="w")
    Radiobutton(
        root,
        text="4. Amazon",
        variable=z,
        value=4,
        command=lambda: miner(ds, de, c, z.get()),
    ).grid(row=10, column=0, sticky="w")
    Radiobutton(
        root,
        text="5. Google",
        variable=z,
        value=5,
        command=lambda: miner(ds, de, c, z.get()),
    ).grid(row=11, column=0, sticky="w")
    Radiobutton(
        root,
        text="6. Bitcoin",
        variable=z,
        value=6,
        command=lambda: miner(ds, de, c, z.get()),
    ).grid(row=12, column=0, sticky="w")
    Radiobutton(
        root,
        text="7. Comparison of all stocks in that period",
        variable=z,
        value=7,
        command=lambda: miner(ds, de, c, z.get()),
    ).grid(row=12, column=0, sticky="w")


startButton = Button(root, text="Start", command=start, anchor="c")
startButton.grid(row=0, column=0, padx=180, pady=5, ipadx=10, columnspan=2)

root.mainloop()
