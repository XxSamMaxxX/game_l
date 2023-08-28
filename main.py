from config import*
saved = 0
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
    if fortress_list:
        for f in fortress_list:
            f.draw()
    if metal:
        for m in metal:
            m.draw()

    keys = p.key.get_pressed()
    if keys[p.K_q]:
        save_data()
    if keys[p.K_w] and saved == 0:
        saved = 1
        with open('data.json', 'r') as file:
            data = json.load(file)
            loaded_tails = []  

            for tail_data in data:
                new_tail = tails(saved,tail_data["x"] ,tail_data["y"],tail_data["image"]  )                      
                new_tail.wood = tail_data["wood"]
                new_tail.iron = tail_data["iron"]
                new_tail.wheat = tail_data["wheat"]
                new_tail.metal = tail_data["metal"]

                loaded_tails.append(new_tail) 
        tail = loaded_tails  
        
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
        elif event.type == p.MOUSEBUTTONDOWN and event.button == 3:
            mouse_x, mouse_y = event.pos    
            for t in tail:
                if t.rect.collidepoint(mouse_x, mouse_y):
                    fortress_list.append(fortress(t.x, t.y))
        
    p.display.flip()
    clock.tick(FPS)
