from controller.module.module import*

current_dir = os.path.dirname(__file__)
music_dir = os.path.join(current_dir, 'music')

music_paths = []
for filename in os.listdir(music_dir):
    if filename.endswith('.mp3'):
        music_path = os.path.join(music_dir, filename)
        music_paths.append(music_path)

p.mixer.init()

musics = []
for music_path in music_paths:
    music = p.mixer.Sound(music_path)
    musics.append(music)

current_music_index = 0

def play_next_music():
    global current_music_index
    if current_music_index < len(musics):
        current_music = musics[current_music_index]
        current_music.play()
        current_music_index += 1

def start_music():
    play_next_music()

