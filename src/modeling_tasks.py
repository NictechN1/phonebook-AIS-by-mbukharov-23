"""
МАТЕМАТИЧЕСКОЕ МОДЕЛИРОВАНИЕ
Решение задач из Раздела 3
"""

import numpy as np
from scipy.optimize import linprog

class ModelingTasks:
    def __init__(self):
        self.tasks = []
    
    def solve_linear_programming(self):
        """Решение задачи линейного программирования (Задача 2 из ТЗ)"""
        print("🔢 РЕШЕНИЕ ЗАДАЧИ ЛИНЕЙНОГО ПРОГРАММИРОВАНИЯ")
        print("Функция: F = 2x₁ + x₂ - x₃ + x₄ - x₅ → max")
        print("Ограничения:")
        print("  x₁ + x₂ + x₃ = 5")
        print("  2x₁ + x₂ + x₄ = 9") 
        print("  x₁ + 2x₂ + x₅ = 7")
        print("  x₁, x₂, x₃, x₄, x₅ ≥ 0")
        
        # Коэффициенты целевой функции (с отрицанием для максимизации)
        c = [-2, -1, 1, -1, 1]
        
        # Матрица ограничений равенств
        A_eq = [
            [1, 1, 1, 0, 0],  # x₁ + x₂ + x₃ = 5
            [2, 1, 0, 1, 0],  # 2x₁ + x₂ + x₄ = 9
            [1, 2, 0, 0, 1]   # x₁ + 2x₂ + x₅ = 7
        ]
        b_eq = [5, 9, 7]
        
        # Границы переменных
        bounds = [(0, None), (0, None), (0, None), (0, None), (0, None)]
        
        try:
            # Решение задачи
            result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')
            
            if result.success:
                print("\n✅ РЕШЕНИЕ НАЙДЕНО:")
                print(f"Максимальное значение F: {-result.fun:.2f}")
                variables = ['x₁', 'x₂', 'x₃', 'x₄', 'x₅']
                for i, var in enumerate(variables):
                    print(f"{var} = {result.x[i]:.2f}")
            else:
                print("\n❌ Решение не найдено")
                
        except Exception as e:
            print(f"\n❌ Ошибка при решении: {e}")
    
    def solve_transport_problem(self):
        """Решение транспортной задачи (Задача 6 из ТЗ)"""
        print("\n🚚 РЕШЕНИЕ ТРАНСПОРТНОЙ ЗАДАЧИ")
        print("Пункты отправления: A1=160, A2=140, A3=60")
        print("Пункты назначения: B1=80, B2=80, B3=60, B4=80")
        print("Матрица стоимостей:")
        print("    B1  B2  B3  B4")
        print("A1:  5   4   3   4")
        print("A2:  3   2   5   5") 
        print("A3:  1   6   3   2")
        
        # Здесь будет алгоритм решения транспортной задачи
        print("\n✅ Решение транспортной задачи будет реализовано")
        print("Используется метод потенциалов или северо-западного угла")
    
    def run_all_tasks(self):
        """Запуск всех задач моделирования"""
        print("=" * 60)
        print("🧮 МАТЕМАТИЧЕСКОЕ МОДЕЛИРОВАНИЕ - РАЗДЕЛ 3")
        print("=" * 60)
        
        self.solve_linear_programming()
        self.solve_transport_problem()

if __name__ == "__main__":
    # Установи scipy если нет: pip install scipy
    tasks = ModelingTasks()
    tasks.run_all_tasks()