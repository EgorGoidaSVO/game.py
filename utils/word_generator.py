import random

class WordGenerator:
    def __init__(self):
        # Слова по уровням сложности
        self.word_pools = {
            1: ['cat', 'dog', 'sun', 'car', 'book', 'house', 'tree', 'fish', 'bird', 'hand'],
            2: ['python', 'mouse', 'phone', 'table', 'chair', 'green', 'black', 'water', 'fire', 'earth'],
            3: ['keyboard', 'monitor', 'program', 'guitar', 'puzzle', 'dragon', 'knight', 'magic', 'sword', 'shield'],
            4: ['algorithm', 'skeleton', 'dungeon', 'treasure', 'victory', 'journey', 'battle', 'monster', 'legend', 'hero'],
            5: ['programming', 'adventure', 'challenge', 'experience', 'knowledge', 'strength', 'courage', 'destiny', 'eternal', 'mystical']
        }
        
        # Дополнительные слова для расширения
        self.extra_words = {
            1: ['ball', 'star', 'moon', 'cloud', 'rain', 'snow', 'wind', 'rock', 'sand', 'wave'],
            2: ['yellow', 'purple', 'silver', 'copper', 'bronze', 'metal', 'stone', 'grass', 'flower', 'heart'],
            3: ['captain', 'pirate', 'ninja', 'wizard', 'archer', 'hunter', 'ranger', 'paladin', 'cleric', 'rogue'],
            4: ['mountain', 'volcano', 'desert', 'forest', 'jungle', 'ocean', 'island', 'crystal', 'ancient', 'sacred'],
            5: ['incredible', 'fantastic', 'brilliant', 'magnificent', 'spectacular', 'remarkable', 'extraordinary', 'unbelievable', 'sensational', 'phenomenal']
        }

    def get_random_word(self, level):
        """Получение случайного слова для уровня"""
        # Защита от выхода за пределы
        level = min(max(level, 1), 5)  # Ограничиваем уровень от 1 до 5
        
        # С вероятностью 30% берем слово из дополнительного списка
        if random.random() < 0.3:
            pool = self.extra_words[level]
        else:
            pool = self.word_pools[level]
            
        return random.choice(pool)

    def get_word_difficulty(self, word):
        """Определение сложности слова на основе его длины"""
        length = len(word)
        
        if length <= 3:
            return 1
        elif length <= 5:
            return 2
        elif length <= 7:
            return 3
        elif length <= 9:
            return 4
        else:
            return 5

    def get_words_by_difficulty(self, difficulty, count=5):
        """Получение нескольких слов определенной сложности"""
        difficulty = min(max(difficulty, 1), 5)
        
        # Объединяем оба пула слов
        all_words = self.word_pools[difficulty] + self.extra_words[difficulty]
        
        # Возвращаем случайные слова без повторений
        if count > len(all_words):
            count = len(all_words)
            
        return random.sample(all_words, count)

    def add_custom_word(self, word, difficulty):
        """Добавление пользовательского слова в пул"""
        difficulty = min(max(difficulty, 1), 5)
        
        if difficulty in self.extra_words:
            if word not in self.extra_words[difficulty] and word not in self.word_pools[difficulty]:
                self.extra_words[difficulty].append(word.lower())
                return True
        return False

    def get_all_words(self, level=None):
        """Получение всех слов (для отладки или тестирования)"""
        if level is not None:
            level = min(max(level, 1), 5)
            return self.word_pools[level] + self.extra_words[level]
        else:
            all_words = {}
            for lvl in range(1, 6):
                all_words[lvl] = self.word_pools[lvl] + self.extra_words[lvl]
            return all_words