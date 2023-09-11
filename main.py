#СПРАВКА
'''

Версия игры: АЛЬФА 1

Стандартные настройки:

Ширина, Высота экрана = 1920 на 1080
ФПС = 60

ИНФО:

Индекс форта присваивается по номеру тайла на котором он будет стоять
Сохранение идет только Биома
Спрайты рисуются по стандартным настройкам

ЗАДАЧИ ПО КОДУ:

Настроить сохранение
Не работает переключение музыки по ее окончанию
Настроить Разную ширину экрана
Провести оптимизацию внутри тайлов
Создать отдельную сцену для меню
Переместить в какой либо конфиг Индексацию Форта(переменную)
Сделайть гладкую систему добавления построек и иконок внутри тайла

'''

#Подключаем необходимые модули и пути для работы
from config import*
from controller.scale.scale import*

#Включаем музыку в игре
p.mixer.init()
#start_music()


#Задержка в 0.25 секунды
time_since_last_execution = 0
execution_interval = 250


#Меню 0-выкл 1-вкл
menu_active = 0
menu = Menu()


#После запуска сразу отрисовать:
tail_draw(tail)         #Тайлы
resurse_draw()          #Ресурсы на тайлах    


while True:

    #Если меню выключено
    if menu_active != 1:
        #Система сохранения
        keys = p.key.get_pressed()

        if keys[p.K_q]:  save_save_data()
        if keys[p.K_r]:  tail = save_loaded_data()
        #=======================================

        #Выход их игры
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                sys.exit()
        #====================================
        
        #Система входа в мир(клетку)
            elif event.type == p.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = event.pos

                for f in fortress_list:

                    if f.rect.collidepoint(mouse_x, mouse_y):
                        if f.world:    
                            intails(f.index)
                            tail_draw(tail)
                            resurse_draw()
                            fortress_draw()
                    
                        else: 
                        
                            if f.rect.collidepoint(mouse_x, mouse_y):
                                f.world = True
                                world_tail.append(InTails(tail[f.index].image, f.index, tail[f.index].biome))
        #=======================================================================

        #Переключаем музыку если она остановится
            elif event.type == p.USEREVENT and event.user_type == p.mixer.SOUND_END:
                play_next_music()
        #=======================================================================

        #Создаем форт на тайле
            elif event.type == p.MOUSEBUTTONDOWN and event.button == 3:
                mouse_x, mouse_y = event.pos
                fortress_index = -1
                for t in tail:
                    fortress_index +=1
                    if t.build_area.collidepoint(mouse_x, mouse_y):
                        if not t.fortress:
                            fortress_list.append(fortress(t.x, t.y, fortress_index))
                            fortress_draw()
        #=======================================================================
        
        #Отображение фпс
        #fps = clock.get_fps()
        #print("FPS:", fps)
        #=======================================

        p.display.flip()
        clock.tick(FPS)

    #Если меню включено
    else:
        
        #Выход из игры
        for event in p.event.get():
            if event.type == p.QUIT: p.quit();  sys.exit()
        #==================================================
        
        #Если нажать кнопку НОВЫЙ МИР
            elif event.type == p.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = event.pos

                if menu.btn_play(mouse_x, mouse_y):
                    menu_active = 0
                    tail_draw(tail)
                    resurse_draw()
        #================================================================
        
        #Постоянно проигрывать анимацию меню
        time_since_last_execution += clock.get_time()

        if time_since_last_execution >= execution_interval:
            time_since_last_execution = 0  
            menu.animation_play()
            menu.draw()


        p.display.flip()
        clock.tick(FPS)
