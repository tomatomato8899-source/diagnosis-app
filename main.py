import tkinter as tk
from tkinter import font

def show_frame(frame):
    frame.tkraise()

def back_to_menu():
    show_frame(main_frame)

root = tk.Tk()
root.configure(bg="#ffeef2")

# 基本フォント
base_font = font.Font(family="Arial", size=14)


# --- 質問画面 ---
question_frame = tk.Frame(root)
question_frame.config(bg="#ffeef2")

question_label = tk.Label(question_frame, text="", font=base_font)
question_label.config(bg="#ffeef2")
question_label.pack(pady=20)


# --- 質問データ ---
job_questions = [
    {
        "q": "どんな仕事に興味がある？やってみたいことは？",
        "choices": ["クリエイティブ系", "対人支援系", "コツコツ作業系"]
    },
    {
        "q": "性格タイプは？",
        "choices": ["論理・分析タイプ", "社交・行動タイプ", "対人・サポートタイプ", "管理・実務タイプ"]
    },
    {
        "q": "得意なことは？",
        "choices": ["ビジネス・スキル系", "コミュニケーション・性格系", "日常生活・その他"]
    },
    {
        "q": "苦手・絶対にやりたくないことは？",
        "choices": ["大勢の前", "細かい作業"]
    },
    {
        "q": "何を一番重視する？",
        "choices": ["給与", "時間", "やりがい", "安定性"]
    }
]

pref_questions = [
    {
        "q": "旅行で行きたい雰囲気は？",
        "choices": ["都会", "自然", "歴史", "海"]
    },
    {
        "q": "気候の好みは？",
        "choices": ["暑いのが好き", "寒いのが好き", "どっちもOK"]
    },
    {
        "q": "食べ物の好みは？",
        "choices": ["海鮮", "肉料理", "麺類", "甘いもの"]
    },
    {
        "q": "住むならどんな場所？",
        "choices": ["便利な街", "静かな田舎", "観光地", "工業地帯"]
    },
    {
        "q": "人の雰囲気は？",
        "choices": ["明るい", "落ち着いてる", "のんびり", "まじめ"]
    }
]

partner_questions = [
    {
        "q": "相手に求める第一印象は？",
        "choices": ["優しさ", "面白さ", "落ち着き", "頼もしさ"]
    },
    {
        "q": "理想のデートは？",
        "choices": ["カフェでまったり", "アクティブにお出かけ", "家でのんびり", "美味しいもの巡り"]
    },
    {
        "q": "相手の性格で重視するのは？",
        "choices": ["誠実さ", "明るさ", "知的さ", "情熱"]
    },
    {
        "q": "あなたの恋愛タイプは？",
        "choices": ["尽くすタイプ", "甘えたいタイプ", "友達みたいな関係", "刺激がほしい"]
    },
    {
        "q": "相手に求める生活スタイルは？",
        "choices": ["安定してる", "自由で柔軟", "一緒に行動したい", "お互い自立"]
    }
]

dream_questions = [
    {
        "q": "最近見た夢の雰囲気は？",
        "choices": ["楽しい", "不思議", "怖い", "悲しい"]
    },
    {
        "q": "夢に出てきた場所は？",
        "choices": ["家", "学校・職場", "知らない場所", "自然の中"]
    },
    {
        "q": "夢に出てきた人物は？",
        "choices": ["家族", "友達", "知らない人", "誰もいない"]
    },
    {
        "q": "夢の中のあなたの気持ちは？",
        "choices": ["安心していた", "焦っていた", "ワクワクしていた", "ぼんやりしていた"]
    },
    {
        "q": "夢の印象は？",
        "choices": ["強く覚えている", "少し覚えている", "ほとんど覚えていない", "断片的に覚えている"]
    }
]

root = tk.Tk()
root.title("診断アプリ")
root.geometry("400x300")

# --- 画面切り替え ---
def show_frame(frame):
    frame.pack(fill="both", expand=True)
    for f in frames:
        if f != frame:
            f.pack_forget()

# --- メイン画面 ---
main_frame = tk.Frame(root)
main_frame.config(bg="#ffeef2")

tk.Label(main_frame, text="テーマを選んでね").pack(pady=20)

selected_theme = tk.StringVar()

def start_test(theme):
    global current_question, answers, current_questions
    selected_theme.set(theme)
    current_question = 0
    answers = []

    if theme == "job":
        current_questions = job_questions
    elif theme == "pref":
        current_questions = pref_questions
    elif theme == "partner":
        current_questions = partner_questions
    elif theme == "fortune":
        show_fortune_result()
        show_frame(result_frame)
        return
    elif theme == "dream":
        current_questions = dream_questions
    load_question()
    show_frame(question_frame)

tk.Button(main_frame, text="① 適職診断", command=lambda: start_test("job")).pack(pady=5)
tk.Button(main_frame, text="② 都道府県診断", command=lambda: start_test("pref")).pack(pady=5)
tk.Button(main_frame, text="③ 理想のパートナー診断", command=lambda: start_test("partner")).pack(pady=5)
tk.Button(main_frame, text="④ 今日の占い", command=lambda: start_test("fortune")).pack(pady=5)
tk.Button(main_frame, text="⑤ 夢のメッセージ", command=lambda: start_test("dream")).pack(pady=5)

# --- 質問画面 ---
# --- 質問画面 ---
question_frame = tk.Frame(root)
question_frame.config(bg="#ffeef2")  

current_question = 0
selected_answer = tk.StringVar()
answers = []

question_label = tk.Label(question_frame, text="", font=base_font)
question_label.config(bg="#ffeef2")  
question_label.pack(pady=20)

question_label.pack(pady=20)



choice_buttons = []

def load_question():
    selected_answer.set("")
    q_data = current_questions[current_question]
    question_label.config(text=q_data["q"])

    for w in choice_buttons:
        w.destroy()
    choice_buttons.clear()

    for choice in q_data["choices"]:
        rb = tk.Radiobutton(question_frame, text=choice, variable=selected_answer, value=choice, font=base_font,bg="#ffeef2",fg="#444444",selectcolor="#ffd6e7")
        rb.pack(anchor="w")
        choice_buttons.append(rb)


def next_question():
    global current_question
    if selected_answer.get() == "":
        return

    answers.append(selected_answer.get())
    current_question += 1

    if current_question < len(current_questions):
        load_question()
    else:
        show_result()
        show_frame(result_frame)

tk.Button(question_frame, text="次へ",font=base_font,bg="#ffd6e7",fg="#333333", command=next_question).pack(pady=10)

# --- 結果画面 ---
result_frame = tk.Frame(root)
result_frame.config(bg="#ffeef2")

result_label = tk.Label(result_frame, text="", font=base_font)
result_label.config(bg="#ffeef2", fg="#444444")

result_label.pack(pady=20)

tk.Button(result_frame,text="メニューに戻る",font=base_font,bg="#ffd6e7",fg="#333333",command=back_to_menu).pack(pady=10)
command=lambda: show_frame(main_frame).pack()

def show_result():
    if selected_theme.get() == "job":
        show_job_result()
    elif selected_theme.get() == "pref":
        show_pref_result()
    elif selected_theme.get() == "partner":
        show_partner_result()
    elif selected_theme.get() == "dream":
        show_dream_result()

# --- 適職診断の結果 ---
def show_job_result():
    scores = {"creative": 0, "support": 0, "steady": 0, "active": 0}

    if answers[0] == "クリエイティブ系":
        scores["creative"] += 2
    elif answers[0] == "対人支援系":
        scores["support"] += 2
    elif answers[0] == "コツコツ作業系":
        scores["steady"] += 2

    if answers[1] == "論理・分析タイプ":
        scores["steady"] += 1
    elif answers[1] == "社交・行動タイプ":
        scores["active"] += 1
    elif answers[1] == "対人・サポートタイプ":
        scores["support"] += 1
    elif answers[1] == "管理・実務タイプ":
        scores["steady"] += 1

    if answers[2] == "ビジネス・スキル系":
        scores["active"] += 1
    elif answers[2] == "コミュニケーション・性格系":
        scores["support"] += 1
    elif answers[2] == "日常生活・その他":
        scores["steady"] += 1

    if answers[3] == "大勢の前":
        scores["creative"] += 1
        scores["steady"] += 1
    elif answers[3] == "細かい作業":
        scores["active"] += 1
        scores["creative"] += 1

    if answers[4] == "給与":
        scores["active"] += 1
    elif answers[4] == "時間":
        scores["steady"] += 1
    elif answers[4] == "やりがい":
        scores["creative"] += 1
        scores["support"] += 1
    elif answers[4] == "安定性":
        scores["steady"] += 1

    result_type = max(scores, key=scores.get)

    messages = {
    "creative": (
        "あなたは【クリエイティブタイプ】\n"
        "自由な発想や表現力を活かす仕事が向いています。\n\n"
        "📌 向いている職業の例：\n"
        "・デザイナー\n"
        "・イラストレーター\n"
        "・ライター\n"
        "・動画編集\n"
        "・企画職\n"
    ),
    "support": (
        "あなたは【サポートタイプ】\n"
        "人の役に立つことに喜びを感じるタイプです。\n\n"
        "📌 向いている職業の例：\n"
        "・看護師\n"
        "・保育士\n"
        "・カウンセラー\n"
        "・接客業\n"
        "・介護職\n"
    ),
    "steady": (
        "あなたは【コツコツ実務タイプ】\n"
        "安定・正確さ・継続力が強みです。\n\n"
        "📌 向いている職業の例：\n"
        "・事務職\n"
        "・経理\n"
        "・データ入力\n"
        "・技術職\n"
        "・図書館司書\n"
    ),
    "active": (
        "あなたは【行動・社交タイプ】\n"
        "行動力とコミュ力が武器です。\n\n"
        "📌 向いている職業の例：\n"
        "・営業\n"
        "・販売\n"
        "・イベントスタッフ\n"
        "・広報\n"
        "・サービス業\n"
    )
}

    result_label.config(text=messages[result_type])

# --- 都道府県診断の結果 ---
def show_pref_result():
    score = {"tokyo": 0, "hokkaido": 0, "kyoto": 0, "okinawa": 0}

    if answers[0] == "都会":
        score["tokyo"] += 2
    elif answers[0] == "自然":
        score["hokkaido"] += 2
    elif answers[0] == "歴史":
        score["kyoto"] += 2
    elif answers[0] == "海":
        score["okinawa"] += 2

    if answers[1] == "寒いのが好き":
        score["hokkaido"] += 1
    elif answers[1] == "暑いのが好き":
        score["okinawa"] += 1

    if answers[2] == "海鮮":
        score["hokkaido"] += 1
        score["okinawa"] += 1
    elif answers[2] == "麺類":
        score["tokyo"] += 1
        score["kyoto"] += 1

    if answers[3] == "便利な街":
        score["tokyo"] += 1
    elif answers[3] == "静かな田舎":
        score["hokkaido"] += 1

    if answers[4] == "明るい":
        score["okinawa"] += 1
    elif answers[4] == "落ち着いてる":
        score["kyoto"] += 1

    result_pref = max(score, key=score.get)

    messages = {
        "tokyo": "あなたに合う都道府県は【東京都】",
        "hokkaido": "あなたに合う都道府県は【北海道】",
        "kyoto": "あなたに合う都道府県は【京都府】",
        "okinawa": "あなたに合う都道府県は【沖縄県】"
    }

    result_label.config(text=messages[result_pref])

def show_partner_result():
    score = {"gentle": 0, "fun": 0, "calm": 0, "strong": 0}

    # 質問1：第一印象
    if answers[0] == "優しさ":
        score["gentle"] += 2
    elif answers[0] == "面白さ":
        score["fun"] += 2
    elif answers[0] == "落ち着き":
        score["calm"] += 2
    elif answers[0] == "頼もしさ":
        score["strong"] += 2

    # 質問2：デート
    if answers[1] == "カフェでまったり":
        score["gentle"] += 1
        score["calm"] += 1
    elif answers[1] == "アクティブにお出かけ":
        score["fun"] += 1
        score["strong"] += 1
    elif answers[1] == "家でのんびり":
        score["calm"] += 1
    elif answers[1] == "美味しいもの巡り":
        score["gentle"] += 1
        score["fun"] += 1

    # 質問3：性格
    if answers[2] == "誠実さ":
        score["gentle"] += 1
    elif answers[2] == "明るさ":
        score["fun"] += 1
    elif answers[2] == "知的さ":
        score["calm"] += 1
    elif answers[2] == "情熱":
        score["strong"] += 1

    # 質問4：恋愛タイプ
    if answers[3] == "尽くすタイプ":
        score["gentle"] += 1
    elif answers[3] == "甘えたいタイプ":
        score["strong"] += 1
    elif answers[3] == "友達みたいな関係":
        score["fun"] += 1
    elif answers[3] == "刺激がほしい":
        score["strong"] += 1

    # 質問5：生活スタイル
    if answers[4] == "安定してる":
        score["calm"] += 1
    elif answers[4] == "自由で柔軟":
        score["fun"] += 1
    elif answers[4] == "一緒に行動したい":
        score["strong"] += 1
    elif answers[4] == "お互い自立":
        score["calm"] += 1

    result_type = max(score, key=score.get)

    messages = {
        "gentle": "あなたに合うのは【優しくて包容力のある人】\n安心感をくれるタイプが相性◎",
        "fun": "あなたに合うのは【明るくて楽しい人】\n一緒に笑って過ごせる関係がぴったり。",
        "calm": "あなたに合うのは【落ち着いた大人な人】\n穏やかで安定した関係が向いています。",
        "strong": "あなたに合うのは【頼れる情熱的な人】\n引っ張ってくれるタイプが相性◎"
    }

    result_label.config(text=messages[result_type])

import random
from datetime import datetime

def show_fortune_result():
    fortunes = ["最高の運勢", "とても良い", "良い", "普通", "注意が必要", "波乱の予感"]
    colors = ["赤", "青", "黄色", "緑", "紫", "ピンク", "白", "黒"]
    items = ["ハンカチ", "スマホ", "アクセサリー", "飲み物", "本", "お菓子", "時計"]

    today = datetime.now().strftime("%Y/%m/%d")

    result_text = f"🔮 今日の占い（{today}）\n\n"
    result_text += f"【総合運】{random.choice(fortunes)}\n"
    result_text += f"【ラッキーカラー】{random.choice(colors)}\n"
    result_text += f"【ラッキーアイテム】{random.choice(items)}\n"

    result_label.config(text=result_text)

def show_dream_result():
    score = {"positive": 0, "mystery": 0, "stress": 0, "memory": 0}

    # 質問1：雰囲気
    if answers[0] == "楽しい":
        score["positive"] += 2
    elif answers[0] == "不思議":
        score["mystery"] += 2
    elif answers[0] == "怖い":
        score["stress"] += 2
    elif answers[0] == "悲しい":
        score["memory"] += 2

    # 質問2：場所
    if answers[1] == "知らない場所":
        score["mystery"] += 1
    elif answers[1] == "家":
        score["memory"] += 1

    # 質問3：人物
    if answers[2] == "家族":
        score["memory"] += 1
    elif answers[2] == "知らない人":
        score["mystery"] += 1

    # 質問4：気持ち
    if answers[3] == "安心していた":
        score["positive"] += 1
    elif answers[3] == "焦っていた":
        score["stress"] += 1
    elif answers[3] == "ワクワクしていた":
        score["positive"] += 1

    # 質問5：印象
    if answers[4] == "強く覚えている":
        score["memory"] += 1

    result_type = max(score, key=score.get)

    messages = {
        "positive": "🌙 あなたの夢は『前向きな変化』を示しています。\n新しいことを始める準備が整っているサイン。",
        "mystery": "🌙 あなたの夢は『直感が冴えている』サイン。\n無意識からのメッセージが届いています。",
        "stress": "🌙 あなたの夢は『心の疲れ』を映しています。\nゆっくり休む時間を作ると良い方向に向かいます。",
        "memory": "🌙 あなたの夢は『大切な気持ち』を思い出させています。\n忘れかけていた想いが心の奥で動いています。"
    }

    result_label.config(text=messages[result_type])

# --- フレーム一覧 ---
frames = [main_frame, question_frame, result_frame]

show_frame(main_frame)
root.mainloop()