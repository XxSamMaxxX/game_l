from config import*
from controller.scale.scale import*
#Сделать отрисовку группы в отдельном файле и поделать тестики
#Сделать отрисовку только видимых объектов
#Оптимизировать математические формулы передвижения объектов
#Что-то решить с обработкой фотографий

p.mixer.init()
start_music()


time_since_last_execution = 0
execution_interval = 250
menu_active = 1
menu = Menu()

while True:


    if menu_active != 1:
        keys = p.key.get_pressed()
        if keys[p.K_q]:  save_save_data()
        if keys[p.K_r]:  tail = save_loaded_data()
        

            
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                sys.exit()
            elif event.type == p.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = event.pos
                #info(mouse_x, mouse_y)
            elif event.type == p.USEREVENT and event.user_type == p.mixer.SOUND_END:
                play_next_music()
            elif event.type == p.MOUSEBUTTONDOWN and event.button == 3:
                mouse_x, mouse_y = event.pos
                for t in tail:
                    if t.rect.collidepoint(mouse_x, mouse_y):
                        fortress_list.append(fortress(t.x, t.y))
                        fortress_draw()

        
        
        #fps = clock.get_fps()
        #print("FPS:", fps)

        p.display.flip()
        clock.tick(FPS)
    else:
              
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                sys.exit()     
            elif event.type == p.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = event.pos
                if menu.btn_play(mouse_x, mouse_y):
                    
                    menu_active = 0
                    tail_draw(tail)
                    resurse_draw()
        time_since_last_execution += clock.get_time()

        if time_since_last_execution >= execution_interval:
            time_since_last_execution = 0  # Сброс времен
            menu.animation_play()
            menu.draw()
        p.display.flip()
        clock.tick(FPS)
