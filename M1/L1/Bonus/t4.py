'''
Напиши історю битви
Вигадай історію битви двох супергероїв та виведи її на екран, використовуючи функцію print() та метод format. Не забувай, що весь текст має бути написаний всередині потрійних лапок.
'''
story = """
У захмарному місті Землі, де правдивість та зло постійно зіткуються, народився новий супергерой - {hero}.
Його суперсилу неможливо було ігнорувати, і він став останнім захисником міста.

Проти нього піднявся арх-злочинець {villain}, з величезною армією підлеглих. Його ціль - підкорити світ
та знищити всіх, хто стоїть на його шляху.

На вулицях міста розгорнулася епічна битва між {hero} та {villain}. Супергерой витягнув свій
{hero_weapon} і ставився в обороні мирного населення.

{villain} не був так легко перемогти. Він викликав поток енергії і сили, випустивши свої темні сили
проти {hero}. Обидва вони використовували свої унікальні навички та здібності, намагаючись один одного
взяти верх.

Після годин тривалої битви, {hero} зрозумів, що йому потрібно використати свої внутрішні резерви сили. 
Він зосередився та випустив потужний удар, який призвів до знищення сил {villain}. 

Місто визнало {hero} героєм та вшанувало його за врятоване життя. Битва виявилася важкою, але місто
було знову в безпеці завдяки силі та мужності {hero}.
"""

# Задайте значення для героя, злодія та їх озброєння
hero = "Блискавич"
villain = "Темний Магнат"
hero_weapon = "меч"

# Виведення історії на екран
print(story.format(hero1=hero, villain=villain, hero1_weapon=hero_weapon))


