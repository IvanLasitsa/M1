'''
У багатьох юрисдикціях до ємностей для напоїв додається невеликий депозит, 
щоб заохотити людей переробляти їх. В одній юрисдикції контейнери для напоїв 
місткістю один літр або менше мають заставу в розмірі 0,10 дол. США, а контейнери
для напоїв місткістю понад один літр мають Депозит 0,25 дол.
Напишіть програму, яка зчитує кількість контейнерів кожного розміру 
від користувача. Ваша програма має продовжити обчислення та відображення 
відшкодування, яке буде отримані за повернення цих контейнерів. Відформатуйте
вихідні дані так, щоб вони містили знак долара і дві цифри праворуч від коми.
'''

малий_контейнер = int(input("Введіть кількість контейнерів місткістю 1 літр або менше: "))
контейнер = int(input("Введіть кількість контейнерів місткістю більше 1 літра: "))

refund = (малий_контейнер * 0.10) + (контейнер * 0.25)

print(f"Відшкодування за повернення контейнерів: ${refund:.2f}")
