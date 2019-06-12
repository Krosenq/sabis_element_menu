from tkinter import*
import crawler

url = "https://www.sabis.se/element/dagens-lunch/"
selector = "#post-1368 > div > div > div.entry-body > div.lunch-data .lunch-day-container"

url_bilia = "http://biliasolna.kvartersmenyn.se/"
selector_bilia = "body > div:nth-child(5) > div > div.divider-full > div > div:nth-child(1)"

data = crawler.day_menu(crawler.request_data(url, selector))

output_string = crawler.render_string(data)

data_2 = crawler.bila_menu(crawler.request_data(url_bilia, selector_bilia))

output_string_2 = crawler.render_string(data_2)

root = Tk()

root.winfo_toplevel().title("Meny Sabis/Bilia, ")

#Sabis
label_menu = Label(root, text = "\n" + crawler.weekday_string() + '\n==================\n\n Dagens lunch, SABIS\n ')
label_menu.config(font=("Arial", 16))
label_menu.pack()

label_text = Label(root, text = output_string)
label_text.config(font=("Arial", 14))
label_text.pack()

#Bilia
label_menu_2 = Label(root, text = '=========================\n\n Dagens lunch, Bilia\n ')
label_menu_2.config(font=("Arial", 16))
label_menu_2.pack()

label_text_2 = Label(root, text = output_string_2)
label_text_2.config(font=("Arial", 14))
label_text_2.pack()

#button
button = Button(root, text='Avsluta', width=25, command=root.destroy)
button.focus()
button.pack()

label_text_3 = Label(root, text = "\n")
label_text_3.pack()



windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()

positionRight = int(root.winfo_screenwidth()/4.5)
positionDown = int(root.winfo_screenheight()/18)

root.geometry("+{}+{}".format(positionRight, positionDown))

root.mainloop()
