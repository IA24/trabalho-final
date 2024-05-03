from interface import Interface
from teste import teste
from interface_grafica import GUIInterface


def main():
    teste()
    app = GUIInterface()
    app.mainloop()
    Interface.interface()


if __name__ == "__main__":
    main()
