import streamlit as st
import random
from datetime import datetime

# --- 初期化 ---
if "page" not in st.session_state:
    st.session_state.page = "menu"
    st.session_state.current_question = 0
    st.session_state.answers = []
    st.session_state.current_questions = []
    st.session_state.current_theme = ""

# --- 質問データ ---
job_questions = [
    {"q": "どんな仕事に興味がある？やってみたいことは？",
     "choices": ["クリエイティブ系", "対人支援系", "コツコツ作業系"]},
    {"q": "性格タイプは？",
     "choices": ["論理・分析タイプ", "社交・行動タイプ", "対人・サポートタイプ", "管理・実務タイプ"]},
    {"q": "得意なことは？",
     "choices": ["ビジネス・スキル系", "コミュニケーション・性格系", "日常生活・その他"]},
    {"q": "苦手・絶対にやりたくないことは？",
     "choices": ["大勢の前", "細かい作業"]},
    {"q": "何を一番重視する？",
     "choices": ["給与", "時間", "やりがい", "安定性"]},
]

pref_questions = [
    {"q": "旅行で行きたい雰囲気は？", "choices": ["都会", "自然", "歴史", "海"]},
    {"q": "気候の好みは？", "choices": ["暑いのが好き", "寒いのが好き", "どっちもOK"]},
    {"q": "食べ物の好みは？", "choices": ["海鮮", "肉料理", "麺類", "甘いもの"]},
    {"q": "住むならどんな場所？", "choices": ["便利な街", "静かな田舎", "観光地", "工業地帯"]},
    {"q": "人の雰囲気は？", "choices": ["明るい", "落ち着いてる", "のんびり", "まじめ"]},
]

partner_questions = [
    {"q": "相手に求める第一印象は？",
     "choices": ["優しさ", "面白さ", "落ち着き", "頼もしさ"]},
    {"q": "理想のデートは？",
     "choices": ["カフェでまったり", "アクティブにお出かけ", "家でのんびり", "美味しいもの巡り"]},
    {"q": "相手の性格で重視するのは？",
     "choices": ["誠実さ", "明るさ", "知的さ", "情熱"]},
    {"q": "あなたの恋愛タイプは？",
     "choices": ["尽くすタイプ", "甘えたいタイプ", "友達みたいな関係", "刺激がほしい"]},
    {"q": "相手に求める生活スタイルは？",
     "choices": ["安定してる", "自由で柔軟", "一緒に行動したい", "お互い自立"]},
]

dream_questions = [
    {"q": "最近見た夢の雰囲気は？", "choices": ["楽しい", "不思議", "怖い", "悲しい"]},
    {"q": "夢に出てきた場所は？", "choices": ["家", "学校・職場", "知らない場所", "自然の中"]},
    {"q": "夢に出てきた人物は？", "choices": ["家族", "友達", "知らない人", "誰もいない"]},
    {"q": "夢の中のあなたの気持ちは？",
     "choices": ["安心していた", "焦っていた", "ワクワクしていた", "ぼんやりしていた"]},
    {"q": "夢の印象は？",
     "choices": ["強く覚えている", "少し覚えている", "ほとんど覚えていない", "断片的に覚えている"]},
]

# --- 都道府県診断 ---
def show_pref_result():
    answers = st.session_state.answers
    score = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}

    if answers[0] == "都会":
        score["A"] += 2
    elif answers[0] == "自然":
        score["B"] += 2
    elif answers[0] == "歴史":
        score["C"] += 2
    elif answers[0] == "海":
        score["D"] += 2

    if answers[1] == "寒いのが好き":
        score["B"] += 1
    elif answers[1] == "暑いのが好き":
        score["D"] += 1

    if answers[2] == "海鮮":
        score["B"] += 1
        score["D"] += 1
    elif answers[2] == "麺類":
        score["A"] += 1
        score["C"] += 1

    if answers[3] == "便利な街":
        score["A"] += 1
    elif answers[3] == "静かな田舎":
        score["B"] += 1

    if answers[4] == "明るい":
        score["D"] += 1
    elif answers[4] == "落ち着いてる":
        score["C"] += 1

    pref_groups = {
        "A": ["東京都","神奈川県","千葉県","埼玉県","大阪府","愛知県","兵庫県","福岡県"],
        "B": ["北海道","青森県","岩手県","秋田県","山形県","長野県","熊本県","宮崎県","鹿児島県"],
        "C": ["京都府","奈良県","石川県","富山県","福井県","広島県","岡山県","香川県"],
        "D": ["沖縄県","高知県","愛媛県","長崎県","佐賀県","大分県","和歌山県"],
        "E": ["新潟県","群馬県","栃木県","茨城県","三重県","岐阜県","滋賀県","鳥取県","島根県"]
    }

    result_type = max(score, key=score.get)
    result_text = "、".join(pref_groups[result_type])

    st.markdown(f"""
### ✨ あなたに合う都道府県 ✨

あなたにぴったりの地域は…

## 【{result_text}】

旅行や移住の参考にしてみてね🌸
""")

# --- パートナー診断 ---
def show_partner_result():
    answers = st.session_state.answers
    score = {"gentle": 0, "fun": 0, "calm": 0, "strong": 0}

    if answers[0] == "優しさ":
        score["gentle"] += 2
    elif answers[0] == "面白さ":
        score["fun"] += 2
    elif answers[0] == "落ち着き":
        score["calm"] += 2
    elif answers[0] == "頼もしさ":
        score["strong"] += 2

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

    if answers[2] == "誠実さ":
        score["gentle"] += 1
    elif answers[2] == "明るさ":
        score["fun"] += 1
    elif answers[2] == "知的さ":
        score["calm"] += 1
    elif answers[2] == "情熱":
        score["strong"] += 1

    if answers[3] == "尽くすタイプ":
        score["gentle"] += 1
    elif answers[3] == "甘えたいタイプ":
        score["strong"] += 1
    elif answers[3] == "友達みたいな関係":
        score["fun"] += 1
    elif answers[3] == "刺激がほしい":
        score["strong"] += 1

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

    st.markdown(f"""
### 💗 あなたに合うパートナータイプ

## {messages[result_type]}

恋愛のヒントにしてみてね💗
""")

# --- 夢診断 ---
def show_dream_result():
    answers = st.session_state.answers
    score = {"happy": 0, "mystery":
