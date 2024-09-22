from time import sleep
class Video:
    def __init__(self, title: str, duration: int, adult_mode=False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        self.time_now = None

    def __repr__(self) -> str:
        return f"{self.title}"


class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.hash_password = hash(password)
        self.age = age

    def __repr__(self) -> str:
        return self.nickname

class UrTube:
    def __init__(self):
        self.videos: list[Video] = []  # Пустой список видео изначально
        self.users = list[User]
        self.current_user: User | None = None

    def add(self, *args: Video):  # Вызов экземпляра
        self.videos.extend(args)

    def get_videos(self, search_string) -> list[Video]:
        result = []
        for video in self.videos:
            if search_string.lower() in video.title.lower():
                result.append(video)
        return result

    def watch_video(self, video_title: str):
        if not self.current_user:
            print("Вы не авторизованы")
        video_to_watch = None
        for video in self.videos:
            if video.title == video_title:
                video_to_watch = video
                break
        if not video_to_watch:
            print("404 Такого видео не существует")
            return
        if video_to_watch.adult_mode and self.current_user.age < 18:
            print("Вы не можете посмотреть данное видео")
            return
        for sec in range(video.duration, -1, -1):
            print(sec)
            sleep(1)

    def _check_password(user: User, password: str):
        return user.hash_password == hash(password)

    def register(self, nickname: str, password: str, age: int):
        for user in self.user:
            if user.nickname == nickname:
                print(f"Пользователь с ником {nickname} существует!")
                return
        user = User(nickname, password, age)
        self.users.append(user)
        self.current_user = user

    def log_in(self, nickname, password):
        log_in_user = None
        for user in self.users:
            if user.nickname == nickname:
                log_in_user = user
                break
        if not log_in_user:
            print(f"Пользователь с ником {nickname} не найден")
            return
        if not self._check_password(log_in_user, password):
            print(f"Неверный пароль")
            return
        self.current_user = log_in_user
        print("Вы авторизованы")

    def log_out(self):
        self.current_user = None
        print("Вы вышли")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
