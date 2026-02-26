import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100
        self.max_health = 100
        self.exp = 0
        self.level = 1
        self.exp_to_next = 100

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def gain_exp(self, amount):
        self.exp += amount
        # Проверка на превышение максимального опыта для текущего уровня
        if self.exp > self.exp_to_next:
            self.exp = self.exp_to_next

    def level_up(self):
        self.level += 1
        self.max_health += 20
        self.health = self.max_health
        self.exp = 0
        self.exp_to_next = int(self.exp_to_next * 1.5)

    def draw(self, screen, font):
        # Рисуем игрока (маленький кораблик/меч)
        color = (100, 200, 255)

        # Тело игрока
        body_rect = pygame.Rect(self.x - 15, self.y - 20, 30, 40)
        pygame.draw.rect(screen, color, body_rect)
        pygame.draw.rect(screen, (255, 255, 255), body_rect, 2)

        # Оружие (меч/носок)
        weapon_points = [
            (self.x + 15, self.y - 10),
            (self.x + 40, self.y - 5),
            (self.x + 40, self.y + 5),
            (self.x + 15, self.y + 10)
        ]
        pygame.draw.polygon(screen, (200, 200, 255), weapon_points)

        # Глаза
        pygame.draw.circle(screen, (255, 255, 255), (self.x - 5, self.y - 10), 3)
        pygame.draw.circle(screen, (255, 255, 255), (self.x + 5, self.y - 10), 3)
        pygame.draw.circle(screen, (0, 0, 0), (self.x - 5, self.y - 10), 1)  # Зрачки
        pygame.draw.circle(screen, (0, 0, 0), (self.x + 5, self.y - 10), 1)

        # Полоска здоровья
        health_width = 50
        health_height = 5
        health_x = self.x - health_width // 2
        health_y = self.y - 30

        # Фон здоровья (серая полоса)
        pygame.draw.rect(screen, (60, 60, 60), (health_x, health_y, health_width, health_height))

        # Текущее здоровье (красная полоса)
        current_health_width = health_width * (self.health / self.max_health)
        if current_health_width > 0:
            pygame.draw.rect(screen, (255, 80, 80), (health_x, health_y, current_health_width, health_height))

        # Отрисовка уровня игрока
        level_text = font.render(f"Lvl: {self.level}", True, (255, 255, 255))
        level_rect = level_text.get_rect(center=(self.x, self.y - 45))
        screen.blit(level_text, level_rect)

    def draw_exp_bar(self, screen):
        """Отрисовка полоски опыта (отдельно от игрока)"""
        exp_width = 200
        exp_height = 10
        exp_x = 10
        exp_y = 10

        # Фон полоски опыта
        pygame.draw.rect(screen, (60, 60, 60), (exp_x, exp_y, exp_width, exp_height))
        
        # Текущий опыт
        current_exp_width = exp_width * (self.exp / self.exp_to_next)
        if current_exp_width > 0:
            pygame.draw.rect(screen, (100, 200, 255), (exp_x, exp_y, current_exp_width, exp_height))

    def is_alive(self):
        """Проверка, жив ли игрок"""
        return self.health > 0

    def heal(self, amount):
        """Восстановление здоровья"""
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health