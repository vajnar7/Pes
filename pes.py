import pyglet
from pyglet.window import key

# Stringi
a0 = "Si želiš imeti psa? 1=ja, 2=ne"

a1 = "Super! Pojdi v zavetišče za živali. Da bi izvedel kje je moraš rešiti uganko:\n Brat mojega brata ima" \
     "očeta januša. januš ima hčerko Angelino. Angelinin dedek je poročen z Evo. Skupaj imata tri otroke.\n" \
     "eden od otrok je Toni. Kaj je meni Toni?:\n" \
     "1= brat\n2= stric\n3= dedek\n4= pradedek"

b1 = "Dobro! prišel si do zavetišča. katerega psa bi rad?\n" \
     "1-haskija\n2-nemškega ovčarja\n3-bordarkolija\n4-kavalirja karla charelsa"

c1 = "Ne upoštevaš pravil! poskusi še enkrat: "

d1 = "Star je eno leto. Ime mu je Skrabel. Lahko ga dresiraš ampak najprej ga moraš nahraniti." \
     "\nPritisni 1 da ga nahraniš!"

d2 = "Stara je eno leto. ime ji je Daja. Lahko jo dresiraš ampak najprej jo moraš nahraniti." \
     "\nPritisni 1 da jo nahraniš:"

d3 = "Star je eno leto. Ime mu je Nek. Lahko ga dresiraš ampak najprej ga moraš nahraniti." \
     "\nPritisni 1 da ga nahraniš:"

e1 = "Oh če pa tega nezmoraš pa si res malo čuknjen!"

f1 = "Ok. Zdaj ga moraš peljati na sprehod. Kam boš šel?\n" \
     "1=hribi\n2=gozd\n3=travnik\n4=ne grem na sprehod"

# Globalne spremenljivke
poglavje = 1
kuza = ""

window = pyglet.window.Window()
label = pyglet.text.Label(a0,
                          font_name='Times New Roman',
                          font_size=15,
                          color=(255, 0, 0, 255),
                          y=window.height - 20,
                          width=window.width,
                          multiline=True)

picture_haski = pyglet.resource.image('haski.jpg')
picture_ovcar = pyglet.resource.image('ovcar.jpg')


@window.event
def on_draw():
    window.clear()
    label.draw()
    if kuza is "haski":
        picture_haski.blit(window.width // 2, 0)
    elif kuza is "ovcar":
        picture_ovcar.blit(window.width // 2, 0)
    else:
        picture_haski.blit(window.width // 2, 0)


@window.event
def on_key_press(symbol, modifiers):
    global poglavje
    global kuza
    if poglavje == 1:
        if symbol == key._1:
            label.text = a1  # uganka
            poglavje = 2
        elif symbol == key._2:  # noces psa
            exit()

    elif poglavje == 2:
        if symbol == key._2:
            label.text = b1  # uganka resena
            poglavje = 3
        else:
            label.text = "NOPE!!!"

    elif poglavje == 3:
        if symbol == key._1:
            label.text = d1  # haski
            poglavje = 4
            kuza = "haski"
        elif symbol == key._2:
            label.text = d2  # ovcar
            poglavje = 4
            kuza = "ovcar"
        elif symbol == key._3:
            label.text = d3  # bordarkoli
            poglavje = 4
            kuza = "bordarkoli"

    elif poglavje == 4:
        if symbol != key._1:
            label.text = e1
        elif symbol == key._1:
            label.text = f1   # Sprehod
            poglavje = 5

    elif poglavje == 5:
        if symbol == key._1:  # hribi
            label.color = (2, 200, 200, 255)
            label.text = "Od tu naprej pa delaj naprej sama, pa Happy Coding\n" \
                         "Dopolni[ lahko vsako poglavje s slikcami v funkciji onDraw\n" \
                         "Example za kuza ze imas. Naj ti da domisljija duska.\n" \
                         "Ce mas vprasanje kr upras!"


pyglet.app.run()
