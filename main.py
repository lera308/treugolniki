class TriangleAnalyzer:
    def __init__(self):
        self.case_success = 0
        self.bug_detected = 0

    def classify_triangle(self, a, b, c):
        try:
            a_f, b_f, c_f = float(a), float(b), float(c)
            if a_f <= 0 or b_f <= 0 or c_f <= 0:
                return "Неверные данные: стороны должны быть положительными"
            if not (a_f + b_f > c_f and a_f + c_f > b_f and b_f + c_f > a_f):
                return "Треугольник не существует"
            if a_f == b_f == c_f:
                return "Равносторонний треугольник"
            elif a_f == b_f or b_f == c_f or a_f == c_f:
                return "Равнобедренный треугольник"
            else:
                return "Разносторонний треугольник"
        except ValueError:
            return "Ошибка: стороны должны быть числами"

    def test_cases(self, a, b, c):
        # Все поля пустые (0)
        if a == '0' and b == '0' and c == '0':
            print("Кейс 1: Все поля пустые — пройден.")
            self.case_success += 1

        # Частично заполненные поля
        partial = (a == '0' and b != '0' and c != '0') or \
                  (a != '0' and b == '0' and c != '0') or \
                  (a != '0' and b != '0' and c == '0')
        if partial:
            print("Кейс 2: Частично заполненные поля — пройден.")
            self.case_success += 1

        # Позитивные кейсы
        positive = [
            ('3', '4', '5'),
            ('2', '3', '4'),
            ('66', '67', '68'),
            ('3', '3', '5'),
            ('6', '6', '6')
        ]
        if (a, b, c) in positive:
            print("Кейс 3-7: Позитивные кейсы — пройдены.")
            self.case_success += 5

        # Не треугольник
        try:
            if float(a) + float(b) <= float(c) or float(a) + float(c) <= float(b) or float(b) + float(c) <= float(a):
                print("Кейс 8: Не треугольник — пройден.")
                self.case_success += 1
        except ValueError:
            pass

        # Не числовой ввод
        try:
            float(a)
            float(b)
            float(c)
        except ValueError:
            print("Кейс 9: Не числовой ввод — пройден.")
            self.case_success += 1

        # Большие числа
        try:
            if float(a) > 4294967295 or float(b) > 4294967295 or float(c) > 4294967295:
                print("Кейс 10: Большие числа — пройден.")
                self.case_success += 1
        except ValueError:
            pass

        # SQL-инъекция
        sql_keywords = ['select', 'or', 'where']
        if any(k in str(a).lower() or k in str(b).lower() or k in str(c).lower() for k in sql_keywords):
            print("Кейс 11: SQL-инъекция — пройден.")
            self.case_success += 1

        # XSS
        if '<script>' in str(a).lower() or '<script>' in str(b).lower() or '<script>' in str(c).lower():
            print("Кейс 12: XSS-уязвимость — пройден.")
            self.case_success += 1

    def check_bugs(self, a, b, c):
        # Поле C не проверяется
        if c == '0' and (a != '0' or b != '0'):
            print("Баг 1: Поле C не проверяется — найден.")
            self.bug_detected += 1


    def run_tests(self, a, b, c):
        self.test_cases(a, b, c)
        self.check_bugs(a, b, c)
        print(f"\nВсего кейсов пройдено: {self.case_success}")
        print(f"Всего багов найдено: {self.bug_detected}")
        self.case_success = 0
        self.bug_detected = 0

def main():
    analyzer = TriangleAnalyzer()
    while True:
        print("\nНапишите 'stop' для выхода")
        a = input("Введите длину первой стороны: ")
        if a.lower() == 'stop':
            break
        b = input("Введите длину второй стороны: ")
        c = input("Введите длину третьей стороны: ")
        analyzer.run_tests(a, b, c)
        print("\nРезультат классификации:", analyzer.classify_triangle(a, b, c))

if __name__ == "__main__":
    main()
