import FreeSimpleGUI as sg

fntStandart = ('Calibri', 14)
fntKop = ('Calibri', 24, 'bold')

vensterTitel = 'CONTACTEN'

def vensterKop():
    return[
        sg.Text('', expand_x=True),
        sg.Image(
            source = 'assets/logo.png'
        ),
        sg.Text(
            text = 'TOP 30',
            font = fntKop
        ),
        sg.Text('', expand_x=True)
    ]

def horizontaal():
    return[
        sg.HorizontalSeparator(
            pad = (0, 10)
        )
    ]

sg.theme('DefaultNoMoreNagging')

sg.set_options(
    icon = 'assets/favicon.ico',
    font = fntStandart
)