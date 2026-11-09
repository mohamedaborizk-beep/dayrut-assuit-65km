import sys, os, json, base64, openpyxl, re
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
prog_path = os.path.join(base_dir, "progress.xlsx")

# 1. Base64 Logo
logo_path = os.path.join(base_dir, "لوجو الشركة.png")
logo_base64 = ""
if os.path.exists(logo_path):
    with open(logo_path, "rb") as f:
        logo_base64 = base64.b64encode(f.read()).decode("utf-8")

# 2. Open progress.xlsx
wb = openpyxl.load_workbook(prog_path, data_only=True)

# A. Project Info & Timeline
project_info = {
    'title': 'أعمال تطوير ورفع كفاءة طريق الصعيد الصحراوي الغربي في المسافة من ديروط حتى أسيوط بطول 65 كم (الأمر المباشر)',
    'subtitle': 'مشروع تطوير طريق الصعيد الصحراوي الغربي - محور ديروط / أسيوط',
    'contract_no': '2023/2022/426 بتاريخ 27/09/2022',
    'owner': 'وزارة النقل - الهيئة العامة للطرق والكباري',
    'supervising_zone': 'المنطقة السابعة بأسيوط',
    'contractor': 'شركة إيماك للمقاولات "إحدى شركات مجموعة الخرافي"',
    'consultant_owner': 'مكتب انترانس للاستشارات الهندسية',
    'consultant_contractor': 'مكتب الرائد للاستشارات الهندسية',
    'admin_email': 'MOHAMEDABORIZK@GMAIL.COM',
    'award_date_1': '2021-09-20',
    'award_date_2': '2021-09-28',
    'site_receipt_date': '2022-07-20',
    'contract_sign_date': '2022-09-27',
    'original_duration_months': 12,
    'original_finish_date': '2023-07-19',
    'approved_extension_months': 34,
    'extended_finish_date': '2026-05-19',
    'total_project_duration_months': 46,
    'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'logo_base64': logo_base64
}

# Extensions
extensions = []
if 'التمديدات الزمنية' in wb.sheetnames:
    ws_ext = wb['التمديدات الزمنية']
    for r in range(4, 13):
        ext_no = ws_ext.cell(r, 1).value
        months = ws_ext.cell(r, 3).value
        status = ws_ext.cell(r, 4).value
        reasons = ws_ext.cell(r, 5).value
        ref_letters = ws_ext.cell(r, 6).value
        notes = ws_ext.cell(r, 7).value
        if ext_no is not None:
            extensions.append({
                'no': str(ext_no).strip(),
                'months': float(months or 0),
                'status': str(status or '').strip(),
                'reasons': str(reasons or '').strip(),
                'ref_letters': str(ref_letters or '').strip(),
                'notes': str(notes or '').strip()
            })

# B. Engineering Components
engineering_components = [
    {
        'category': 'طرق الخدمة (إنشاء جديد)',
        'type': 'رصف خرساني - 3 حارات (عرض الرصف 12 متر)',
        'inside_contract': 'طول 65 كم (من كم 282 حتى كم 347) بعدد طريقي خدمة (طريق بكل اتجاه)',
        'outside_contract': 'طول 7 كم (من كم 347 حتى كم 354) بعدد طريقي خدمة (طريق بكل اتجاه)',
        'total_length': '72 كم لكل اتجاه (إجمالي 144 كم طولي فرعي)',
        'notes': 'إنشاء جديد بالكامل لخدمة النقل الثقيل والمحلي'
    },
    {
        'category': 'الطرق الرئيسية (رفع كفاءة)',
        'type': 'رصف أسفلتي - 3 حارات رفع كفاءة الطرق القائمة',
        'inside_contract': 'طول 65 كم (من كم 282 حتى كم 347) بعدد طريقي رئيسي (طريق بكل اتجاه)',
        'outside_contract': 'طول 7 كم (من كم 347 حتى كم 354) بعدد طريقي رئيسي (طريق بكل اتجاه)',
        'total_length': '72 كم لكل اتجاه (إجمالي 144 كم طولي فرعي)',
        'notes': 'كشط وإعادة تدوير FDR وطبقات رابطة وسطحية'
    },
    {
        'category': 'طرق التقاطعات الحرة والرامبات',
        'type': 'إنشاء جديد (طرق ربط ودوران سطحي ورامبات صعود/نزول)',
        'inside_contract': '3 تقاطعات رئيسية (نفق القوصية كم 290، دوران للخلف كم 310، منفلوط تنيدة كم 329) + 10 رامبات صعود/نزول Slip Ramps',
        'outside_contract': 'تقاطعان رئيسيان (نفق الخارجة كم 347.9، نفق المطار كم 352) + 5 رامبات صعود/نزول Slip Ramps',
        'total_length': '5 تقاطعات رئيسية حرة + 15 رامب Slip Ramps',
        'notes': 'تأمين الحركة المرورية الحرة وفصل التقاطعات السطحية'
    },
    {
        'category': 'الأنفاق السطحية للتقاطعات',
        'type': 'أعمال صناعية - كباري وأنفاق خرسانية مسلحة',
        'inside_contract': '3 أنفاق (نفق القوصية كم 290، دوران للخلف كم 310، منفلوط تنيدة كم 329)',
        'outside_contract': 'نفقان (نفق الخارجة كم 347.9، نفق المطار كم 352)',
        'total_length': 'إجمالي 5 أنفاق سطحية بالمسار',
        'notes': 'تم تنفيذ وتسليم الـ 3 أنفاق داخل مسار العقد بالكامل'
    },
    {
        'category': 'برابخ تصريف مياه الأمطار والسيول',
        'type': 'مواسير خرسانية مسلحة قطر داخلي 1 متر مع أعمال حماية خرسانية عادية',
        'inside_contract': '9 مواقع برابخ (كم 5، 11، 13، 15، 20، 30، 33.9، 40، 43)',
        'outside_contract': 'موقع واحد بربخ بالكم 65.250',
        'total_length': 'إجمالي 10 مواقع برابخ مسار الطريق',
        'notes': 'تم تسليم 8 برابخ حتى جزئي 04'
    }
]

# C. Executive & Financial Status (from 'بيانات المشروع' Rows 29..44)
ws_info = wb['بيانات المشروع']
financial_status = {
    'award_value': float(ws_info.cell(29, 3).value or 2898000000.0),
    'boq_value': float(ws_info.cell(30, 3).value or 2359723935.81),
    'app_contract': float(ws_info.cell(31, 3).value or 2086050607.03),
    'app_pv': float(ws_info.cell(32, 3).value or 641018581.12),
    'app_gross_comp': float(ws_info.cell(33, 3).value or 696174051.24),
    'app_net_comp': float(ws_info.cell(34, 3).value or 242063288.91),
    'app_total': float(ws_info.cell(35, 3).value or 2969132477.06),
    'billed_contract': float(ws_info.cell(36, 3).value or 1967696022.27),
    'billed_pv': float(ws_info.cell(37, 3).value or 498474410.80),
    'billed_gross_comp': float(ws_info.cell(38, 3).value or 419383914.81),
    'billed_net_comp': float(ws_info.cell(39, 3).value or 227173977.10),
    'billed_total': float(ws_info.cell(40, 3).value or 2693344410.17),
    'rem_contract': float(ws_info.cell(41, 3).value or 118354584.76),
    'rem_pv': float(ws_info.cell(42, 3).value or 142544170.32),
    'rem_net_comp': float(ws_info.cell(43, 3).value or 14889311.81),
    'rem_total': float(ws_info.cell(44, 3).value or 275788066.89),
}

# D. Handover Distances & Financials (from 'بيانات المشروع' Rows 47..66 & 'التسليمات الجزئية والمحتجزات')
ws_ho = wb['التسليمات الجزئية والمحتجزات']

handover_distances = []
for r in range(2, 6):
    name = ws_ho.cell(r, 2).value
    pave_type = ws_ho.cell(r, 3).value
    scope_km = float(ws_ho.cell(r, 4).value or 0)
    fin_km = float(ws_ho.cell(r, 5).value or 0)
    ini_km = float(ws_ho.cell(r, 6).value or 0)
    tot_km = float(ws_ho.cell(r, 7).value or 0)
    rem_km = float(ws_ho.cell(r, 8).value or 0)
    pct = float(ws_ho.cell(r, 9).value or 0)
    details = ws_ho.cell(r, 10).value
    handover_distances.append({
        'name': str(name),
        'pave_type': str(pave_type),
        'scope_km': scope_km,
        'final_km': fin_km,
        'initial_km': ini_km,
        'total_km': tot_km,
        'remaining_km': rem_km,
        'percentage': pct,
        'details': str(details)
    })

structures_handover = {
    'tunnels': {
        'total': 3,
        'handed_over': 3,
        'pct': 1.0,
        'details': 'نفق القوصية (كم 290) + نفق الدوران للخلف (كم 310) + نفق منفلوط تنيدة (كم 329) - 100%'
    },
    'culverts': {
        'total': 9,
        'handed_over': 8,
        'pct': 8.0 / 9.0,
        'details': 'برابخ الكم: (5، 11، 13، 15، 20، 30، 40، 43) - 8 مواقع من أصل 9'
    }
}

handover_financials = {
    'final_contract': float(ws_ho.cell(14, 5).value or 1236682126.49),
    'final_pv': float(ws_ho.cell(14, 6).value or 147706564.19),
    'final_total': float(ws_ho.cell(14, 7).value or 1384388690.68),
    'initial_contract': float(ws_ho.cell(15, 5).value or 531194210.05),
    'initial_pv': float(ws_ho.cell(15, 6).value or 323924398.94),
    'initial_total': float(ws_ho.cell(15, 7).value or 855118608.99),
    'grand_contract': float(ws_ho.cell(16, 5).value or 1767876336.54),
    'grand_pv': float(ws_ho.cell(16, 6).value or 471630963.13),
    'grand_total': float(ws_ho.cell(16, 7).value or 2239507299.67),
}

retentions = {
    'works_retention': {
        'deducted': float(ws_ho.cell(19, 5).value or 98384801.11),
        'due_release': float(ws_ho.cell(20, 5).value or 88393816.83),
        'remaining': float(ws_ho.cell(21, 5).value or 9990984.29),
        'due_release_pct': float(ws_ho.cell(20, 6).value or 0.8984),
        'remaining_pct': float(ws_ho.cell(21, 6).value or 0.1016),
        'note': 'يُرد محتجز الـ 5% بموجب التسليم الابتدائي (5% × الأعمال المسلمة ابتدائياً 1,767.88 مليون ج.م)'
    },
    'bank_guarantee': {
        'original': float(ws_ho.cell(23, 5).value or 144900000.0),
        'boq_equivalent': float(ws_ho.cell(24, 5).value or 117986196.79),
        'scope_reduction': float(ws_ho.cell(25, 5).value or 26913803.21),
        'final_ho_reduction': float(ws_ho.cell(26, 5).value or 61834106.32),
        'total_reduction': float(ws_ho.cell(27, 5).value or 88747909.53),
        'total_reduction_pct': float(ws_ho.cell(27, 6).value or 0.6125),
        'remaining_active': float(ws_ho.cell(28, 5).value or 56152090.47),
        'remaining_active_pct': float(ws_ho.cell(28, 6).value or 0.3875),
        'note': 'يُخفض خطاب الضمان بمقدار 5% من فرق الحصر الفعلي + 5% من الأعمال المسلمة تسليماً نهائياً'
    }
}

# Individual Handovers List
handovers_list = []
for r in range(11, 16):
    if r == 14: continue # Subtotal row
    ho_id = ws_ho.cell(r, 1).value
    ho_title = ws_ho.cell(r, 2).value
    ho_status = ws_ho.cell(r, 3).value
    ho_dates = ws_ho.cell(r, 4).value
    c_val = float(ws_ho.cell(r, 5).value or 0)
    pv_val = float(ws_ho.cell(r, 6).value or 0)
    tot_val = float(ws_ho.cell(r, 7).value or 0)
    notes = ws_ho.cell(r, 10).value
    handovers_list.append({
        'id': str(ho_id),
        'title': str(ho_title),
        'status': str(ho_status),
        'dates': str(ho_dates),
        'contract_val': c_val,
        'pv_val': pv_val,
        'total_val': tot_val,
        'notes': str(notes)
    })

# E. 9 Main Work Categories from 'مقايسة الأعمال معاد القياس'
main_categories = []
ws_boq = wb['مقايسة الأعمال معاد القياس']
for r in range(3, 12):
    cat_name = ws_boq.cell(r, 2).value
    items_count = int(ws_boq.cell(r, 3).value or 0)
    boq_val = float(ws_boq.cell(r, 4).value or 0)
    weight_pct = float(ws_boq.cell(r, 5).value or 0)
    app_val = float(ws_boq.cell(r, 6).value or 0)
    bil_val = float(ws_boq.cell(r, 7).value or 0)
    rem_val = float(ws_boq.cell(r, 8).value or 0)
    progress_pct = float(ws_boq.cell(r, 9).value or 0)
    main_categories.append({
        'name': str(cat_name),
        'items_count': items_count,
        'boq_val': boq_val,
        'weight_pct': weight_pct,
        'approved_val': app_val,
        'billed_val': bil_val,
        'remaining_val': rem_val,
        'progress_pct': progress_pct
    })

# F. Detailed 74 BOQ Items
boq_items = []
for r in range(16, 90):
    code = ws_boq.cell(r, 2).value
    item_no = ws_boq.cell(r, 3).value
    desc = ws_boq.cell(r, 4).value
    cat = ws_boq.cell(r, 5).value
    unit = ws_boq.cell(r, 6).value
    rate = float(ws_boq.cell(r, 7).value or 0)
    boq_qty = float(ws_boq.cell(r, 8).value or 0)
    boq_val = float(ws_boq.cell(r, 9).value or 0)
    app_qty = float(ws_boq.cell(r, 10).value or 0)
    app_val = float(ws_boq.cell(r, 11).value or 0)
    bil_qty = float(ws_boq.cell(r, 12).value or 0)
    bil_val = float(ws_boq.cell(r, 13).value or 0)
    rem_qty = float(ws_boq.cell(r, 14).value or 0)
    prog_pct = float(ws_boq.cell(r, 15).value or 0)
    boq_items.append({
        'code': str(code),
        'item_no': str(item_no),
        'desc': str(desc),
        'category': str(cat),
        'unit': str(unit),
        'rate': rate,
        'boq_qty': boq_qty,
        'boq_val': boq_val,
        'approved_qty': app_qty,
        'approved_val': app_val,
        'billed_qty': bil_qty,
        'billed_val': bil_val,
        'remaining_qty': rem_qty,
        'progress_pct': prog_pct
    })

# G. Pay Apps (Pay App-01 to Pay App-16) from 'بيانات المشروع' Rows 69..84
pay_apps = []
for r in range(69, 85):
    pa_name = ws_info.cell(r, 2).value
    app_c = float(ws_info.cell(r, 3).value or 0)
    app_pv = float(ws_info.cell(r, 4).value or 0)
    app_comp_gr = float(ws_info.cell(r, 5).value or 0)
    app_comp_net = float(ws_info.cell(r, 6).value or 0)
    bil_c = float(ws_info.cell(r, 7).value or 0)
    bil_pv = float(ws_info.cell(r, 8).value or 0)
    bil_comp_gr = float(ws_info.cell(r, 9).value or 0)
    bil_comp_net = float(ws_info.cell(r, 10).value or 0)
    
    pay_apps.append({
        'name': str(pa_name),
        'app_contract': app_c,
        'app_pv': app_pv,
        'app_comp_gross': app_comp_gr,
        'app_comp_net': app_comp_net,
        'app_total': app_c + app_pv + app_comp_net,
        'billed_contract': bil_c,
        'billed_pv': bil_pv,
        'billed_comp_gross': bil_comp_gr,
        'billed_comp_net': bil_comp_net,
        'billed_total': bil_c + bil_pv + bil_comp_net,
        'is_locked': bil_c > 0 and r <= 75 # Pay App 1..7 locked for comp, 1..14 locked for PV, 1..15 locked for contract
    })

# Monthly Trend from PROGRESS
ws_prog = wb['PROGRESS']
monthly_dict = {}
for r in ws_prog.iter_rows(min_row=4, values_only=True):
    btype = str(r[4] or '').strip()
    status = str(r[8] or '').strip()
    m_val = r[10]
    amt = float(r[13] or 0.0)
    if not m_val or status != 'Approved':
        continue
    m_str = m_val.strftime('%Y-%m') if isinstance(m_val, datetime) else str(m_val).strip()
    if not re.match(r'^\d{4}-\d{2}$', m_str):
        continue
    if m_str not in monthly_dict:
        monthly_dict[m_str] = {'month': m_str, 'contract': 0.0, 'pv': 0.0, 'comp': 0.0}
    if btype == 'Contract':
        monthly_dict[m_str]['contract'] += amt
    elif btype == 'Price Variation':
        monthly_dict[m_str]['pv'] += amt
    elif btype == 'Compensation':
        monthly_dict[m_str]['comp'] += amt

monthly_trend = [monthly_dict[k] for k in sorted(monthly_dict.keys())]

wb.close()

# Save final structured JSON
full_dataset = {
    'project_info': project_info,
    'extensions': extensions,
    'engineering_components': engineering_components,
    'financial_status': financial_status,
    'handover_distances': handover_distances,
    'structures_handover': structures_handover,
    'handover_financials': handover_financials,
    'retentions': retentions,
    'handovers_list': handovers_list,
    'main_categories': main_categories,
    'boq_items': boq_items,
    'pay_apps': pay_apps,
    'monthly_trend': monthly_trend,
    'authorized_users': [
        {
            'email': 'MOHAMEDABORIZK@GMAIL.COM',
            'password': 'admin',
            'name': 'م. محمد أبو رزق',
            'role': 'مدير النظام (Admin)'
        },
        {
            'email': 'admin@emac.com',
            'password': '123',
            'name': 'إدارة إيماك للمقاولات',
            'role': 'مدير المشروع'
        },
        {
            'email': 'roads.zone7@mot.gov.eg',
            'password': '123',
            'name': 'المنطقة السابعة بأسيوط',
            'role': 'جهة الإشراف (المالك)'
        },
        {
            'email': 'qs@emac.com',
            'password': '123',
            'name': 'المكتب الفني والحصر',
            'role': 'مهندس حصر ومكتب فني'
        }
    ]
}

out_file = os.path.join(base_dir, "app", "project_data.json")
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(full_dataset, f, ensure_ascii=False, indent=2)

print(f"Successfully generated full data in {out_file}!")
print(f"- Main Categories: {len(main_categories)}")
print(f"- BOQ Items: {len(boq_items)}")
print(f"- Pay Apps: {len(pay_apps)}")
print(f"- Extensions: {len(extensions)}")
print(f"- Handover Distances: {len(handover_distances)}")

import subprocess
build_script = os.path.join(os.path.dirname(os.path.abspath(__file__)), "build_html.py")
if os.path.exists(build_script):
    subprocess.run([sys.executable, build_script], check=True)
