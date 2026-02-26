import pygame
import sys
from game import Game

def main():
    pygame.init()
    pygame.display.set_caption("Type & Slayer - Рогалик с печатью")

    # Настройки экрана
    screen_info = pygame.display.Info()
    WINDOW_WIDTH = 1024
    WINDOW_HEIGHT = 768

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    
    # Установка иконки (если есть)
    try:
        icon = pygame.Surface((32, 32))
        icon.fill((100, 200, 255))
        pygame.display.set_icon(icon)
    except:
        pass

    # Создание игры
    game = Game(screen, WINDOW_WIDTH, WINDOW_HEIGHT)

    # Основной цикл
    running = True
    while running:
        dt = clock.tick(60) / 1000.0  # Дельта времени в секундах (макс 60 FPS)

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False  # Выход по ESC
                elif event.key == pygame.K_F11:
                    # Переключение полноэкранного режима (для будущего обновления)
                    pass
            game.handle_event(event)

        # Обновление логики игры
        game.update(dt)
        
        # Отрисовка
        game.draw()
        pygame.display.flip()

    pygame.quit()
    sys.exit()

def handle_exceptions():
    """Обработчик исключений для отладки"""
    try:
        main()
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        import traceback
        traceback.print_exc()
        pygame.quit()
        sys.exit(1)

if __name__ == "__main__":
    # Запуск с обработкой ошибок
    handle_exceptions()