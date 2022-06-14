def main_code(taishoumoji, kessonmoji, hyoujimoji): #すべてリストで与える。
    import datetime
    st = datetime.datetime.now()
    print("対象文字")
    print(taishoumoji)
    print("表示文字")
    print(hyoujimoji)
    i = 0
    kessonsuu_ans = input("欠損文字はいくつあるでしょうか？")
    if int(kessonsuu_ans) == len(kessonmoji):
        print("正解です。それでは、具体的に欠損文字を1つずつ入力して下さい。")
        while True:
            i += 1
            if i == len(kessonmoji)+1:
                print("全問正解！")
                ed = datetime.datetime.now()
                print("回答時間:" + str((ed-st).seconds) + "秒")
                break
            text = str(i) + "つ目の文字を入力して下さい。"
            kesson_ans = input(text)
            if kesson_ans in kessonmoji:
                continue
            else:
                print("不正解です。またチャレンジしてください。")
                ed = datetime.datetime.now()
                print("回答時間:" + str((ed-st).seconds) + "秒")
                break
    else:
        print("不正解です。またチャレンジしてください")
        ed = datetime.datetime.now()
        print("回答時間:" + str((ed-st).seconds) + "秒")

            
def sub_code1_create_taishoumoji(mojisuu):
    import random
    alp_l = [chr(i) for i in range(65,91)]
    s_alp = random.sample(alp_l,mojisuu)
    return s_alp

def sub_code2_create_hyoujimoji(taishoumoji,kessonnsuu):
    import random
    hyoujimoji = random.sample(taishoumoji,kessonnsuu)
    return hyoujimoji

def sub_code3_create_kessonmoji(taishoumoji,hyoujimoji):
    kessonmoji = []
    for i in taishoumoji:
        if i not in hyoujimoji:
            kessonmoji.append(i)
    return kessonmoji

def jikkou(taishoumojisuu,kessonmojisuu):
    taishoumoji = sub_code1_create_taishoumoji(taishoumojisuu)
    hyoujimoji = sub_code2_create_hyoujimoji(taishoumoji,taishoumojisuu - kessonmojisuu)
    kessonmoji = sub_code3_create_kessonmoji(taishoumoji,hyoujimoji)
    main_code(taishoumoji,kessonmoji,hyoujimoji)

global taishoumojisuu, kessonmojisuu
taishoumojisuu = 10
kessonmojisuu = 3
jikkou(taishoumojisuu, kessonmojisuu)