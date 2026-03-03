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

    if st.button("② 都道府県診断"):
        st.session_state.current_theme = "pref"
        st.session_state.current_questions = pref_questions
        st.session_state.current_question = 0
        st.session_state.answers = []
        st.session_state.page = "question"

    if st.button("③ 理想のパートナー診断"):
        st.session_state.current_theme = "partner"
        st.session_state.current_questions = partner_questions
        st.session_state.current_question = 0
        st.session_state.answers = []
        st.session_state.page = "question"

    if st.button("④ 今日の占い"):
        st.session_state.page = "fortune"

    if st.button("⑤ 夢のメッセージ"):
        st.session_state.current_theme = "dream"
        st.session_state.current_questions = dream_questions
        st.session_state.current_question = 0
        st.session_state.answers = []
        st.session_state.page = "question"

# --- 質問画面 ---
if st.session_state.page == "question":
    q = st.session_state.current_questions[st.session_state.current_question]
    st.write(f"**Q{st.session_state.current_question+1}. {q['q']}**")

    choice = st.radio("選択肢を選んでね", q["choices"])

    if st.button("次へ"):
        st.session_state.answers.append(choice)
        st.session_state.current_question += 1

        if st.session_state.current_question >= len(st.session_state.current_questions):
            st.session_state.page = "result"
        else:
            st.rerun()

    if st.button("メニューに戻る"):
        st.session_state.page = "menu"
        st.rerun()

# --- 結果ロジック ---
def show_job_result():
    answers = st.session_state.answers
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
        "creative": "あなたは【クリエイティブタイプ】\n自由な発想や表現力を活かす仕事が向いています。",
        "support": "あなたは【サポートタイプ】\n人の役に立つことに喜びを感じるタイプです。",
        "steady": "あなたは【コツコツ実務タイプ】\n安定・正確さ・継続力が強みです。",
        "active": "あなたは【行動・社交タイプ】\n行動力とコミュ力が武器です。",
    }

    st.markdown(messages[result_type])

# --- 結果画面 ---
if st.session_state.page == "result":
    st.title("✨ あなたの結果 ✨")

    if st.session_state.current_theme == "job":
        show_job_result()

    if st.button("メニューに戻る"):
        st.session_state.page = "menu"
        st.rerun()

# --- 今日の占い ---
if st.session_state.page == "fortune":
    st.title("🔮 今日の占い")
    st.markdown("今日の運勢は…（ここに占いロジックを入れる）")

    if st.button("メニューに戻る"):
        st.session_state.page = "menu"
        st.rerun()
