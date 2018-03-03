# Grafika vkljucena
# import pyglet
# window = pyglet.window.Window()
#
# @window.event
# def on_draw():
#     window.clear()
#     start()
#
# @window.event
# def on_key_press(symbol, modifiers):
#     print("Pritisnjena tipka")
#     print(symbol)
#     # Kaj se zgodi ko pritisnes doloceno tipko......


# \n so znaki ki pomenijo novo vrstico
def start():
    msg = "==si želiš imeti psa?\n" \
          "1==ja, 2==ne:"
    i = int(input(msg))
    if i == 1:
        dva()


def dva():
    msg = "==super!pojdi v zavetišče za živali. da bi izvedel kje je moraš rešiti uganko: brat mojega brata ima\n" \
          "očeta januša. januš ima hčerko angelino. angelinin dedek je poročen z evo. skupaj imata tri otroke.\n" \
          "eden od otrok je toni. kaj je meni toni?:\n" \
          "1= brat, 2= stric, 3= dedek, 4= pradedek:"
    i = int(input(msg))
    while i > 4:
        msg = "==ne upoštevaš pravil! poskusi še enkrat: "
        i = int(input(msg))
    if i != 2:
        print("Nope!! Adijo")
    else:
        tri()


def tri():
    msg = "==dobro! prišel si do zavetišča. katerega psa bi rad?\n" \
          "1-haskija 2-nemškega ovčarja 3-bordarkolija 4-kavalirja karla charelsa ?:"
    i = int(input(msg))
    while i > 4:
        msg = "==ne upoštevaš pravil! poskusi še enkrat: "
        i = int(input(msg))

    if i == 1:    # haski
        msg = "==star je eno leto.ime mu je Skrabel. lahko ga dresiraš ampak najprej ga moraš nahraniti.\n" \
              "pritisni 1 da ga nahraniš: "
    elif i == 2:  # ovcar
        msg = "==stara je eno leto.ime mu je Daja. lahko jo dresiraš ampak najprej jo moraš nahraniti.\n" \
              "pritisni 1 da jo nahraniš:"
    # tu naredis se za ostale kuze
    # elif i == 3 ....

    # hranjenje
    i = int(input(msg))
    while i != 1:
        i = int(input("==oh če pa tega nezmoraš pa si res malo čuknjen"))


start()
