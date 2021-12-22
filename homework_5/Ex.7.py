import json


with open('new_file_7_1.txt') as file:
    content = file.readlines()
    av_list = []
    res_dict = {}
    for el in content:
        el = el.split(' ')
        if (int(el[2]) - int(el[3])) > 0:
            av_list.append(int(el[2]) - int(el[3]))
        res_dict[el[0]] = (int(el[2]) - int(el[3]))
    av_pr = sum(av_list) / len(av_list)
    av_dict = {'average_profit': av_pr}
    res_list = [res_dict, av_dict]

with open('new_file_7_2.json', 'w') as file:
    json.dump(res_list, file)
