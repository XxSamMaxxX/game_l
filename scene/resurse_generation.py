from map.tail.script.tail import*
def resurse_draw():
    if wood:
        for w in wood:
            w.draw()
    if iron:
        for i in iron:
            i.draw()
    if wheat:
        for w in wheat:
            w.draw()
    if metal:
        for m in metal:
            m.draw()

  