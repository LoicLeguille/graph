# Buttons - art from Kenney.nl
# Projet Graph made by Loïc Leguille

from gui import *

# main function
def main():
    root = Tk()
    g = GUI(root)
    g.pack(fill = BOTH, expand = 'yes')
    root.mainloop()

# run program
if __name__ == '__main__':
    main()
