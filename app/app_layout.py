import FreeSimpleGUI as sg
from .init_layout import vensterKop, horizontaal

kolomLinks = sg.Column(
    layout=[
        [
            sg.Frame(
                title='TOP 30',
                layout=[
                    [
                        sg.Listbox(
                            values=[],
                            size=(30, 20),
                            pad=(12, 12),
                            select_mode=sg.LISTBOX_SELECT_MODE_SINGLE,
                            key='-LBX-TOP30-',
                            enable_events=True
                        )
                    ]
                ]
            )
        ]
    ]
)

kolomRechts = sg.Column(
    layout=[
        # Ряд 1
        [
            sg.Text(
                text='Titel',
                size=(18, 1)
            ),
            sg.Text(
                text='',
                size=(8, 1),
                justification='right',
                key='-TXT-TITEL-'
            )
        ],
        [
            sg.Text(
                text='Performer',
                size=(18, 1)
            ),
            sg.Text(
                text='',
                size=(8, 1),
                justification='right',
                key='-TXT-PERFORMER-'
            )
        ],
        # Ряд 2
        [
            sg.HorizontalSeparator(
                pad=(0, 70)
            )
        ],
        # Ряд 3
        [
            sg.Image(
                key = '-IMG-IMG-'
            )
        ],
        # Ряд 5
        [
            sg.HorizontalSeparator(
                pad=(0, 70)
            )
        ],
        # Ряд 7
        [
            sg.Button(
                button_text='Afsluiten',
                size=(26, 2),
                key='-BTN-AFSLUITEN-'
            )
        ]
    ]
)

def appLayout():
    return [
        # Ряд 1
        vensterKop(),
        # Ряд 2
        horizontaal(),
        # Ряд 3
        [
            kolomLinks,
            sg.VerticalSeparator(
                pad=(5, 0)
            ),
            kolomRechts
        ]
    ]
