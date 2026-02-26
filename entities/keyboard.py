import pygame
import time

class VirtualKeyboard:
    def __init__(self, x, y, colors):
        self.x = x
        self.y = y
        self.colors = colors
        self.keys = {}
        self.pressed_keys = {}
        self.press_time = {}

        # Раскладка клавиатуры (ряды)
        self.key_rows = [
            list('qwertyuiop[]'),
            list('asdfghjkl;\' '),
            list('zxcvbnm,./'),
            ['space', 'backspace', 'enter']
        ]

        self.create_keys()

    def create_keys(self):
        """Создание клавиш"""
        key_width = 50
        key_height = 50
        key_margin = 5

        for row_index, row in enumerate(self.key_rows):
            for col_index, key in enumerate(row):
                if key == 'space':
                    # Специальная обработка для пробела
                    x = self.x + 150
                    width = key_width * 5
                elif key == 'backspace':
                    x = self.x + (len(row) - 2) * (key_width + key_margin)
                    width = key_width * 2
                elif key == 'enter':
                    x = self.x + (len(row) - 1) * (key_width + key_margin)
                    width = key_width * 2
                else:
                    x = self.x + col_index * (key_width + key_margin)
                    width = key_width

                y = self.y + row_index * (key_height + key_margin)

                self.keys[key] = {
                    'rect': pygame.Rect(x, y, width, key_height),
                    'char': key,
                    'pressed': False
                }

    def handle_event(self, event):
        """Обработка событий мыши для виртуальной клавиатуры"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for key_char, key_data in self.keys.items():
                if key_data['rect'].collidepoint(mouse_pos):
                    key_data['pressed'] = True
                    self.pressed_keys[key_char] = time.time()
                    self.press_time[key_char] = time.time()
                    return key_char
        
        elif event.type == pygame.MOUSEBUTTONUP:
            pass  # Не сбрасываем сразу, чтобы была анимация
        
        return None

    def update(self, current_time):
        """Обновление состояния клавиш (для анимации нажатия)"""
        keys_to_remove = []
        
        for key_char, press_time in self.press_time.items():
            if current_time - press_time > 0.1:  # 100 мс анимация нажатия
                if key_char in self.keys:
                    self.keys[key_char]['pressed'] = False
                keys_to_remove.append(key_char)
        
        # Безопасное удаление из словаря
        for key_char in keys_to_remove:
            if key_char in self.press_time:
                del self.press_time[key_char]
            if key_char in self.pressed_keys:
                del self.pressed_keys[key_char]

    def draw(self, screen):
        """Отрисовка клавиатуры"""
        # Фон клавиатуры
        keyboard_rect = pygame.Rect(
            self.x - 10,
            self.y - 10,
            800,
            200
        )
        pygame.draw.rect(screen, self.colors['keyboard_bg'], keyboard_rect)
        pygame.draw.rect(screen, (255, 255, 255), keyboard_rect, 2)

        # Отрисовка клавиш
        for key_char, key_data in self.keys.items():
            rect = key_data['rect']

            # Выбор цвета в зависимости от состояния
            if key_data['pressed']:
                color = self.colors['key_pressed']
            elif key_char in ('space', 'enter', 'backspace'):
                color = self.colors['key_special']
            else:
                color = self.colors['key_normal']

            # Рисуем клавишу
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, (255, 255, 255), rect, 1)

            # 3D эффект (небольшая тень)
            shadow_rect = rect.copy()
            shadow_rect.x += 2
            shadow_rect.y += 2
            pygame.draw.rect(screen, (40, 40, 50), shadow_rect, 1)

            # Рисуем символ на клавише
            font = pygame.font.Font(None, 24)
            
            if key_char == 'space':
                text = "ПРОБЕЛ"
            elif key_char == 'backspace':
                text = "⌫"
            elif key_char == 'enter':
                text = "↵"
            else:
                text = key_char.upper()

            text_surface = font.render(text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=rect.center)
            screen.blit(text_surface, text_rect)

    def reset_pressed_keys(self):
        """Сброс состояния нажатых клавиш"""
        for key_data in self.keys.values():
            key_data['pressed'] = False
        self.pressed_keys.clear()
        self.press_time.clear()

    def get_pressed_keys(self):
        """Получение списка нажатых клавиш"""
        return list(self.pressed_keys.keys())