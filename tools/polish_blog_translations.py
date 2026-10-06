"""Repeatable editorial corrections for automatic translation ambiguities."""
import json
from pathlib import Path

ROOT=Path(__file__).parent/'translations'
HEADINGS=[
 'Learner driver guides',
 'Why choose Learners Test Australia for your learner test?',
 'How the NSW Driver Knowledge Test works',
 'The Victorian learner permit test explained',
 'QLD written road rules test vs PrepL: which should you do?',
 'Give way rules every learner driver must know',
 'How to use mock tests and mistakes to prepare for your learner test',
 'Hazard perception test: what it is in NSW, VIC and QLD',
]
TRANSLATED={
 'zh-Hans': ['学车与驾照考试指南','为什么选择 Learners Test Australia 备考驾照理论考试？','NSW 驾驶知识考试（DKT）指南','维多利亚州学习驾照理论考试详解','QLD 道路规则笔试与 PrepL：如何选择？','学车者必须了解的让行规则','如何利用模拟考试和错题准备驾照理论考试','NSW、VIC 和 QLD 的危险感知测试（HPT）详解'],
 'ar': ['أدلة تعلّم القيادة','لماذا تختار Learners Test Australia للتحضير لاختبار القيادة النظري؟','كيف يعمل اختبار المعرفة بالقيادة في NSW؟','شرح اختبار تصريح تعلّم القيادة في فيكتوريا','اختبار قواعد المرور الكتابي في QLD أم PrepL: أيهما تختار؟','قواعد إعطاء الأولوية التي يجب أن يعرفها كل متعلّم قيادة','كيف تستفيد من الاختبارات التجريبية والأخطاء للتحضير لاختبار القيادة النظري','شرح اختبار إدراك المخاطر في NSW وVIC وQLD'],
 'vi': ['Hướng dẫn học lái xe','Vì sao chọn Learners Test Australia để ôn thi lý thuyết lái xe?','Tìm hiểu bài thi kiến thức lái xe DKT tại NSW','Giải thích bài thi cấp giấy phép học lái xe tại Victoria','Thi viết luật giao thông QLD hay PrepL: nên chọn hình thức nào?','Quy tắc nhường đường mọi người học lái xe cần biết','Cách dùng bài thi thử và lỗi sai để ôn thi lý thuyết lái xe','Tìm hiểu bài thi nhận biết nguy hiểm tại NSW, VIC và QLD'],
 'es': ['Guías para aprender a conducir','¿Por qué elegir Learners Test Australia para preparar el examen teórico?','Cómo funciona el examen de conocimientos de conducción de NSW','Guía del examen para el permiso de aprendiz en Victoria','Examen escrito de normas de tránsito de QLD o PrepL: ¿cuál elegir?','Reglas para ceder el paso que todo aprendiz debe conocer','Cómo usar los exámenes de práctica y los errores para preparar el examen teórico','Cómo es la prueba de percepción de peligros en NSW, VIC y QLD'],
}
ROUNDABOUT={
 'zh-Hans':'必须让行给所有已经进入环岛的车辆，不论它们位于你的右侧、正前方还是左侧。仅向右侧来车让行是一种常见误解。留意已经进入环岛、较难看见的摩托车骑手，并记住你旁边或前方的车辆可能即将驶出环岛，穿过你的行驶路线。',
 'ar':'أعطِ الأولوية لكل مركبة موجودة بالفعل داخل الدوار، سواء كانت على يمينك أو أمامك أو على يسارك. من الأخطاء الشائعة الاعتقاد بأن الأولوية للمركبات القادمة من اليمين فقط. انتبه لراكبي الدراجات الموجودين داخل الدوار، فقد يصعب رؤيتهم، وتذكّر أن مركبة بجانبك أو أمامك قد تستعد للخروج عبر مسارك.',
 'vi':'Nhường đường cho mọi phương tiện đã ở trong vòng xuyến, dù ở bên phải, phía trước hay bên trái bạn. Chỉ nhường đường cho xe từ bên phải là một hiểu lầm phổ biến. Hãy chú ý đến người đi xe hai bánh đang ở trong vòng xuyến vì họ khó được nhìn thấy hơn. Xe bên cạnh hoặc phía trước bạn có thể sắp ra khỏi vòng xuyến và cắt ngang hướng đi của bạn.',
 'es':'Debe ceder el paso a todos los vehículos que ya estén dentro de la rotonda, ya sea a su derecha, delante o a su izquierda. Es un error frecuente creer que solo se cede el paso a los vehículos de la derecha. Vigile a los conductores de vehículos de dos ruedas que ya circulan por la rotonda, pues pueden ser difíciles de ver. Un vehículo a su lado o delante puede estar a punto de salir cruzando su trayectoria.',
}
MISTAKES={
 'zh-Hans':'可以把它理解为允许答错的题数：常识部分最多可错 3 题，道路安全部分最多可错 1 题。道路安全部分的题量是常识部分的两倍，容错空间又很小，因此值得投入更多复习时间。',
 'ar':'فكّر في الأمر بوصفه الحد الأقصى المسموح به للأخطاء: يمكنك الإجابة خطأ عن 3 أسئلة في قسم المعرفة العامة، لكن عن سؤال واحد فقط في قسم السلامة على الطرق. عدد أسئلة السلامة ضعف عدد أسئلة المعرفة العامة، والهامش المسموح للأخطاء ضيق، لذا خصّص له معظم وقت المراجعة.',
 'vi':'Có thể hiểu đây là số câu được phép trả lời sai: tối đa 3 câu ở phần kiến thức chung, nhưng chỉ 1 câu ở phần an toàn giao thông. Phần an toàn giao thông có số câu gấp đôi và cho phép rất ít lỗi, nên bạn cần dành phần lớn thời gian ôn tập cho phần này.',
 'es':'Piense en el número máximo de errores permitidos: puede fallar 3 preguntas de conocimientos generales, pero solo 1 de seguridad vial. La sección de seguridad vial tiene el doble de preguntas y deja muy poco margen de error, por lo que merece gran parte del tiempo de repaso.',
}
REPLACEMENTS={
 'zh-Hans': [('美元','澳元'),('学习许可证','学习驾照'),('学习许可测试','学习驾照考试'),('学习驾驶员','学车者'),('状态差异','各州差异'),('您的主管','您的陪练驾驶员'),('在主管时','在陪练时')],
 'ar': [('دولارًا أمريكيًا','دولارًا أستراليًا'),('دولار أمريكي','دولار أسترالي'),('تفسح المجال للحق','تعطي الأولوية للمركبات القادمة من اليمين'),('اختلافات الحالة','الاختلافات بين الولايات'),('الوهمية','التجريبية'),('وهمية','تجريبية'),('الوهمي','التجريبي'),('وهمي','تجريبي'),('بحالتك','بولايتك'),('حالتك وجهازك','ولايتك وجهازك'),('خاصة بالحالة','خاصة بالولاية')],
 'vi': [('USD','AUD'),('giấy phép học tập','giấy phép học lái xe'),('bài kiểm tra người học','bài thi lý thuyết lái xe'),('phân biệt trạng thái','sự khác biệt giữa các tiểu bang'),('người học ô tô','người học lái ô tô'),('Bạn có thể ngồi sau khi','Bạn có thể dự thi sau khi'),('không có thẻ HPT','chưa đỗ bài thi HPT')],
 'es': [('estudiantes de automóviles','aprendices de conducción'),('prueba de aprendizaje','examen teórico de conducir'),('diferencias de estado','diferencias entre estados')],
}

def main():
    from build import all_pages
    pages={p.path:p for p in all_pages()}
    descriptions={
      'ar': {
        'how-to-use-mock-tests-and-mistakes':'تعلّم كيف تستفيد من الاختبارات التجريبية: افهم حدود الأخطاء في كل قسم، وراجع الإجابات الخاطئة، ثم ضع خطة للتحضير لاختبار القيادة النظري.',
        'qld-written-road-rules-test-vs-prepl':'قارن اختبار قواعد المرور الكتابي في QLD مع PrepL: الأسئلة، ودرجات النجاح، والعمر، والتكلفة، وإعادة المحاولة، لاختيار المسار المناسب لك.',
      },
      'es': {
        'how-to-use-mock-tests-and-mistakes':'Prepara el examen teórico con simulacros: conoce el margen de error de cada sección, revisa tus fallos y organiza un plan de estudio para aprender las normas.',
        'index':'Guías para aprender a conducir: exámenes de NSW, Victoria y Queensland, reglas para ceder el paso, consejos de estudio y percepción de peligros.',
        'qld-written-road-rules-test-vs-prepl':'Compara el examen escrito de normas de tránsito de Queensland con PrepL: preguntas, nota mínima, edad, coste y nuevos intentos para elegir tu ruta.',
        'victorian-learner-permit-test-explained':'Conoce el examen para el permiso de aprendiz en Victoria: curso en línea, examen presencial, documentos necesarios, contenidos y normas específicas del estado.',
        'why-choose-learners-test-australia':'Descubre Learners Test Australia: práctica por estado, respuestas explicadas, repasos diarios, estudio sin conexión y Premium opcional con pago único.',
      },
      'vi': {
        'hazard-perception-test-nsw-vic-qld':'Tìm hiểu bài thi nhận biết nguy hiểm HPT tại NSW, VIC và QLD: kỹ năng cần học, thời điểm được dự thi, thời hạn kết quả và cách luyện tập.',
        'how-to-use-mock-tests-and-mistakes':'Cách ôn thi lý thuyết lái xe bằng bài thi thử: hiểu số lỗi được phép ở mỗi phần, luyện tập như thi thật và biến từng lỗi sai thành nội dung ôn tập.',
        'index':'Hướng dẫn học lái xe: bài thi tại NSW, Victoria và Queensland, quy tắc nhường đường, cách ôn tập bằng bài thi thử và kỹ năng nhận biết nguy hiểm.',
        'qld-written-road-rules-test-vs-prepl':'So sánh bài thi viết luật giao thông Queensland với PrepL về số câu hỏi, điểm đỗ, độ tuổi, chi phí và thi lại để chọn hình thức phù hợp.',
        'victorian-learner-permit-test-explained':'Tìm hiểu bài thi cấp giấy phép học lái xe Victoria: khóa học trực tuyến, bài thi trực tiếp, giấy tờ cần thiết, nội dung và quy tắc riêng của bang.',
        'why-choose-learners-test-australia':'Khám phá Learners Test Australia: luyện thi theo tiểu bang, giải thích đáp án, ôn tập hằng ngày, học ngoại tuyến và gói Premium trả phí một lần.',
      },
    }
    for lang in TRANSLATED:
        path=ROOT/(lang+'.json')
        data=json.loads(path.read_text(encoding='utf-8')); strings=data['strings']
        for key,value in strings.items():
            for old,new in REPLACEMENTS[lang]: value=value.replace(old,new)
            if key.startswith('Every vehicle already in the roundabout,'): value=ROUNDABOUT[lang]
            if key.startswith('It helps to think of this as a mistake budget.'): value=MISTAKES[lang]
            if key in ('A$0','A$5.99'): value=key
            strings[key]=value
        strings.update(zip(HEADINGS,TRANSLATED[lang]))
        for name in ('Overpass', 'Atkinson Hyperlegible Next'):
            if name in strings: strings[name]=name
        strings['Everything in Free, plus:']={
            'zh-Hans':'包含免费版的所有功能，另加：',
            'ar':'جميع مزايا الخطة المجانية، بالإضافة إلى:',
            'vi':'Mọi tính năng của gói Miễn phí, cộng thêm:',
            'es':'Todo lo incluido en el plan gratuito, más:',
        }[lang]
        if lang=='ar':
            strings.update({'States':'الولايات','states':'الولايات','territories':'الأقاليم',
                            'state guides':'أدلة الولايات','state or territory':'الولاية أو الإقليم',
                            'give way to the right':'أعطِ الأولوية للمركبات القادمة من يمينك'})
        # Metadata uses the same reviewed topic wording, without the long brand suffix.
        titles={
          'Learner Driver Guides | Learners Test Australia':0,
          'Why Choose Our Learner Test App? | Learners Test Australia':1,
          'NSW Driver Knowledge Test Guide | Learners Test Australia':2,
          'VIC Learner Permit Test Explained | Learners Test Australia':3,
          'QLD Road Rules Test vs PrepL | Learners Test Australia':4,
          'Give Way Rules for Learner Drivers | Learners Test Australia':5,
          'Mock Test Tips for Learners | Learners Test Australia':6,
          'Hazard Perception Test Explained | Learners Test Australia':7,
        }
        for key,index in titles.items():
            if key in strings: strings[key]=TRANSLATED[lang][index]
        for slug,desc in descriptions.get(lang,{}).items():
            strings[pages['blog/'+slug+'.html'].description]=desc
        if lang=='ar': strings['Mock Test Tips for Learners | Learners Test Australia']='كيف تستفيد من الاختبارات التجريبية وأخطائك في المراجعة؟'
        if lang=='es':
            strings['Mock Test Tips for Learners | Learners Test Australia']='Cómo aprender de los exámenes de práctica y de tus errores'
            strings['Why Choose Our Learner Test App? | Learners Test Australia']='¿Por qué elegir Learners Test Australia?'
        data['editorial_notes']='Topic headings, driving terminology, roundabout wording, error allowances and currency spot-checked; not a professional translation review.'
        path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')


if __name__=='__main__': main()
