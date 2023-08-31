from config import*
from controller.scale.scale import*
#Сделать отрисовку группы в отдельном файле и поделать тестики
#Сделать отрисовку только видимых объектов
#Оптимизировать математические формулы передвижения объектов
#Что-то решить с обработкой фотографий

p.mixer.init()
start_music()

visible_objects = [] 
camera = Camera(WIDTH, HEIGHT)
buffer_surface = p.Surface((WIDTH, HEIGHT))

#tail_draw(tail)


#resurse_draw()
#fortress_draw()
while True:
    visible_objects = [] 
    keys = p.key.get_pressed()
    
    
    if keys[p.K_q]:  save_save_data()
    if keys[p.K_r]:  tail = save_loaded_data()
    

        
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            sys.exit()
        elif event.type == p.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            info(mouse_x, mouse_y)
        elif event.type == p.USEREVENT and event.user_type == p.mixer.SOUND_END:
            play_next_music()
        elif event.type == p.MOUSEBUTTONDOWN and event.button == 3:
            mouse_x, mouse_y = event.pos
            for t in tail:
                if t.rect.collidepoint(mouse_x, mouse_y):
                    fortress_list.append(fortress(t.x, t.y))
        elif event.type == p.MOUSEBUTTONDOWN:
            if event.button == 4:
                camera.scale_plus()
            elif event.button == 5:
                camera.scale_minus()


    if keys[p.K_a]:
        camera.move_left()
        buffer_surface.fill(WHITE)
        for t in tile_group:
            scaled_x, scaled_y = t.calculate_scaled_coordinates(camera)
            scaled_size = int(t.sprite_px * camera.scale)
            
            if camera.is_point_visible(scaled_x, scaled_y):
                visible_objects.append((t, scaled_x, scaled_y, scaled_size))  # Добавляем объект в список видимых
    
        for t, scaled_x, scaled_y, scaled_size in visible_objects:
            t.draw_to_buffer(buffer_surface, camera)
    elif keys[p.K_d]:
        camera.move_right()
        buffer_surface.fill(WHITE)
        for t in tile_group:
            scaled_x, scaled_y = t.calculate_scaled_coordinates(camera)
            scaled_size = int(t.sprite_px * camera.scale)
            
            if camera.is_point_visible(scaled_x, scaled_y):
                visible_objects.append((t, scaled_x, scaled_y, scaled_size))  # Добавляем объект в список видимых
    
        for t, scaled_x, scaled_y, scaled_size in visible_objects:
            t.draw_to_buffer(buffer_surface, camera)
    elif keys[p.K_w]:
        buffer_surface.fill(WHITE)
        camera.move_up()
        for t in tile_group:
            scaled_x, scaled_y = t.calculate_scaled_coordinates(camera)
            scaled_size = int(t.sprite_px * camera.scale)
            
            if camera.is_point_visible(scaled_x, scaled_y):
                visible_objects.append((t, scaled_x, scaled_y, scaled_size))  # Добавляем объект в список видимых
    
        for t, scaled_x, scaled_y, scaled_size in visible_objects:
            t.draw_to_buffer(buffer_surface, camera)

    elif keys[p.K_s]:
        buffer_surface.fill(WHITE)
        camera.move_down()   
        tile_group.draw(buffer_surface)
        
    
    
    fps = clock.get_fps()
    #print("FPS:", fps)
    screen.blit(buffer_surface, (0, 0))
    print(camera.scale)
              
        
    p.display.flip()
    clock.tick(FPS)
