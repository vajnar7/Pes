import pyglet

window = pyglet.window.Window()



# ==najberž je šlo za napako. poskusi še enkrat:"))  ---- to je za kopirat
w = int(input("==si želiš imeti psa? 1==ja, 2==ne:"))

if w ==1:
    a = int(input("==super!pojdi v zavetišče za živali. da bi izvedel kje je moraš rešiti uganko: brat mojega brata ima očeta januša. januš ima hčerko angelino. angelinin dedek je poročen z evo. skupaj imata tri otroke. eden od otrok je toni. kaj je meni toni?: 1= brat, 2= stric, 3= dedek, 3= pradedek:"))
    if a == 2:
        b= int(input("==dobro! prišel si do zavetišča. katerega psa bi rad? 1-haskija 2-nemškega ovčarja 3-bordarkolija 4-kavalirja karla charelsa ?:"))
        if b > 4:
            b = int(input("==ne upoštevaš pravil! poskusi še enkrat:"))
# 1==1_prvi sprehod in začetki_____________________________________________________________________
        if b ==1:
            c = int(input("==star je eno leto.ime mu je Skrabel. lahko ga dresiraš ampak najprej ga moraš nahraniti. pritisni 1 da ga nahraniš:"))
            if c != 1:
                print ("==oh če pa tega nezmoraš pa si res malo čuknjen")                
            if c ==1:
                d = int(input("==ok. zdaj ga moraš peljati na sprehod. kam boš šel? 1=hribi, 2=gozd, 3=travnik, 4=ne grem na sprehod:"))
                if d ==4:
                    e =int(input("==tega pa ne smeš narediti drugače ti bomo vzeli psa. 1=hribi, 2=gozd, 3=travnik, 4=vseeno ne grem na sprehod:"))
                    if e == 4:
                        print ("==uzeli smo ti psa!")
                    if e > 4:
                       sh = print("==tega ne smeš")                            
                if d > 4:
                    ch = int(input("==tega ne smeš. daj še enkrat:"))
                    if ch > 3:
                        print ("==ti si sploh ne zaslužiš psa")
                if d or e or ch == 1 or 2 or 3:
                    f = int(input("==dober sprehod zdaj pa je čas za spanje.pritisni 1:"))
                    if f != 1:
                        print ("==resno. tega nezmoreš")
                    if f == 1:
                        g = int(input("==zdaj se je Skrabel naspal. ampak nikjer ga ne najdeš. da izveš kje je moraš rešiti to uganko: nekje je prostor v hiši kamor se tvoj pes rad skrije. to je tam kjer je dovolj toplo in je dovolj vode. vendar če bo poskušal piti vodo bo padel vanjo in za vsak slučaj preden si umiješ zobe preveri če niso na njej pasje dlake. kje je to? 1=kuhinja 2=dnevna soba 3=kopalnica 4=pred soba:"))
                        if g != 3:
                            print ("==narobe! neboš več našel psa")
                            #hrana
                        if g == 3:
                            h = int(input("== našel si psa. zdaj ga nahrani z briketi številka 1, 2 ali 3:"))
#1==2_drugi dan________________________________________________________                            
                            if h > 3:
                                h = int(input("==najberš je šlo za napako. poskusi še enkrat:"))
                            #sprehod_2
                            if h < 4:
                                i = int(input("==čas za sprehod.kam boš šel zdaj. pozor ne smeš isto kot včeraj. 1=hribi, 2=gozd, 3=travnik:"))
                                if i > 3:
                                    i = int(input("==najberš je šlo za napako. poskusi še enkrat:")) 
                                if i== d :
                                    i = int(input("==rečeno je bilo da nasmeš na enak sprehod. daj še enkrat:"))
                                    if i > 3:
                                        print ("==težko rečem da je to še ena napaka. izgubil si")
                                if i != d and i < 4:
                                    if d == 4:
                                        if i == e:
                                            i = int(input("==rečeno je bilo da nasmeš na enak sprehod. daj še enkrat:"))
                                            if i > 3:
                                                print ("==tega nimaš na izbiro. izgubil si")
                                        if i != e:
                                            j = int(input("==zdaj, ko si prišel iz sprehoda ga lahko treniraš. 1=treniral ga bom, 2=ne bom ga treniral:"))
                                    if d != 4:
                                        j = int(input("==zdaj, ko si prišel iz sprehoda ga lahko treniraš. 1=treniral ga bom, 2=ne bom ga treniral:"))
#1==3_dresiranje_____________________________________________________________________                                    
                                        if j != 1 and 2:
                                            j = int(input("==najberž je šlo za napako. poskusi še enkrat"))
                                        if j == 2:
                                            #KONEC
                                            k = int(input("==ok. pa ne. v tem primer u si zaključil z vajami zate tu je legenda."))
                                            print("1==POSEBNA HRANA ZA PSE")
                                            print("2==SPREHOD")
                                            print("3==NOČEM VEČ IMETI PSA")
                                            print("4==IGRAL SE BOM S PSOM")
                                            #k = ASDFGH
                                            if k == 1 or 2 or 4:
                                                k = int(input("SUPER. še vedno lahko izbiraš kaj boš delal:"))
                                                if k == 1 or 2 or 4:
                                                    k = int(input("SUPER. še vedno lahko izbiraš kaj boš delal:"))
                                                    if k == 1 or 2 or 4:
                                                        k = int(input("SUPER. še vedno lahko izbiraš kaj boš delal:"))
                                                        if k == 1 or 2 or 4:
                                                            k = int(input("SUPER. še vedno lahko izbiraš kaj boš delal:"))
                                                            if k == 1 or 2 or 4:
                                                                k = int(input("SUPER. še vedno lahko izbiraš kaj boš delal:"))
                                                                if k == 1 or 2 or 4:
                                                                    k = int(input("SUPER. še vedno lahko izbiraš kaj boš delal:"))
                                                                    if k == 1 or 2 or 4:
                                                                        print("super smo se zabavali a zdaj mora pes oditi ker je bil pri tebi le začasno. ADIJO")
                                            if k ==4:
                                                print ("prav uzeli smo ti psa") 
                                        if j == 1:
                                            l = int(input("==v redu.začni z: 1== glas ali 2== tačka:"))
                                            if l != 1 and 2:
                                                l = int(input("==najberž je šlo za napako. poskusi še enkrat"))
                                            if l ==1:
                                                print("==HOW! HOW! HOW!")
                                            if l ==2:
                                                print("   ")
                                                print("         **")
                                                print("  **    ****     **")
                                                print("****** ******  ******")
                                                print("*********************")
                                                print("*********************")
                                                print("*********************")
                                                print(" *******************")
                                                print("  *****************")
                                                print("   ***************")
                                                print("     ***********")
                                                print("       *******")
#1==4_priboljšek____________________________________________________________________________
                                            m = int(input("==dobro. zdaj mu daj priboljšek, da bo vedel da je tako prav. pritisni 4, 5 ali 6:"))
                                        if m == 1 or 2 or 3:
                                            m=int(input("==te možnosti pa nimaš. daj mu poosebne priboljške za treniranje psov(4, 5, 6):"))
                                        if m > 6:
                                            m = int(input("teh priboljškov pa še nimaš. izberi še enkrat:"))
                                            if m == 1 or 2 or 3:
                                                m=int(input("==te možnosti pa nimaš. daj mu poosebne priboljške za treniranje psov(4, 5, 6):"))
                                            if m > 6:
                                                print ("==joj, če ne upoštevaš pravil ti vzememo psa")
                                        if m == 1 or 2 or 3:
#1==5_nekineki________________________________________________________________________________________                                            
                                            n = int(input("==zagotovo se mu je zdelo slastno. zdaj pa je čas za kosilo. izberi mu kaj naj je daj mu posebno mešanico za pse tako da pritisneš 7:"))
                                            if n != 7:
                                                na = int(input("==najberž je šlo za napako. poskusi še enkrat:"))
                                                if na != 7:
                                                    print("težko račem da je šlo za napako. izgubil si")
                                            if n == 7:
                                                o =int(input("JKLČĆŽ"))
                                            if n != 7:
                                                if na ==7:
                                                    o = int(input("JKLČĆŽ"))
#2==1_začetki_______________________________________________________________________                            
        if b ==2:
            c = int(input("==stara je eno leto.ime mu je Daja. lahko jo dresiraš ampak najprej jo moraš nahraniti. pritisni 1 da jo nahraniš:"))
            if c != 1:
                print ("==oh če pa tega nezmoraš pa si res malo čuknjen")                
            if c ==1:
                d = int(input("==ok. zdaj jo moraš peljati na sprehod. kam boš šel? 1=hribi, 2=gozd, 3=travnik, 4=ne grem na sprehod:"))
                if d ==4:
                    e =int(input("==tega pa ne smeš narediti drugače ti bomo vzeli psa. 1=hribi, 2=gozd, 3=travnik, 4=vseeno ne grem na sprehod:"))
                    if e == 4:
                        print ("==uzeli smo ti psa!")
                    if e > 4:
                       sh = print("==tega ne smeš")                            
                if d > 4:
                    ch = int(input("==tega ne smeš. daj še enkrat:"))
                    if ch > 3:
                        print ("==ti si sploh ne zaslužiš psa")
                if d or e or ch == 1 or 2 or 3:
                    f = int(input("==dober sprehod zdaj pa je čas za spanje.pritisni 1:"))
                    if f != 1:
                        print ("==resno. tega nezmoreš")
                    if f == 1:
                        g = int(input("==zdaj se je Daja naspala. ampak nikjer je ne najdeš. da izveš kje je moraš rešiti to uganko: nekje je prostor v hiši kamor se tvoj pes rad skrije. to je tam kjer je dovolj toplo in je dovolj vode. vendar če bo poskušal piti vodo bo padel vanjo in za vsak slučaj preden si umiješ zobe preveri če niso na njej pasje dlake. kje je to? 1=kuhinja 2=dnevna soba 3=kopalnica 4=pred soba:"))
                        if g != 3:
                            print ("==narobe! neboš več našel psa")
                            #hrana
                        if g == 3:
                            h = int(input("== našel si psa. zdaj ga nahrani z briketi številka 1, 2 ali 3:"))

#2==2___________________________________________________________________
                            if h > 4:
                                h = int(input("==najberš je šlo za napako. poskusi še enkrat:"))
                            #sprehod_2
                            if h < 4:
                                i = int(input("==čas za sprehod.kam boš šel zdaj. pozor ne smeš isto kot včeraj. 1=hribi, 2=gozd, 3=travnik:"))
                                if i > 3:
                                    i = int(input("==najberš je šlo za napako. poskusi še enkrat:")) 
                                if i== d :
                                    i = int(input("==rečeno je bilo da nasmeš na enak sprehod. daj še enkrat:"))
                                    if i > 3:
                                        print ("==težko rečem da je to še ena napaka. izgubil si")
                                if i != d and i < 3:
                                    if d == 4:
                                        if i == e:
                                            i = int(input("==rečeno je bilo da nasmeš na enak sprehod. daj še enkrat:"))
                                            if i > 3:
                                                print("==tega nesmeš. izgubil si.")
                                            if i == e:
                                                print ("==joj ti bedak. tega nemoreš. izgubil si")
                                        if i != e:
                                            j = int(input("==zdaj, ko si prišel iz sprehoda ga lahko treniraš. 1=treniral jo bom, 2=ne bom je treniral:"))
                            #dresiranje_e___________________________________________________________
                                            if j == 2:
                                                #KONEC
                                                k = int(input("==ok. pa ne. v tem primer u si zaključil z vajami zate tu je legenda."))
                                                print("1==POSEBNA HRANA ZA PSE")
                                                print("2==SPREHOD")
                                                print("3==NOČEM VEČ IMETI PSA")
                                                print("4==IGRAL SE BOM S PSOM")
                                                #k = ASDFGH
                                                if k == 1 or 2 or 4:
                                                    k = int(input("SUPER. še vedno lahko izbiraš kaj boš delal:"))
                                                    if k == 1 or 2 or 4:
                                                        k = int(input("SUPER. še vedno lahko izbiraš kaj boš delal:"))
                                                        if k == 1 or 2 or 4:
                                                            k = int(input("SUPER. še vedno lahko izbiraš kaj boš delal:"))
                                                            if k == 1 or 2 or 4:
                                                                k = int(input("SUPER. še vedno lahko izbiraš kaj boš delal:"))
                                                                if k == 1 or 2 or 4:
                                                                    k = int(input("SUPER. še vedno lahko izbiraš kaj boš delal:"))
                                                                    if k == 1 or 2 or 4:
                                                                        k = int(input("SUPER. še vedno lahko izbiraš kaj boš delal:"))
                                                                        if k == 1 or 2 or 4:
                                                                            print("super smo se zabavali a zdaj mora pes oditi ker je bil pri tebi le začasno. ADIJO")
                                                if k ==4:
                                                    print ("prav uzeli smo ti psa") 
                                        if j == 1:
                                            #k je za kasneje ASDDFGH
                                            l = int(input("==v redu.začni z: 1== glas ali 2== tačka:"))
                                            if l ==1:
                                                print("==HOW! HOW! HOW!")
                                                m = int(input("==dobro. zdaj ji daj priboljšek,da bo vedela  da je tako prav.pritisni 4, 5 ali 6:"))
                                            if l ==2:
                                                print("          ")
                                                print("         **")
                                                print("  **    ****     **")
                                                print("****** ******  ******")
                                                print("*********************")
                                                print("*********************")
                                                print(" *******************")
                                                print("  *****************")
                                                print("  *****************")
                                                print("   ***************")
                                                print("     ***********")
                                                print("       *******")
                                    if d != 4:               
#2==3_dresiranje___________________________________________________________________________
                                        j = int(input("==zdaj, ko si prišel iz sprehoda jo lahko treniraš. 1=treniral jo bom, 2=ne bom je treniral:"))
                                        if j == 2:
                                            k = int(input("==ok. pa ne. ASDFGH."))
                                        if j == 1:
                                            #k je za kasneje ASDDFGH
                                            l = int(input("==v redu.začni z: 1== glas ali 2== tačka:"))
                                            if l ==1:
                                                print("==HOW!HOW!HOW!")
                                            if l ==2:
                                                print(" ")
                                                print("         **")
                                                print("  **    ****     **")
                                                print("****** ******  ******")
                                                print("*********************")
                                                print("*********************")
                                                print(" *******************")
                                                print("  *****************")
                                                print("  *****************")
                                                print("   ***************")
                                                print("     ***********")
                                                print("       *******")
                                        #if d ==4:
                                            #if
#2==4_priboljšek____________________________________________________________________________
                                            m = int(input("==dobro. zdaj ji daj priboljšek, da bo vedela da je tako prav. pritisni 4, 5 ali 6:"))
                                        if m <4:
                                            m=int(input("==te možnosti pa nimaš. daj ji poosebne priboljške za treniranje psov(4, 5, 6):"))
                                        if m > 6:
                                            m = int(input("teh priboljškov pa še nimaš. izberi še enkrat:"))
                                            if m <4:
                                                m=int(input("==te možnosti pa nimaš. daj ji poosebne priboljške za treniranje psov(4, 5, 6):"))
                                            if m > 6:
                                                print ("joj, če ne upoštevaš pravil ti vzememo psa")
                                        if m < 7 and m > 3:
                                            n = int(input("zagotovo se ji je zdelo slastno. "))
                                                                               
#3==1_začetki_______________________________________________________________________                   
        if b ==3:
            c = int(input("==star je eno leto.ime mu je Nek. lahko ga dresiraš ampak najprej ga moraš nahraniti. pritisni 1 da ga nahraniš:"))
            if c != 1:
                print ("==oh če pa tega nezmoraš pa si res malo čuknjen")                
            if c ==1:
                d = int(input("==ok. zdaj ga moraš peljati na sprehod. kam boš šel? 1=hribi, 2=gozd, 3=travnik, 4=ne grem na sprehod:"))
                if d ==4:
                    e =int(input("==tega pa ne smeš narediti drugače ti bomo vzeli psa. 1=hribi, 2=gozd, 3=travnik, 4=vseeno ne grem na sprehod:"))
                    if e == 4:
                        print ("==uzeli smo ti psa!")
                    if e > 4:
                       sh = print("==tega ne smeš")                            
                if d > 4:
                    ch = int(input("==tega ne smeš. daj še enkrat:"))
                    if ch > 3:
                        print ("==ti si sploh ne zaslužiš psa")
                if d or e or ch == 1 or 2 or 3:
                    f = int(input("==dober sprehod zdaj pa je čas za spanje.pritisni 1:"))
                    if f != 1:
                        print ("==resno. tega nezmoreš")
                    if f == 1:
                        g = int(input("==zdaj se je Nek naspal. ampak nikjer ga ne najdeš. da izveš kje je moraš rešiti to uganko: nekje je prostor v hiši kamor se tvoj pes rad skrije. to je tam kjer je dovolj toplo in je dovolj vode. vendar če bo poskušal piti vodo bo padel vanjo in za vsak slučaj preden si umiješ zobe preveri če niso na njej pasje dlake. kje je to? 1=kuhinja 2=dnevna soba 3=kopalnica 4=pred soba:"))
                        if g != 3:
                            print ("==narobe! neboš več našel psa")
                            #hrana
                        if g == 3:
                            h = int(input("== našel si psa. zdaj ga nahrani z briketi številka 1, 2 ali 3:"))
#3==2_drugi dan________________________________________________________                            
                            if h > 3:
                                h = int(input("==najberš je šlo za napako. poskusi še enkrat:"))
                            #sprehod_2
                            if h < 4:
                                i = int(input("==čas za sprehod.kam boš šel zdaj. pozor ne smeš isto kot včeraj. 1=hribi, 2=gozd, 3=travnik:"))
                                if i > 3:
                                    i = int(input("==najberš je šlo za napako. poskusi še enkrat:")) 
                                if i== d :
                                    i = int(input("==rečeno je bilo da nasmeš na enak sprehod. daj še enkrat:"))
                                    if i > 3:
                                        print ("==težko rečem da je to še ena napaka. izgubil si")
                                if i != d and i < 4:
                                    if d == 4:
                                        if i == e:
                                            i = int(input("==rečeno je bilo da nasmeš na enak sprehod. daj še enkrat:"))
                                            if i > 3:
                                                print ("==tega nimaš na izbiro. izgubil si")
                                        if i != e:
                                            j = int(input("==zdaj, ko si prišel iz sprehoda ga lahko treniraš. 1=treniral ga bom, 2=ne bom ga treniral:"))
                                    if d != 4:
                                        j = int(input("==zdaj, ko si prišel iz sprehoda ga lahko treniraš. 1=treniral ga bom, 2=ne bom ga treniral:"))
#3==3_dresiranje_____________________________________________________________________                                    
                                        if j != 1 and 2:
                                            j = int(input("==najberž je šlo za napako. poskusi še enkrat"))
                                        if j == 2:
                                            k = int(input("==ok. pa ne. ASDFGH."))
                                        if j == 1:
                                            #k je za kasneje tudi ASDDFGH
                                            l = int(input("==v redu.začni z: 1== glas ali 2== tačka:"))
                                            if l != 1 and 2:
                                                l = int(input("==najberž je šlo za napako. poskusi še enkrat"))
                                            if l ==1:
                                                print("==HOW! HOW! HOW!")
                                            if l ==2:
                                                print("   ")
                                                print("         **")
                                                print("  **    ****     **")
                                                print("****** ******  ******")
                                                print("*********************")
                                                print("*********************")
                                                print("*********************")
                                                print(" *******************")
                                                print("  *****************")
                                                print("   ***************")
                                                print("     ***********")
                                                print("       *******")
#3==4_priboljšek____________________________________________________________________________
                                            m = int(input("==dobro. zdaj mu daj priboljšek, da bo vedel da je tako prav. pritisni 4, 5 ali 6:"))
                                        if m == 1 or 2 or 3:
                                            m=int(input("==te možnosti pa nimaš. daj mu poosebne priboljške za treniranje psov(4, 5, 6):"))
                                        if m > 6:
                                            m = int(input("teh priboljškov pa še nimaš. izberi še enkrat:"))
                                            if m == 1 or 2 or 3:
                                                m=int(input("==te možnosti pa nimaš. daj mu poosebne priboljške za treniranje psov(4, 5, 6):"))
                                            if m > 6:
                                                print ("==joj, če ne upoštevaš pravil ti vzememo psa")
                                        if m == 1 or 2 or 3:
                                            n = int(input("==zagotovo se mu je zdelo slastno. "))
#4==1_začetki_______________________________________________________________________                            
        if b ==4:
            c = int(input("==stara je eno leto.ime mu je Queen. lahko jo dresiraš ampak najprej jo moraš nahraniti. pritisni 1 da jo nahraniš:"))
            if c != 1:
                print ("==oh če pa tega nezmoraš pa si res malo čuknjen")                
            if c ==1:
                d = int(input("==ok. zdaj jo moraš peljati na sprehod. kam boš šel? 1=hribi, 2=gozd, 3=travnik, 4=ne grem na sprehod:"))
                if d ==4:
                    e =int(input("==tega pa ne smeš narediti drugače ti bomo vzeli psa. 1=hribi, 2=gozd, 3=travnik, 4=vseeno ne grem na sprehod:"))
                    if e == 4:
                        print ("==uzeli smo ti psa!")
                    if e > 4:
                       sh = print("==tega ne smeš")                            
                if d > 4:
                    ch = int(input("==tega ne smeš. daj še enkrat:"))
                    if ch > 3:
                        print ("==ti si sploh ne zaslužiš psa")
                if d or e or ch == 1 or 2 or 3:
                    f = int(input("==dober sprehod zdaj pa je čas za spanje.pritisni 1:"))
                    if f != 1:
                        print ("==resno. tega nezmoreš")
                    if f == 1:
                        g = int(input("==zdaj se je Queen naspala. ampak nikjer je ne najdeš. da izveš kje je moraš rešiti to uganko: nekje je prostor v hiši kamor se tvoj pes rad skrije. to je tam kjer je dovolj toplo in je dovolj vode. vendar če bo poskušal piti vodo bo padel vanjo in za vsak slučaj preden si umiješ zobe preveri če niso na njej pasje dlake. kje je to? 1=kuhinja 2=dnevna soba 3=kopalnica 4=pred soba:"))
                        if g != 3:
                            print ("==narobe! neboš več našel psa")
                            #hrana
                        if g == 3:
                            h = int(input("== našel si psa. zdaj ga nahrani z briketi številka 1, 2 ali 3:"))

#4==2___________________________________________________________________
                            if h > 4:
                                h = int(input("==najberš je šlo za napako. poskusi še enkrat:"))
                            #sprehod_2
                            if h < 4:
                                i = int(input("==čas za sprehod.kam boš šel zdaj. pozor ne smeš isto kot včeraj. 1=hribi, 2=gozd, 3=travnik:"))
                                if i > 3:
                                    i = int(input("==najberš je šlo za napako. poskusi še enkrat:")) 
                                if i== d :
                                    i = int(input("==rečeno je bilo da nasmeš na enak sprehod. daj še enkrat:"))
                                    if i > 3:
                                        print ("==težko rečem da je to še ena napaka. izgubil si")
                                if i != d and i < 3:
                                    if d == 4:
                                        if i == e:
                                            i = int(input("==rečeno je bilo da nasmeš na enak sprehod. daj še enkrat:"))
                                            if i > 3:
                                                print("==tega nesmeš. izgubil si.")
                                            if i == e:
                                                print ("==joj ti bedak. tega nemoreš. izgubil si")
                                        if i != e:
                                            j = int(input("==zdaj, ko si prišel iz sprehoda ga lahko treniraš. 1=treniral jo bom, 2=ne bom je treniral:"))
                            #dresiranje_e___________________________________________________________
                                            if j == 2:
                                                k = int(input("==ok. pa ne. ASDFGH."))
                                        if j == 1:
                                            #k je za kasneje ASDDFGH
                                            l = int(input("==v redu.začni z: 1== glas ali 2== tačka:"))
                                            if l ==1:
                                                print("==HOW! HOW! HOW!")
                                                m = int(input("==dobro. zdaj ji daj priboljšek,da bo vedela  da je tako prav.pritisni 4, 5 ali 6:"))
                                            if l ==2:
                                                print("          ")
                                                print("         **")
                                                print("  **    ****     **")
                                                print("****** ******  ******")
                                                print("*********************")
                                                print("*********************")
                                                print(" *******************")
                                                print("  *****************")
                                                print("  *****************")
                                                print("   ***************")
                                                print("     ***********")
                                                print("       *******")
                                    if d != 4:               
#4==3_dresiranje___________________________________________________________________________
                                        j = int(input("==zdaj, ko si prišel iz sprehoda jo lahko treniraš. 1=treniral jo bom, 2=ne bom je treniral:"))
                                        if j == 2:
                                            k = int(input("==ok. pa ne. ASDFGH."))
                                        if j == 1:
                                            #k je za kasneje ASDDFGH
                                            l = int(input("==v redu.začni z: 1== glas ali 2== tačka:"))
                                            if l ==1:
                                                print("==HOW!HOW!HOW!")
                                            if l ==2:
                                                print(" ")
                                                print("         **")
                                                print("  **    ****     **")
                                                print("****** ******  ******")
                                                print("*********************")
                                                print("*********************")
                                                print(" *******************")
                                                print("  *****************")
                                                print("  *****************")
                                                print("   ***************")
                                                print("     ***********")
                                                print("       *******")
                                        #if d ==4:
                                            #if
#4==4_priboljšek____________________________________________________________________________
                                            m = int(input("==dobro. zdaj ji daj priboljšek, da bo vedela da je tako prav. pritisni 4, 5 ali 6:"))
                                        if m <4:
                                            m=int(input("==te možnosti pa nimaš. daj ji poosebne priboljške za treniranje psov(4, 5, 6):"))
                                        if m > 6:
                                            m = int(input("teh priboljškov pa še nimaš. izberi še enkrat:"))
                                            if m <4:
                                                m=int(input("==te možnosti pa nimaš. daj ji poosebne priboljške za treniranje psov(4, 5, 6):"))
                                            if m > 6:
                                                print ("joj, če ne upoštevaš pravil ti vzememo psa")
                                        if m < 7 and m > 3:
                                            n = int(input("zagotovo se ji je zdelo slastno. "))
                                                                               
                                            
#naprej________________________________________________________________________
                                        
    if a != 2:
        print ("==narobe. nemoreš posvojiti psa.")
if w ==2:
    print ("==ok. potem pa ne")
if w > 2:
    print ("==ne upoštevaš pravil!")



