"""Home page block "Try a question" (design phase 3, October 2026).

Three questions from the web app, one each from the NSW, VIC and QLD packs, answered right on the page with HTML and
CSS only: no script, no outside request. The questions, their translations and their pictures come from
tools/data/try-questions.json and assets/img/try/, written by the LearnerTest platform's tools/try-questions.ts from
the content the web app serves (it also checks that the release is the live one and gives the count of questions).
Never edit those files by hand: run the tool again, then build.

The block is not part of the translated text (tools/i18n.py): the home page holds the marker MARKER, and render() in
sitelib.py puts the block for the page's language there, with the bank's own translations of the questions and the
strings below. A question the bank has not translated is shown in English, with a note.
"""
from __future__ import annotations

import html
import json
from pathlib import Path

DATA = json.loads((Path(__file__).resolve().parent / "data" / "try-questions.json").read_text(encoding="utf-8"))
MARKER = "<!--TRY-QUESTION-->"

# Extra attributes on every question picture.
IMG_ATTRS = ""

STRINGS = {
    "en": {
        "eyebrow": "Try it now", "title": "Try a question",
        "intro": "Three questions from the web app, from the NSW, VIC and QLD packs. Pick an answer to see if you're right, and why.",
        "step": "Question {i} of {n}", "tag_ok": "Correct answer", "tag_no": "Your answer",
        "say_ok": "Correct.", "say_no": "Not quite.", "answer_is": "The correct answer is:", "next": "Next question",
        "cta": "Practise all {n} questions free in the web app",
        "note": "Free with an account, on any phone or computer. Every state and territory, each in its own test format.",
        "en_note": "This question isn't translated yet, so it is shown in English.",
    },
    "zh": {
        "eyebrow": "马上试试", "title": "试做一道题",
        "intro": "三道来自网页版应用的题目，分别出自 NSW、VIC 和 QLD 题库。选一个答案，看看你是否答对，以及原因。",
        "step": "第 {i} 题，共 {n} 题", "tag_ok": "正确答案", "tag_no": "你的答案",
        "say_ok": "答对了。", "say_no": "不太对。", "answer_is": "正确答案是：", "next": "下一题",
        "cta": "在网页版应用中免费练习全部 {n} 道题",
        "note": "注册免费账户即可使用，任何手机或电脑都可以。涵盖每个州和领地，各按其考试形式出题。",
        "en_note": "这道题还没有翻译，所以显示英文。",
    },
    "ar": {
        "eyebrow": "جرّبه الآن", "title": "جرّب سؤالًا",
        "intro": "ثلاثة أسئلة من تطبيق الويب، من حزم أسئلة NSW وVIC وQLD. اختر إجابة لتعرف إن كانت صحيحة ولماذا.",
        "step": "السؤال {i} من {n}", "tag_ok": "الإجابة الصحيحة", "tag_no": "إجابتك",
        "say_ok": "إجابة صحيحة.", "say_no": "ليست صحيحة تمامًا.", "answer_is": "الإجابة الصحيحة هي:", "next": "السؤال التالي",
        "cta": "تدرّب مجانًا على كل الأسئلة وعددها {n} في تطبيق الويب",
        "note": "مجانًا بحساب، على أي هاتف أو كمبيوتر. لكل ولاية ومقاطعة، كلٌّ بصيغة اختبارها.",
        "en_note": "لم يُترجم هذا السؤال بعد، لذلك يظهر بالإنجليزية.",
    },
    "vi": {
        "eyebrow": "Thử ngay", "title": "Thử một câu hỏi",
        "intro": "Ba câu hỏi trong ứng dụng web, lấy từ bộ câu hỏi NSW, VIC và QLD. Chọn một đáp án để xem bạn đúng hay sai, và vì sao.",
        "step": "Câu {i} trên {n}", "tag_ok": "Đáp án đúng", "tag_no": "Đáp án của bạn",
        "say_ok": "Đúng rồi.", "say_no": "Chưa đúng.", "answer_is": "Đáp án đúng là:", "next": "Câu tiếp theo",
        "cta": "Luyện miễn phí cả {n} câu hỏi trong ứng dụng web",
        "note": "Miễn phí với một tài khoản, trên mọi điện thoại hoặc máy tính. Có đủ mọi bang và lãnh thổ, mỗi nơi theo đúng hình thức thi của mình.",
        "en_note": "Câu hỏi này chưa được dịch nên đang hiển thị bằng tiếng Anh.",
    },
    "es": {
        "eyebrow": "Pruébalo ahora", "title": "Prueba una pregunta",
        "intro": "Tres preguntas de la aplicación web, de los paquetes de NSW, VIC y QLD. Elige una respuesta para ver si aciertas y por qué.",
        "step": "Pregunta {i} de {n}", "tag_ok": "Respuesta correcta", "tag_no": "Tu respuesta",
        "say_ok": "Correcto.", "say_no": "No exactamente.", "answer_is": "La respuesta correcta es:", "next": "Siguiente pregunta",
        "cta": "Practica gratis las {n} preguntas en la aplicación web",
        "note": "Gratis con una cuenta, en cualquier teléfono o computadora. Todos los estados y territorios, cada uno con el formato de su examen.",
        "en_note": "Esta pregunta todavía no está traducida, por eso se muestra en inglés.",
    },
}

# The pack each question comes from (tools/i18n/TRANSLATING.md: state names, code kept).
SOURCES = {
    "nsw": {"en": "New South Wales (NSW)", "zh": "新南威尔士州 (NSW)", "ar": "نيو ساوث ويلز (NSW)", "vi": "New South Wales (NSW)", "es": "Nueva Gales del Sur (NSW)"},
    "vic": {"en": "Victoria (VIC)", "zh": "维多利亚州 (VIC)", "ar": "فيكتوريا (VIC)", "vi": "Victoria (VIC)", "es": "Victoria (VIC)"},
    "qld": {"en": "Queensland (QLD)", "zh": "昆士兰州 (QLD)", "ar": "كوينزلاند (QLD)", "vi": "Queensland (QLD)", "es": "Queensland (QLD)"},
}


def number(n: int, lang: str) -> str:
    """3,770 / 3.770 as the translations write it (tools/i18n: vi and es group with a dot)."""
    return f"{n:,}".replace(",", ".") if lang in ("vi", "es") else f"{n:,}"


def section(lang: str, rtl: bool = False) -> str:
    """The whole home page section for [lang] (put at MARKER by sitelib.render)."""
    from sitelib import icon  # sitelib imports this module
    s = STRINGS[lang]
    return f"""<section class="section section-alt tq" id="try" aria-labelledby="tq-title">
<div class="container">
<div class="section-head">
<p class="eyebrow">{_esc(s["eyebrow"])}</p>
<h2 id="tq-title">{_esc(s["title"])}</h2>
<p>{_esc(s["intro"])}</p>
</div>
{quiz(lang, img_prefix="@/", rtl=rtl)}
<p class="tq-cta"><a class="btn btn-primary" href="/app/">{_esc(s["cta"].format(n=number(DATA["count"], lang)))}{icon("arrow", "icon icon-go")}</a></p>
<p class="tq-note">{_esc(s["note"])}</p>
</div>
</section>"""


# ── The quiz (the same code on every LearnerTest site) ────────────────────────────────────────
# How it works without script: each question is a <fieldset> of radio buttons, written before their labels so CSS
# sibling selectors can react to them (site.css, "Try a question"). Picking a choice marks it, marks the right one,
# shows the reason and fills a polite status line that screen readers announce. Three more radio buttons, drawn as
# round "1 2 3" buttons, choose which question is shown. Everything that only belongs after an answer carries the
# hidden attribute, so without the stylesheet the page shows the first question, its choices and the link to the
# web app, and gives nothing away.

KEYS = "ABCDEFGH"


def _esc(text: str) -> str:
    return html.escape(text, quote=True)


def _text(value: dict, lang: str, rtl: bool) -> tuple[str, str]:
    """A question text in the page language, or in English with its own lang (and direction) when not translated."""
    if value.get(lang):
        return _esc(value[lang]), ""
    return _esc(value["en"]), ' lang="en"' + (' dir="ltr"' if rtl else "")


def translated(question: dict, lang: str) -> bool:
    """Whether the bank has this question in [lang] (stem, every choice and the explanation)."""
    return bool(question["stem"].get(lang) and question["explanation"].get(lang)
                and all(option["text"].get(lang) for option in question["options"]))


def _question(i: int, n: int, q: dict, lang: str, s: dict, img_prefix: str, rtl: bool, source: str) -> str:
    name = f"tq{i}"
    stem, stem_lang = _text(q["stem"], lang, rtl)
    src = f'<span class="tq-src">{_esc(source)}</span>' if source else ""
    out = [f'<fieldset class="tq-q" id="tq-q{i}"{"" if i == 1 else " hidden"}>',
           f'<legend class="tq-legend">{src}<span class="tq-stem"{stem_lang}>{stem}</span></legend>']
    if not translated(q, lang):
        out.append(f'<p class="tq-lang-note">{_esc(s["en_note"])}</p>')
    img = q.get("image")
    if img:
        alt, alt_lang = _text(img["alt"], lang, rtl)
        out.append(f'<img class="tq-img" src="{img_prefix}{img["src"]}" width="{img["width"]}" height="{img["height"]}" '
                   f'alt="{alt}"{alt_lang}{IMG_ATTRS} loading="lazy" decoding="async">')
    for k, o in enumerate(q["options"]):
        ok = "ok" if o["id"] == q["correct"] else "no"
        out.append(f'<input class="tq-in tq-in-{ok}" type="radio" name="{name}" id="{name}-{o["id"]}" autocomplete="off">')
    correct_text = ""
    for k, o in enumerate(q["options"]):
        text, text_lang = _text(o["text"], lang, rtl)
        is_ok = o["id"] == q["correct"]
        if is_ok:
            correct_text = f'<span{text_lang}>{text}</span>' if text_lang else text
            tag = f'<span class="tq-tag tq-tag-ok" aria-hidden="true" hidden>{_esc(s["tag_ok"])}</span>'
        else:
            tag = f'<span class="tq-tag tq-tag-no" aria-hidden="true" hidden>{_esc(s["tag_no"])}</span>'
        out.append(f'<label class="tq-opt{" tq-ok" if is_ok else ""}" for="{name}-{o["id"]}"><span class="tq-key" aria-hidden="true">'
                   f'{KEYS[k]}</span><span class="tq-txt"{text_lang}>{text}</span>{tag}</label>')
    out.append(f'<p class="tq-say" role="status"><span class="tq-say-ok" hidden><strong>{_esc(s["say_ok"])}</strong></span>'
               f'<span class="tq-say-no" hidden><strong>{_esc(s["say_no"])}</strong> {_esc(s["answer_is"])} {correct_text}</span></p>')
    fb = ['<div class="tq-fb" hidden>']
    whys = [o.get("whyWrong") for o in q["options"]]
    if any(whys):
        cells = []
        for o, why in zip(q["options"], whys):
            if why and o["id"] != q["correct"]:
                text, text_lang = _text(why, lang, rtl)
                cells.append(f"<p{text_lang}>{text}</p>")
            else:
                cells.append("<p></p>")
        fb.append(f'<div class="tq-whys">{"".join(cells)}</div>')
    expl, expl_lang = _text(q["explanation"], lang, rtl)
    fb.append(f'<p class="tq-expl"{expl_lang}>{expl}</p>')
    if i < n:
        arrow = "←" if rtl else "→"
        fb.append(f'<p class="tq-more"><label class="tq-next" for="tq-s{i + 1}">{_esc(s["next"])} '
                  f'<span aria-hidden="true">{arrow}</span></label></p>')
    fb.append("</div>")
    out.append("".join(fb))
    out.append("</fieldset>")
    return "\n".join(out)


def quiz(lang: str, *, img_prefix: str = "", rtl: bool = False) -> str:
    """The questions with their round 1-2-3 buttons (no heading, no link: the site's own section wraps them)."""
    s = STRINGS[lang]
    questions = DATA["questions"]
    n = len(questions)
    out = ['<div class="tq-box">']
    for i in range(1, n + 1):
        out.append(f'<input class="tq-step" type="radio" name="tq-step" id="tq-s{i}"{" checked" if i == 1 else ""} '
                   f'autocomplete="off" aria-label="{_esc(s["step"].format(i=i, n=n))}" hidden>')
    out.append('<div class="tq-tabs" aria-hidden="true" hidden>'
               + "".join(f'<label for="tq-s{i}">{i}</label>' for i in range(1, n + 1)) + "</div>")
    for i, q in enumerate(questions, 1):
        source = SOURCES.get(q.get("source") or "", {}).get(lang, "")
        out.append(_question(i, n, q, lang, s, img_prefix, rtl, source))
    out.append("</div>")
    return "\n".join(out)
