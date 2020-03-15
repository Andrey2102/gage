##Сцена с горничной (разгавор по душам)
label dinner:
    scene koridor
    with slo
    "..."
    scene kitchen
    show vitnorm at right
    with slo
    "*долго искать кухню не пришлось*"
    show starnorm at left
    with slo
    hide starnorm
    show starsmile at left
    with slo

    gor"О, Виталик, а ты чего здесь?"
    i"Да я проголодался немного, вот и решил найти что-нибудь пожевать."
    gor"А ведь точно, тебе ведь не удалось нормально поесть с утра, я сейчас что-то принесу."
    "*Лиза скрылась за дверями кладовой, но уже через минуту вернулась держа в руках тарелку с фруктами и бутылку с мутным содержимым*"
    scene kitchen-pro
    with slo
    i"А в бутылке что?"
    gor"Я подумала тебе нужно немного расслабиться."
    "*Лиза достала два бокала*"
    gor""
    i""
    i""
    jump sleeping
    return


label sleeping:
    scene dark
    with slo
    "..."
    scene badroom
    with slo
    "*ты просыпаешься по среди ночи*"
    "Прилег не на долго называеться..."
    "*спать не хотелось совершенно и ты решил прогуляться по замку*"
    jump princess
    return