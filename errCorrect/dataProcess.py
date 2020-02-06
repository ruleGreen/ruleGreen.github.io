# coding: utf-8
types = ['生活', '成語', '字型']
typesId = ['life', 'idiom', 'font']
subTypes = [['動詞', '名詞', '形容詞'], ['描寫人物', '描寫事物', '描寫風景'], ['音近別字', '型近別字', '部件別字']]
subTypesId = [['verb', 'norm', 'adj'], ['person', 'object', 'scenery'], ['pron', 'format', 'part']]
mission = [[1, 2, 3], [1,2], [1], [1, 2, 3], [1, 2], [1, 2], [1, 2, 3], [1, 2], [1]]
data = {}

for i in range(len(types)):
    # typeId = ''.join(random.sample(string.ascii_letters + string.digits, 6))
    # print(typeId)
    typeId = typesId[i]
    data[typeId] = {}
    data[typeId]['typeName'] = types[i]
    data[typeId]['subTypes'] = {}
    for j in range(len(subTypes[i])):
        # subTypeId = ''.join(random.sample(string.ascii_letters + string.digits, 6))
        # print(subTypeId)
        subTypeId = subTypesId[i][j]
        print(typeId, subTypeId)

        data[typeId]['subTypes'][subTypeId] = {}
        data[typeId]['subTypes'][subTypeId]["typeName"] = subTypes[i][j]
        data[typeId]['subTypes'][subTypeId]["mission"] = {}

        for p in range(len(mission[3*i+j])):

            """
            "done":0,
            "answerWord":"",
            "answerErrIndex": 0,
            "result":0,
            """
            # print(data[typeId]['subTypes'][subTypeId]["mission"])
            data[typeId]['subTypes'][subTypeId]["mission"][mission[3*i+j][p]] = {}
            data[typeId]['subTypes'][subTypeId]["mission"][mission[3*i+j][p]]["questions"] = {
                        0:{
                            "questionName":"題目一",
                            "content":"這個網站被黑客攻激，完全看不到畫面的內容了。",
                            "correct":"擊",
                            "errIndex":8,
                        },
                        1:{
                            "questionName":"題目二",
                            "content":"現代科技的發展日新月義，不斷進步。",
                            "correct":"異",
                            "errIndex":10,
                        },
                        2:{
                            "questionName":"題目三",
                            "content":"這個週末，我們全家去度假村泡溫泉。",
                            "correct":"渡",
                            "errIndex":10,
                        },
                        3:{
                            "questionName":"題目四",
                            "content":"你大吵大鬧影響了別人做生意，必須要陪償他們的損失。",
                            "correct":"賠",
                            "errIndex":17,
                        },
                        4:{
                            "questionName":"題目五",
                            "content":"地震催毀了這個曾經非常繁華的城市。",
                            "correct":"嗺",
                            "errIndex":2,
                        },
                        5:{
                            "questionName":"題目六",
                            "content":"這家人的關係非常溶洽，家裏常常充滿歡聲笑語。",
                            "correct":"融",
                            "errIndex":8,
                        },
                        6:{
                            "questionName":"題目七",
                            "content":"美玲偷懶不溫習功課，結果考試不合格，真是得不嘗失啊！",
                            "correct":"償",
                            "errIndex":22,
                        },
                        7:{
                            "questionName":"題目八",
                            "content":"爺爺的農莊裏有一些小胡蘆，我常用它們來裝水。",
                            "correct":"葫",
                            "errIndex":10,
                        },
                        8:{
                            "questionName":"題目九",
                            "content":"雖然他沒贏得比賽，但爸爸一如繼往地支持他練習玩魔術。",
                            "correct":"既",
                            "errIndex":14,
                        },
                        9:{
                            "questionName":"題目十",
                            "content":"這個演員經常出現在電視螢幕上，深受觀眾的歡迎。",
                            "correct":"熒",
                            "errIndex":11,
                        }
                    }


    print('\n')

print(data)