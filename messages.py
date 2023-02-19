messages = {
    "start_messages": """- ....
- Блин, рука затекла
- ....
- Ээх спина болит
- .. Стоп, я что уснул?!!
>> проснувшись, я понял, что я уснул во время занятия по программированию на языке "Python" и когда оно закончилось все 
ушли не разбудив и оставив меня в кабинете, где выключен свет и ничего не работает.
- Надо что то делать и выбираться отсюда""",
    "question": "В какую комнату пойти дальше?",
    "error": "Введены некорректные данные",
    "inventory_error": "Я не могу взять с собой, ведь у меня не три руки! Скинуть ли мне это: ",
    "update_inventory": "Сейчас у меня с собой: ",
    "item_question": "Нужно ли мне это: ",
    "огнетушитель": """>> поводив светом от фонарика по комнате, я заметил в углу ящик с огнетушителем
- хм, а интересно. Вещь вроде полезная да только зачем она мне ночью в кванториуме? Нужна ли мне она?""",
    "фонарик": """>> я попытался порыться в ящиках преподавателей, но к сожалению мне не удалось нормально все рассмотреть,
так как не было ничего, что хоть как-то излучало свет
>> я все равно не отчаивался и пытался хоть что-нибудь найти. И спустя где то 10 минут я нашел фонарик, как раз кстати)  
- теперь получше будет
>> уже во второй раз порывшись в ящиках, я нашел пачку печенья. Съев их, мне стало чуть получше, потому что в последний 
раз я ел очень давно""",
    "аптечка": """>>  поискав здесь что-нибудь полезное добрых 5 минут, я все же нашел аптечку
- ого, прямо реальная аптечка, я такую только в школе видел, на инструктаже, однажды, когда-то
- ....или в фильме"""
}

room_description = {
    "Кабинет 'PYTHON'": """>> кабинет, в котором я проснулся. Ничего необычного: большой стол с ноутбуками, шкафы, 
    стол у моего преподователя, доска, чтобы писать на ней
- ничего полезного""",
    "Коридор": """>> выйдя в коридор, я понял, что у меня есть целых 5 путей: туалет, учительская и 2 кабинета, 
похожих на тот, в котором я проснулся""",
    "Учительская": """- хм, я ни разу не был в учительской, но мне всегда интересно чем они тут занимаются
- сегодня отличный повод это узнать""",
    "Кабинет 'JAVA'": """>> зайдя в кабинет и попытавшись приглядеться в него, я понял, что это кабинет идентичный тому 
в котором я проснулся
- не думаю, что найду здесь что то полезное""",
    "Служебное помещение 'JAVA'": """>> зайдя сюда, я еще больше убедился в том, что кабинет джавы бесполезен в моем 
сегодняшнем приключении
>> ничего не обычного: просто шкафы и коробки, которые можно увидеть даже в темноте""",
    "Туалет": """>> даже в полной темноте я понял где я нахожусь: высокая влажность, запах мыла и дезинфицирующих средств,
которые сразу бросились в нос неприятным запахом, звук капающего крана и звона кафеля от моих шагов - все говорило 
что я нахожусь в туалете.
- тут не было чего-то привлекательного да и искать  чего-то в темноте тут особо не хотелось""",
    "Кабинет 'SCRATCH": """>> хах, очередной кабинет аналогичный кабинету, в котором у меня проходят занятия, за исключением
того, что он был больше моего в 2 раза
>> чуть-чуть походив по кабинету я не нашел ничего полезного""",
    "Служебное помещение 'SCRATCH'": """>> обычное техническое помещение помещение без каких-либо отличительный черт
- скучно...""",
    "Техническое помещение": """>> довольно забавно находить помещения, о которых даже не думал, что они есть
- здесь надо бы получше осмотреться, чтобы было что рассказывать своим друзьям""",
    "Холл": """>> Я вышел в холл. Здесь у нас круто и мне тут очень нравится: приятные диванчики, гардероб, автомат со 
снеками и кофе, кулер с водой, напольные цветы, красивый дизайн - очень приятно и мотивирует учиться
- надо выбирать как мне добираться на улицу: на лифте или по лестнице""",
    "Вентеляция": """>> решив, что раз уж устраивать себе приключение, то надо полностью соглашаться на все безумные идеи
>> немного пошумев отверткой, с которой я никогда не расстаюсь, мне удалось открыть путь в вентиляционную шахту
- что ж, в добрый путь мне
>> и нырнув в вентиляцию, я пополз к свободе""",
    "Лестница": """>>  ну лестница че
>> с пасхалкой""",
    "Лифт": """>> ну лифт хули
>>он шумный че""",
    "Вахта": """В разработке""",
    "Концовка 1": """В разработке""",
    "Концовка 2": """В разработке""",
    "Концовка 3": """В разработке""",
    "Концовка 4": """В разработке""",
    "Концовка 5": """В разработке""",
    "Концовка 6": """В разработке"""
}

fight_messages = {
    "first_hit": """- ха, воришка оказывается тут бродит и не скрывается 
>> поравнявшись с охранником, я попытался ему объяснить ему, что я не какой-то там воришка, как он сказал, и что вообще 
я хочу уйти домой
>> я попытался его обойти, но он не дал мне это сделать, потому что в меня полетел его кулак
 у меня есть всего два выбора как увернуться (Вправо/Влево)""",
    "first_hit_to_right": """>> мне удалось увернуться от его удара""",
    "first_hit_to_left": """>> мне не удалось увернуться от его удара и в меня достаточно сильно прилетело, от чего я чуть
не упал, но устояв на ногах отошел от него на 2 метра""",
    "second_hit": """ блин, его надо ударить, чтобы пройти, иначе я нкогда отсюда не уйду
>> ударить охранника (Да/ Нет)""",
    "second_hit_to_right": """>>  попытавшись ударить его тем, что было, я отошел от него на метр
>> я промахнулся""",
    "second_hit_to_left": """>>  я ничего не сделал и ничего не поменялось: он все также недружелюбно смотрел на меня
>> у меня участился пульс - адреналин зашкаливал - драться в темноте в кванториуме тот еще экстрим""",
    "third_hit": """>> я заметил, что он снова замахивается на меня
>> надо уклоняться, только вот куда? (Вправо/Влево)""",
    "third_hit_to_right": """>> удар был настолько сильным, что у меня зазвенело в ушах. Ещё один такой я не выдержу""",
    "third_hit_to_left": """>> кулак просвистел в миллиметре от моего уха - мне повезло. Сам же я его несильно ударил в
живот, от этого удара он даже не сморщился.""",
    "fourth_hit": """>> охранник начал отдышиватся после такой-то не большой "драки" - это мой шанс, ударить его или нет? (Да/Нет)""",
}

endings = {
    "ending_yes_with_kit": """>> решив, что это мой единственный путь наружу - я ударяю ящиком аптечки в бедро охранника 
    - секунда времени, а охранник уже лежит на полу, схватившись за бедро и рядом с ним валяется связка ключей, схватив ее, 
    я побежал к входным дверям 
>>  секунд 5 и вот я уже бегу по улице
- Домой! Наконец-то! Домой!
>> воздух свистел в ушах и в лицо бился свежий ночной ветер лета""",
    "ending_no_with_kit": """>> решив, что разумным решением будет объяснить ситуацию охраннику, я положил аптечку на пол, 
    в ту же секунду в мое лицо прилетает колено охранника
>> увидев пару звездочек, я падаю без сознания на пол""",
    "ending_yes_with_extinguisher": """>> аккуратно бросив огнетушитель и упав на пол, я попятился к стене.  Я очень долго 
    тяжело дышал. Спустя минут 5 я смог подняться
>> подойдя к охраннику и пошарившись у него в карманах, я нашел связку ключей, с ней я пошел к выходу и начал подбирать 
нужный ключ
>> потратив еще добрые 5 минут, я нахожу его. Дрожащей рукой я открыл входную дверь
>> вдохнув  свежего и слегка прохладного летнего воздуха, измотанный я пошел домой""",
    "ending_no_with_extinguisher": """>> выбив из моих рук огнетушитель, охранник сказал: 
- нету больше оружия у наглого воришки?
>> я съежившись пятился назад в попытках объяснить почему я здесь - во что, очевидно, охранник не верил. Встав к стене, 
я зажмурил глаза от страха - тело ватное, ничего не хочет двигаться
>> следующие 2 секунды были стремительными - прилетел кулак в челюсть. Не ожидав такого мощного импульса, я падаю без 
сознания на пол""",
    "ending_with_nothing": """>> пара легких уворотов от не очень молодого охранника и я уже убегаю от него к запасному 
    выходу
- надеюсь фортуна на моей стороне
>> надавив всем телом на дверь, я понял, что она мне поддалась и, уже довольно улыбнувшись, я проскользнул в дверь
>> пробежав метров 15, я повернулся в надежде не увидеть охранника - мне повезло - он стоял около  двери запасного выхода 
и кричал мне в след скорее всего очень неприятные вещи
>> побежав домой, я чувствовал на себе легкость летней ночи""",
    "ending_without_fight": """>> ползя по пыльной вентиляции уже около 40 минут, я почувствовал на себе свежий ветерок 
    и, уже сменив направление к нему, я выполз к выходящей на улицу  части вентиляции. В очередной раз погремев отверткой, 
    я выбиваю  вентиляционную крышку
>> выглянув на улицу, я вижу на достаточно близком для меня расстоянии тополь
>> собравшись, я прыгаю на его ветви -  я не промахнулся - дальше должно быть полегче
>> скользя по веткам с жуткой болью и треском, я падаю на землю
>> я засмеялся - вот уж безумное приключение у меня выдалось
>> полежав на земле еще минут 20 я поднялся, отряхнулся и весь в синяках и ссадинах поковылял домой"""
}
