import tkinter as tk
from tkinter import messagebox

import main
subtotal = 0.00

#lookup upc in the database
def search():
    global subtotal
    #strip upc of any other chars
    upc = upcQuery.get().strip()
    #empty the entry box
    upcQuery.delete(0, tk.END)
    #find upc and print item + price
    result = main.lookup(upc)
    name, price = result
    receipt.insert(tk.END, f"Item: {name}\nPrice: ${price}\n")


    #update running total
    subtotal+=float(price)
    totalLabel.config(text=f"Total: ${subtotal:.2f}")


#our ui window
root = tk.Tk()
root.title("Product Scanner")

#input box to get the upc query
tk.Label(root, text="Enter UPC:")
upcQuery = tk.Entry(root, width=50)
upcQuery.pack()

#send the upc
scanner = tk.Button(root, text="Scan", command=search)
scanner.pack()

#show the product infos
receipt = tk.Text(root, width=50, height=10)
receipt.pack()

#show the running total
totalLabel = tk.Label(root, text="Total: $0.00")
totalLabel.pack()

root.mainloop()