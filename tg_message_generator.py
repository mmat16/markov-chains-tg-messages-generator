from tkinter import *
import mk2


def mode_1():
    global rows_count_1
    row = rows_count_1
    rows_count_1 += 1
    txt = Text(width=30, height=5, wrap=WORD)
    txt.insert(1.0, mk2.text_model_me.make_short_sentence(150))
    txt.grid(row=row, column=0)

    # label = tk.Label(win, text=txt, font=('Arial', 20), justify=tk.LEFT)
    # label.grid(row=row)


def mode_2():
    global rows_count_2
    row = rows_count_2
    rows_count_2 += 1
    txt = Text(width=30, height=5, wrap=WORD)
    txt.insert(1.0, mk2.text_model_di.make_short_sentence(150))
    # label = Label(win, text=txt, font=('Arial', 20), justify=LEFT)
    txt.grid(row=row, column=1)


def mode_3():
    global rows_count_3
    row = rows_count_3
    rows_count_3 += 1
    text = Text(width=60, height=10, wrap=WORD)
    txt = 'dina: ' + mk2.text_model_di.make_short_sentence(150) + '\nmisha: ' + mk2.text_model_me.make_short_sentence(
        150) + '\ndina: ' + mk2.text_model_di.make_short_sentence(150) + '\nmisha: ' + mk2.text_model_me.\
        make_short_sentence(150)
    text.insert(1.0, txt)
    # label = Label(win, text=txt,
    #                  font=('Arial', 20),
    #                  padx=1,
    #                  pady=1,
    #                  width=len(txt),
    #                  height=4,
    #                  anchor='e',
    #                  relief=RAISED,
    #                  justify=LEFT,
    #                  )
    text.grid(row=row, column=2)


def mode_4():
    global rows_count_4
    row = rows_count_4
    rows_count_4 += 1
    txt = mk2.text_model_mix.make_sentence()
    while txt is None:
        txt = mk2.text_model_mix.make_sentence()
    text = Text(width=30, height=5, wrap=WORD)
    text.insert(1.0, txt)
    # label = Label(win, text=txt, font=('Arial', 20), justify=LEFT)
    text.grid(row=row, column=3)


rows_count_1 = 1
rows_count_2 = 1
rows_count_3 = 1
rows_count_4 = 1

win = Tk()
photo = PhotoImage(file='telegram-logo.png')
win.iconphoto(False, photo)
# win.config(bg='#2B74B7')
win.title('Message Generator')
win.geometry('2560x1600')

btn1 = Button(win, text='message from me', bg='#2B74B7', command=mode_1,)
btn2 = Button(win, text='message from dina', bg='#2B74B7', command=mode_2,)
btn3 = Button(win, text='dialog', bg='#2B74B7', command=mode_3,)
btn4 = Button(win, text='mixed message', bg='#2B74B7', command=mode_4,)

btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)
btn4.grid(row=0, column=3)

# label1 = tk.Label(win, text='sample', bg='#2B74B7', font=())
# label1.pack()

win.mainloop()
