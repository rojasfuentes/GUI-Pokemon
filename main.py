import toga


def on_press(widget):
    print("Funciona")


def new_button():
    button = toga.Button('Working!', on_press=on_press)
    button.style.padding = 20
    button.style.width = 200

    return button


def build(app):
    box = toga.Box()

    button1 = new_button()
    box.add(button1)

    return box


def main():
    app = toga.App('Prueba Interfaz Gráfica', 'com.wiwis.toga', startup=build)
    return app


if __name__ == '__main__':
    app = main()
    app.main_loop()
