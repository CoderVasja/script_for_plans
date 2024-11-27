import mysql.connector
import json
import pandas as pd
import ast

# Нужно ввести ваши данные для подключения
conn = mysql.connector.connect(
    host="",
    user="",
    password="",
    database=""
)
cursor = conn.cursor()


version_id = 651 # Поменять на нужную вам версию
object_ids = [13663] #Поменять на нужные вам айдишники объектов через запятую

excel_id = '120xmm7PtqFeKePACNdQh7DoGxklUHQL-3rXagC5D8Ac' # Id excel файла
sheet_id = 676142383 # id листа с балансом

start_range = '' # Строка первого плана
end_range =  '' # Строка последнего плана  

col_delta_1 = '5' # колонка count для 1 ресурса
col_delta_2 = '9' # колонка count для 2 ресурса
col_delta_3 = '13' # колонка count для 3 ресурса
col_delta_4 = '17' # колонка count для 4 ресурса

col_res_1 = '7' # колонка resource_id для 1 ресурса
col_res_2 = '11' # колонка resource_id для 2 ресурса
col_res_3 = '15' # колонка resource_id для 3 ресурса
col_res_4 = '19' # колонка resource_id для 4 ресурса


col_res_result = '2' # колонка resource_id 
col_item_value = '35' # колонка Item Value
col_prem_cost = '37' # колонка One Item Prem Cost

col_cycle = '21' # колонка cycle
col_enabled = '22' # колонка enabled
col_res_delta = '23' # колонка Result quantity
col_xp = '24' # колонка XP

col_event_id = '25' # колонка event_id
col_episode_id = '26' # колонка episode_id

url = f'https://docs.google.com/spreadsheets/d/{excel_id}/gviz/tq?tqx=out:csv&gid={sheet_id}'

df = pd.read_csv(url,header=None,skiprows=10)
df.index+1 

"""
Строчку ниже нужно разкоментировать убрав # перед ней
"""
print(df.iloc[:60,]) 
print(df.loc[12:16, df.columns[5]]) 


if isinstance(object_ids, tuple) and len(object_ids) == 1:
    object_ids_str = str(object_ids[0])  
else:
    object_ids_str = ", ".join(map(str, object_ids))

if start_range and end_range:
    get_ingredients_query = f"SELECT ingredients FROM plan WHERE version_id = {version_id} AND object_id IN ({object_ids_str})" 
    get_add_info = f"SELECT cycle, enabled, event_id, episode_id, quest_action,reward,additional_rewards FROM plan WHERE version_id = {version_id} AND object_id IN ({object_ids_str})" 



    # Получаем данные из excel по планам
    delta_1 = [
        None if pd.isna(val) else int(val) if isinstance(val, float) and val.is_integer() else val
        for val in df.iloc[int(start_range):int(end_range), df.columns[int(col_delta_1)]].tolist()
    ]
    res_1 = [
        None if pd.isna(val) else int(val) if isinstance(val, float) and val.is_integer() else val
        for val in df.iloc[int(start_range):int(end_range), df.columns[int(col_res_1)]].tolist()
    ]
    delta_2 = [
        None if pd.isna(val) else int(val) if isinstance(val, float) and val.is_integer() else val
        for val in df.iloc[int(start_range):int(end_range), df.columns[int(col_delta_2)]].tolist()
    ]
    res_2 = [
        None if pd.isna(val) else int(val) if isinstance(val, float) and val.is_integer() else val
        for val in df.iloc[int(start_range):int(end_range), df.columns[int(col_res_2)]].tolist()
    ]
    delta_3 = [
        None if pd.isna(val) else int(val) if isinstance(val, float) and val.is_integer() else val
        for val in df.iloc[int(start_range):int(end_range), df.columns[int(col_delta_3)]].tolist()
    ]
    res_3 = [
        None if pd.isna(val) else int(val) if isinstance(val, float) and val.is_integer() else val
        for val in df.iloc[int(start_range):int(end_range), df.columns[int(col_res_3)]].tolist()
    ]
    delta_4 = [
        None if pd.isna(val) else int(val) if isinstance(val, float) and val.is_integer() else val
        for val in df.iloc[int(start_range):int(end_range), df.columns[int(col_delta_4)]].tolist()
    ]
    res_4 = [
        None if pd.isna(val) else int(val) if isinstance(val, float) and val.is_integer() else val
        for val in df.iloc[int(start_range):int(end_range), df.columns[int(col_res_4)]].tolist()
    ]

    # Получаем данные из excel по ресурсам которые дает план
    res_result = [
        None if pd.isna(val) else int(val) if isinstance(val, float) and val.is_integer() else val
        for val in df.iloc[int(start_range):int(end_range), df.columns[int(col_res_result)]].tolist()
    ]
    item_value = [
        None if pd.isna(val) else int(val) if isinstance(val, float) and val.is_integer() else val
        for val in df.iloc[int(start_range):int(end_range), df.columns[int(col_item_value)]].tolist()
    ]
    prem_cost = [
        None if pd.isna(val) else int(val) if isinstance(val, float) and val.is_integer() else val
        for val in df.iloc[int(start_range):int(end_range), df.columns[int(col_prem_cost)]].tolist()
    ]

    # Получаем данные из excel по ресурсам которые дает план
    cycle = [
        None if pd.isna(val) else int(val) if isinstance(val, float) and val.is_integer() else val
        for val in df.iloc[int(start_range):int(end_range), df.columns[int(col_cycle)]].tolist()
    ]
    enabled = [
        None if pd.isna(val) else int(val) if isinstance(val, float) and val.is_integer() else val
        for val in df.iloc[int(start_range):int(end_range), df.columns[int(col_enabled)]].tolist()
    ]
    res_delta = [
        None if pd.isna(val) else int(val) if isinstance(val, float) and val.is_integer() else val
        for val in df.iloc[int(start_range):int(end_range), df.columns[int(col_res_delta)]].tolist()
    ]

    xp = [
        None if pd.isna(val) else int(val) if isinstance(val, float) and val.is_integer() else val
        for val in df.iloc[int(start_range):int(end_range), df.columns[int(col_xp)]].tolist()
    ]

    event_id = [
        None if pd.isna(val) else int(val) if isinstance(val, float) and val.is_integer() else val
        for val in df.iloc[int(start_range):int(end_range), df.columns[int(col_event_id)]].tolist()
    ]
    episode_id = [
        None if pd.isna(val) else int(val) if isinstance(val, float) and val.is_integer() else val
        for val in df.iloc[int(start_range):int(end_range), df.columns[int(col_episode_id)]].tolist()
    ]

    # Данные
    excel_data_res_info = {
        'res_results': res_result,
        'item_value': item_value,
        'prem_cost': prem_cost,
    }

    # Данные
    excel_data_plan_info = {
        'delta_1': delta_1,
        'res_1': res_1,
        'delta_2': delta_2,
        'res_2': res_2,
        'delta_3': delta_3,  
        'res_3': res_3,
        'delta_4': delta_4,  
        'res_4': res_4
    }

    # Выполнение запроса
    cursor.execute(get_ingredients_query)

    get_all_plans  = cursor.fetchall() # получаем все планы из БД

    plans_from_bd = []

    for entry in get_all_plans:
        
        json_data = ast.literal_eval(entry[0])  # Преобразуем строку в список
        
        # Преобразуем 'delta' и 'resource_id' в строки
        for item in json_data:
            item['delta'] = int(item['delta'])  # Преобразуем 'delta' в строку
            item['resource_id'] = int(item['resource_id'])  # Преобразуем 'resource_id' в строку
        
        # Добавляем преобразованный список в новый список
        plans_from_bd.append(json_data)


    # Генерация JSON
    plans_from_excel = []
    for i in range(len(excel_data_plan_info['delta_1'])):
        entry = []
        # Добавляем первый и второй наборы данных
        entry.append({"delta": excel_data_plan_info['delta_1'][i], "resource_id": excel_data_plan_info['res_1'][i]})
        entry.append({"delta": excel_data_plan_info['delta_2'][i], "resource_id": excel_data_plan_info['res_2'][i]})

        # Проверка наличия третьего набора данных
        if excel_data_plan_info['delta_3'][i] is not None and excel_data_plan_info['res_3'][i] is not None:
            entry.append({"delta": excel_data_plan_info['delta_3'][i], "resource_id": excel_data_plan_info['res_3'][i]})

        # Проверка наличия четвертого набора данных
        if excel_data_plan_info['delta_4'][i] is not None and excel_data_plan_info['res_4'][i] is not None:
            entry.append({"delta": excel_data_plan_info['delta_4'][i], "resource_id": excel_data_plan_info['res_4'][i]})

        plans_from_excel.append(entry)

    print("\n" * 2 + f'\033[33m{"--"*30} Проверка ингредиентов плана {"--"*30}\033[0m')


    # Применяем функцию к данным
    def compare_plans(plans_excel, plans_bd):
        differences = []
        
        for i, (plan_excel, plan_bd) in enumerate(zip(plans_excel, plans_bd)):
            for j, (resource_excel, resource_bd) in enumerate(zip(plan_excel, plan_bd)):
                # Преобразуем значения в int перед сравнением
                delta_excel = int(resource_excel['delta'])
                delta_bd = int(resource_bd['delta'])
                resource_id_excel = int(resource_excel['resource_id'])
                resource_id_bd = int(resource_bd['resource_id'])

                # Сравниваем каждый ресурс
                if delta_excel != delta_bd or resource_id_excel != resource_id_bd:
                    diff_message = f"У плана {i + 1} ({j + 1}-й ресурс): "
                
                    # Определяем, что именно отличается
                    if resource_id_excel != resource_id_bd:
                        diff_message += f"неверный resource_id ожидается resource_id: {resource_id_excel} вместо resource_id: {resource_id_bd} "
                    if delta_excel != delta_bd:
                        diff_message += f"неверная delta у ресурса {resource_id_excel} ожидается delta: {delta_excel} вместо delta: {delta_bd}"
                    
                    differences.append(diff_message)
        
        # Выводим все различия
        if differences:
            for diff in differences:
                print(diff)
            print(f'\033[32m{"--"*30} Ингредиенты проверены {"--"*25}\033[0m'"")      
        else:
            print(f'\033[32m{"--"*30} Ингредиенты заполнены верно {"--"*30}\033[0m')


    # Вызываем функцию
    compare_plans(plans_from_excel, plans_from_bd)


    print("\n" * 2 + f'\033[33m{"--"*30} Проверка Item value и Prem cost {"--"*25}\033[0m')


    res_info_from_excel = []

    for i in range(len(excel_data_res_info['res_results'])):
        res_info_from_excel.append({
            excel_data_res_info['res_results'][i]: {
                'item_value': int(excel_data_res_info['item_value'][i]),
                'prem_cost': int(excel_data_res_info['prem_cost'][i])
            }
        })


    ids =", ".join(map(str, res_result))

    get_all_res_query = f"SELECT id, nominal_value, premium_exchange_rate FROM resource WHERE id IN ({ids}) ORDER BY FIELD(id, {ids})" 


    #Выполнение запроса
    cursor.execute(get_all_res_query)

    get_all_res  = cursor.fetchall() # получаем все ресуры планов из БД

    res_info_from_db =[]

    for i in range(len(get_all_res)):
        res_info_from_db.append({
            get_all_res[i][0]: {
                'item_value': int(get_all_res[i][1]),
                'prem_cost': int(get_all_res[i][2])
            }
        })

    # Преобразуем списки в словари для быстрого поиска
    dict1 = {list(d.keys())[0]: d[list(d.keys())[0]] for d in res_info_from_db}
    dict2 = {list(d.keys())[0]: d[list(d.keys())[0]] for d in res_info_from_excel}

    # Приводим ключи к строкам для корректного сравнения
    dict1 = {str(k): v for k, v in dict1.items()}
    dict2 = {str(k): v for k, v in dict2.items()}

    # Сравнение
    differences = []

    for index, key in enumerate(dict1):
        if dict1[key] != dict2.get(key):
            item_value1 = dict1[key].get('item_value')
            item_value2 = dict2.get(key, {}).get('item_value')
            prem_cost1 = dict1[key].get('prem_cost')
            prem_cost2 = dict2.get(key, {}).get('prem_cost')
                
            # Формируем сообщение о различиях
            diff_message = f"У плана {index + 1} у ресурса {key} "
            if item_value1 != item_value2:
                diff_message += f"item_value: {item_value1} а должно быть {item_value2}. "
            if prem_cost1 != prem_cost2:
                diff_message += f"prem_cost: {prem_cost1} а должно быть {prem_cost2}."
            differences.append(diff_message)

    if differences:    
        print("\n".join(differences))
        print(f'\033[32m{"--"*30} Item value и Prem проверены {"--"*25}\033[0m'"")   
    else:
        print(f'\033[32m{"--"*30} Item value и Prem cost верные {"--"*25}\033[0m'"")
    



    #Выполнение запроса
    cursor.execute(get_add_info)
    get_info  = cursor.fetchall() # получаем все планы из БД       



    db_cycle = [t[0] for t in get_info]
    db_enabled = [t[1] for t in get_info]
    db_event_id = [t[2] for t in get_info]
    db_episode_id = [t[3] for t in get_info]
    db_quest_action = [t[4] for t in get_info]

    main_reward = [t[5] for t in get_info]
    add_reward = [t[6] for t in get_info]


    main_reward_delta = []
    main_reward_res  = []

    add_reward_delta = []
    add_reward_res = []

    #достаем отдельно delta и id ресурса для main_reward
    for item in main_reward:
        parsed_item = json.loads(item)  # Преобразуем строку в словарь
        main_reward_delta.append(parsed_item["delta"])  # Добавляем значение delta
        main_reward_res.append(parsed_item["resource_id"])  # Добавляем значение resource_id


    #достаем отдельно delta и id ресурса для additional_reward
    for item in add_reward:
        parsed_item = json.loads(item)  # Преобразуем строку в список словарей
        for obj in parsed_item:  # Проходим по словарям внутри списка
            add_reward_delta.append(obj["delta"])  # Добавляем значение delta
            add_reward_res.append(obj["resource_id"])  # Добавляем значение resource_id

    #Проверяем правильный ли cycle у планов
    cycle_info = []
    print("\n" * 2 + f'\033[33m{"--"*30} Проверка Cycle {"--"*25}\033[0m')
    for index, (a, b) in enumerate(zip(db_cycle, cycle)):
        if a != b:
            cycle_info.append(f"У плана {index+1} невереный cycle должен быть {b} вместо {a}") 

    if cycle_info:
        print("\n".join(cycle_info))        
    else:
        print(f'\033[32m{"--"*30} Cycle верный {"--"*25}\033[0m'"")

    #Проверяем правильный ли enabled у планов
    enabled_info = []
    print("\n" * 2 + f'\033[33m{"--"*30} Проверка Enabled {"--"*25}\033[0m')
    for index, (a, b) in enumerate(zip(db_enabled, enabled)):
        if a != int(b):
            enabled_info.append(f"У плана {index+1} невереный enabled должен быть {b} вместо {a}")     

    if enabled_info:
        print("\n".join(enabled_info))        
    else:
        print(f'\033[32m{"--"*30} Enabled верный {"--"*25}\033[0m'"")
        

    #Проверяем правильный ли Result quantity у планов
    result_info = []
    print("\n" * 2 + f'\033[33m{"--"*30} Проверка Result quantity {"--"*25}\033[0m')
    for index, (a, b) in enumerate(zip(main_reward_delta, res_delta)):
        if a != int(b):
            result_info.append(f"У плана {index+1} невереный Result quantity должен быть {b} вместо {a}")  

    for index, (a, b) in enumerate(zip(main_reward_res, res_result)):
        if a != int(b):
            result_info.append(f"У плана {index+1} невереный id ресурса в награду должен быть {b} вместо {a}")            

    if result_info:
        print("\n".join(result_info))        
    else:
        print(f'\033[32m{"--"*30} Result quantity верный {"--"*25}\033[0m'"")  


    #Проверяем правильный ли XP у планов
    xp_info = []
    print("\n" * 2 + f'\033[33m{"--"*30} Проверка XP {"--"*25}\033[0m')
    for index, (a, b) in enumerate(zip(add_reward_delta, xp)):
        if a != int(b):
            xp_info.append(f"У плана {index+1} невереное кол XP должно быть {b} вместо {a}")     

    for index, (a, b) in enumerate(zip(add_reward_res, xp)):
        xp_id = 3
        if a != xp_id:
            xp_info.append(f"У плана {index+1} невереный ресурс в additional_reward должен быть {xp_id} вместо {a}") 

    if xp_info:
        print("\n".join(xp_info))        
    else:
        print(f'\033[32m{"--"*30} XP верный {"--"*25}\033[0m'"") 


    
    #Если event_id не пустой то проверем event_id иначе проверяем episdoe_id

    if None in event_id:
        #Проверяем правильный ли Episode_id у планов
        ep_id_info = []
        print("\n" * 2 + f'\033[33m{"--"*30} Проверка Episode_id {"--"*25}\033[0m')
        for index, (a, b) in enumerate(zip(db_episode_id, episode_id)):
            if a != int(b):
                ep_id_info.append(f"У плана {index+1} неверный Episode id должен быть {b} вместо {a}")     

        if ep_id_info:
            print("\n".join(ep_id_info))        
        else:
            print(f'\033[32m{"--"*30} Episode_id верный {"--"*25}\033[0m'"") 
    else:
        #Проверяем правильный ли event_id у планов
        ev_id_info = []
        print("\n" * 2 + f'\033[33m{"--"*30} Проверка Event_id {"--"*25}\033[0m')
        for index, (a, b) in enumerate(zip(db_event_id, event_id)):
            if a != int(b):
                ev_id_info.append(f"У плана {index+1} неверный Event id должен быть {b} вместо {a}")     

        if ev_id_info:
            print("\n".join(ev_id_info))        
        else:
            print(f'\033[32m{"--"*30} Event_id верный {"--"*25}\033[0m'"")                      
else:
    print("\033[91mСначала заполни start_range и end_range\033[0m")
          