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

    # --- デザイン（ここから） ---
    st.markdown("""
        <style>
            .result-box {
                background-color: #fff7fb;
                padding: 25px;
                border-radius: 20px;
                border: 2px solid #ffb6d9;
                box-shadow: 0 0 10px rgba(255, 182, 217, 0.4);
                font-size: 1.2rem;
                line-height: 1.8;
            }
            .result-title {
                font-size: 1.6rem;
                font-weight: bold;
                color: #ff69b4;
                text-align: center;
                margin-bottom: 10px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="result-box">', unsafe_allow_html=True)

    st.markdown(f"""
        <div class="result-title">✨ あなたに合う都道府県 ✨</div>

        あなたにぴったりの地域は…

        <h2>【{result_text}】</h2>

        旅行や移住の参考にしてみてね🌸
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe

# --- 適職診断 ---
def show_job_result():
    answers = st.session_state.answers

    score = {"creative": 0, "support": 0, "steady": 0, "active": 0}

    # 質問1
    if answers[0] == "クリエイティブ系":
        score["creative"] += 2
    elif answers[0] == "対人支援系":
        score["support"] += 2
    elif answers[0] == "コツコツ作業系":
        score["steady"] += 2

    # 質問2
    if answers[1] == "論理・分析タイプ":
        score["steady"] += 1
    elif answers[1] == "社交・行動タイプ":
        score["active"] += 1
    elif answers[1] == "対人・サポートタイプ":
        score["support"] += 1
    elif answers[1] == "管理・実務タイプ":
        score["steady"] += 1

    # 質問3
    if answers[2] == "ビジネス・スキル系":
        score["active"] += 1
    elif answers[2] == "コミュニケーション・性格系":
        score["support"] += 1
    elif answers[2] == "日常生活・その他":
        score["steady"] += 1

    # 質問4
    if answers[3] == "大勢の前":
        score["creative"] += 1
    elif answers[3] == "細かい作業":
        score["active"] += 1

    # 質問5
    if answers[4] == "給与":
        score["active"] += 1
    elif answers[4] == "時間":
        score["steady"] += 1
    elif answers[4] == "やりがい":
        score["creative"] += 1
    elif answers[4] == "安定性":
        score["support"] += 1

    result_type = max(score, key=score.get)

    messages = {
        "creative": "あなたは【クリエイティブタイプ】✨\n自由な発想で新しいものを生み出す仕事が向いています。",
        "support": "あなたは【サポートタイプ】✨\n人の役に立つ仕事で力を発揮できます。",
        "steady": "あなたは【安定・コツコツタイプ】✨\n丁寧で正確な作業が得意です。",
        "active": "あなたは【アクティブタイプ】✨\n行動力があり、動きのある仕事が向いています。"
    }

    # --- デザイン（ここから） ---
    st.markdown("""
        <style>
            .result-box {
                background-color: #fff7fb;
                padding: 25px;
                border-radius: 20px;
                border: 2px solid #ffb6d9;
                box-shadow: 0 0 10px rgba(255, 182, 217, 0.4);
                font-size: 1.2rem;
                line-height: 1.8;
            }
            .result-title {
                font-size: 1.6rem;
                font-weight: bold;
                color: #ff69b4;
                text-align: center;
                margin-bottom: 10px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="result-box">', unsafe_allow_html=True)

    st.markdown(f"""
        <div class="result-title">💼 適職診断の結果 ✨</div>

        <h2>{messages[result_type]}</h2>

        自分の強みを活かしてみてね✨
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    # --- デザイン（ここまで） ---

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
        "gentle": "あなたに合うのは【優しくて包容力のある人】💞\n安心感をくれるタイプが相性◎",
        "fun": "あなたに合うのは【明るくて楽しい人】🎉\n一緒に笑って過ごせる関係がぴったり。",
        "calm": "あなたに合うのは【落ち着いた大人な人】🌿\n穏やかで安定した関係が向いています。",
        "strong": "あなたに合うのは【頼れる情熱的な人】🔥\n引っ張ってくれるタイプが相性◎"
    }

    # --- デザイン（ここから） ---
    st.markdown("""
        <style>
            .result-box {
                background-color: #fff7fb;
                padding: 25px;
                border-radius: 20px;
                border: 2px solid #ffb6d9;
                box-shadow: 0 0 10px rgba(255, 182, 217, 0.4);
                font-size: 1.2rem;
                line-height: 1.8;
            }
            .result-title {
                font-size: 1.6rem;
                font-weight: bold;
                color: #ff69b4;
                text-align: center;
                margin-bottom: 10px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="result-box">', unsafe_allow_html=True)

    st.markdown(f"""
        <div class="result-title">💗 パートナー診断の結果 ✨</div>

        <h2>{messages[result_type]}</h2>

        恋愛のヒントにしてみてね💗
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    # --- デザイン（ここまで） ---

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
        "gentle": "あなたに合うのは【優しくて包容力のある人】💞\n安心感をくれるタイプが相性◎",
        "fun": "あなたに合うのは【明るくて楽しい人】🎉\n一緒に笑って過ごせる関係がぴったり。",
        "calm": "あなたに合うのは【落ち着いた大人な人】🌿\n穏やかで安定した関係が向いています。",
        "strong": "あなたに合うのは【頼れる情熱的な人】🔥\n引っ張ってくれるタイプが相性◎"
    }

    # --- デザイン（ここから） ---
    st.markdown("""
        <style>
            .result-box {
                background-color: #fff7fb;
                padding: 25px;
                border-radius: 20px;
                border: 2px solid #ffb6d9;
                box-shadow: 0 0 10px rgba(255, 182, 217, 0.4);
                font-size: 1.2rem;
                line-height: 1.8;
            }
            .result-title {
                font-size: 1.6rem;
                font-weight: bold;
                color: #ff69b4;
                text-align: center;
                margin-bottom: 10px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="result-box">', unsafe_allow_html=True)

    st.markdown(f"""
        <div class="result-title">💗 パートナー診断の結果 ✨</div>

        <h2>{messages[result_type]}</h2>

        恋愛のヒントにしてみてね💗
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    # --- デザイン（ここまで） --
# --- 夢診断 ---
def show_dream_result():
    answers = st.session_state.answers
    score = {"happy": 0, "mystery": 0, "fear": 0, "sad": 0}

    if answers[0] == "楽しい":
        score["happy"] += 2
    elif answers[0] == "不思議":
        score["mystery"] += 2
    elif answers[0] == "怖い":
        score["fear"] += 2
    elif answers[0] == "悲しい":
        score["sad"] += 2

    if answers[1] == "家":
        score["happy"] += 1
    elif answers[1] == "学校・職場":
        score["sad"] += 1
    elif answers[1] == "知らない場所":
        score["mystery"] += 1
    elif answers[1] == "自然の中":
        score["happy"] += 1

    if answers[2] == "家族":
        score["happy"] += 1
    elif answers[2] == "友達":
        score["happy"] += 1
    elif answers[2] == "知らない人":
        score["mystery"] += 1
    elif answers[2] == "誰もいない":
        score["sad"] += 1

    if answers[3] == "安心していた":
        score["happy"] += 1
    elif answers[3] == "焦っていた":
        score["fear"] += 1
    elif answers[3] == "ワクワクしていた":
        score["happy"] += 1
    elif answers[3] == "ぼんやりしていた":
        score["mystery"] += 1

    if answers[4] == "強く覚えている":
        score["mystery"] += 1
    elif answers[4] == "少し覚えている":
        score["happy"] += 1
    elif answers[4] == "ほとんど覚えていない":
        score["sad"] += 1
    elif answers[4] == "断片的に覚えている":
        score["fear"] += 1

    result_type = max(score, key=score.get)

    messages = {
        "happy": "あなたの夢は【前向きで心が元気なサイン】✨\n良いエネルギーが満ちています🌈",
        "mystery": "あなたの夢は【直感が冴えているサイン】🔮\n新しい気づきや変化が近づいています。",
        "fear": "あなたの夢は【不安やストレスのサイン】🌙\n無理をしすぎていないか、少し休んでね。",
        "sad": "あなたの夢は【心が少し疲れているサイン】💐\n優しい時間を自分にあげてね。"
    }

    # --- デザイン（ここから） ---
    st.markdown("""
        <style>
            .result-box {
                background-color: #f7f4ff;
                padding: 25px;
                border-radius: 20px;
                border: 2px solid #c9b7ff;
                box-shadow: 0 0 12px rgba(150, 130, 255, 0.3);
                font-size: 1.2rem;
                line-height: 1.8;
            }
            .result-title {
                font-size: 1.6rem;
                font-weight: bold;
                color: #8a6bff;
                text-align: center;
                margin-bottom: 10px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="result-box">', unsafe_allow_html=True)

    st.markdown(f"""
        <div class="result-title">🌙 夢診断の結果 ✨</div>

        <h2>{messages[result_type]}</h2>

        夢は心の声だから、少し意識してみると気づきがあるかも。
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    # --- デザイン（ここまで） ---

# --- 今日の占い ---
def show_fortune_result():
    fortunes = [
        "最高の運勢", "とても良い", "良い", "普通", "注意が必要", "波乱の予感",
        "チャンス到来", "直感が冴える日", "ゆっくり休む日", "新しい出会いの予感"
    ]

    colors = [
        "赤", "青", "黄色", "緑", "紫", "ピンク", "白", "黒",
        "ゴールド", "シルバー"
    ]

    items = {
        "小物": ["ハンカチ", "スマホ", "アクセサリー", "腕時計", "鍵", "メガネ", "イヤホン"],
        "飲み物": ["カフェラテ", "抹茶ラテ", "紅茶", "緑茶", "ココア", "炭酸水", "レモネード"],
        "お菓子": ["チョコレート", "クッキー", "グミ", "キャンディ", "ポッキー", "マカロン"]
    }

    lucky_foods = [
        "オムライス", "カレーライス", "ハンバーグ", "パスタ",
        "寿司", "ラーメン", "サンドイッチ", "おにぎり", "フルーツ", "ヨーグルト"
    ]

    lucky_actions = [
        "深呼吸をする", "散歩に出かける", "お気に入りの音楽を聴く",
        "ストレッチをする"
    ]

    fortune = random.choice(fortunes)
    color = random.choice(colors)
    category = random.choice(list(items.keys()))
    item = random.choice(items[category])
    food = random.choice(lucky_foods)
    action = random.choice(lucky_actions)

    # --- デザイン（ここから） ---
    st.markdown("""
        <style>
            .fortune-box {
                background-color: #fff8f0;
                padding: 25px;
                border-radius: 20px;
                border: 2px solid #ffd9a8;
                box-shadow: 0 0 12px rgba(255, 200, 150, 0.4);
                font-size: 1.2rem;
                line-height: 1.8;
            }
            .fortune-title {
                font-size: 1.6rem;
                font-weight: bold;
                color: #ff9a3c;
                text-align: center;
                margin-bottom: 10px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="fortune-box">', unsafe_allow_html=True)

    st.markdown(f"""
        <div class="fortune-title">🔮 今日の運勢 ✨</div>

        <h2>【{fortune}】</h2>

        <ul>
            <li><b>ラッキーカラー：</b> {color}</li>
            <li><b>ラッキーアイテム：</b> {item}（{category}）</li>
            <li><b>ラッキーフード：</b> {food}</li>
            <li><b>ラッキーアクション：</b> {action}</li>
        </ul>

        今日が素敵な一日になりますように ✨🌟
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    # --- デザイン（ここまで） ---

# --- 質問画面 ---
if st.session_state.page == "question":
    q = st.session_state.current_questions[st.session_state.current_question]
    st.write(f"**Q{st.session_state.current_question+1}. {q['q']}**")

    choice = st.radio("選択肢を選んでね", q["choices"], key=f"radio_{st.session_state.current_question}")

    if st.button("次へ", key=f"next_{st.session_state.current_question}"):
        st.session_state.answers.append(choice)
        st.session_state.current_question += 1

        if st.session_state.current_question >= len(st.session_state.current_questions):
            st.session_state.page = "result"
        else:
            st.rerun()

    if st.button("メニューに戻る", key=f"back_{st.session_state.current_question}"):
        st.session_state.page = "menu"
        st.rerun()
        
# --- 結果画面 ---
if st.session_state.page == "result":
    st.title("✨ あなたの結果 ✨")

    if st.session_state.current_theme == "job":
        show_job_result()
    elif st.session_state.current_theme == "pref":
        show_pref_result()
    elif st.session_state.current_theme == "partner":
        show_partner_result()
    elif st.session_state.current_theme == "dream":
        show_dream_result()

    if st.button("メニューに戻る"):
        st.session_state.page = "menu"
        st.rerun()

# --- 結果画面のデザイン ---
st.markdown("""
    <style>
        .result-box {
            background-color: #fff7fb;
            padding: 25px;
            border-radius: 20px;
            border: 2px solid #ffb6d9;
            box-shadow: 0 0 10px rgba(255, 182, 217, 0.4);
            font-size: 1.2rem;
            line-height: 1.8;
        }
        .result-title {
            font-size: 1.6rem;
            font-weight: bold;
            color: #ff69b4;
            text-align: center;
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="result-box">', unsafe_allow_html=True)

# --- 今日の占い ---
if st.session_state.page == "fortune":
    st.title("🔮 今日の占い")
    show_fortune_result()

    if st.button("メニューに戻る"):
        st.session_state.page = "menu"
        st.rerun()

# --- メニュー画面 ---
if st.session_state.page == "menu":
    st.title("✨ 診断アプリ ✨")
    st.write("テーマを選んでね")

    if st.button("① 適職診断"):
        st.session_state.current_theme = "job"
        st.session_state.current_questions = job_questions
        st.session_state.current_question = 0
        st.session_state.answers = []
        st.session_state.page = "question"
        st.rerun()

    if st.button("② 都道府県診断"):
        st.session_state.current_theme = "pref"
        st.session_state.current_questions = pref_questions
        st.session_state.current_question = 0
        st.session_state.answers = []
        st.session_state.page = "question"
        st.rerun()

    if st.button("③ パートナー診断"):
        st.session_state.current_theme = "partner"
        st.session_state.current_questions = partner_questions
        st.session_state.current_question = 0
        st.session_state.answers = []
        st.session_state.page = "question"
        st.rerun()

    if st.button("④ 夢診断"):
        st.session_state.current_theme = "dream"
        st.session_state.current_questions = dream_questions
        st.session_state.current_question = 0
        st.session_state.answers = []
        st.session_state.page = "question"
        st.rerun()

    if st.button("⑤ 今日の占い"):
        st.session_state.page = "fortune"
        st.rerun()


