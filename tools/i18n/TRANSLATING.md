# Translating learnertest.com

The website has pages in Simplified Chinese (`zh`), Arabic (`ar`), Vietnamese (`vi`) and Spanish (`es`), the app's
languages. `tools/i18n.py` explains the mechanics; this file is the style guide.

## Who reads it

People living in Australia whose first language is Chinese, Arabic, Vietnamese or Spanish, preparing for their learner
driver test, and their parents. Write the way a careful native speaker in Australia would write for them: natural, plain
and friendly, like the app. Translate the meaning, not word for word. Address the reader as the app does: 你 (zh),
singular أنت (ar, Modern Standard Arabic), bạn (vi), tú (es, neutral Spanish that reads well in Latin America and
Spain).

## Keep the meaning exactly

- Facts, numbers, prices, conditions and dates must say exactly what the English says. Do not add claims, superlatives
  or marketing that the English does not have. Keep every hedge ("an estimate, not a guarantee", "check the official
  website").
- Never suggest the app or site is official, government-run or endorsed. Keep the independence disclaimer complete.
- ACT: never use, or translate, the terms "Pre-Learner Licence", "Pre-Learner course", "Road Rules Knowledge Test" or
  "Safe Plates", and never call any ACT question mandatory or compulsory. The English avoids these; don't add them.

## Placeholders

Segments show inline markup as numbered placeholders:

- `<t1>text</t1>`: a link, bold text or similar. Translate the text inside and keep the pair. You may move it to suit
  your word order.
- `<x2/>`: an icon, image, line break or name that stays as it is. Keep it, normally in the same position.

Every placeholder in the English must appear exactly once in your translation, and no other tags. Keep HTML entities
such as `&amp;` (or write the character). Never write a bare `<`.

## Keep these as they are

- Names: Learners Test Australia, Learners Test Australia: DKT, BlueOrbit, DTT Ireland, Google Play, Android,
  Premium (the app keeps "Premium" in every language), the email address.
- Prices and numbers: A$5.99 and every number in digits 0-9 (Arabic too: no Arabic-Indic digits).
- Codes, in Latin letters: NSW, VIC, QLD, SA, WA, TAS, ACT, NT, DKT, HPT, PrepL, myLs, MVR. If the English uses a code,
  your translation must contain it.
- Official names of tests, handbooks, laws, agencies and websites (Driver Knowledge Test, Road User Handbook, Road to
  Solo Driving, Road Traffic Code 2000, Service NSW, VicRoads, Access Canberra, Plates Plus, Service Tasmania,
  nt.gov.au...). Keep the English name, because that is what the reader will see at the licensing office and on
  official websites, and add a short translation in brackets the first time it helps, for example
  vi: `bài thi Driver Knowledge Test (DKT, thi lý thuyết lái xe)`.

## Terms (use the app's words)

`tools/i18n/app-glossary.tsv` has the app's own translations; use the same words. The key ones:

| English | zh | ar | vi | es |
|---|---|---|---|---|
| knowledge test, learners test | 交规笔试 (学习驾照笔试) | الاختبار النظري | thi lý thuyết (thi bằng L) | examen teórico |
| learner licence / learner permit | 学习驾照 (L 牌) | رخصة المتعلم (L) | bằng lái tập sự (bằng L) | licencia de aprendiz (L) |
| L plates / P plates | L 牌 / P 牌 | لوحات L / لوحات P | biển L / biển P | placas L / placas P |
| mock test | 模拟考试 | اختبار تجريبي | thi thử | simulacro de examen |
| hazard perception test | 危险感知测试 | اختبار إدراك المخاطر | thi nhận biết nguy hiểm | prueba de percepción de riesgos |
| hazard perception clips | 危险感知短片 | مقاطع إدراك المخاطر | đoạn phim nhận biết nguy hiểm | clips de percepción de riesgos |
| pass chance | 通过概率 | فرصة النجاح | khả năng đậu | probabilidad de aprobar |
| quick check | 快速摸底 | تقييم سريع | kiểm tra nhanh | prueba rápida |
| weak spots | 薄弱环节 | نقاط الضعف | điểm yếu | puntos débiles |
| give way | 让行 | إعطاء الأولوية | nhường đường | ceder el paso |
| supervised driving hours | 陪练驾驶时数 | ساعات القيادة تحت الإشراف | số giờ lái có giám sát | horas de conducción supervisada |

States and territories (keep the code next to the name when the English has the code):

| English | zh | ar | vi | es |
|---|---|---|---|---|
| New South Wales | 新南威尔士州 | نيو ساوث ويلز | New South Wales | Nueva Gales del Sur |
| Victoria | 维多利亚州 | فيكتوريا | Victoria | Victoria |
| Queensland | 昆士兰州 | كوينزلاند | Queensland | Queensland |
| South Australia | 南澳 (南澳大利亚州) | جنوب أستراليا | Nam Úc | Australia Meridional |
| Western Australia | 西澳 (西澳大利亚州) | غرب أستراليا | Tây Úc | Australia Occidental |
| Tasmania | 塔斯马尼亚州 | تسمانيا | Tasmania | Tasmania |
| Australian Capital Territory | 首都领地 (澳大利亚首都领地) | إقليم العاصمة الأسترالية | Lãnh thổ Thủ đô Úc | Territorio de la Capital Australiana |
| Northern Territory | 北领地 | الإقليم الشمالي | Lãnh thổ Bắc Úc | Territorio del Norte |

## Search engines (titles and descriptions)

The `title` and `description` segments are what people see in Google. Write them the way a native speaker in Australia
would search: put the main phrase in your language first, keep the English test name or code where the English title has
one (people search both, for example "NSW DKT 练习"), and keep "| Learners Test Australia" at the end of titles if
there is room. Length limits (characters): zh title up to 40, description 45-100; ar title up to 70, description
100-175; vi title up to 70, description 110-190; es title up to 70, description 120-190. Each title must be different.

Search phrases people use (use where they fit naturally, don't stuff):
- zh: 澳洲驾照笔试, 学车笔试, 交规考试, 学习驾照, 考L牌, 各州交规笔试
- ar: اختبار رخصة القيادة في أستراليا, الاختبار النظري للقيادة, رخصة المتعلم
- vi: thi bằng lái xe ở Úc, thi lý thuyết lái xe, thi bằng L, luyện thi bằng lái
- es: examen teórico de conducir en Australia, licencia de aprendiz, test de conducir

## Punctuation

Use your language's normal punctuation and quotation marks (zh “”和全角标点, ar «» or “” and the Arabic comma ،,
vi “”, es “” or «»). Avoid straight double quotes `"` in the text.

## Workflow for a translator

1. Your file is a JSON list of segments: `key`, `kind`, `note`, `pages` (where it appears), `src` (English) and `t`
   (empty). Fill in `t` for every entry and change nothing else. Read a few neighbouring entries for context: they are
   in page order.
2. Save the file as valid UTF-8 JSON (escape `"` and `\` inside strings).
3. Run `python tools/i18n.py validate LANG FILE` and fix every problem until it reports 0.
4. Don't run `merge` or `build.py`; the lead merges the parts.
