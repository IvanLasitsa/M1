'''
Вигадай свого супергероя.
Вигадай свого супергероя. Опиши його вміння, якості, силу, здібності і т. Д., І виведи опис на екран за допомогою функції print (). За допомогою методу format зроби опис динмічним. Не забувай, що весь текст повинен бути написаний всередині потрійних лапок.
'''

story = """
У світі, де потрібна захисту від темряви та зла, з'явився новий супергерой - {superhero_name}.
Зі своїми унікальними здібностями та високими моральними якостями, він став останнім шансом для порятунку.

{superhero_name} обладнаний неймовірною швидкістю, яка дозволяє йому миттєво врятувати тих, хто потребує
допомоги. Він також володіє силовим полем, яке захищає його від будь-яких атак і робить його майже
непереможним.

Однією з найвражаючих здібностей {superhero_name} є його здатність маніпулювати енергією блискавок.
Він може не лише створювати могутні блискавки для атаки ворогів, але і використовувати їх для вирішення
складних завдань.

Його броня має вбудований комп'ютер, який аналізує ситуацію та розробляє оптимальні стратегії для перемоги.
{superhero_name} завжди готовий вступити в бій заради правди та справедливості, надія для всіх, хто вірить у
героїзм.

"""

# Задайте значення для супергероя
superhero_name = "Блискавич"

# Виведення опису супергероя на екран
print(story.format(superhero_name=superhero_name))
