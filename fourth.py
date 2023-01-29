import numpy as np

varvar = {"Имя": "Крушила",
          "Раса": "Варвар",
          "Сила": np.random.randint(3, 6),
          "Ловкость": np.random.randint(1, 4),
          "Интеллект": np.random.randint(1, 3),
          "Мудрость": np.random.randint(1, 3),
          "Харизма": np.random.randint(2, 5),
          "Магия": np.random.randint(1, 2),
          "Здоровье": 50
          }

eelf = {"Имя": "Леголас",
        "Раса": "Эльф",
        "Сила": np.random.randint(1, 4),
        "Ловкость": np.random.randint(3, 6),
        "Интеллект": np.random.randint(3, 6),
        "Мудрость": np.random.randint(2, 4),
        "Харизма": np.random.randint(2, 5),
        "Магия": np.random.randint(1, 3),
        "Здоровье": 50}

mag = {"Имя": "Мудрое дерево",
       "Раса": "Чародей",
       "Сила": np.random.randint(1, 3),
       "Ловкость": np.random.randint(2, 4),
       "Интеллект": np.random.randint(3, 6),
       "Мудрость": np.random.randint(3, 6),
       "Харизма": np.random.randint(2, 6),
       "Магия": np.random.randint(3, 6),
       "Здоровье": 50
       }

print("| Доступны следующие персонажи!\n")
for ch in (varvar, eelf, mag):
    for item in ch.keys():
        print(f"| {item:10}: {ch[item]}")
    print()

player = 0
while True:
    print("| Выберите своего славного война!\n1.Варвар 'Крушила'\n2.Эльф 'Леголас'\n3.Чародей 'Мудрое дерево'")
    player_chose = int(input())
    if player_chose == 1:
        player = varvar
        break
    elif player_chose == 2:
        player = eelf
        break
    elif player_chose == 3:
        player = mag
        break
    else:
        print("Некорректное значение выбора! Попробуйте еще раз!")

ai = 0
ai_chose = np.random.randint(1, 3)
if ai_chose == 1:
    ai = varvar
    print("| Противник выбрал Варвара!")
elif ai_chose == 2:
    ai = eelf
    print("| Противник выбрал Эльфа!")
elif ai_chose == 3:
    ai = mag
    print("| Противник выбрал Чародея")

print("| Да начнется славная битва!")
now = True
while player["Здоровье"] > 0 and ai["Здоровье"] > 0:
    challenge, dmg = "", 0
    pl = np.random.randint(1, 6)
    if now:
        if pl == 1:
            dmg = player["Сила"] * 4
            challenge = "Сила"
        elif pl == 2:
            dmg = player["Ловкость"] * 4
            challenge = "Ловкость"
        elif pl == 3:
            dmg = player["Интеллект"] * 4
            challenge = "Интеллект"
        elif pl == 4:
            dmg = player["Мудрость"] * 4
            challenge = "Мудрость"
        elif pl == 5:
            dmg = player["Харизма"] * 4
            challenge = "Харизма"
        elif pl == 6:
            dmg = player["Магия"] * 4
            challenge = "Магия"
        ai["Здоровье"] -= dmg
        ai["Здоровье"] = 0 if ai["Здоровье"] <= 0 else ai["Здоровье"]
        print(f'| Ход игрока. "{challenge}" нанесла противнику {dmg} единиц урона.\n| У противника осталось '
              f'{ai["Здоровье"]}')
        now = False
    else:
        if pl == 1:
            dmg = ai["Сила"] * 4
            challenge = "Сила"
        elif pl == 2:
            dmg = ai["Ловкость"] * 4
            challenge = "Ловкость"
        elif pl == 3:
            dmg = ai["Интеллект"] * 4
            challenge = "Интеллект"
        elif pl == 4:
            dmg = ai["Мудрость"] * 4
            challenge = "Мудрость"
        elif pl == 5:
            dmg = ai["Харизма"] * 4
            challenge = "Харизма"
        elif pl == 6:
            dmg = ai["Магия"] * 4
            challenge = "Магия"
        player["Здоровье"] -= dmg
        player["Здоровье"] = 0 if player["Здоровье"] <= 0 else player["Здоровье"]
        print(f'| Ход противника. "{challenge}" нанесла игроку {dmg} единиц урона.\n| У игрока осталось '
              f'{player["Здоровье"]}')
        now = True
    print()

if player["Здоровье"] <= 0:
    print(f"| Игрок повержен!\n\n| Победил {ai['Раса']} {ai['Имя']}")
else:
    print(f"| Противник повержен!\n\n| Победил '{player['Раса']} {player['Имя']}'")