# ==========================================
# HW09｜Python 資料型別上機實作：兩場活動報名整理器
# 姓名：連廣晉
# 學號：D1245382
# ==========================================

# ------------------------------------------
# 【測試一】使用原始資料
# ------------------------------------------
print("================ 【測試一】 ================")

# 1. 原始資料設定
activity_names = ("桌遊體驗", "電影欣賞")  # tuple: 保存固定的兩個活動名稱
board_raw = " Amy, Ben, amy, Cora "        # str: 桌遊體驗原始報名文字
movie_raw = " ben, Dora, ERIC, ben "       # str: 電影欣賞原始報名文字
unit_fees = {"桌遊體驗": 120, "電影欣賞": 80}  # dict: 以活動名稱查詢每人費用

# 2. 讀取活動名稱，建立兩份整理後的串列 (list)
# 使用拆包 (unpacking) 取得兩個活動名稱
board_name, movie_name = activity_names

# 移除半形空白 -> 轉小寫 -> 依逗號拆成 list (保留原始順序與重複項目)
board_list = board_raw.replace(" ", "").lower().split(",")
movie_list = movie_raw.replace(" ", "").lower().split(",")

# 3. 使用集合 (set) 去重並比較名單
board_set = set(board_list)  # 桌遊去重集合
movie_set = set(movie_list)  # 電影去重集合

both_set = board_set & movie_set          # 交集：兩場都有參加
all_set = board_set | movie_set           # 聯集：至少參加一場
only_board_set = board_set - movie_set    # 差集：只參加桌遊者
only_movie_set = movie_set - board_set    # 差集：只參加電影者

# 4. 建立排序串列，使用切片取得前兩位
board_sorted = sorted(board_set)
movie_sorted = sorted(movie_set)
both_sorted = sorted(both_set)
only_board_sorted = sorted(only_board_set)
only_movie_sorted = sorted(only_movie_set)

all_sorted = sorted(all_set)
preview_list = all_sorted[:2]  # 切片取得前兩位作為通知名單預覽

# 5. 使用字典 (dict) 保存摘要，計算人數與應收費用
board_count = len(board_set)
movie_count = len(movie_set)
board_fee_total = board_count * unit_fees[board_name]
movie_fee_total = movie_count * unit_fees[movie_name]

summary = {
    "桌遊人數": board_count,
    "電影人數": movie_count,
    "共同人數": len(both_set),
    "總不重複人數": len(all_set),
    "報名人次": board_count + movie_count,
    "桌遊應收": board_fee_total,
    "電影應收": movie_fee_total,
    "總應收": board_fee_total + movie_fee_total
}

# 6. 輸出完整摘要
print("HW09 活動報名摘要")
print(f"活動：{board_name}，每人 {unit_fees[board_name]:.2f} 元")
print(f"活動：{movie_name}，每人 {unit_fees[movie_name]:.2f} 元")
print(f"桌遊整理串列：{board_list}")
print(f"電影整理串列：{movie_list}")
print(f"桌遊去重名單：{board_sorted}")
print(f"電影去重名單：{movie_sorted}")
print(f"桌遊人數：{summary['桌遊人數']} 人")
print(f"電影人數：{summary['電影人數']} 人")
print(f"共同參加者：{both_sorted}")
print(f"共同人數：{summary['共同人數']} 人")
print(f"只參加桌遊者：{only_board_sorted}")
print(f"只參加電影者：{only_movie_sorted}")
print(f"全部參加者：{all_sorted}")
print(f"總不重複人數：{summary['總不重複人數']} 人")
print(f"報名人次：{summary['報名人次']} 人次")
print(f"通知名單前兩位：{preview_list}")
print(f"桌遊應收：{summary['桌遊應收']:.2f} 元")
print(f"電影應收：{summary['電影應收']:.2f} 元")
print(f"總應收：{summary['總應收']:.2f} 元\n")


# ------------------------------------------
# 【測試二】新增一位電影參加者 Frank
# ------------------------------------------
print("================ 【測試二】 ================")

# 從測試一原始資料重新開始，只修改 movie_raw
activity_names = ("桌遊體驗", "電影欣賞")
board_raw = " Amy, Ben, amy, Cora "
movie_raw = " ben, Dora, ERIC, ben, Frank "
unit_fees = {"桌遊體驗": 120, "電影欣賞": 80}

board_name, movie_name = activity_names
board_list = board_raw.replace(" ", "").lower().split(",")
movie_list = movie_raw.replace(" ", "").lower().split(",")

board_set = set(board_list)
movie_set = set(movie_list)

both_set = board_set & movie_set
all_set = board_set | movie_set
only_board_set = board_set - movie_set
only_movie_set = movie_set - board_set

board_sorted = sorted(board_set)
movie_sorted = sorted(movie_set)
both_sorted = sorted(both_set)
only_board_sorted = sorted(only_board_set)
only_movie_sorted = sorted(only_movie_set)
all_sorted = sorted(all_set)
preview_list = all_sorted[:2]

board_count = len(board_set)
movie_count = len(movie_set)
board_fee_total = board_count * unit_fees[board_name]
movie_fee_total = movie_count * unit_fees[movie_name]

summary = {
    "桌遊人數": board_count,
    "電影人數": movie_count,
    "共同人數": len(both_set),
    "總不重複人數": len(all_set),
    "報名人次": board_count + movie_count,
    "桌遊應收": board_fee_total,
    "電影應收": movie_fee_total,
    "總應收": board_fee_total + movie_fee_total
}

print("HW09 活動報名摘要")
print(f"活動：{board_name}，每人 {unit_fees[board_name]:.2f} 元")
print(f"活動：{movie_name}，每人 {unit_fees[movie_name]:.2f} 元")
print(f"桌遊整理串列：{board_list}")
print(f"電影整理串列：{movie_list}")
print(f"桌遊去重名單：{board_sorted}")
print(f"電影去重名單：{movie_sorted}")
print(f"桌遊人數：{summary['桌遊人數']} 人")
print(f"電影人數：{summary['電影人數']} 人")
print(f"共同參加者：{both_sorted}")
print(f"共同人數：{summary['共同人數']} 人")
print(f"只參加桌遊者：{only_board_sorted}")
print(f"只參加電影者：{only_movie_sorted}")
print(f"全部參加者：{all_sorted}")
print(f"總不重複人數：{summary['總不重複人數']} 人")
print(f"報名人次：{summary['報名人次']} 人次")
print(f"通知名單前兩位：{preview_list}")
print(f"桌遊應收：{summary['桌遊應收']:.2f} 元")
print(f"電影應收：{summary['電影應收']:.2f} 元")
print(f"總應收：{summary['總應收']:.2f} 元\n")


# ------------------------------------------
# 【測試三】兩場去重後完全相同
# ------------------------------------------
print("================ 【測試三】 ================")

# 從測試一原始資料重新開始，只修改 movie_raw
activity_names = ("桌遊體驗", "電影欣賞")
board_raw = " Amy, Ben, amy, Cora "
movie_raw = " AMY, ben, CORA, amy "
unit_fees = {"桌遊體驗": 120, "電影欣賞": 80}

board_name, movie_name = activity_names
board_list = board_raw.replace(" ", "").lower().split(",")
movie_list = movie_raw.replace(" ", "").lower().split(",")

board_set = set(board_list)
movie_set = set(movie_list)

both_set = board_set & movie_set
all_set = board_set | movie_set
only_board_set = board_set - movie_set
only_movie_set = movie_set - board_set

board_sorted = sorted(board_set)
movie_sorted = sorted(movie_set)
both_sorted = sorted(both_set)
only_board_sorted = sorted(only_board_set)
only_movie_sorted = sorted(only_movie_set)
all_sorted = sorted(all_set)
preview_list = all_sorted[:2]

board_count = len(board_set)
movie_count = len(movie_set)
board_fee_total = board_count * unit_fees[board_name]
movie_fee_total = movie_count * unit_fees[movie_name]

summary = {
    "桌遊人數": board_count,
    "電影人數": movie_count,
    "共同人數": len(both_set),
    "總不重複人數": len(all_set),
    "報名人次": board_count + movie_count,
    "桌遊應收": board_fee_total,
    "電影應收": movie_fee_total,
    "總應收": board_fee_total + movie_fee_total
}

print("HW09 活動報名摘要")
print(f"活動：{board_name}，每人 {unit_fees[board_name]:.2f} 元")
print(f"活動：{movie_name}，每人 {unit_fees[movie_name]:.2f} 元")
print(f"桌遊整理串列：{board_list}")
print(f"電影整理串列：{movie_list}")
print(f"桌遊去重名單：{board_sorted}")
print(f"電影去重名單：{movie_sorted}")
print(f"桌遊人數：{summary['桌遊人數']} 人")
print(f"電影人數：{summary['電影人數']} 人")
print(f"共同參加者：{both_sorted}")
print(f"共同人數：{summary['共同人數']} 人")
print(f"只參加桌遊者：{only_board_sorted}")
print(f"只參加電影者：{only_movie_sorted}")
print(f"全部參加者：{all_sorted}")
print(f"總不重複人數：{summary['總不重複人數']} 人")
print(f"報名人次：{summary['報名人次']} 人次")
print(f"通知名單前兩位：{preview_list}")
print(f"桌遊應收：{summary['桌遊應收']:.2f} 元")
print(f"電影應收：{summary['電影應收']:.2f} 元")
print(f"總應收：{summary['總應收']:.2f} 元")