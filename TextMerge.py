from tkinter import *
import pyperclip

count = 0


def set_input():
    e1.delete(1.0, END)
    e1.insert(END, pyperclip.paste())


def add():
    global count
    all_text.append(e1.get(1.0, END))
    e1.delete(1.0, END)
    count +=1
    count_label['text'] = "Add Count: "+str(count)


def finnish():
    global count
    count = 0
    merged_list = []
    merged_text = ""
    for text in all_text:
        merged_list.append(list(filter(None, text.splitlines())))
    for i in range(0, len(merged_list[0])):
        for j in range(0, len(merged_list)):
            merged_text += merged_list[j][i]+"\n"
        merged_text += "\n"
    e1.delete(1.0, END)
    e1.insert(END, merged_text)
    merged_text = ""
    count_label['text'] = "Add Count: " + str(count)

def copy():
    copy_text = e1.get(1.0, END)
    pyperclip.copy(copy_text)

if __name__ == "__main__":
    all_text =[]
    master = Tk()
    upperFrame = Frame(master)
    upperFrame.pack()

    lowerFrame = Frame(master)
    lowerFrame.pack(side=BOTTOM)

    textLabel = Label(upperFrame, text="Text")
    textLabel.pack(side=TOP)

    e1 = Text(lowerFrame, height=20, width=40)
    e1.pack()
    paste_button = Button(lowerFrame, text="Paste", command=set_input)
    paste_button.pack(side=LEFT)
    finnish_button = Button(lowerFrame, text="Finnish", command=finnish)
    finnish_button.pack(side=RIGHT)

    copy_button = Button(lowerFrame, text="Copy", command=copy)
    copy_button.pack(side=BOTTOM)
    count_label = Label(lowerFrame, text="Add Count: "+str(count))
    count_label.pack(side=BOTTOM)
    add_button = Button(lowerFrame, text="Add", command=add)
    add_button.pack(side=BOTTOM)
    master.mainloop()