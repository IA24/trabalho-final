from interface.interface import Interface
from teste import teste
from interface.gui.main_window import MainWindow


def main():
    teste()
    app = MainWindow()
    app.mainloop()
    Interface.interface()


if __name__ == "__main__":
    main()
