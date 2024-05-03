from interface import Interface
from teste import teste
from interface_grafica import GUIInterface


def main():
    teste()
    Interface.interface()
    app = GUIInterface()
    app.mainloop()


if __name__ == "__main__":
    main()
