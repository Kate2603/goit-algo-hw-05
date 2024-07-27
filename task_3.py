from collections import defaultdict
import timeit

# Алгоритм Боєра-Мура
def boyer_moore(text, pattern):
    def bad_char_heuristic(pattern):
        bad_char = defaultdict(lambda: -1)
        for i, char in enumerate(pattern):
            bad_char[char] = i
        return bad_char

    m = len(pattern)
    n = len(text)
    bad_char = bad_char_heuristic(pattern)
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            return s
        s += max(1, j - bad_char[text[s + j]])
    return -1

# Алгоритм Кнута-Морріса-Пратта
def kmp_search(text, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = compute_lps(pattern)
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            return i - j
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

# Алгоритм Рабіна-Карпа
def rabin_karp(text, pattern):
    d = 256
    q = 101
    M = len(pattern)
    N = len(text)
    i = 0
    j = 0
    p = 0
    t = 0
    h = 1
    result = []

    for i in range(M - 1):
        h = (h * d) % q

    for i in range(M):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(N - M + 1):
        if p == t:
            if text[i:i + M] == pattern:
                result.append(i)

        if i < N - M:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + M])) % q
            if t < 0:
                t = t + q

    return result

# Тестування алгоритмів
def test_algorithms(text, pattern):
    bm_time = timeit.timeit(lambda: boyer_moore(text, pattern), number=1)
    kmp_time = timeit.timeit(lambda: kmp_search(text, pattern), number=1)
    rk_time = timeit.timeit(lambda: rabin_karp(text, pattern), number=1)
    
    print(f"Boyer-Moore time: {bm_time:.5f} seconds")
    print(f"KMP time: {kmp_time:.5f} seconds")
    print(f"Rabin-Karp time: {rk_time:.5f} seconds")

# Приклад використання
text = "ABAAABCD"
pattern = "ABC"

# Запускаємо тестування алгоритмів
test_algorithms(text, pattern)

# Приклад використання
text = "Тому основне завдання програміста - аналізувати і вирішувати проблеми, де код - це всього лише інструмент досягнення мети. Часто виникають проблеми, які важко вирішити, тоді програмісту слід розробити новий алгоритм або поміркувати, як використовувати існуючий. Адже якщо знати про принципи роботи алгоритмів, тоді існує більша ймовірність знайти краще рішення. Іноді навіть нову проблему можна звести до старої, але для цього потрібно володіти фундаментальними знаннями."
pattern = "Іноді навіть нову проблему можна звести до старої, але для цього потрібно володіти фундаментальними знаннями."

# Запускаємо тестування алгоритмів
test_algorithms(text, pattern)

# Приклад використання
text = "Відповідно до результатів проведених експериментів, розгорнутий список показав найкращі показники швидкодії та використання пам’яті. Профілювання показало, що 75% часу роботи тесту варіанту з розгорнутим списком зайняло генерування випадкових даних для програмного імітаційного моделювання агентів та предметів рекомендаційної системи, тож, саме сховище даних має високі показники ефективності. Профілювання варіанту із інвертованим списком показало, що доступ до випадкових блоків займає більше часу через неможливість закешувати їх, тож, за умов реального навантаження час вставки нових даних буде більшим, а відносна ефективність застосування інвертованого списку зросте. Для найбільш ефективного використання пам’яті розмір блоку зв’язного списку має бути адаптований таким чином, щоб блоки були максимально заповнені. Блоки малого розміру зменшують втрати пам’яті, але збільшують час обходу усіх елементів списку та збільшують накладні витрати пам’яті."
pattern = "Для найбільш ефективного використання пам’яті розмір блоку зв’язного списку має бути адаптований таким чином, щоб блоки були максимально заповнені."

# Запускаємо тестування алгоритмів
test_algorithms(text, pattern)


# Висновки: Boyer-Moore часто найшвидший у реальних сценаріях завдяки своїй здатності швидко пропускати непотрібні перевірки.
# KMP може бути відмінним вибором для випадків з повторюваними шаблонами або коли потрібно гарантувати стабільний час виконання.
# Rabin-Karp корисний, якщо потрібно знайти всі входження патерну або є специфічні вимоги до хешування.
# Може бути корисно протестувати ці алгоритми на більшій кількості текстів і патернів різної довжини та різних типів для більш 
# точного розуміння їх переваг і обмежень у вашій конкретній задачі.