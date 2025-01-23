import FreeSimpleGUI as sg
import os
from PIL import Image, ImageTk
from entiteit.top30 import Top30
from app.app_layout import appLayout

class App:
    def __init__(self):
        self._collectie = []
        self.top30 = Top30() 
        self._laad_top30() 

    def _laad_top30(self):
        self._collectie = self.top30.lijst()

    def lijst(self):
        return self._collectie

    def load_image(self, image_path):
        try:
            img = Image.open(image_path)
            img = img.resize((300, 300))
            img.thumbnail((300, 300))

            img_tk = ImageTk.PhotoImage(img)

            return img_tk
        except Exception as e:
            print(f"Ошибка при загрузке изображения {image_path}: {e}")
            return None

    def run(self):
        window = sg.Window('TOP 30', layout=appLayout(), finalize=True)

        listbox_values = [f"{liedje.titel} - {liedje.performer}" for liedje in self.lijst()]
        window['-LBX-TOP30-'].update(listbox_values)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == '-BTN-AFSLUITEN-': 
                break

            if event == '-LBX-TOP30-':
                selected_values = values['-LBX-TOP30-']
                if selected_values: 
                    selected_value = selected_values[0]
                    selected_index = listbox_values.index(selected_value)
                    liedje = self.lijst()[selected_index]
                    window['-TXT-PERFORMER-'].update(liedje.performer)
                    window['-TXT-TITEL-'].update(liedje.titel)

                    image_path = os.path.join('data', 'afbeeldingen', liedje.foto)
                    print(f"Пытаемся загрузить изображение: {image_path}")

                    if os.path.exists(image_path):
                        img_tk = self.load_image(image_path)
                        if img_tk:
                            window['-IMG-IMG-'].update(data=img_tk)
                        else:
                            window['-IMG-IMG-'].update(filename='data/afbeeldingen/default.jpg')
                    else:
                        print(f"Изображение не найдено: {image_path}")
                        window['-IMG-IMG-'].update(filename='data/afbeeldingen/default.jpg')

        window.close()
