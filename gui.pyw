from tkinter import*
import crawler

url = "https://www.sabis.se/element/dagens-lunch/"
selector = "#post-1368 > div > div > div.entry-body > div.lunch-data .lunch-day-container"

data = crawler.day_menu(crawler.request_data(url, selector))

output_string = crawler.render_string(data)

root = Tk()

root.winfo_toplevel().title("Meny Sabis")

label_menu = Label(root, text = '\n Dagens lunch, SABIS\n ')
label_menu.config(font=("Arial", 25))
label_menu.pack()

label_text = Label(root, text = output_string)
label_text.config(font=("Arial", 20))
label_text.pack()

windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()

positionRight = int(root.winfo_screenwidth()/5)
positionDown = int(root.winfo_screenheight()/5)

root.geometry("+{}+{}".format(positionRight, positionDown))

root.mainloop()
