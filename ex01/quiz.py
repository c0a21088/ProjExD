quiz_list = ["サザエの旦那の名前は？","カツオの妹の名前は？","タラオはカツオから見てどんな関係？"]
ans_list = [["マスオ","ますお"],["ワカメ","わかめ"],["甥","おい","甥っ子","おいっこ"]]
def quiz(q_list,a_list):
    import datetime
    import random
    st = datetime.datetime.now()
    random_x = random.randint(0,len(q_list)-1)
    print("問題:")
    print(q_list[random_x])
    ans = input("答えるんだ!:")
    if ans in a_list[random_x]:
        ed = datetime.datetime.now()
        print("正解!")
    else:
        print("地獄に落ちてください")
        ed = datetime.datetime.now()
    print("回答時間:" + str((ed-st).seconds) + "秒")
quiz(quiz_list,ans_list)
