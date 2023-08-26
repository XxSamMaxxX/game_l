from config import*

while True:
    screen.fill(WHITE)
    for t in tail:
        t.draw()
    if wood:
        for w in wood:
            w.draw()
    if iron:
        for i in iron:
            i.draw()
    if wheat:
        for w in wheat:
            w.draw()

    keys = p.key.get_pressed()
        
    for event in p.event.get():
        if event.type == p.QUIT: p.quit(); sys.exit()
        elif event.type == p.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            for t in tail:
                if t.rect.collidepoint(mouse_x, mouse_y):
                    if t.wood:
                        print("Наличие дерева на ячейке:", t.wood)
                    else:
                        print("Наличие дерева на ячейке:", t.wood)
    
        
    p.display.flip()
    clock.tick(FPS)
