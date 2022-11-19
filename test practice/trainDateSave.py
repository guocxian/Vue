import json

event2id = {
    "None": 0,
    "明知": 1,
    "投案": 2,
    "供述": 3,
    "谅解": 4,
    "赔偿": 5,
    "退赃": 6,
    "销赃": 7,
    "分赃": 8,
    "搜查/扣押": 9,
    "举报": 10,
    "拘捕": 11,
    "报警/报案": 12,
    "鉴定": 13,
    "冲突": 14,
    "言语冲突": 15,
    "肢体冲突": 16,
    "买卖": 17,
    "卖出": 18,
    "买入": 19,
    "租/借": 20,
    "出租/出借": 21,
    "租用/借用": 22,
    "归还/偿还": 23,
    "获利": 24,
    "雇佣": 25,
    "放贷": 26,
    "集资": 27,
    "支付/给付": 28,
    "签订合同/订立协议": 29,
    "制造": 30,
    "遗弃": 31,
    "运输/运送": 32,
    "邮寄": 33,
    "组织/安排": 34,
    "散布": 35,
    "联络": 36,
    "通知/提醒": 37,
    "介绍/引荐": 38,
    "邀请/招揽": 39,
    "纠集": 40,
    "阻止/妨碍": 41,
    "挑衅/挑拨": 42,
    "帮助/救助": 43,
    "提供": 44,
    "放纵": 45,
    "跟踪": 46,
    "同意/接受": 47,
    "拒绝/抗拒": 48,
    "放弃/停止": 49,
    "要求/请求": 50,
    "建议": 51,
    "约定": 52,
    "饮酒": 53,
    "自然灾害": 54,
    "洪涝": 55,
    "干旱": 56,
    "山体滑坡": 57,
    "事故": 58,
    "交通事故": 59,
    "火灾事故": 60,
    "爆炸事故": 61,
    "暴力": 62,
    "杀害": 63,
    "伤害人身": 64,
    "言语辱骂": 65,
    "敲诈勒索": 66,
    "威胁/强迫": 67,
    "持械/持枪": 68,
    "拘束/拘禁": 69,
    "绑架": 70,
    "欺骗": 71,
    "拐骗": 72,
    "冒充": 73,
    "伪造": 74,
    "变造": 75,
    "盗窃财物": 76,
    "抢夺财物": 77,
    "抢劫财物": 78,
    "挪用财物": 79,
    "侵占财物": 80,
    "毁坏财物": 81,
    "猥亵": 82,
    "强奸": 83,
    "卖淫": 84,
    "嫖娼": 85,
    "吸毒": 86,
    "贩卖毒品": 87,
    "赌博": 88,
    "开设赌场": 89,
    "指使/教唆": 90,
    "共谋": 91,
    "违章驾驶": 92,
    "泄露信息": 93,
    "私藏/藏匿": 94,
    "入室/入户": 95,
    "贿赂": 96,
    "逃匿": 97,
    "放火": 98,
    "走私": 99,
    "投毒": 100,
    "自杀": 101,
    "死亡": 102,
    "受伤": 103,
    "被困": 104,
    "中毒": 105,
    "昏迷": 106,
    "遗失": 107,
    "受损": 108
}


         
with open(r"C:\Users\Administrator\Desktop\LEVEN\train.jsonl", "r", encoding="utf-8")as f:
    lines = f.readlines()
    dataset = []
    for line in lines:
        line = line.rstrip()
        line = json.loads(line)
        dataset.append(line)


for i in dataset:
    subset = {
        "title": "",
        "id": "",
        "crime": "",
        "case_no": "",
        "content": [],
        "events": [],
        'typeVector': '',
        
    }
    typeVector = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    subset["title"] = i["title"]
    subset["id"] = i["id"]
    subset["crime"] = i["crime"]
    subset["case_no"] = i["case_no"]
    for item in i["content"]:
        subset["content"].append(item['sentence'])

    for item in i["events"]:
        subset["events"].append({"type": item['type'], "typeid": item["type_id"],"trigger_word": item["mention"][0]["trigger_word"]})
        typeVector[item['type_id']] += 1

    subset["typeVector"] = [x/len(i["events"]) for x in typeVector]
    print(subset)



