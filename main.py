from config import*
from controller.scale.scale import*

p.mixer.init()
start_music()

tail_draw(tail)
resurse_draw()
fortress_draw()
while True:
    keys = p.key.get_pressed()
    #screen.fill(WHITE)
    
    if keys[p.K_q]:  save_save_data()
    if keys[p.K_w]:  tail = save_loaded_data()



        
    for event in p.event.get():
        if event.type == p.QUIT: p.quit(); sys.exit()
        elif event.type == p.MOUSEBUTTONDOWN and event.button == 1: mouse_x, mouse_y = event.pos; info(mouse_x, mouse_y)
        elif event.type == p.USEREVENT and event.user_type == p.mixer.SOUND_END: play_next_music()
        elif event.type == p.MOUSEBUTTONDOWN and event.button == 3:
            mouse_x, mouse_y = event.pos    
            for t in tail:
                if t.rect.collidepoint(mouse_x, mouse_y):
                    fortress_list.append(fortress(t.x, t.y))
    
        elif event.type == p.MOUSEBUTTONDOWN:
            if event.button == 4:
                scale_plus()
                tail_draw(tail)
                resurse_draw()
                fortress_draw()
            elif event.button == 5:
                scale_minus()
                tail_draw(tail)
                resurse_draw()
                fortress_draw()

    if keys[p.K_a]: 
        camera_moving_left()
        tail_draw(tail)
        resurse_draw()
        fortress_draw()
    if keys[p.K_d]: 
        camera_moving_right()
        tail_draw(tail)
        resurse_draw()
        fortress_draw()

    fps = clock.get_fps()
    print("FPS:", fps)
                
        
    p.display.flip()
    clock.tick(FPS)
