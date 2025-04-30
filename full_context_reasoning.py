
# full_context_reasoning_v2.py (Ready for inserting Reasoning Tree 9 ชั้น + Post-Processing Layer)

def full_context_reasoning(text):
    text = text.lower()
    matched_sdgs = set()

    # === นายสามารถนำ Reasoning Tree 9 ชั้นมาใส่ในส่วนนี้ ===
# SDG 1 - No Poverty (Full Context Reasoning Tree with Keywords from Excel)

    # Layer 1: Direct mention of poverty eradication (Expanded from sdg_keywords.xlsx)
    if (
        "poverty" in text
        or "end poverty" in text
        or "poverty alleviation" in text
        or "poverty reduction" in text
        or "poverty eradication" in text
        or "eradicate poverty" in text
        or "alleviating poverty" in text
        or "combat poverty" in text
        or "extreme poverty" in text
        or "lift people out of poverty" in text
        or "การลดความยากจน" in text
        or "ขจัดความยากจน" in text
        or "ยุติความยากจน" in text
        or "บรรเทาความยากจน" in text
        or "ยกระดับชีวิตคนจน" in text
        or "ลดความยากจน" in text
        or "การขจัดความยากจนขั้นรุนแรง" in text
        or "ลดปัญหาความยากจน" in text
        or "ลดช่องว่างทางรายได้" in text
        or "ช่วยเหลือผู้ยากไร้" in text
        or "สร้างโอกาสทางเศรษฐกิจให้ผู้มีรายได้น้อย" in text
    ):
        matched_sdgs.add('1')

    # Layer 2: Focus on vulnerable groups and low income support
    if (
        "vulnerable groups" in text
        or "กลุ่มเปราะบาง" in text
        or "คนจน" in text
        or "รายได้น้อย" in text
        or "poor communities" in text
        or "กลุ่มผู้มีรายได้น้อย" in text
        or "กลุ่มด้อยโอกาส" in text
        or "กลุ่มคนชายขอบ" in text
        or "disadvantaged populations" in text
        or "support vulnerable" in text
        or "การสนับสนุนกลุ่มเปราะบาง" in text
        or "การคุ้มครองทางสังคมสำหรับกลุ่มเสี่ยง" in text
        or "uplift marginalized groups" in text
    ):
        matched_sdgs.add('1')

    # Layer 3: Access to basic services for vulnerable populations
    if (
        "access to basic services" in text
        or "basic services" in text
        or "universal access to basic services" in text
        or "access to education" in text
        or "access to healthcare" in text
        or "access to sanitation" in text
        or "access to financial services" in text
        or "การเข้าถึงบริการพื้นฐาน" in text
        or "เข้าถึงการศึกษา" in text
        or "เข้าถึงบริการสาธารณสุข" in text
        or "เข้าถึงสาธารณูปโภคพื้นฐาน" in text
        or ("สิทธิเข้าถึง" in text and ("บริการพื้นฐาน" in text or "บริการสุขภาพ" in text or "การศึกษา" in text))
    ):
        matched_sdgs.add('1')

    # Layer 4: Financial aid, social welfare, and protection systems
    if (
        "financial aid" in text
        or "social protection" in text
        or "welfare system" in text
        or "cash transfer" in text
        or "microfinance access" in text
        or "emergency financial support" in text
        or "universal social protection" in text
        or "ระบบสวัสดิการสังคม" in text
        or "เงินช่วยเหลือ" in text
        or "การสนับสนุนทางการเงิน" in text
        or "การคุ้มครองทางสังคม" in text
        or ("การเข้าถึง" in text and ("สวัสดิการสังคม" in text or "การคุ้มครองทางสังคม" in text))
    ):
        matched_sdgs.add('1')

    # Layer 5: Economic inequality and inclusive growth
    if (
        "income inequality" in text
        or "economic inequality" in text
        or "reduce economic disparity" in text
        or "ลดความเหลื่อมล้ำทางเศรษฐกิจ" in text
        or "inclusive growth" in text
        or "inclusive economy" in text
        or "การพัฒนาเศรษฐกิจอย่างทั่วถึง" in text
        or "เศรษฐกิจที่ครอบคลุมทุกกลุ่ม" in text
        or "โอกาสทางเศรษฐกิจที่เท่าเทียม" in text
    ):
        matched_sdgs.add('1')

    # Layer 6: Resilience building for poor communities
    if (
        "community resilience" in text
        or "build resilience" in text
        or "เสริมสร้างความสามารถในการฟื้นตัว" in text
        or ("เสริมศักยภาพ" in text and ("ชุมชนเปราะบาง" in text or "ชุมชนยากจน" in text))
        or ("resilience" in text and ("community" in text or "economic resilience" in text))
        or "ลดความเสี่ยงจากภัยพิบัติ" in text
        or "เพิ่มความสามารถในการฟื้นตัว" in text
    ):
        matched_sdgs.add('1')

    # Layer 7: Access to resources (land, finance, markets)
    if (
        "access to land" in text
        or "access to finance" in text
        or "access to markets" in text
        or "การเข้าถึงที่ดิน" in text
        or "การเข้าถึงแหล่งเงินทุน" in text
        or "การเข้าถึงตลาด" in text
        or "ที่ดิน" in text
        or "แหล่งเงินทุน" in text
    ):
        matched_sdgs.add('1')

    # Layer 8: Pro-poor policy and inclusive economic policies
    if (
        "pro-poor policy" in text
        or "inclusive growth" in text
        or "inclusive economic policy" in text
        or "นโยบายเศรษฐกิจเพื่อคนจน" in text
        or "นโยบายที่ครอบคลุม" in text
    ):
        matched_sdgs.add('1')

    # Layer 9: Structural solutions to eradicate poverty
    if (
        "address root causes of poverty" in text
        or "tackle poverty at its roots" in text
        or "แก้ไขสาเหตุของความยากจน" in text
        or "การเปลี่ยนแปลงโครงสร้างเศรษฐกิจ" in text
    ):
        matched_sdgs.add('1')

# SDG 2 - Zero Hunger (Full Context Reasoning Tree with Keywords from Excel)

    # Layer 1: Direct mention of hunger eradication (Expanded from sdg_keywords.xlsx)
    if (
        "hunger" in text
        or "end hunger" in text
        or "reduce hunger" in text
        or "food security" in text
        or "zero hunger" in text
        or "eradicate hunger" in text
        or "ยุติความหิวโหย" in text
        or "ลดความหิวโหย" in text
        or "การลดปัญหาความหิวโหย" in text
        or "ความมั่นคงทางอาหาร" in text
        or "ขจัดความหิวโหย" in text
        or "อาหารเพียงพอ" in text
    ):
        matched_sdgs.add('2')

    # Layer 2: Focus on food access for vulnerable populations
    if (
        "food access" in text
        or "food insecurity" in text
        or "food aid" in text
        or "ขาดแคลนอาหาร" in text
        or "การเข้าถึงอาหาร" in text
        or "อาหารเพื่อคนยากจน" in text
        or "อาหารเพื่อกลุ่มเปราะบาง" in text
        or "การช่วยเหลือด้านอาหาร" in text
    ):
        matched_sdgs.add('2')

    # Layer 3: Sustainable agriculture and food production systems
    if (
        "sustainable agriculture" in text
        or "agricultural productivity" in text
        or "sustainable food production" in text
        or "การเกษตรที่ยั่งยืน" in text
        or "การผลิตอาหารที่ยั่งยืน" in text
        or "ผลผลิตทางการเกษตร" in text
        or "การพัฒนาการเกษตรอย่างยั่งยืน" in text
    ):
        matched_sdgs.add('2')

    # Layer 4: Support for small-scale farmers and agricultural systems
    if (
        "small-scale farmers" in text
        or "smallholder farmers" in text
        or "local farmers" in text
        or "เกษตรกรรายย่อย" in text
        or "เกษตรกรท้องถิ่น" in text
        or "เกษตรกรรายย่อยที่ยั่งยืน" in text
        or "การสนับสนุนเกษตรกรรายย่อย" in text
    ):
        matched_sdgs.add('2')

    # Layer 5: Food distribution and equity in access to food
    if (
        "food distribution" in text
        or "food equity" in text
        or "การกระจายอาหาร" in text
        or "ความเท่าเทียมในการเข้าถึงอาหาร" in text
        or "การกระจายอาหารอย่างยั่งยืน" in text
        or "การแบ่งปันอาหารกับคนยากจน" in text
    ):
        matched_sdgs.add('2')

    # Layer 6: Addressing climate change impacts on food security
    if (
        "climate change impacts" in text
        or "climate resilience" in text
        or "sustainable farming in changing climate" in text
        or "ผลกระทบจากการเปลี่ยนแปลงสภาพภูมิอากาศ" in text
        or "เกษตรกรรมที่ยั่งยืนในสภาพอากาศเปลี่ยนแปลง" in text
        or "การฟื้นฟูความมั่นคงทางอาหารในสภาพภูมิอากาศเปลี่ยนแปลง" in text
    ):
        matched_sdgs.add('2')

    # Layer 7: Promoting responsible consumption and production in food systems
    if (
        "sustainable food consumption" in text
        or "reduce food waste" in text
        or "responsible food production" in text
        or "อาหารที่ยั่งยืน" in text
        or "ลดขยะอาหาร" in text
        or "การบริโภคอาหารอย่างรับผิดชอบ" in text
        or "การผลิตอาหารที่รับผิดชอบ" in text
    ):
        matched_sdgs.add('2')

    # Layer 8: Strengthening food systems for resilience and sustainability
    if (
        "food systems" in text
        or "food system resilience" in text
        or "sustainable food systems" in text
        or "การพัฒนาระบบอาหารอย่างยั่งยืน" in text
        or "ระบบอาหารที่ยั่งยืน" in text
        or "การเสริมสร้างความสามารถในการฟื้นตัวของระบบอาหาร" in text
    ):
        matched_sdgs.add('2')

    # Layer 9: Long-term policy solutions to end hunger
    if (
        "long-term food security" in text
        or "food security policies" in text
        or "นโยบายความมั่นคงทางอาหาร" in text
        or "การแก้ปัญหาความหิวโหยระยะยาว" in text
        or "การแก้ปัญหาความหิวโหยในระยะยาว" in text
    ):
        matched_sdgs.add('2')

# SDG 3 - Good Health and Well-Being (Full Context Reasoning Tree with Keywords from Excel)

    # Layer 1: Direct mention of health improvement and well-being
    if (
        "health care" in text
        or "health services" in text
        or "universal health coverage" in text
        or "good health" in text
        or "mental health" in text
        or "maternal health" in text
        or "child health" in text
        or "health promotion" in text
        or "disease prevention" in text
        or "road safety" in text
        or "การดูแลสุขภาพ" in text
        or "บริการสุขภาพ" in text
        or "หลักประกันสุขภาพถ้วนหน้า" in text
        or "สุขภาพที่ดี" in text
        or "สุขภาพจิต" in text
        or "สุขภาพแม่และเด็ก" in text
        or "การส่งเสริมสุขภาพ" in text
        or "การป้องกันโรค" in text
        or "ความปลอดภัยทางถนน" in text
    ):
        matched_sdgs.add('3')

    # Layer 2: Focus on health access, preventive measures, and health systems
    if (
        "primary health care" in text
        or "health system strengthening" in text
        or "vaccination programs" in text
        or "emergency health response" in text
        or "mental health support" in text
        or "nutrition programs" in text
        or "บริการปฐมภูมิ" in text
        or "เสริมสร้างระบบสุขภาพ" in text
        or "การฉีดวัคซีน" in text
        or "การตอบสนองฉุกเฉินด้านสุขภาพ" in text
        or "การสนับสนุนสุขภาพจิต" in text
        or "โภชนาการ" in text
    ):
        matched_sdgs.add('3')

    # Layer 3: Related to key health services and risk prevention
    if (
        "clinics and hospitals" in text
        or "vaccination campaigns" in text
        or "nutrition education" in text
        or "mental health services" in text
        or "health insurance" in text
        or "disaster response" in text
        or "คลินิกและโรงพยาบาล" in text
        or "การรณรงค์ฉีดวัคซีน" in text
        or "การให้ความรู้ด้านโภชนาการ" in text
        or "บริการสุขภาพจิต" in text
        or "ประกันสุขภาพ" in text
        or "การตอบสนองภัยพิบัติ" in text
    ):
        matched_sdgs.add('3')

    # Layer 4: Specific health interventions and programs
    if (
        "build rural clinics" in text
        or "polio eradication" in text
        or "school meal programs" in text
        or "suicide prevention programs" in text
        or "mobile emergency units" in text
        or "community health outreach" in text
        or "สร้างคลินิกชนบท" in text
        or "การกำจัดโปลิโอ" in text
        or "โครงการอาหารกลางวันโรงเรียน" in text
        or "โครงการป้องกันการฆ่าตัวตาย" in text
        or "หน่วยฉุกเฉินเคลื่อนที่" in text
        or "การเข้าถึงชุมชนด้านสุขภาพ" in text
    ):
        matched_sdgs.add('3')

    # Layer 5: Program examples targeting health outcomes
    if (
        "community health workers" in text
        or "hpv vaccination" in text
        or "vitamin supplementation" in text
        or "crisis hotlines" in text
        or "field hospitals" in text
        or "health insurance rollout" in text
        or "อาสาสมัครสาธารณสุข" in text
        or "การฉีดวัคซีน HPV" in text
        or "การเสริมวิตามิน" in text
        or "สายด่วนสุขภาพจิต" in text
        or "โรงพยาบาลสนาม" in text
        or "การขยายประกันสุขภาพ" in text
    ):
        matched_sdgs.add('3')

    # Layer 6: Health-related measurable indicators
    if (
        "vaccination coverage" in text
        or "suicide rate" in text
        or "nutrition improvement" in text
        or "emergency response time" in text
        or "health service access rate" in text
        or "insurance coverage" in text
        or "อัตราการฉีดวัคซีน" in text
        or "อัตราการฆ่าตัวตาย" in text
        or "การพัฒนาโภชนาการ" in text
        or "เวลาตอบสนองเหตุฉุกเฉิน" in text
        or "อัตราการเข้าถึงบริการสุขภาพ" in text
        or "ความครอบคลุมของการประกันสุขภาพ" in text
    ):
        matched_sdgs.add('3')

    # Layer 7: Health outcomes and behavior change
    if (
        "increased patient access" in text
        or "reduced disease outbreaks" in text
        or "improved mental health" in text
        or "improved child health" in text
        or "higher health literacy" in text
        or "ลดการระบาดของโรค" in text
        or "สุขภาพจิตที่ดีขึ้น" in text
        or "สุขภาพเด็กที่ดีขึ้น" in text
        or "ความรู้ด้านสุขภาพที่เพิ่มขึ้น" in text
    ):
        matched_sdgs.add('3')

    # Layer 8: Impact on broader health system and society
    if (
        "reduce maternal mortality" in text
        or "end epidemics" in text
        or "access to reproductive health" in text
        or "integrate mental health" in text
        or "improve road safety" in text
        or "ลดอัตราการเสียชีวิตของมารดา" in text
        or "ยุติการแพร่ระบาดของโรค" in text
        or "การเข้าถึงบริการอนามัยการเจริญพันธุ์" in text
        or "บูรณาการสุขภาพจิตในระบบสุขภาพปฐมภูมิ" in text
        or "ปรับปรุงความปลอดภัยทางถนน" in text
    ):
        matched_sdgs.add('3')

    # Layer 9: Contribution to global health goals
    if (
        "healthier populations" in text
        or "enhanced workforce productivity" in text
        or "reduce poverty from medical costs" in text
        or "strengthen health systems" in text
        or "increase life expectancy" in text
        or "ประชากรมีสุขภาพดีขึ้น" in text
        or "เพิ่มประสิทธิภาพแรงงาน" in text
        or "ลดความยากจนจากค่าใช้จ่ายทางการแพทย์" in text
        or "เสริมสร้างระบบสุขภาพ" in text
        or "เพิ่มอายุขัยเฉลี่ย" in text
    ):
        matched_sdgs.add('3')

# SDG 4 - Quality Education (Full Context Reasoning Tree with Keywords from Excel)

    # Layer 1: Direct mention of education and learning
    if (
        "quality education" in text
        or "inclusive education" in text
        or "equitable education" in text
        or "lifelong learning" in text
        or "access to education" in text
        or "การศึกษาที่มีคุณภาพ" in text
        or "การศึกษาที่ครอบคลุม" in text
        or "การศึกษาที่เท่าเทียม" in text
        or "การเรียนรู้ตลอดชีวิต" in text
        or "การเข้าถึงการศึกษา" in text
    ):
        matched_sdgs.add('4')

    # Layer 2: Early childhood to tertiary education
    if (
        "early childhood education" in text
        or "primary education" in text
        or "secondary education" in text
        or "tertiary education" in text
        or "technical education" in text
        or "การศึกษาปฐมวัย" in text
        or "การศึกษาขั้นพื้นฐาน" in text
        or "การศึกษามัธยมศึกษา" in text
        or "การศึกษาระดับอุดมศึกษา" in text
        or "การศึกษาอาชีวศึกษา" in text
    ):
        matched_sdgs.add('4')

    # Layer 3: Access and equity
    if (
        "free education" in text
        or "affordable education" in text
        or "education for vulnerable" in text
        or "education for disabled" in text
        or "gender equality in education" in text
        or "การศึกษาโดยไม่เสียค่าใช้จ่าย" in text
        or "การศึกษาในราคาที่เอื้อมถึงได้" in text
        or "การศึกษาสำหรับกลุ่มเปราะบาง" in text
        or "การศึกษาสำหรับคนพิการ" in text
        or "ความเสมอภาคทางเพศในระบบการศึกษา" in text
    ):
        matched_sdgs.add('4')

    # Layer 4: Skills for work and life
    if (
        "technical skills" in text
        or "vocational skills" in text
        or "entrepreneurship education" in text
        or "relevant skills for employment" in text
        or "การฝึกทักษะด้านเทคนิค" in text
        or "ทักษะอาชีพ" in text
        or "การศึกษาผู้ประกอบการ" in text
        or "ทักษะที่เกี่ยวข้องกับการจ้างงาน" in text
    ):
        matched_sdgs.add('4')

    # Layer 5: Quality learning environments
    if (
        "safe learning environment" in text
        or "inclusive learning environment" in text
        or "effective learning environment" in text
        or "สิ่งแวดล้อมการเรียนรู้ที่ปลอดภัย" in text
        or "สิ่งแวดล้อมการเรียนรู้ที่ครอบคลุม" in text
        or "สิ่งแวดล้อมการเรียนรู้ที่มีประสิทธิภาพ" in text
    ):
        matched_sdgs.add('4')

    # Layer 6: Literacy and numeracy
    if (
        "literacy skills" in text
        or "numeracy skills" in text
        or "basic literacy" in text
        or "basic numeracy" in text
        or "ทักษะการรู้หนังสือ" in text
        or "ทักษะการคำนวณ" in text
        or "การรู้หนังสือขั้นพื้นฐาน" in text
        or "การคำนวณขั้นพื้นฐาน" in text
    ):
        matched_sdgs.add('4')

    # Layer 7: Education policy and financing
    if (
        "education policy" in text
        or "education financing" in text
        or "investment in education" in text
        or "นโยบายด้านการศึกษา" in text
        or "การจัดสรรงบประมาณเพื่อการศึกษา" in text
        or "การลงทุนในภาคการศึกษา" in text
    ):
        matched_sdgs.add('4')

    # Layer 8: Teacher training and capacity building
    if (
        "teacher training" in text
        or "teacher qualification" in text
        or "capacity building for teachers" in text
        or "การฝึกอบรมครู" in text
        or "คุณสมบัติของครู" in text
        or "การพัฒนาศักยภาพครู" in text
    ):
        matched_sdgs.add('4')

    # Layer 9: Global citizenship and sustainable education
    if (
        "education for sustainable development" in text
        or "education for global citizenship" in text
        or "human rights education" in text
        or "education for cultural diversity" in text
        or "การศึกษาด้านการพัฒนาที่ยั่งยืน" in text
        or "การศึกษาด้านพลเมืองโลก" in text
        or "การศึกษาด้านสิทธิมนุษยชน" in text
        or "การศึกษาด้านความหลากหลายทางวัฒนธรรม" in text
    ):
        matched_sdgs.add('4')

 # SDG 5 - Gender Equality (Full Context Reasoning Tree with Keywords from Excel)

    # Layer 1: Direct mention of gender equality
    if (
        "gender equality" in text
        or "women empowerment" in text
        or "end discrimination against women" in text
        or "ยุติการเลือกปฏิบัติต่อผู้หญิง" in text
        or "ความเสมอภาคทางเพศ" in text
        or "การเสริมสร้างพลังให้ผู้หญิง" in text
    ):
        matched_sdgs.add('5')

    # Layer 2: Discrimination and violence elimination
    if (
        "violence against women" in text
        or "domestic violence" in text
        or "sexual violence" in text
        or "end all violence against women" in text
        or "ยุติความรุนแรงต่อผู้หญิง" in text
        or "ความรุนแรงในครอบครัว" in text
        or "ความรุนแรงทางเพศ" in text
    ):
        matched_sdgs.add('5')

    # Layer 3: Access to leadership and decision-making
    if (
        "women in leadership" in text
        or "women participation in decision-making" in text
        or "increase women's political participation" in text
        or "ผู้หญิงในตำแหน่งผู้นำ" in text
        or "การมีส่วนร่วมของผู้หญิงในการตัดสินใจ" in text
        or "การเพิ่มการมีส่วนร่วมทางการเมืองของผู้หญิง" in text
    ):
        matched_sdgs.add('5')

    # Layer 4: Access to economic resources
    if (
        "equal access to economic resources" in text
        or "women's right to land and property" in text
        or "financial services for women" in text
        or "การเข้าถึงทรัพยากรทางเศรษฐกิจอย่างเท่าเทียม" in text
        or "สิทธิของผู้หญิงในที่ดินและทรัพย์สิน" in text
        or "บริการทางการเงินสำหรับผู้หญิง" in text
    ):
        matched_sdgs.add('5')

    # Layer 5: Sexual and reproductive health rights
    if (
        "sexual and reproductive health" in text
        or "access to reproductive rights" in text
        or "education on reproductive health" in text
        or "สุขภาพทางเพศและอนามัยการเจริญพันธุ์" in text
        or "การเข้าถึงสิทธิด้านการเจริญพันธุ์" in text
        or "การศึกษาด้านสุขภาพการเจริญพันธุ์" in text
    ):
        matched_sdgs.add('5')

    # Layer 6: Legal frameworks for gender equality
    if (
        "laws promoting gender equality" in text
        or "legal protection for women" in text
        or "นโยบายส่งเสริมความเสมอภาคทางเพศ" in text
        or "การคุ้มครองทางกฎหมายสำหรับผู้หญิง" in text
    ):
        matched_sdgs.add('5')

    # Layer 7: Shared domestic responsibilities
    if (
        "recognize unpaid care and domestic work" in text
        or "shared responsibility within the household" in text
        or "ยอมรับงานดูแลและงานบ้านที่ไม่ได้รับค่าจ้าง" in text
        or "การแบ่งปันความรับผิดชอบในครอบครัว" in text
    ):
        matched_sdgs.add('5')

    # Layer 8: Gender equality in technology and innovation
    if (
        "women in technology" in text
        or "equal opportunities in innovation" in text
        or "ผู้หญิงในเทคโนโลยี" in text
        or "โอกาสที่เท่าเทียมในการนวัตกรรม" in text
    ):
        matched_sdgs.add('5')

    # Layer 9: Global support and partnerships for gender equality
    if (
        "global partnerships for gender equality" in text
        or "international support for women's rights" in text
        or "ความร่วมมือระดับโลกเพื่อความเสมอภาคทางเพศ" in text
        or "การสนับสนุนสิทธิสตรีในระดับสากล" in text
    ):
        matched_sdgs.add('5')

    # SDG 6 - Clean Water and Sanitation (Excel-based Full Reasoning)

    # Layer 1: Core Concepts - Clean Water and Sanitation
    if (
        "clean water" in text
        or "safe drinking water" in text
        or "water access" in text
        or "sanitation" in text
        or "hygiene" in text
        or "affordable water" in text
        or "water quality" in text
        or "น้ำสะอาด" in text
        or "น้ำดื่มปลอดภัย" in text
        or "การเข้าถึงน้ำ" in text
        or "การสุขาภิบาล" in text
        or "สุขอนามัย" in text
        or "น้ำราคาไม่แพง" in text
        or "คุณภาพน้ำ" in text
    ):
        matched_sdgs.add('6')

    # Layer 2: Water Resources Management
    if (
        "water management" in text
        or "integrated water resources management" in text
        or "river basin management" in text
        or "การจัดการน้ำ" in text
        or "การบริหารจัดการทรัพยากรน้ำแบบบูรณาการ" in text
        or "การบริหารลุ่มน้ำ" in text
    ):
        matched_sdgs.add('6')

    # Layer 3: Wastewater and Pollution Control
    if (
        "wastewater treatment" in text
        or "water pollution" in text
        or "wastewater reuse" in text
        or "การบำบัดน้ำเสีย" in text
        or "มลพิษทางน้ำ" in text
        or "การนำกลับมาใช้น้ำเสีย" in text
    ):
        matched_sdgs.add('6')

    # Layer 4: Water Efficiency and Conservation
    if (
        "water efficiency" in text
        or "water conservation" in text
        or "reuse water" in text
        or "ประสิทธิภาพการใช้น้ำ" in text
        or "การอนุรักษ์น้ำ" in text
        or "การนำน้ำกลับมาใช้" in text
    ):
        matched_sdgs.add('6')

    # Layer 5: Water Ecosystems Protection
    if (
        "protect aquatic ecosystems" in text
        or "ecosystem restoration" in text
        or "freshwater ecosystems" in text
        or "การปกป้องระบบนิเวศทางน้ำ" in text
        or "การฟื้นฟูระบบนิเวศ" in text
        or "ระบบนิเวศน้ำจืด" in text
    ):
        matched_sdgs.add('6')

    # Layer 6: Community Participation
    if (
        "community participation in water management" in text
        or "local water initiatives" in text
        or "การมีส่วนร่วมของชุมชนในการบริหารน้ำ" in text
        or "โครงการน้ำในท้องถิ่น" in text
    ):
        matched_sdgs.add('6')

    # Layer 7: International Cooperation
    if (
        "international cooperation on water" in text
        or "capacity-building in water sector" in text
        or "ความร่วมมือระหว่างประเทศด้านน้ำ" in text
        or "การเสริมสร้างศักยภาพในภาคส่วนน้ำ" in text
    ):
        matched_sdgs.add('6')

    # Layer 8: Infrastructure for Water and Sanitation
    if (
        "water supply systems" in text
        or "sanitation infrastructure" in text
        or "investment in water systems" in text
        or "ระบบจ่ายน้ำ" in text
        or "โครงสร้างพื้นฐานด้านสุขาภิบาล" in text
        or "การลงทุนในระบบน้ำ" in text
    ):
        matched_sdgs.add('6')

    # Layer 9: Climate Change and Water Disasters
    if (
        "climate resilience in water" in text
        or "flood and drought management" in text
        or "การรับมือการเปลี่ยนแปลงสภาพภูมิอากาศในด้านน้ำ" in text
        or "การจัดการน้ำท่วมและภัยแล้ง" in text
    ):
        matched_sdgs.add('6')

    # SDG 7 - Affordable and Clean Energy (Excel-based Full Reasoning)

    # Layer 1: Core Concepts - Energy Access and Clean Energy
    if (
        "affordable energy" in text
        or "clean energy" in text
        or "energy access" in text
        or "พลังงานราคาประหยัด" in text
        or "พลังงานสะอาด" in text
        or "การเข้าถึงพลังงาน" in text
    ):
        matched_sdgs.add('7')

    # Layer 2: Renewable Energy
    if (
        "renewable energy" in text
        or "solar energy" in text
        or "wind energy" in text
        or "hydropower" in text
        or "biomass energy" in text
        or "geothermal energy" in text
        or "ocean energy" in text
        or "พลังงานหมุนเวียน" in text
        or "พลังงานแสงอาทิตย์" in text
        or "พลังงานลม" in text
        or "พลังงานน้ำ" in text
        or "พลังงานชีวมวล" in text
        or "พลังงานความร้อนใต้พิภพ" in text
        or "พลังงานจากมหาสมุทร" in text
    ):
        matched_sdgs.add('7')

    # Layer 3: Energy Efficiency
    if (
        "energy efficiency" in text
        or "energy conservation" in text
        or "efficient energy use" in text
        or "ประสิทธิภาพการใช้พลังงาน" in text
        or "การอนุรักษ์พลังงาน" in text
        or "การใช้พลังงานอย่างมีประสิทธิภาพ" in text
    ):
        matched_sdgs.add('7')

    # Layer 4: Modern Energy Services
    if (
        "modern energy services" in text
        or "reliable energy" in text
        or "sustainable energy" in text
        or "บริการพลังงานสมัยใหม่" in text
        or "พลังงานที่เชื่อถือได้" in text
        or "พลังงานที่ยั่งยืน" in text
    ):
        matched_sdgs.add('7')

    # Layer 5: Energy Infrastructure and Upgrade
    if (
        "energy infrastructure" in text
        or "upgrade energy systems" in text
        or "โครงสร้างพื้นฐานด้านพลังงาน" in text
        or "การอัปเกรดระบบพลังงาน" in text
    ):
        matched_sdgs.add('7')

    # Layer 6: Investment and International Cooperation
    if (
        "investment in clean energy" in text
        or "international cooperation on energy" in text
        or "การลงทุนในพลังงานสะอาด" in text
        or "ความร่วมมือระหว่างประเทศด้านพลังงาน" in text
    ):
        matched_sdgs.add('7')

    # Layer 7: Technology and Innovation for Energy
    if (
        "energy technology innovation" in text
        or "research on clean energy" in text
        or "นวัตกรรมเทคโนโลยีพลังงาน" in text
        or "การวิจัยด้านพลังงานสะอาด" in text
    ):
        matched_sdgs.add('7')

    # Layer 8: Energy Access in Developing Countries
    if (
        "energy access in least developed countries" in text
        or "sustainable energy for all" in text
        or "การเข้าถึงพลังงานในประเทศพัฒนาน้อยที่สุด" in text
        or "พลังงานที่ยั่งยืนสำหรับทุกคน" in text
    ):
        matched_sdgs.add('7')

    # Layer 9: Capacity Building for Energy Management
    if (
        "capacity-building in energy management" in text
        or "training for sustainable energy" in text
        or "การเสริมสร้างศักยภาพในการบริหารจัดการพลังงาน" in text
        or "การฝึกอบรมด้านพลังงานอย่างยั่งยืน" in text
    ):
        matched_sdgs.add('7')

    # SDG 8 - Decent Work and Economic Growth (Excel-based Full Reasoning)

    # Layer 1: Core Concepts - Decent Work and Economic Growth
    if (
        "decent work" in text
        or "productive employment" in text
        or "economic growth" in text
        or "งานที่มีคุณค่า" in text
        or "การจ้างงานที่มีผลิตภาพ" in text
        or "การเติบโตทางเศรษฐกิจ" in text
    ):
        matched_sdgs.add('8')

    # Layer 2: Employment and Labor Rights
    if (
        "employment opportunities" in text
        or "full employment" in text
        or "labor rights" in text
        or "โอกาสการจ้างงาน" in text
        or "การจ้างงานเต็มที่" in text
        or "สิทธิแรงงาน" in text
    ):
        matched_sdgs.add('8')

    # Layer 3: Safe and Secure Work Environments
    if (
        "safe working environments" in text
        or "workplace security" in text
        or "occupational safety" in text
        or "สภาพแวดล้อมการทำงานที่ปลอดภัย" in text
        or "ความปลอดภัยในสถานที่ทำงาน" in text
        or "ความปลอดภัยในการทำงาน" in text
    ):
        matched_sdgs.add('8')

    # Layer 4: Youth Employment and Education
    if (
        "youth employment" in text
        or "education and training for youth" in text
        or "การจ้างงานเยาวชน" in text
        or "การศึกษาและการฝึกอบรมสำหรับเยาวชน" in text
    ):
        matched_sdgs.add('8')

    # Layer 5: Economic Productivity and Innovation
    if (
        "increase economic productivity" in text
        or "innovation-driven economy" in text
        or "การเพิ่มผลิตภาพทางเศรษฐกิจ" in text
        or "เศรษฐกิจที่ขับเคลื่อนด้วยนวัตกรรม" in text
    ):
        matched_sdgs.add('8')

    # Layer 6: Entrepreneurship and SMEs Support
    if (
        "support for entrepreneurship" in text
        or "small and medium-sized enterprises" in text
        or "การสนับสนุนผู้ประกอบการ" in text
        or "วิสาหกิจขนาดกลางและขนาดย่อม" in text
    ):
        matched_sdgs.add('8')

    # Layer 7: Financial Services Access
    if (
        "access to financial services" in text
        or "access to affordable credit" in text
        or "การเข้าถึงบริการทางการเงิน" in text
        or "การเข้าถึงสินเชื่อในอัตราที่เอื้อมถึงได้" in text
    ):
        matched_sdgs.add('8')

    # Layer 8: Sustainable Tourism and Job Creation
    if (
        "sustainable tourism" in text
        or "job creation through tourism" in text
        or "การท่องเที่ยวอย่างยั่งยืน" in text
        or "การสร้างงานผ่านการท่องเที่ยว" in text
    ):
        matched_sdgs.add('8')

    # Layer 9: Forced Labor and Modern Slavery Elimination
    if (
        "eradicate forced labor" in text
        or "end modern slavery" in text
        or "การขจัดแรงงานบังคับ" in text
        or "การยุติทาสยุคใหม่" in text
    ):
        matched_sdgs.add('8')

    # SDG 9 - Industry, Innovation and Infrastructure (Excel-based Full Reasoning)

    # Layer 1: Core Concepts - Industry, Innovation and Infrastructure
    if (
        "sustainable industrialization" in text
        or "infrastructure development" in text
        or "innovation" in text
        or "อุตสาหกรรมที่ยั่งยืน" in text
        or "การพัฒนาโครงสร้างพื้นฐาน" in text
        or "นวัตกรรม" in text
    ):
        matched_sdgs.add('9')

    # Layer 2: Resilient and Sustainable Infrastructure
    if (
        "resilient infrastructure" in text
        or "sustainable infrastructure" in text
        or "โครงสร้างพื้นฐานที่มีความสามารถในการฟื้นตัว" in text
        or "โครงสร้างพื้นฐานที่ยั่งยืน" in text
    ):
        matched_sdgs.add('9')

    # Layer 3: Inclusive and Sustainable Industrialization
    if (
        "inclusive industrialization" in text
        or "promote inclusive and sustainable industrialization" in text
        or "การพัฒนาอุตสาหกรรมอย่างทั่วถึงและยั่งยืน" in text
        or "การส่งเสริมอุตสาหกรรมที่ทั่วถึงและยั่งยืน" in text
    ):
        matched_sdgs.add('9')

    # Layer 4: Research, Development and Innovation
    if (
        "research and innovation" in text
        or "increase scientific research" in text
        or "การวิจัยและนวัตกรรม" in text
        or "การเพิ่มการวิจัยทางวิทยาศาสตร์" in text
    ):
        matched_sdgs.add('9')

    # Layer 5: Small-Scale Industry Development
    if (
        "support for small-scale industries" in text
        or "upgrade small industries" in text
        or "การสนับสนุนอุตสาหกรรมขนาดเล็ก" in text
        or "การยกระดับอุตสาหกรรมขนาดเล็ก" in text
    ):
        matched_sdgs.add('9')

    # Layer 6: Access to Information and Communication Technology
    if (
        "access to information and communication technology" in text
        or "internet access" in text
        or "การเข้าถึงเทคโนโลยีสารสนเทศและการสื่อสาร" in text
        or "การเข้าถึงอินเทอร์เน็ต" in text
    ):
        matched_sdgs.add('9')

    # Layer 7: Industrial Diversification
    if (
        "industrial diversification" in text
        or "technology upgrading" in text
        or "การกระจายอุตสาหกรรม" in text
        or "การยกระดับเทคโนโลยี" in text
    ):
        matched_sdgs.add('9')

    # Layer 8: Infrastructure for Economic Development
    if (
        "economic infrastructure" in text
        or "regional and transborder infrastructure" in text
        or "โครงสร้างพื้นฐานทางเศรษฐกิจ" in text
        or "โครงสร้างพื้นฐานระดับภูมิภาคและข้ามพรมแดน" in text
    ):
        matched_sdgs.add('9')

    # Layer 9: Sustainable and Resilient Industrial Systems
    if (
        "sustainable industrial systems" in text
        or "resilient industrialization" in text
        or "ระบบอุตสาหกรรมที่ยั่งยืน" in text
        or "การพัฒนาอุตสาหกรรมที่มีความสามารถในการฟื้นตัว" in text
    ):
        matched_sdgs.add('9')

  # SDG 10 - Reduced Inequalities (Excel-based Full Reasoning + Expanded)

    # Layer 1: Core Concepts - Reducing Inequality
    if (
        "reduce inequality" in text
        or "inequality" in text
        or "income inequality" in text
        or "ลดความเหลื่อมล้ำ" in text
        or "ความไม่เท่าเทียมกัน" in text
        or "ความเหลื่อมล้ำทางรายได้" in text
    ):
        matched_sdgs.add('10')

    # Layer 2: Social, Economic, Political Inclusion
    if (
        "social inclusion" in text
        or "economic inclusion" in text
        or "political inclusion" in text
        or "การรวมทางสังคม" in text
        or "การรวมทางเศรษฐกิจ" in text
        or "การมีส่วนร่วมทางการเมือง" in text
    ):
        matched_sdgs.add('10')

    # Layer 3: Equal Opportunity and Policies
    if (
        "equal opportunity" in text
        or "equity policies" in text
        or "anti-discrimination policies" in text
        or "โอกาสที่เท่าเทียมกัน" in text
        or "นโยบายเพื่อความเสมอภาค" in text
        or "นโยบายต่อต้านการเลือกปฏิบัติ" in text
    ):
        matched_sdgs.add('10')

    # Layer 4: Fiscal, Wage, and Social Protection Policies
    if (
        "fiscal policy for equality" in text
        or "progressive taxation" in text
        or "social protection systems" in text
        or "นโยบายการคลังเพื่อความเท่าเทียม" in text
        or "ภาษีก้าวหน้า" in text
        or "ระบบการคุ้มครองทางสังคม" in text
    ):
        matched_sdgs.add('10')

    # Layer 5: Migration and Mobility Governance
    if (
        "safe migration" in text
        or "orderly migration" in text
        or "migration governance" in text
        or "การอพยพที่ปลอดภัย" in text
        or "การอพยพอย่างมีระเบียบ" in text
        or "การบริหารจัดการการโยกย้ายถิ่นฐาน" in text
    ):
        matched_sdgs.add('10')

    # Layer 6: Representation and Empowerment
    if (
        "political representation" in text
        or "empower marginalized groups" in text
        or "การเป็นตัวแทนทางการเมือง" in text
        or "การเสริมพลังกลุ่มเปราะบาง" in text
    ):
        matched_sdgs.add('10')

    # Layer 7: Global Governance Reform and Financial Systems
    if (
        "reform global governance" in text
        or "inclusive global institutions" in text
        or "regulate global financial markets" in text
        or "การปฏิรูปการปกครองโลก" in text
        or "สถาบันโลกที่ครอบคลุม" in text
        or "การกำกับดูแลตลาดการเงินโลก" in text
    ):
        matched_sdgs.add('10')

    # Layer 8: Facilitate Migration Remittances
    if (
        "remittance costs" in text
        or "lower cost of remittances" in text
        or "ค่าธรรมเนียมการส่งเงินกลับประเทศ" in text
        or "การลดค่าธรรมเนียมการโอนเงิน" in text
    ):
        matched_sdgs.add('10')

    # Layer 9: Special and Differential Treatment for Developing Countries
    if (
        "special treatment for developing countries" in text
        or "differential treatment for least developed countries" in text
        or "การปฏิบัติพิเศษสำหรับประเทศกำลังพัฒนา" in text
        or "การปฏิบัติแตกต่างสำหรับประเทศพัฒนาน้อยที่สุด" in text
    ):
        matched_sdgs.add('10')

    # SDG 11 - Sustainable Cities and Communities (Expanded with Excel + Official Targets)

    # Layer 1: Core Concepts - Sustainable Cities and Communities
    if (
        "sustainable cities" in text
        or "sustainable communities" in text
        or "urban sustainability" in text
        or "เมืองที่ยั่งยืน" in text
        or "ชุมชนที่ยั่งยืน" in text
        or "ความยั่งยืนของเมือง" in text
    ):
        matched_sdgs.add('11')

    # Layer 2: Safe, Inclusive, and Resilient Cities
    if (
        "safe cities" in text
        or "inclusive cities" in text
        or "resilient cities" in text
        or "เมืองที่ปลอดภัย" in text
        or "เมืองที่ครอบคลุม" in text
        or "เมืองที่มีความสามารถในการฟื้นตัว" in text
    ):
        matched_sdgs.add('11')

    # Layer 3: Affordable and Adequate Housing
    if (
        "affordable housing" in text
        or "adequate housing" in text
        or "housing upgrade" in text
        or "ที่อยู่อาศัยที่ราคาจับต้องได้" in text
        or "ที่อยู่อาศัยที่เพียงพอ" in text
        or "การปรับปรุงที่อยู่อาศัย" in text
    ):
        matched_sdgs.add('11')

    # Layer 4: Sustainable Transport and Mobility
    if (
        "sustainable transport" in text
        or "public transport" in text
        or "accessible transportation" in text
        or "urban mobility" in text
        or "ระบบขนส่งที่ยั่งยืน" in text
        or "ระบบขนส่งสาธารณะ" in text
        or "การคมนาคมที่เข้าถึงได้" in text
        or "การเคลื่อนที่ในเมือง" in text
    ):
        matched_sdgs.add('11')

    # Layer 5: Integrated Urban Planning and Management
    if (
        "urban planning" in text
        or "urban management" in text
        or "integrated urban planning" in text
        or "การวางผังเมือง" in text
        or "การจัดการเมือง" in text
        or "การวางผังเมืองแบบบูรณาการ" in text
    ):
        matched_sdgs.add('11')

    # Layer 6: Cultural and Natural Heritage Protection
    if (
        "protect cultural heritage" in text
        or "protect natural heritage" in text
        or "preserve cultural sites" in text
        or "การอนุรักษ์มรดกทางวัฒนธรรม" in text
        or "การอนุรักษ์มรดกธรรมชาติ" in text
        or "การสงวนแหล่งมรดกทางวัฒนธรรม" in text
    ):
        matched_sdgs.add('11')

    # Layer 7: Disaster Risk Reduction and Resilience
    if (
        "disaster risk reduction" in text
        or "urban resilience" in text
        or "resilience to disasters" in text
        or "การลดความเสี่ยงจากภัยพิบัติ" in text
        or "การฟื้นตัวของเมืองจากภัยพิบัติ" in text
    ):
        matched_sdgs.add('11')

    # Layer 8: Air Quality, Waste Management, and Sustainable Buildings
    if (
        "improve air quality" in text
        or "sustainable waste management" in text
        or "sustainable building design" in text
        or "การปรับปรุงคุณภาพอากาศ" in text
        or "การจัดการขยะอย่างยั่งยืน" in text
        or "การออกแบบอาคารอย่างยั่งยืน" in text
    ):
        matched_sdgs.add('11')

    # Layer 9: Access to Green Spaces and Smart Cities
    if (
        "access to green spaces" in text
        or "public green spaces" in text
        or "smart cities" in text
        or "การเข้าถึงพื้นที่สีเขียว" in text
        or "พื้นที่สีเขียวสาธารณะ" in text
        or "เมืองอัจฉริยะ" in text
    ):
        matched_sdgs.add('11')

 # SDG 12 - Responsible Consumption and Production (Expanded)

    # Layer 1: Core Concepts - Sustainable Consumption and Production
    if (
        "sustainable consumption" in text
        or "sustainable production" in text
        or "responsible consumption" in text
        or "responsible production" in text
        or "การบริโภคอย่างยั่งยืน" in text
        or "การผลิตอย่างยั่งยืน" in text
        or "การบริโภคอย่างมีความรับผิดชอบ" in text
        or "การผลิตอย่างมีความรับผิดชอบ" in text
    ):
        matched_sdgs.add('12')

    # Layer 2: Resource Efficiency and Circular Economy
    if (
        "efficient resource use" in text
        or "resource efficiency" in text
        or "circular economy" in text
        or "การใช้ทรัพยากรอย่างมีประสิทธิภาพ" in text
        or "เศรษฐกิจหมุนเวียน" in text
    ):
        matched_sdgs.add('12')

    # Layer 3: Waste Reduction, Recycling and Management
    if (
        "waste reduction" in text
        or "waste management" in text
        or "recycling" in text
        or "การลดขยะ" in text
        or "การจัดการขยะ" in text
        or "การรีไซเคิล" in text
    ):
        matched_sdgs.add('12')

    # Layer 4: Chemicals and Hazardous Waste Management
    if (
        "chemical waste management" in text
        or "hazardous waste" in text
        or "safe management of chemicals" in text
        or "การจัดการขยะเคมี" in text
        or "ขยะอันตราย" in text
        or "การจัดการสารเคมีอย่างปลอดภัย" in text
    ):
        matched_sdgs.add('12')

    # Layer 5: Sustainable Business, Industry and Supply Chains
    if (
        "sustainable business practices" in text
        or "sustainable industrial practices" in text
        or "sustainable supply chain" in text
        or "แนวปฏิบัติทางธุรกิจที่ยั่งยืน" in text
        or "แนวปฏิบัติทางอุตสาหกรรมที่ยั่งยืน" in text
        or "ห่วงโซ่อุปทานอย่างยั่งยืน" in text
    ):
        matched_sdgs.add('12')

    # Layer 6: Public Awareness, Education and Eco-Labeling
    if (
        "awareness for sustainable lifestyles" in text
        or "education for responsible consumption" in text
        or "eco-labeling" in text
        or "การสร้างความตระหนักรู้เกี่ยวกับการดำรงชีวิตอย่างยั่งยืน" in text
        or "การศึกษาเกี่ยวกับการบริโภคอย่างมีความรับผิดชอบ" in text
        or "การติดฉลากสิ่งแวดล้อม" in text
    ):
        matched_sdgs.add('12')

    # Layer 7: Green Public Procurement and Sustainable Practices
    if (
        "green public procurement" in text
        or "sustainable procurement" in text
        or "การจัดซื้อจัดจ้างสีเขียว" in text
        or "การจัดซื้อจัดจ้างอย่างยั่งยืน" in text
    ):
        matched_sdgs.add('12')

    # Layer 8: Sustainable Tourism and Consumer Engagement
    if (
        "sustainable tourism" in text
        or "responsible tourism" in text
        or "consumer engagement" in text
        or "การท่องเที่ยวอย่างยั่งยืน" in text
        or "การท่องเที่ยวอย่างมีความรับผิดชอบ" in text
        or "การมีส่วนร่วมของผู้บริโภค" in text
    ):
        matched_sdgs.add('12')

    # Layer 9: Monitoring, Reporting and Innovation
    if (
        "monitor sustainable practices" in text
        or "report on sustainable production" in text
        or "innovation for sustainable consumption" in text
        or "การติดตามแนวปฏิบัติที่ยั่งยืน" in text
        or "การรายงานการผลิตที่ยั่งยืน" in text
        or "นวัตกรรมเพื่อการบริโภคอย่างยั่งยืน" in text
    ):
        matched_sdgs.add('12')

    # SDG 13 - Climate Action (Expanded)

    # Layer 1: Core Concepts - Climate Action
    if (
        "climate action" in text
        or "combat climate change" in text
        or "address climate crisis" in text
        or "การดำเนินการด้านสภาพภูมิอากาศ" in text
        or "การรับมือการเปลี่ยนแปลงสภาพภูมิอากาศ" in text
        or "แก้ไขวิกฤตสภาพภูมิอากาศ" in text
    ):
        matched_sdgs.add('13')

    # Layer 2: Greenhouse Gas Emission Reduction and Carbon Neutrality
    if (
        "reduce greenhouse gas emissions" in text
        or "lower carbon emissions" in text
        or "achieve carbon neutrality" in text
        or "ลดการปล่อยก๊าซเรือนกระจก" in text
        or "ลดการปล่อยคาร์บอน" in text
        or "บรรลุความเป็นกลางทางคาร์บอน" in text
    ):
        matched_sdgs.add('13')

    # Layer 3: Climate Resilience and Adaptation
    if (
        "climate resilience" in text
        or "adaptation to climate change" in text
        or "nature-based solutions" in text
        or "การฟื้นตัวจากการเปลี่ยนแปลงสภาพภูมิอากาศ" in text
        or "การปรับตัวต่อการเปลี่ยนแปลงสภาพภูมิอากาศ" in text
        or "แนวทางที่ใช้ธรรมชาติเป็นพื้นฐาน" in text
    ):
        matched_sdgs.add('13')

    # Layer 4: Disaster Risk Reduction and Adaptation Planning
    if (
        "disaster risk reduction" in text
        or "build resilience to climate-related disasters" in text
        or "adaptation planning for disasters" in text
        or "การลดความเสี่ยงจากภัยพิบัติ" in text
        or "การสร้างความสามารถในการรับมือภัยพิบัติที่เกี่ยวข้องกับสภาพภูมิอากาศ" in text
        or "การวางแผนปรับตัวต่อภัยพิบัติ" in text
    ):
        matched_sdgs.add('13')

    # Layer 5: Climate Policy, Governance and Legislation
    if (
        "climate policies" in text
        or "national climate action plans" in text
        or "climate change legislation" in text
        or "นโยบายด้านสภาพภูมิอากาศ" in text
        or "แผนปฏิบัติการด้านสภาพภูมิอากาศระดับชาติ" in text
        or "กฎหมายว่าด้วยการเปลี่ยนแปลงสภาพภูมิอากาศ" in text
    ):
        matched_sdgs.add('13')

    # Layer 6: Climate Education, Awareness and Capacity-Building
    if (
        "education on climate change" in text
        or "raising awareness on climate change" in text
        or "capacity-building for climate action" in text
        or "การศึกษาเรื่องการเปลี่ยนแปลงสภาพภูมิอากาศ" in text
        or "การสร้างความตระหนักรู้เรื่องการเปลี่ยนแปลงสภาพภูมิอากาศ" in text
        or "การเสริมสร้างขีดความสามารถในการดำเนินการด้านสภาพภูมิอากาศ" in text
    ):
        matched_sdgs.add('13')

    # Layer 7: International Cooperation on Climate Action
    if (
        "international cooperation on climate" in text
        or "global partnerships for climate action" in text
        or "climate agreements" in text
        or "ความร่วมมือระหว่างประเทศด้านสภาพภูมิอากาศ" in text
        or "หุ้นส่วนระดับโลกเพื่อการดำเนินการด้านสภาพภูมิอากาศ" in text
        or "ข้อตกลงด้านสภาพภูมิอากาศ" in text
    ):
        matched_sdgs.add('13')

    # Layer 8: Early Warning Systems and Climate Information
    if (
        "climate early warning systems" in text
        or "disaster early warning systems" in text
        or "climate information services" in text
        or "ระบบเตือนภัยล่วงหน้าด้านสภาพภูมิอากาศ" in text
        or "ระบบเตือนภัยล่วงหน้าจากภัยพิบัติ" in text
        or "บริการข้อมูลสภาพภูมิอากาศ" in text
    ):
        matched_sdgs.add('13')

    # Layer 9: Climate Finance and Investment
    if (
        "climate finance" in text
        or "funding for climate initiatives" in text
        or "investment in climate resilience" in text
        or "การเงินด้านสภาพภูมิอากาศ" in text
        or "การสนับสนุนทางการเงินสำหรับโครงการด้านสภาพภูมิอากาศ" in text
        or "การลงทุนในความสามารถในการฟื้นตัวจากการเปลี่ยนแปลงสภาพภูมิอากาศ" in text
    ):
        matched_sdgs.add('13')

    # SDG 14 - Life Below Water (Expanded)

    # Layer 1: Core Concepts - Conservation of Oceans and Marine Ecosystems
    if (
        "conserve oceans" in text
        or "protect marine ecosystems" in text
        or "safeguard marine biodiversity" in text
        or "การอนุรักษ์มหาสมุทร" in text
        or "การปกป้องระบบนิเวศทางทะเล" in text
        or "การคุ้มครองความหลากหลายทางทะเล" in text
    ):
        matched_sdgs.add('14')

    # Layer 2: Marine Pollution Control
    if (
        "reduce marine pollution" in text
        or "marine litter" in text
        or "plastic pollution in oceans" in text
        or "ลดมลพิษทางทะเล" in text
        or "ขยะทะเล" in text
        or "มลพิษพลาสติกในมหาสมุทร" in text
    ):
        matched_sdgs.add('14')

    # Layer 3: Sustainable Marine Resources Management
    if (
        "sustainable marine management" in text
        or "sustainable ocean management" in text
        or "blue economy" in text
        or "การบริหารจัดการทะเลอย่างยั่งยืน" in text
        or "การบริหารจัดการมหาสมุทรอย่างยั่งยืน" in text
        or "เศรษฐกิจสีน้ำเงิน" in text
    ):
        matched_sdgs.add('14')

    # Layer 4: Ocean Acidification and Climate Change Mitigation
    if (
        "ocean acidification" in text
        or "reduce ocean acidification" in text
        or "climate change impact on oceans" in text
        or "ภาวะกรดในมหาสมุทร" in text
        or "ลดภาวะกรดในมหาสมุทร" in text
        or "ผลกระทบของการเปลี่ยนแปลงสภาพภูมิอากาศต่อมหาสมุทร" in text
    ):
        matched_sdgs.add('14')

    # Layer 5: Sustainable Fisheries and Aquaculture
    if (
        "sustainable fisheries" in text
        or "end overfishing" in text
        or "sustainable aquaculture" in text
        or "การประมงอย่างยั่งยืน" in text
        or "การยุติการจับปลามากเกินไป" in text
        or "การเพาะเลี้ยงสัตว์น้ำอย่างยั่งยืน" in text
    ):
        matched_sdgs.add('14')

    # Layer 6: Marine Protected Areas and Coastal Ecosystems
    if (
        "marine protected areas" in text
        or "expand marine reserves" in text
        or "protect coastal ecosystems" in text
        or "พื้นที่คุ้มครองทางทะเล" in text
        or "การขยายเขตอนุรักษ์ทางทะเล" in text
        or "การปกป้องระบบนิเวศชายฝั่ง" in text
    ):
        matched_sdgs.add('14')

    # Layer 7: Support for Small-Scale Fisheries
    if (
        "support small-scale fisheries" in text
        or "small fisheries livelihood" in text
        or "economic support for artisanal fisheries" in text
        or "การสนับสนุนการประมงขนาดเล็ก" in text
        or "การดำรงชีวิตของชาวประมงขนาดเล็ก" in text
        or "การสนับสนุนทางเศรษฐกิจแก่การประมงพื้นบ้าน" in text
    ):
        matched_sdgs.add('14')

    # Layer 8: Scientific Research, Innovation and Technology for Ocean Health
    if (
        "marine scientific research" in text
        or "technology transfer for ocean health" in text
        or "innovation for marine conservation" in text
        or "การวิจัยทางวิทยาศาสตร์ทางทะเล" in text
        or "การถ่ายทอดเทคโนโลยีเพื่อสุขภาพมหาสมุทร" in text
        or "นวัตกรรมเพื่อการอนุรักษ์ทางทะเล" in text
    ):
        matched_sdgs.add('14')

    # Layer 9: International Law and Ocean Governance (UNCLOS)
    if (
        "implement international law for oceans" in text
        or "UNCLOS" in text
        or "global ocean governance" in text
        or "การบังคับใช้กฎหมายระหว่างประเทศด้านมหาสมุทร" in text
        or "อนุสัญญาสหประชาชาติว่าด้วยกฎหมายทะเล (UNCLOS)" in text
        or "การบริหารจัดการมหาสมุทรในระดับโลก" in text
    ):
        matched_sdgs.add('14')

    # SDG 15 - Life on Land (Expanded)

    # Layer 1: Core Concepts - Protect, Restore and Promote Sustainable Use of Terrestrial Ecosystems
    if (
        "protect terrestrial ecosystems" in text
        or "restore degraded land" in text
        or "sustainable use of terrestrial ecosystems" in text
        or "ส่งเสริมการใช้ระบบนิเวศบนบกอย่างยั่งยืน" in text
        or "ฟื้นฟูพื้นที่เสื่อมโทรม" in text
        or "การอนุรักษ์ระบบนิเวศบนบก" in text
    ):
        matched_sdgs.add('15')

    # Layer 2: Forest Management and Restoration
    if (
        "sustainable forest management" in text
        or "halt deforestation" in text
        or "restore forests" in text
        or "การจัดการป่าไม้อย่างยั่งยืน" in text
        or "ยุติการตัดไม้ทำลายป่า" in text
        or "การฟื้นฟูป่าไม้" in text
    ):
        matched_sdgs.add('15')

    # Layer 3: Combat Desertification and Land Degradation
    if (
        "combat desertification" in text
        or "land degradation neutrality" in text
        or "halt land degradation" in text
        or "ต่อสู้กับการแปรสภาพเป็นทะเลทราย" in text
        or "ความเป็นกลางด้านการเสื่อมโทรมของที่ดิน" in text
        or "ยุติการเสื่อมโทรมของที่ดิน" in text
    ):
        matched_sdgs.add('15')

    # Layer 4: Biodiversity Conservation
    if (
        "conserve biodiversity" in text
        or "halt biodiversity loss" in text
        or "protect endangered species" in text
        or "การอนุรักษ์ความหลากหลายทางชีวภาพ" in text
        or "ยุติการสูญเสียความหลากหลายทางชีวภาพ" in text
        or "การปกป้องสัตว์ใกล้สูญพันธุ์" in text
    ):
        matched_sdgs.add('15')

    # Layer 5: Protect Natural Habitats
    if (
        "protect natural habitats" in text
        or "manage protected areas" in text
        or "restore ecosystems" in text
        or "การปกป้องถิ่นที่อยู่อาศัยตามธรรมชาติ" in text
        or "การจัดการพื้นที่คุ้มครอง" in text
        or "การฟื้นฟูระบบนิเวศ" in text
    ):
        matched_sdgs.add('15')

    # Layer 6: End Poaching and Wildlife Trafficking
    if (
        "end poaching" in text
        or "illegal wildlife trade" in text
        or "combat wildlife trafficking" in text
        or "ยุติการล่าสัตว์ผิดกฎหมาย" in text
        or "การค้าสัตว์ป่าอย่างผิดกฎหมาย" in text
        or "การปราบปรามการลักลอบค้าสัตว์ป่า" in text
    ):
        matched_sdgs.add('15')

    # Layer 7: Control Invasive Alien Species
    if (
        "control invasive alien species" in text
        or "prevent invasive species" in text
        or "การควบคุมชนิดพันธุ์ต่างถิ่นรุกราน" in text
        or "การป้องกันการรุกรานของชนิดพันธุ์ต่างถิ่น" in text
    ):
        matched_sdgs.add('15')

    # Layer 8: Integrate Biodiversity Values into Development
    if (
        "integrate biodiversity into planning" in text
        or "ecosystem values in development" in text
        or "mainstream biodiversity in development" in text
        or "บูรณาการความหลากหลายทางชีวภาพในการวางแผน" in text
        or "ค่านิยมระบบนิเวศในการพัฒนา" in text
        or "การบูรณาการความหลากหลายทางชีวภาพในการพัฒนา" in text
    ):
        matched_sdgs.add('15')

    # Layer 9: Mobilize Financial Resources for Conservation
    if (
        "mobilize financial resources for conservation" in text
        or "increase biodiversity funding" in text
        or "fund ecosystem protection" in text
        or "ระดมทรัพยากรทางการเงินเพื่อการอนุรักษ์" in text
        or "เพิ่มเงินทุนเพื่อความหลากหลายทางชีวภาพ" in text
        or "เงินทุนสำหรับการปกป้องระบบนิเวศ" in text
    ):
        matched_sdgs.add('15')

 # SDG 16 - Peace, Justice and Strong Institutions (Expanded)

    # Layer 1: Core Concepts - Peace, Justice, and Strong Institutions
    if (
        "peace and justice" in text
        or "strong institutions" in text
        or "การสร้างสันติภาพและความยุติธรรม" in text
        or "สถาบันที่เข้มแข็ง" in text
    ):
        matched_sdgs.add('16')

    # Layer 2: Access to Justice and Legal Aid
    if (
        "access to justice" in text
        or "legal aid" in text
        or "การเข้าถึงความยุติธรรม" in text
        or "การช่วยเหลือทางกฎหมาย" in text
    ):
        matched_sdgs.add('16')

    # Layer 3: Combating Corruption and Bribery
    if (
        "anti-corruption" in text
        or "combat bribery" in text
        or "การต่อต้านการทุจริต" in text
        or "การปราบปรามการติดสินบน" in text
    ):
        matched_sdgs.add('16')

    # Layer 4: Inclusive, Accountable, and Transparent Institutions
    if (
        "inclusive institutions" in text
        or "accountable institutions" in text
        or "transparent governance" in text
        or "สถาบันที่ครอบคลุมทุกคน" in text
        or "สถาบันที่มีความรับผิดชอบ" in text
        or "การบริหารจัดการที่โปร่งใส" in text
    ):
        matched_sdgs.add('16')

    # Layer 5: Participation in Decision-Making and Governance
    if (
        "participation in decision-making" in text
        or "public participation" in text
        or "การมีส่วนร่วมในการตัดสินใจ" in text
        or "การมีส่วนร่วมของประชาชน" in text
    ):
        matched_sdgs.add('16')

    # Layer 6: Human Rights Protection
    if (
        "human rights" in text
        or "human rights protection" in text
        or "สิทธิมนุษยชน" in text
        or "การคุ้มครองสิทธิมนุษยชน" in text
    ):
        matched_sdgs.add('16')

    # Layer 7: Strengthening the Rule of Law
    if (
        "rule of law" in text
        or "strengthen rule of law" in text
        or "การเสริมสร้างหลักนิติธรรม" in text
        or "การเสริมสร้างการปกครองโดยกฎหมาย" in text
    ):
        matched_sdgs.add('16')

    # Layer 8: Non-Violent Conflict Resolution
    if (
        "non-violent conflict resolution" in text
        or "mediation and negotiation" in text
        or "การแก้ปัญหาขัดแย้งโดยสันติ" in text
        or "การไกล่เกลี่ยและการเจรจาต่อรอง" in text
    ):
        matched_sdgs.add('16')

    # Layer 9: Accountability, Transparency, and Effective Institutions
    if (
        "institutional accountability" in text
        or "effective public institutions" in text
        or "ตรวจสอบได้และโปร่งใส" in text
        or "สถาบันที่มีประสิทธิภาพและโปร่งใส" in text
    ):
        matched_sdgs.add('16')

 # SDG 17 - Partnerships for the Goals (Expanded)

    # Layer 1: Core Concepts - Global Partnerships and Cooperation
    if (
        "global partnerships" in text
        or "partnerships for the goals" in text
        or "การสร้างหุ้นส่วนระดับโลก" in text
        or "ความร่วมมือสำหรับเป้าหมาย" in text
    ):
        matched_sdgs.add('17')

    # Layer 2: Finance Mobilization and ODA
    if (
        "official development assistance" in text
        or "oda" in text
        or "mobilize financial resources" in text
        or "การช่วยเหลือเพื่อการพัฒนาอย่างเป็นทางการ" in text
        or "การระดมทรัพยากรทางการเงิน" in text
    ):
        matched_sdgs.add('17')

    # Layer 3: Technology, Science and Innovation
    if (
        "technology transfer" in text
        or "science and innovation" in text
        or "technology cooperation" in text
        or "การถ่ายทอดเทคโนโลยี" in text
        or "วิทยาศาสตร์และนวัตกรรม" in text
        or "ความร่วมมือทางเทคโนโลยี" in text
    ):
        matched_sdgs.add('17')

    # Layer 4: Capacity Building and Institutional Strengthening
    if (
        "capacity building" in text
        or "technical assistance" in text
        or "institutional capacity" in text
        or "การเสริมสร้างศักยภาพ" in text
        or "การให้ความช่วยเหลือทางเทคนิค" in text
        or "ศักยภาพสถาบัน" in text
    ):
        matched_sdgs.add('17')

    # Layer 5: Trade and Market Access
    if (
        "promote trade" in text
        or "market access" in text
        or "trade cooperation" in text
        or "ส่งเสริมการค้า" in text
        or "การเข้าถึงตลาด" in text
        or "ความร่วมมือทางการค้า" in text
    ):
        matched_sdgs.add('17')

    # Layer 6: Data, Monitoring and Accountability
    if (
        "data availability" in text
        or "monitoring and reporting" in text
        or "accountability mechanisms" in text
        or "การเข้าถึงข้อมูล" in text
        or "การติดตามและรายงาน" in text
        or "กลไกความรับผิดชอบ" in text
    ):
        matched_sdgs.add('17')

    # Layer 7: Policy and Institutional Coherence
    if (
        "policy coherence" in text
        or "institutional coherence" in text
        or "integrated policies" in text
        or "ความสอดคล้องของนโยบาย" in text
        or "ความสอดคล้องของสถาบัน" in text
        or "นโยบายแบบบูรณาการ" in text
    ):
        matched_sdgs.add('17')

    # Layer 8: Multi-Stakeholder Partnerships
    if (
        "civil society partnerships" in text
        or "private sector engagement" in text
        or "multi-stakeholder" in text
        or "ความร่วมมือกับภาคประชาสังคม" in text
        or "การมีส่วนร่วมของภาคเอกชน" in text
        or "หุ้นส่วนที่หลากหลาย" in text
    ):
        matched_sdgs.add('17')

    # Layer 9: Resource Efficiency and Sustainable Financing
    if (
        "sustainable financing" in text
        or "resource efficiency" in text
        or "green finance" in text
        or "การจัดหาเงินทุนอย่างยั่งยืน" in text
        or "ประสิทธิภาพในการใช้ทรัพยากร" in text
        or "การเงินสีเขียว" in text
    ):
        matched_sdgs.add('17')

    # === Post-Processing Layer (เสริมความแม่นยำ) ===
    if any(word in text for word in ["earthquake", "disaster", "flood", "emergency response", "ภัยพิบัติ", "แผ่นดินไหว", "อุทกภัย", "น้ำท่วม"]):
        matched_sdgs.add('11')

    if any(word in text for word in ["climate", "global warming", "greenhouse gas", "climate change", "ภาวะโลกร้อน", "การเปลี่ยนแปลงสภาพภูมิอากาศ"]):
        matched_sdgs.add('13')

    if any(word in text for word in ["infrastructure", "resilient infrastructure", "resilient buildings", "โครงสร้างพื้นฐาน", "อาคารปลอดภัย"]):
        matched_sdgs.add('9')

    if any(word in text for word in ["ocean", "marine life", "ทะเล", "ทรัพยากรทางทะเล", "สัตว์ทะเล"]):
        matched_sdgs.add('14')

    if any(word in text for word in ["forest", "biodiversity", "wildlife", "ป่าไม้", "ความหลากหลายทางชีวภาพ"]):
        matched_sdgs.add('15')

    if any(word in text for word in ["clean water", "safe drinking water", "sanitation", "น้ำสะอาด", "สุขาภิบาล"]):
        matched_sdgs.add('6')

    if any(word in text for word in ["gender equality", "women empowerment", "ความเสมอภาคทางเพศ", "สิทธิสตรี"]):
        matched_sdgs.add('5')

    if any(word in text for word in ["recycling", "waste management", "circular economy", "เศรษฐกิจหมุนเวียน", "การรีไซเคิล", "การจัดการของเสีย"]):
        matched_sdgs.add('12')

    if any(word in text for word in ["peace", "justice", "human rights", "strong institutions", "สันติภาพ", "ความยุติธรรม", "สิทธิมนุษยชน"]):
        matched_sdgs.add('16')

    if any(word in text for word in ["global partnership", "international cooperation", "partnerships", "ความร่วมมือระหว่างประเทศ", "ความร่วมมือเพื่อการพัฒนา"]):
        matched_sdgs.add('17')

    if '4' in matched_sdgs and not any(word in text for word in ["education", "training", "school", "learning", "literacy", "การศึกษา", "การฝึกอบรม", "การเรียนรู้", "การรู้หนังสือ"]):
        matched_sdgs.discard('4')

    return sorted(list(matched_sdgs))
