import PySimpleGUI as sg
import datetime

date_1 = datetime.date.today().strftime("%d-%m-%Y")

sg.theme("DarkGreen5")

sg.set_options(element_padding=(0, 0))


row1 = sg.Column([[sg.Frame("Date:",[[
    sg.Text(),
    sg.Column([
        [sg.Input(
        key="-Date-",
        readonly= True,
        default_text = date_1,
        enable_events = True)],
    ])
]])]])

files = open("countries.txt")

row2 = sg.Column([[sg.Frame("Registration:",[[
    sg.Text(),
    sg.Column([
    [sg.Text()],
        [sg.Text("Name")],
        [sg.Input(key="-Name-" )],
        [sg.Text("Adress")],
        [sg.Input(key="-Adress-")],
        [sg.Text("Country")],
        [sg.Combo(list(files),
            default_value = "Choose Country",
            readonly = True,
            key="-Combo_Country-")],
        [sg.Text("Birthday")],
        [sg.Input(key="-Birthday-")],
    [sg.Text()]
    ]),
    sg.Text(), sg.Text(), sg.Text(), sg.Text(),
    sg.Column([
    [sg.Text()],
        [sg.Text("Surname")],
        [sg.Input(key="-Surname-")],
        [sg.Text("City-Town")],
        [sg.Input(key="-City-")],
        [sg.Text("Postal Code")],
        [sg.Input(key="-PC-")],
        [sg.Text("Personal ID")],
        [sg.Input(key="-ID-")],
    [sg.Text()],
    ])
]])]])

files.close()
row3 = sg.Column([[sg.Frame("Contact Details:",[[
    sg.Text(),
    sg.Column([
    [sg.Text()],
        [sg.Text("E-mail")],
        [sg.Input(key="-email-")],
    [sg.Text()]
    ]),
    sg.Text(), sg.Text(), sg.Text(),sg.Text(),
    sg.Column([
    [sg.Text()],
        [sg.Text("Phone Number")],
        [sg.Input(key="-phone-")],
    [sg.Text()]
        ])
]])]])

row4 = sg.Column([[sg.Frame("Booking Dates:",[[
    sg.Text(),
    sg.Column([
    [sg.Text()],
    [sg.CalendarButton(
        button_text = "Pick a Check-In Date",
        close_when_date_chosen=True,
        format = "%d-%m-%Y %H:%M:%S",
        target="-checkin-",
    )],
    [sg.Text()],
    [sg.Input(key="-checkin-")],
    [sg.Text()]
    ]),
    sg.Text(), sg.Text(), sg.Text(), sg.Text(),
    sg.Column([
    [sg.Text()],
    [sg.CalendarButton(
        button_text = "Pick a Check-Out Date",
        close_when_date_chosen=True,
        format = "%d-%m-%Y %H:%M:%S",
        target="-checkout-",
    )],
    [sg.Text()],
    [sg.Input(key="-checkout-")],
    [sg.Text()]
        ])
]])]])


row5 = sg.Column([[sg.Frame('Actions:',[[
    sg.Text(),
    sg.Column([[
        sg.Text(), sg.Text(), sg.Text(), sg.Text(),
        sg.Button("Book"),
        sg.Text(), sg.Text(), sg.Text(), sg.Text(),
        sg.Button("Clear"),
        sg.Text(), sg.Text(), sg.Text(), sg.Text(),
        sg.Button("Delete"),
        sg.Text(), sg.Text(), sg.Text(), sg.Text(),
        sg.Text("Room #"),
        sg.Input(key="-room-", size=(12,6)),
        sg.Text(), sg.Text(), sg.Text(), sg.Text(),
    ]])
]])]])

layout = [[row1],[row2],[row3],[row4],[row5]]

window = sg.Window("Registration App",
         layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break

window.close()
