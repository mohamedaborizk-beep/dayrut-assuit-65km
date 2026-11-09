import json, sys, os

sys.stdout.reconfigure(encoding='utf-8')

app_dir = os.path.join(r"e:\000\Template\Client\06- QS\03- progress", "app")
json_path = os.path.join(app_dir, 'project_data.json')
with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

json_str = json.dumps(data, ensure_ascii=False)

html_code = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>مشروع ديروط - أسيوط 65 كم | لوحة المتابعة التنفيذية</title>
  
  <!-- PWA & Mobile Web App Meta Tags -->
  <link rel="manifest" href="manifest.json">
  <meta name="theme-color" content="#0284c7">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="apple-mobile-web-app-title" content="ديروط 65كم">
  <link rel="apple-touch-icon" href="icon.png">
  <link rel="icon" type="image/png" href="icon.png">

  <!-- Google Fonts: Cairo & Tajawal -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;500;600;700;800;900&family=Tajawal:wght@400;500;700;800&display=swap" rel="stylesheet">
  
  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  
  <!-- FontAwesome 6.5 -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  
  <!-- Chart.js 4 -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

  <script>
    tailwind.config = {{
      darkMode: 'class',
      plugins: [
        function({{ addVariant }}) {{
          addVariant('light', '.light &');
        }}
      ],
      theme: {{
        extend: {{
          fontFamily: {{
            cairo: ['Cairo', 'sans-serif'],
            tajawal: ['Tajawal', 'sans-serif'],
          }},
          colors: {{
            brand: {{
              50: '#f0f9ff',
              100: '#e0f2fe',
              500: '#0ea5e9',
              600: '#0284c7',
              700: '#0369a1',
              800: '#075985',
              900: '#0c4a6e',
            }},
            navy: {{
              800: '#111c38',
              900: '#0a1024',
              950: '#050814',
            }}
          }}
        }}
      }}
    }}
  </script>

  <style>
    body {{
      font-family: 'Cairo', sans-serif;
      transition: background-color 0.3s ease, color 0.3s ease;
      -webkit-tap-highlight-color: transparent;
    }}
    
    /* Modern Glass Card */
    .glass-card {{
      transition: all 0.2s ease;
    }}
    .dark .glass-card {{
      background: rgba(15, 23, 42, 0.75);
      backdrop-filter: blur(12px);
      border: 1px solid rgba(255, 255, 255, 0.08);
    }}
    .light .glass-card {{
      background: #ffffff !important;
      border: 1px solid #e2e8f0 !important;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05) !important;
    }}

    /* Global Light Mode CSS Overrides */
    html.light body {{
      background-color: #f8fafc !important;
      color: #0f172a !important;
    }}
    html.light header {{
      background-color: #ffffff !important;
      border-bottom-color: #e2e8f0 !important;
    }}
    html.light header nav {{
      background-color: #f1f5f9 !important;
      border-color: #e2e8f0 !important;
    }}
    html.light footer {{
      background-color: #ffffff !important;
      border-top-color: #e2e8f0 !important;
    }}
    html.light .stat-card {{
      background-color: #ffffff !important;
      border: 1px solid #e2e8f0 !important;
      box-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.06), 0 1px 2px -1px rgb(0 0 0 / 0.06) !important;
    }}
    html.light .bg-navy-950,
    html.light .bg-navy-900,
    html.light .bg-navy-800,
    html.light .bg-slate-950,
    html.light .bg-slate-900 {{
      background-color: #ffffff !important;
    }}
    html.light [class*="border-slate-800"] {{
      border-color: #e2e8f0 !important;
    }}
    html.light .text-slate-100,
    html.light .text-slate-200 {{
      color: #0f172a !important;
    }}
    html.light .text-slate-300,
    html.light .text-slate-400 {{
      color: #475569 !important;
    }}
    html.light [class*="bg-slate-800/"],
    html.light [class*="bg-slate-900/"] {{
      background-color: #f8fafc !important;
    }}
    html.light tr:hover {{
      background-color: #f1f5f9 !important;
    }}
    html.light #mobileBottomNav {{
      background-color: #ffffff !important;
      border-top-color: #e2e8f0 !important;
    }}

    /* Stat Cards Hover */
    .stat-card:hover {{
      transform: translateY(-2px);
    }}

    /* Table Responsive Scrollbar */
    .table-responsive {{
      scrollbar-width: thin;
    }}
    .dark .table-responsive {{
      scrollbar-color: #334155 #0f172a;
    }}
    .light .table-responsive {{
      scrollbar-color: #cbd5e1 #f8fafc;
    }}

    /* Print Header & Footer default hidden on screen */
    .print-only {{
      display: none !important;
    }}

    /* ========================================================================= */
    /* A3 LANDSCAPE PRINT OPTIMIZATION                                          */
        /* ========================================================================= */
    /* A3 LANDSCAPE EXECUTIVE PRINT OPTIMIZATION (High Clarity & Multi-page)     */
    /* ========================================================================= */
    @page {{
      size: A3 landscape;
      margin: 10mm 12mm 12mm 12mm;
    }}

    @media print {{
      /* 1. Hide all webpage navbar, mobile nav, modals, buttons, and screen tools */
      header, nav, #mobileBottomNav, button, input, select, .no-print, 
      #loginOverlay, #userManageModal, .install-prompt-banner, footer,
      .scrollbar-none {{
        display: none !important;
      }}

      /* 2. Unblock root flexbox so Chrome paginates cleanly across multiple pages */
      html, body {{
        display: block !important;
        height: auto !important;
        min-height: auto !important;
        max-height: none !important;
        overflow: visible !important;
        position: static !important;
        background: #ffffff !important;
        color: #000000 !important;
        font-size: 11pt !important;
        line-height: 1.4 !important;
        font-family: 'Cairo', 'Tajawal', sans-serif !important;
        padding: 0 !important;
        margin: 0 !important;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }}

      main, #app, .tab-content {{
        display: block !important;
        height: auto !important;
        min-height: auto !important;
        max-height: none !important;
        overflow: visible !important;
        position: static !important;
        width: 100% !important;
        padding: 0 !important;
        margin: 0 !important;
      }}

      /* Force display of active tab only */
      .tab-content.hidden {{
        display: none !important;
      }}
      .tab-content:not(.hidden) {{
        display: block !important;
      }}

      /* 3. Official High-Contrast Print Header */
      .print-only.print-header {{
        display: flex !important;
        justify-content: space-between;
        align-items: center;
        border-bottom: 2.5px solid #000000 !important;
        padding-bottom: 10px !important;
        margin-bottom: 14px !important;
        background: #ffffff !important;
        page-break-after: avoid !important;
        break-after: avoid !important;
      }}

      .print-only.print-header div {{
        color: #000000 !important;
      }}

      #printActiveTabTitle {{
        font-size: 14pt !important;
        font-weight: 900 !important;
        color: #000000 !important;
        border: 2.5px solid #000000 !important;
        border-radius: 8px !important;
        padding: 4px 18px !important;
        background: #f8fafc !important;
      }}

      /* 4. Official Print Footer */
      .print-only.print-footer {{
        display: flex !important;
        justify-content: space-between;
        align-items: center;
        border-top: 1.5px solid #000000 !important;
        padding-top: 6px !important;
        margin-top: 14px !important;
        font-size: 10pt !important;
        font-weight: 700 !important;
        color: #000000 !important;
        background: #ffffff !important;
        page-break-before: auto !important;
      }}

      /* 5. A3 Grid Layouts across 420mm width */
      #tabOverview > .grid:first-of-type {{
        display: grid !important;
        grid-template-columns: repeat(6, 1fr) !important;
        gap: 8px !important;
        margin-bottom: 12px !important;
      }}

      #tabOverview > .grid:nth-of-type(2) {{
        display: grid !important;
        grid-template-columns: 1fr 1fr !important;
        gap: 12px !important;
        margin-bottom: 12px !important;
      }}

      #tabOverview > .grid:nth-of-type(3) {{
        display: grid !important;
        grid-template-columns: repeat(3, 1fr) !important;
        gap: 10px !important;
        margin-bottom: 12px !important;
      }}

      #tabHandovers > .grid:first-of-type,
      #tabHandovers .grid-cols-4 {{
        display: grid !important;
        grid-template-columns: repeat(4, 1fr) !important;
        gap: 10px !important;
        margin-bottom: 12px !important;
      }}

      #tabHandovers .grid-cols-2 {{
        display: grid !important;
        grid-template-columns: 1fr 1fr !important;
        gap: 12px !important;
        margin-bottom: 12px !important;
      }}

      /* 6. Sharp Cards & KPI Boxes */
      .glass-card, .stat-card {{
        background: #ffffff !important;
        border: 1.5px solid #475569 !important;
        box-shadow: none !important;
        color: #000000 !important;
        border-radius: 8px !important;
        padding: 10px 12px !important;
        margin-bottom: 12px !important;
        break-inside: avoid !important;
        page-break-inside: avoid !important;
      }}

      /* Card numbers and titles clarity */
      .glass-card .text-xl, 
      .glass-card .text-2xl, 
      .glass-card .text-3xl {{
        color: #000000 !important;
        font-weight: 900 !important;
        font-size: 17pt !important;
        font-family: 'Cairo', sans-serif !important;
      }}

      .glass-card .text-xs,
      .glass-card .text-sm {{
        color: #0f172a !important;
        font-weight: 800 !important;
        font-size: 11pt !important;
      }}

      .glass-card [class*="text-[11px]"],
      .glass-card [class*="text-[10px]"] {{
        color: #334155 !important;
        font-weight: 700 !important;
        font-size: 9.5pt !important;
      }}

      /* 7. Crystal-Clear High-Contrast Tables */
      .overflow-x-auto, .table-responsive {{
        overflow: visible !important;
        width: 100% !important;
      }}

      table {{
        width: 100% !important;
        border-collapse: collapse !important;
        border-spacing: 0 !important;
        margin-top: 8px !important;
        margin-bottom: 14px !important;
        page-break-inside: auto !important;
        break-inside: auto !important;
      }}

      thead {{
        display: table-header-group !important; /* Repeats table headers on every page */
      }}

      tfoot {{
        display: table-footer-group !important;
      }}

      tr {{
        break-inside: avoid !important;
        page-break-inside: avoid !important;
      }}

      th {{
        background-color: #e2e8f0 !important;
        color: #000000 !important;
        font-size: 11pt !important;
        font-weight: 800 !important;
        text-align: center !important;
        border: 1.5px solid #000000 !important;
        padding: 7px 8px !important;
        vertical-align: middle !important;
      }}

      td {{
        border: 1.2px solid #475569 !important;
        color: #000000 !important;
        padding: 6px 8px !important;
        font-size: 10.5pt !important;
        font-weight: 600 !important;
        vertical-align: middle !important;
      }}

      /* Zebra Striping */
      tbody tr:nth-child(even) td {{
        background-color: #f8fafc !important;
      }}
      tbody tr:nth-child(odd) td {{
        background-color: #ffffff !important;
      }}

      /* Totals Rows */
      tr.font-black td, tr.font-bold td, tfoot td {{
        background-color: #e2e8f0 !important;
        font-weight: 900 !important;
        font-size: 11.5pt !important;
        border-top: 2.5px solid #000000 !important;
        border-bottom: 2.5px solid #000000 !important;
      }}

      /* Numeric Data in Tables */
      .font-mono, td[class*="text-emerald"], td[class*="text-sky"], 
      td[class*="text-amber"], td[class*="text-purple"] {{
        font-weight: 800 !important;
        font-size: 11pt !important;
        font-family: 'Cairo', monospace !important;
      }}

      /* Section Headings */
      h3, h4 {{
        color: #000000 !important;
        font-weight: 900 !important;
        font-size: 13pt !important;
        border-bottom: 1.5px solid #000000 !important;
        padding-bottom: 4px !important;
        margin-bottom: 8px !important;
      }}

      /* Status Badges */
      span[class*="rounded-full"], span[class*="rounded-lg"] {{
        border: 1.2px solid #000000 !important;
        font-weight: 800 !important;
        font-size: 9.5pt !important;
        padding: 2px 6px !important;
        color: #000000 !important;
        background-color: #f1f5f9 !important;
      }}

      /* 8. Deep, Sharp Colors for Print (No Faint Text) */
      .text-emerald-400, .text-emerald-500, .text-emerald-600, .text-emerald-700, .text-emerald-300 {{ 
        color: #065f46 !important; 
        font-weight: 800 !important; 
      }}
      .text-brand-400, .text-brand-600, .text-sky-400, .text-sky-600, .text-sky-700, .text-blue-400, .text-blue-600 {{ 
        color: #1e40af !important; 
        font-weight: 800 !important; 
      }}
      .text-amber-400, .text-amber-500, .text-amber-600, .text-amber-700, .text-amber-300 {{ 
        color: #92400e !important; 
        font-weight: 800 !important; 
      }}
      .text-purple-400, .text-purple-600, .text-purple-700 {{ 
        color: #6b21a8 !important; 
        font-weight: 800 !important; 
      }}
      .text-teal-400, .text-teal-600, .text-teal-700 {{ 
        color: #0f766e !important; 
        font-weight: 800 !important; 
      }}
      .text-rose-400, .text-rose-600, .text-rose-700, .text-red-500, .text-red-600 {{ 
        color: #991b1b !important; 
        font-weight: 800 !important; 
      }}
      .text-white, .text-slate-100, .text-slate-200, .text-slate-800, .text-slate-900 {{ 
        color: #000000 !important; 
      }}
      .text-slate-300, .text-slate-400, .text-slate-500, .text-slate-600, .text-slate-700 {{ 
        color: #334155 !important; 
        font-weight: 700 !important; 
      }}

      /* Charts in Print */
      canvas {{
        max-width: 100% !important;
        height: auto !important;
      }}
    }}
  </style>
</head>

<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col antialiased selection:bg-brand-500 selection:text-white pb-16 md:pb-0">

  <!-- ========================================================================= -->
  <!-- A3 PRINT FIXED HEADER (Visible only during Print)                         -->
  <!-- ========================================================================= -->
  <div class="print-only print-header">
    <div class="flex items-center gap-3">
      <div class="text-right">
        <div class="text-xs font-bold text-slate-700">جمهورية مصر العربية - وزارة النقل</div>
        <div class="text-xs font-extrabold text-slate-900">الهيئة العامة للطرق والكباري - المنطقة السابعة بأسيوط</div>
        <div class="text-sm font-black text-blue-900 mt-0.5">مشروع تطوير طريق الصعيد الصحراوي الغربي (ديروط - أسيوط 65 كم)</div>
      </div>
    </div>
    <div class="text-center">
      <div class="text-base font-black px-4 py-1 border-2 border-slate-800 rounded-lg inline-block" id="printActiveTabTitle">
        الموقف التنفيذي والبيانات الأساسية
      </div>
      <div class="text-[10px] text-slate-500 mt-1">عقد رقم: 2023/2022/426 بتاريخ 2022/09/27 | مقاس الطباعة المعتمد: A3 بالعرض (Landscape)</div>
    </div>
    <div class="text-left">
      <div class="text-xs font-bold text-slate-800">شركة إيماك للمقاولات</div>
      <div class="text-[10px] text-slate-500">إحدى شركات مجموعة الخرافي</div>
      <div class="text-[10px] text-slate-500 mt-0.5" id="printTimestamp">تاريخ الطباعة: </div>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- TOP EXECUTIVE HEADER                                                      -->
  <!-- ========================================================================= -->
  <header class="bg-navy-900 dark:bg-navy-900 light:bg-white border-b border-slate-800 dark:border-slate-800 light:border-slate-200 sticky top-0 z-40 shadow-xl backdrop-blur-md bg-opacity-95 light:bg-opacity-95">
    <div class="max-w-[1750px] mx-auto px-3 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between py-2.5 gap-2 sm:gap-4">
        
        <!-- Right: Branding & Titles -->
        <div class="flex items-center gap-2.5 sm:gap-4 min-w-0">
          <div class="w-10 h-10 sm:w-12 sm:h-12 rounded-xl bg-gradient-to-tr from-brand-600 to-indigo-600 flex items-center justify-center shadow-lg shadow-brand-500/20 border border-white/10 shrink-0">
            <i class="fa-solid fa-road text-xl sm:text-2xl text-white"></i>
          </div>
          <div class="min-w-0">
            <div class="flex items-center gap-1.5 sm:gap-2 flex-wrap">
              <span class="px-2 py-0.5 text-[10px] sm:text-[11px] font-bold rounded-full bg-emerald-500/15 text-emerald-400 light:text-emerald-700 border border-emerald-500/30 flex items-center gap-1">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
                موقف تنفيذي نشط
              </span>
              <span class="text-[11px] text-slate-400 light:text-slate-500 hidden sm:inline" id="headerContractNo">عقد رقم 2023/2022/426</span>
            </div>
            <h1 class="text-sm sm:text-lg font-black text-white light:text-slate-900 truncate tracking-tight mt-0.5">
              مشروع تطوير طريق الصعيد الصحراوي الغربي (ديروط - أسيوط 65 كم)
            </h1>
            <p class="text-[10px] sm:text-xs text-slate-400 light:text-slate-600 font-medium truncate hidden md:flex items-center gap-2">
              <span>المالك: الهيئة العامة للطرق والكباري</span>
              <span>•</span>
              <span>المقاول: شركة إيماك للمقاولات (مجموعة الخرافي)</span>
            </p>
          </div>
        </div>

        <!-- Left Controls: User Auth Info, Theme Toggle, Print, User Management -->
        <div class="flex items-center gap-1.5 sm:gap-3 shrink-0">
          
          <!-- Quick Status Stats (Hidden on small screens) -->
          <div class="hidden xl:flex items-center bg-slate-900/90 dark:bg-slate-900/90 light:bg-slate-100 border border-slate-800 dark:border-slate-800 light:border-slate-200 rounded-xl px-3 py-1.5 text-xs divide-x divide-x-reverse divide-slate-800 dark:divide-slate-800 light:divide-slate-300 gap-2.5">
            <div class="text-right">
              <div class="text-slate-400 light:text-slate-500 text-[10px]">المقايسة (65 كم)</div>
              <div class="font-bold text-slate-200 light:text-slate-800" id="quickBoqVal">2,359.72 م.ج</div>
            </div>
            <div class="pr-2.5 text-right">
              <div class="text-slate-400 light:text-slate-500 text-[10px]">المنفذ المعتمد</div>
              <div class="font-bold text-emerald-400 light:text-emerald-600" id="quickApprovedVal">2,969.13 م.ج</div>
            </div>
            <div class="pr-2.5 text-right">
              <div class="text-slate-400 light:text-slate-500 text-[10px]">المنصرف</div>
              <div class="font-bold text-sky-400 light:text-sky-600" id="quickBilledVal">2,693.34 م.ج</div>
            </div>
            <div class="pr-2.5 text-right">
              <div class="text-slate-400 light:text-slate-500 text-[10px]">المستحق للمقاول</div>
              <div class="font-bold text-amber-400 light:text-amber-600" id="quickRemainingVal">275.79 م.ج</div>
            </div>
          </div>

          <!-- Day / Night Mode Toggle Button -->
          <button id="themeToggleBtn" onclick="toggleTheme()" title="التبديل بين الوضع الليلي والنهاري" class="w-9 h-9 sm:w-10 sm:h-10 rounded-xl bg-slate-800 dark:bg-slate-800 light:bg-slate-100 text-slate-300 light:text-slate-700 hover:text-white border border-slate-700/80 dark:border-slate-700/80 light:border-slate-300 flex items-center justify-center transition shadow-sm">
            <i class="fa-solid fa-sun text-amber-400 text-sm hidden" id="themeSunIcon"></i>
            <i class="fa-solid fa-moon text-blue-400 text-sm" id="themeMoonIcon"></i>
          </button>

          <!-- A3 Print Button -->
          <button onclick="triggerA3Print()" title="طباعة الصفحة بتنسيق A3 بالعرض (Landscape)" class="px-2.5 sm:px-3.5 py-2 rounded-xl bg-slate-800 dark:bg-slate-800 light:bg-slate-100 hover:bg-slate-700 text-slate-200 light:text-slate-800 border border-slate-700/80 dark:border-slate-700/80 light:border-slate-300 text-xs font-bold flex items-center gap-1.5 transition shadow-sm">
            <i class="fa-solid fa-print text-brand-400"></i>
            <span class="hidden sm:inline">طباعة A3 بالعرض</span>
          </button>

          <!-- User Management (Admin Only) -->
          <button id="userManageBtn" onclick="openUserManageModal()" class="hidden px-3 py-2 rounded-xl bg-purple-950/60 light:bg-purple-100 text-purple-300 light:text-purple-800 border border-purple-500/30 text-xs font-bold items-center gap-1.5 transition">
            <i class="fa-solid fa-users-gear text-purple-400"></i>
            <span class="hidden lg:inline">إدارة الصلاحيات</span>
          </button>

          <!-- Current User Profile & Logout -->
          <div id="userProfileBadge" class="hidden items-center gap-2 bg-slate-900 dark:bg-slate-900 light:bg-slate-100 border border-slate-800 dark:border-slate-800 light:border-slate-300 px-2.5 py-1 rounded-xl text-xs">
            <div class="text-right leading-tight hidden sm:block">
              <div class="font-bold text-white light:text-slate-900" id="currentUserName">م. محمد</div>
              <div class="text-[10px] text-brand-400" id="currentUserRole">Admin</div>
            </div>
            <button onclick="logout()" title="تسجيل الخروج" class="text-slate-400 hover:text-rose-400 p-1 transition">
              <i class="fa-solid fa-arrow-right-from-bracket"></i>
            </button>
          </div>

        </div>
      </div>
    </div>

    <!-- Desktop Navigation Tabs (Hidden on print) -->
    <nav class="bg-navy-950/90 dark:bg-navy-950/90 light:bg-slate-100 border-t border-slate-800/80 dark:border-slate-800/80 light:border-slate-200 px-3 sm:px-6 lg:px-8 py-1.5 overflow-x-auto hidden md:flex gap-2 text-xs font-bold scrollbar-none no-print">
      <button onclick="switchTab('tabOverview', 'الموقف التنفيذي والبيانات الأساسية للمشروع')" class="tab-btn px-4 py-2 rounded-xl text-white bg-brand-600 transition flex items-center gap-2 whitespace-nowrap shadow-md shadow-brand-600/20 active" data-target="tabOverview">
        <i class="fa-solid fa-chart-line"></i>
        <span>الموقف التنفيذي والبيانات الأساسية</span>
      </button>

      <button onclick="switchTab('tabHandovers', 'التسليمات الجزئية والمحتجزات التعاقدية (حتى جزئي 04)')" class="tab-btn px-4 py-2 rounded-xl text-slate-300 dark:text-slate-300 light:text-slate-600 hover:text-white light:hover:text-slate-900 transition flex items-center gap-2 whitespace-nowrap" data-target="tabHandovers">
        <i class="fa-solid fa-handshake-angle text-emerald-400"></i>
        <span>التسليمات الجزئية والمحتجزات التعاقدية (حتى جزئي 04)</span>
      </button>

      <button onclick="switchTab('tabBoq', 'مقايسة الأعمال معاد القياس (65 كم - 9 فئات رئيسية)')" class="tab-btn px-4 py-2 rounded-xl text-slate-300 dark:text-slate-300 light:text-slate-600 hover:text-white light:hover:text-slate-900 transition flex items-center gap-2 whitespace-nowrap" data-target="tabBoq">
        <i class="fa-solid fa-layer-group text-sky-400"></i>
        <span>مقايسة الأعمال معاد القياس (65 كم - 9 فئات رئيسية)</span>
      </button>

      <button onclick="switchTab('tabPayApps', 'المستخلصات الجارية وفروق الأسعار والتعويضات (1-16)')" class="tab-btn px-4 py-2 rounded-xl text-slate-300 dark:text-slate-300 light:text-slate-600 hover:text-white light:hover:text-slate-900 transition flex items-center gap-2 whitespace-nowrap" data-target="tabPayApps">
        <i class="fa-solid fa-file-invoice-dollar text-purple-400"></i>
        <span>المستخلصات الجارية وفروق الأسعار والتعويضات (1-16)</span>
      </button>
    </nav>
  </header>

  <!-- ========================================================================= -->
  <!-- MOBILE STICKY BOTTOM NAVIGATION BAR (md:hidden)                           -->
  <!-- ========================================================================= -->
  <nav id="mobileBottomNav" class="md:hidden fixed bottom-0 left-0 right-0 z-40 bg-navy-900/95 dark:bg-navy-900/95 light:bg-white border-t border-slate-800 dark:border-slate-800 light:border-slate-200 backdrop-blur-md px-1 py-1.5 flex justify-around text-[10px] font-bold shadow-2xl no-print">
    <button onclick="switchTab('tabOverview', 'الموقف التنفيذي والبيانات الأساسية')" class="mobile-nav-btn flex flex-col items-center gap-1 p-1.5 text-brand-400 active" data-target="tabOverview">
      <i class="fa-solid fa-chart-line text-base"></i>
      <span>الموقف التنفيذي</span>
    </button>
    <button onclick="switchTab('tabHandovers', 'التسليمات الجزئية والمحتجزات')" class="mobile-nav-btn flex flex-col items-center gap-1 p-1.5 text-slate-400 light:text-slate-600" data-target="tabHandovers">
      <i class="fa-solid fa-handshake-angle text-base text-emerald-400"></i>
      <span>التسليمات (04)</span>
    </button>
    <button onclick="switchTab('tabBoq', 'مقايسة الأعمال معاد القياس')" class="mobile-nav-btn flex flex-col items-center gap-1 p-1.5 text-slate-400 light:text-slate-600" data-target="tabBoq">
      <i class="fa-solid fa-layer-group text-base text-sky-400"></i>
      <span>المقايسة (9 فئات)</span>
    </button>
    <button onclick="switchTab('tabPayApps', 'المستخلصات وفروق الأسعار')" class="mobile-nav-btn flex flex-col items-center gap-1 p-1.5 text-slate-400 light:text-slate-600" data-target="tabPayApps">
      <i class="fa-solid fa-file-invoice-dollar text-base text-purple-400"></i>
      <span>المستخلصات</span>
    </button>
  </nav>

  <!-- ========================================================================= -->
  <!-- MAIN CONTENT CONTAINER                                                    -->
  <!-- ========================================================================= -->
  <main class="flex-1 max-w-[1750px] w-full mx-auto px-3 sm:px-6 lg:px-8 py-5 space-y-6">

    <!-- Mobile Horizontal Swipe Tip -->
    <div class="md:hidden flex items-center justify-between bg-brand-500/10 border border-brand-500/20 text-brand-300 light:text-brand-700 px-3 py-1.5 rounded-xl text-[11px] no-print">
      <span><i class="fa-solid fa-mobile-screen ml-1.5"></i>عرض مخصص للهواتف المحمولة</span>
      <span>اسحب الجداول أفقياً لعرض باقي البيانات ↔</span>
    </div>

    <!-- ======================================================================= -->
    <!-- TAB 1: الموقف التنفيذي والبيانات الأساسية                               -->
    <!-- ======================================================================= -->
    <section id="tabOverview" class="tab-content space-y-6">
      
      <!-- Top 6 KPI Cards Grid (Avoid page break in print) -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-6 gap-3 sm:gap-4 avoid-break">
        
        <!-- Card 1: أمر الإسناد -->
        <div class="glass-card stat-card rounded-2xl p-4 relative overflow-hidden">
          <div class="flex items-center justify-between text-slate-400 light:text-slate-500 text-xs mb-1">
            <span>قيمة أمر الإسناد</span>
            <i class="fa-solid fa-file-signature text-blue-400"></i>
          </div>
          <div class="text-xl sm:text-2xl font-black text-white light:text-slate-900" id="kpiAwardVal">2,898.00 <span class="text-xs font-normal text-slate-400">م.ج</span></div>
          <div class="mt-2 text-[11px] text-slate-400 light:text-slate-500 flex items-center justify-between border-t border-slate-800/80 light:border-slate-200 pt-2">
            <span>التعاقد الأصلي</span>
            <span class="text-blue-400 light:text-blue-600 font-bold">100%</span>
          </div>
        </div>

        <!-- Card 2: مقايسة 65 كم -->
        <div class="glass-card stat-card rounded-2xl p-4 relative overflow-hidden">
          <div class="flex items-center justify-between text-slate-400 light:text-slate-500 text-xs mb-1">
            <span>المقايسة معاد القياس</span>
            <i class="fa-solid fa-calculator text-purple-400"></i>
          </div>
          <div class="text-xl sm:text-2xl font-black text-white light:text-slate-900" id="kpiBoqVal">2,359.72 <span class="text-xs font-normal text-slate-400">م.ج</span></div>
          <div class="mt-2 text-[11px] text-slate-400 light:text-slate-500 flex items-center justify-between border-t border-slate-800/80 light:border-slate-200 pt-2">
            <span>من أمر الإسناد</span>
            <span class="text-purple-400 light:text-purple-600 font-bold" id="kpiBoqPct">81.43%</span>
          </div>
        </div>

        <!-- Card 3: المنفذ المعتمد بأسعار التعاقد -->
        <div class="glass-card stat-card rounded-2xl p-4 relative overflow-hidden border-brand-500/30">
          <div class="flex items-center justify-between text-slate-400 light:text-slate-500 text-xs mb-1">
            <span>المنفذ بأسعار التعاقد</span>
            <i class="fa-solid fa-check-double text-brand-400"></i>
          </div>
          <div class="text-xl sm:text-2xl font-black text-white light:text-slate-900" id="kpiAppContract">2,086.05 <span class="text-xs font-normal text-slate-400">م.ج</span></div>
          <div class="mt-2 text-[11px] text-slate-400 light:text-slate-500 flex items-center justify-between border-t border-slate-800/80 light:border-slate-200 pt-2">
            <span>من المقايسة (65 كم)</span>
            <span class="text-emerald-400 light:text-emerald-600 font-bold" id="kpiAppContractPct">88.40%</span>
          </div>
        </div>

        <!-- Card 4: فروق الأسعار -->
        <div class="glass-card stat-card rounded-2xl p-4 relative overflow-hidden">
          <div class="flex items-center justify-between text-slate-400 light:text-slate-500 text-xs mb-1">
            <span>فروق الأسعار المعتمدة</span>
            <i class="fa-solid fa-arrow-trend-up text-amber-400"></i>
          </div>
          <div class="text-xl sm:text-2xl font-black text-white light:text-slate-900" id="kpiAppPv">641.02 <span class="text-xs font-normal text-slate-400">م.ج</span></div>
          <div class="mt-2 text-[11px] text-slate-400 light:text-slate-500 flex items-center justify-between border-t border-slate-800/80 light:border-slate-200 pt-2">
            <span>من المقايسة</span>
            <span class="text-amber-400 light:text-amber-600 font-bold" id="kpiAppPvPct">27.16%</span>
          </div>
        </div>

        <!-- Card 5: صافي التعويضات -->
        <div class="glass-card stat-card rounded-2xl p-4 relative overflow-hidden">
          <div class="flex items-center justify-between text-slate-400 light:text-slate-500 text-xs mb-1">
            <span>صافي التعويضات المعتمدة</span>
            <i class="fa-solid fa-scale-balanced text-teal-400"></i>
          </div>
          <div class="text-xl sm:text-2xl font-black text-white light:text-slate-900" id="kpiAppComp">242.06 <span class="text-xs font-normal text-slate-400">م.ج</span></div>
          <div class="mt-2 text-[11px] text-slate-400 light:text-slate-500 flex items-center justify-between border-t border-slate-800/80 light:border-slate-200 pt-2">
            <span>مقارنة كل مستخلص</span>
            <span class="text-teal-400 light:text-teal-600 font-bold" id="kpiAppCompPct">10.26%</span>
          </div>
        </div>

        <!-- Card 6: إجمالي المنفذ الشامل -->
        <div class="glass-card stat-card rounded-2xl p-4 relative overflow-hidden bg-gradient-to-br from-emerald-950/40 to-slate-900 light:from-emerald-50 light:to-white border-emerald-500/30">
          <div class="flex items-center justify-between text-slate-400 light:text-slate-500 text-xs mb-1">
            <span>إجمالي المنفذ الشامل</span>
            <i class="fa-solid fa-crown text-emerald-400"></i>
          </div>
          <div class="text-xl sm:text-2xl font-black text-emerald-400 light:text-emerald-700" id="kpiAppTotal">2,969.13 <span class="text-xs font-normal text-slate-400">م.ج</span></div>
          <div class="mt-2 text-[11px] text-slate-300 light:text-slate-600 flex items-center justify-between border-t border-slate-800/80 light:border-slate-200 pt-2">
            <span>نسبة الإنجاز المالية</span>
            <span class="text-emerald-300 light:text-emerald-700 font-extrabold" id="kpiAppTotalPct">125.83%</span>
          </div>
        </div>

      </div>

      <!-- Cash Flow & Billing Stats -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 avoid-break">
        <!-- Billed & Locked Box -->
        <div class="glass-card rounded-2xl p-4 sm:p-5 border-l-4 border-l-sky-500 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-2 flex-wrap gap-1">
              <span class="text-xs font-bold text-sky-400 light:text-sky-700 uppercase tracking-wider flex items-center gap-1.5">
                <i class="fa-solid fa-file-invoice"></i>
                إجمالي المستخلصات الجارية المعتمدة (Billed & Locked)
              </span>
              <span class="text-[10px] sm:text-xs bg-sky-500/10 text-sky-300 light:text-sky-700 px-2.5 py-0.5 rounded-full border border-sky-500/20">معتمدة مع المالك</span>
            </div>
            <div class="flex items-baseline gap-2 sm:gap-3 my-2 flex-wrap">
              <span class="text-2xl sm:text-3xl font-black text-white light:text-slate-900" id="statBilledTotal">2,693,344,410.17</span>
              <span class="text-xs sm:text-sm text-slate-400">جنيه مصري</span>
              <span class="mr-auto text-xs font-bold text-emerald-400 light:text-emerald-700 bg-emerald-500/10 px-2 py-0.5 rounded-lg">90.71% من المنفذ</span>
            </div>
            <div class="grid grid-cols-3 gap-2 sm:gap-3 mt-3 pt-3 border-t border-slate-800 light:border-slate-200 text-xs">
              <div class="bg-slate-900/60 light:bg-slate-50 p-2 sm:p-2.5 rounded-xl border border-slate-800/80 light:border-slate-200">
                <div class="text-slate-400 light:text-slate-500 text-[10px] sm:text-[11px]">أعمال التعاقد (1-15)</div>
                <div class="font-bold text-slate-200 light:text-slate-800 mt-0.5" id="statBilledContract">1,967.70 م.ج</div>
              </div>
              <div class="bg-slate-900/60 light:bg-slate-50 p-2 sm:p-2.5 rounded-xl border border-slate-800/80 light:border-slate-200">
                <div class="text-slate-400 light:text-slate-500 text-[10px] sm:text-[11px]">فروق أسعار (1-14)</div>
                <div class="font-bold text-amber-300 light:text-amber-700 mt-0.5" id="statBilledPv">498.47 م.ج</div>
              </div>
              <div class="bg-slate-900/60 light:bg-slate-50 p-2 sm:p-2.5 rounded-xl border border-slate-800/80 light:border-slate-200">
                <div class="text-slate-400 light:text-slate-500 text-[10px] sm:text-[11px]">صافي تعويضات (1-7)</div>
                <div class="font-bold text-teal-300 light:text-teal-700 mt-0.5" id="statBilledComp">227.17 م.ج</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Remaining Due Box -->
        <div class="glass-card rounded-2xl p-4 sm:p-5 border-l-4 border-l-amber-500 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-2 flex-wrap gap-1">
              <span class="text-xs font-bold text-amber-400 light:text-amber-700 uppercase tracking-wider flex items-center gap-1.5">
                <i class="fa-solid fa-clock-rotate-left"></i>
                إجمالي المستحقات المتبقية للمقاول عن الأعمال المنفذة
              </span>
              <span class="text-[10px] sm:text-xs bg-amber-500/10 text-amber-300 light:text-amber-700 px-2.5 py-0.5 rounded-full border border-amber-500/20">جارٍ استصدارها</span>
            </div>
            <div class="flex items-baseline gap-2 sm:gap-3 my-2 flex-wrap">
              <span class="text-2xl sm:text-3xl font-black text-amber-400 light:text-amber-600" id="statRemainingTotal">275,788,066.89</span>
              <span class="text-xs sm:text-sm text-slate-400">جنيه مصري</span>
              <span class="mr-auto text-xs font-bold text-amber-400 light:text-amber-700 bg-amber-500/10 px-2 py-0.5 rounded-lg">9.29% من المنفذ</span>
            </div>
            <div class="grid grid-cols-3 gap-2 sm:gap-3 mt-3 pt-3 border-t border-slate-800 light:border-slate-200 text-xs">
              <div class="bg-slate-900/60 light:bg-slate-50 p-2 sm:p-2.5 rounded-xl border border-slate-800/80 light:border-slate-200">
                <div class="text-slate-400 light:text-slate-500 text-[10px] sm:text-[11px]">متبقي أعمال العقد</div>
                <div class="font-bold text-slate-200 light:text-slate-800 mt-0.5" id="statRemainingContract">118.35 م.ج</div>
              </div>
              <div class="bg-slate-900/60 light:bg-slate-50 p-2 sm:p-2.5 rounded-xl border border-slate-800/80 light:border-slate-200">
                <div class="text-slate-400 light:text-slate-500 text-[10px] sm:text-[11px]">متبقي فروق أسعار</div>
                <div class="font-bold text-amber-300 light:text-amber-700 mt-0.5" id="statRemainingPv">142.54 م.ج</div>
              </div>
              <div class="bg-slate-900/60 light:bg-slate-50 p-2 sm:p-2.5 rounded-xl border border-slate-800/80 light:border-slate-200">
                <div class="text-slate-400 light:text-slate-500 text-[10px] sm:text-[11px]">متبقي صافي تعويضات</div>
                <div class="font-bold text-teal-300 light:text-teal-700 mt-0.5" id="statRemainingComp">14.89 م.ج</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Project Parties & Timeline Details Grid -->
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-4 sm:gap-6 avoid-break">
        
        <!-- Column 1: Contractual Parties & Dates -->
        <div class="glass-card rounded-2xl p-4 sm:p-5 space-y-3">
          <div class="flex items-center justify-between border-b border-slate-800 light:border-slate-200 pb-2.5">
            <h3 class="text-sm font-extrabold text-white light:text-slate-900 flex items-center gap-2">
              <i class="fa-solid fa-briefcase text-brand-400"></i>
              بيانات المشروع التعاقدية
            </h3>
            <span class="text-[10px] text-slate-400 light:text-slate-600 bg-slate-800 light:bg-slate-100 px-2 py-0.5 rounded">الأمر المباشر</span>
          </div>

          <div class="space-y-2 text-xs">
            <div class="flex justify-between items-center py-1 border-b border-slate-800/60 light:border-slate-100">
              <span class="text-slate-400 light:text-slate-500">جهة الإسناد / المالك:</span>
              <span class="font-bold text-slate-200 light:text-slate-800 text-left">الهيئة العامة للطرق والكباري</span>
            </div>
            <div class="flex justify-between items-center py-1 border-b border-slate-800/60 light:border-slate-100">
              <span class="text-slate-400 light:text-slate-500">المنطقة المشرفة:</span>
              <span class="font-bold text-slate-200 light:text-slate-800 text-left">المنطقة السابعة بأسيوط</span>
            </div>
            <div class="flex justify-between items-center py-1 border-b border-slate-800/60 light:border-slate-100">
              <span class="text-slate-400 light:text-slate-500">المقاول العام:</span>
              <span class="font-bold text-emerald-400 light:text-emerald-700 text-left">شركة إيماك للمقاولات (الخرافي)</span>
            </div>
            <div class="flex justify-between items-center py-1 border-b border-slate-800/60 light:border-slate-100">
              <span class="text-slate-400 light:text-slate-500">استشاري المالك:</span>
              <span class="font-bold text-slate-200 light:text-slate-800 text-left">مكتب انترانس للاستشارات</span>
            </div>
            <div class="flex justify-between items-center py-1 border-b border-slate-800/60 light:border-slate-100">
              <span class="text-slate-400 light:text-slate-500">استشاري المقاول:</span>
              <span class="font-bold text-slate-200 light:text-slate-800 text-left">مكتب الرائد للاستشارات</span>
            </div>
            <div class="flex justify-between items-center py-1 border-b border-slate-800/60 light:border-slate-100">
              <span class="text-slate-400 light:text-slate-500">خطاب النوايا 1 / 2:</span>
              <span class="font-bold text-slate-300 light:text-slate-700 text-left">2021/09/20 - 2021/09/28</span>
            </div>
            <div class="flex justify-between items-center py-1 border-b border-slate-800/60 light:border-slate-100">
              <span class="text-slate-400 light:text-slate-500">استلام الموقع:</span>
              <span class="font-bold text-sky-400 light:text-sky-700 text-left">2022/07/20</span>
            </div>
            <div class="flex justify-between items-center py-1">
              <span class="text-slate-400 light:text-slate-500">توقيع العقد:</span>
              <span class="font-bold text-slate-300 light:text-slate-700 text-left">2022/09/27</span>
            </div>
          </div>
        </div>

        <!-- Column 2: Timeline & Extensions -->
        <div class="glass-card rounded-2xl p-4 sm:p-5 space-y-3">
          <div class="flex items-center justify-between border-b border-slate-800 light:border-slate-200 pb-2.5">
            <h3 class="text-sm font-extrabold text-white light:text-slate-900 flex items-center gap-2">
              <i class="fa-solid fa-calendar-check text-emerald-400"></i>
              الموقف الزمني للمشروع
            </h3>
            <span class="text-[10px] text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded border border-emerald-500/20">34 شهر تمديد</span>
          </div>

          <div class="space-y-2.5 text-xs">
            <div class="bg-slate-900/70 light:bg-slate-50 p-2.5 rounded-xl border border-slate-800/80 light:border-slate-200">
              <div class="flex justify-between text-slate-400 light:text-slate-500 text-[10px] mb-1">
                <span>مدة العقد الأصلية</span>
                <span class="text-slate-200 light:text-slate-800 font-bold">12 شهر ميلادي</span>
              </div>
              <div class="flex justify-between items-center font-bold text-slate-300 light:text-slate-700">
                <span>من 2022/07/20</span>
                <span>حتى 2023/07/19</span>
              </div>
            </div>

            <div class="bg-brand-950/40 light:bg-sky-50 p-2.5 rounded-xl border border-brand-500/30 light:border-sky-200">
              <div class="flex justify-between text-brand-300 light:text-sky-800 text-[10px] mb-1">
                <span>التمديدات الزمنية المعتمدة</span>
                <span class="text-brand-300 light:text-sky-800 font-extrabold">34 شهر ميلادي</span>
              </div>
              <div class="flex justify-between items-center font-bold text-white light:text-sky-900">
                <span>من 2023/07/20</span>
                <span>حتى 2026/05/19</span>
              </div>
            </div>

            <div class="bg-emerald-950/40 light:bg-emerald-50 p-2.5 rounded-xl border border-emerald-500/30 light:border-emerald-200">
              <div class="flex justify-between text-emerald-400 light:text-emerald-800 text-[10px] mb-1">
                <span>إجمالي مدة المشروع الكلية</span>
                <span class="text-emerald-300 light:text-emerald-800 font-extrabold">46 شهر ميلادي</span>
              </div>
              <div class="flex justify-between items-center font-bold text-emerald-200 light:text-emerald-900">
                <span>تاريخ النهو التعاقدي:</span>
                <span class="text-sm">2026/05/19</span>
              </div>
            </div>

            <div class="pt-1">
              <div class="flex justify-between text-[11px] text-slate-400 light:text-slate-500 mb-1">
                <span>التمديدات المعتمدة رسمياً</span>
                <span class="text-emerald-400 light:text-emerald-700 font-bold">8 تمديدات معتمدة</span>
              </div>
              <div class="w-full bg-slate-800 light:bg-slate-200 rounded-full h-2 flex overflow-hidden">
                <div class="bg-blue-500 h-2" style="width: 26%" title="الأصلية (12 شهر)"></div>
                <div class="bg-emerald-500 h-2" style="width: 74%" title="التمديدات (34 شهر)"></div>
              </div>
            </div>
          </div>
        </div>

        <!-- Column 3: Extension Approvals Details -->
        <div class="glass-card rounded-2xl p-4 sm:p-5 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between border-b border-slate-800 light:border-slate-200 pb-2.5 mb-2.5">
              <h3 class="text-sm font-extrabold text-white light:text-slate-900 flex items-center gap-2">
                <i class="fa-solid fa-list-ol text-purple-400"></i>
                بيان تمديدات التعاقد والمعوقات
              </h3>
              <span class="text-[10px] text-slate-400">ملف الـ PDF الرسمي</span>
            </div>

            <div class="space-y-2 max-h-[250px] overflow-y-auto pr-1 text-xs" id="extensionsContainer">
              <!-- Rendered via JS -->
            </div>
          </div>
        </div>

      </div>

      <!-- Engineering Scope & Components Table (Avoid page break in print) -->
      <div class="glass-card rounded-2xl p-4 sm:p-5 space-y-3 ">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 light:border-slate-200 pb-3">
          <div>
            <h3 class="text-sm sm:text-base font-extrabold text-white light:text-slate-900 flex items-center gap-2">
              <i class="fa-solid fa-compass-drafting text-brand-400"></i>
              مكونات المشروع ونطاق الأعمال (مسار 72 كم: 65 كم داخل العقد + 7 كم خارج العقد)
            </h3>
            <p class="text-xs text-slate-400 light:text-slate-500 mt-0.5">تفصيل المسارات والأعمال لطرق الخدمة، الطرق الرئيسية، التقاطعات الحرة، الرامبات، الأنفاق والبرابخ</p>
          </div>
          <span class="text-xs font-bold bg-slate-800 light:bg-slate-100 text-slate-200 light:text-slate-800 px-3 py-1 rounded-xl self-start sm:self-auto border border-slate-700 light:border-slate-300">
            طول المسار: 72 كم بالاتجاهين
          </span>
        </div>

        <div class="overflow-x-auto table-responsive rounded-xl border border-slate-800 light:border-slate-200">
          <table class="w-full text-right text-xs">
            <thead class="bg-slate-900/90 light:bg-slate-100 text-slate-300 light:text-slate-800 font-bold border-b border-slate-800 light:border-slate-200">
              <tr>
                <th class="p-2.5 sm:p-3">مكون العمل</th>
                <th class="p-2.5 sm:p-3">طبيعة ومواصفة التنفيذ</th>
                <th class="p-2.5 sm:p-3">داخل نطاق العقد (65 كم: 282 إلى 347)</th>
                <th class="p-2.5 sm:p-3">خارج نطاق العقد (7 كم: 347 إلى 354)</th>
                <th class="p-2.5 sm:p-3">إجمالي المسار</th>
                <th class="p-2.5 sm:p-3">ملاحظات هندسية</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-800/60 light:divide-slate-200 font-medium text-slate-200 light:text-slate-700" id="componentsTableBody">
              <!-- Rendered via JS -->
            </tbody>
          </table>
        </div>
      </div>

      <!-- Financial Status Table & Donut Chart -->
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 ">
        
        <!-- Table (2 cols) -->
        <div class="lg:col-span-2 glass-card rounded-2xl p-4 sm:p-5 space-y-3">
          <div class="flex items-center justify-between border-b border-slate-800 light:border-slate-200 pb-2.5">
            <h3 class="text-sm font-extrabold text-white light:text-slate-900 flex items-center gap-2">
              <i class="fa-solid fa-table-cells text-emerald-400"></i>
              جدول الموقف المالي والتنفيذي الشامل (مطابق لملف progress.xlsx)
            </h3>
            <span class="text-xs text-slate-400">جنيه مصري</span>
          </div>

          <div class="overflow-x-auto table-responsive rounded-xl border border-slate-800 light:border-slate-200">
            <table class="w-full text-right text-xs">
              <thead class="bg-slate-900/90 light:bg-slate-100 text-slate-300 light:text-slate-800 font-bold border-b border-slate-800 light:border-slate-200">
                <tr>
                  <th class="p-2.5 text-center">م</th>
                  <th class="p-2.5">البيان المالي والتنفيذي</th>
                  <th class="p-2.5 text-left">القيمة (ج.م)</th>
                  <th class="p-2.5 text-center">النسبة من الإسناد</th>
                  <th class="p-2.5 text-center">النسبة من المقايسة</th>
                  <th class="p-2.5">المرجع والمعادلة</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-800/60 light:divide-slate-200 font-medium text-slate-200 light:text-slate-700" id="financialTableBody">
                <!-- Rendered via JS -->
              </tbody>
            </table>
          </div>
        </div>

        <!-- Donut Chart (1 col) -->
        <div class="glass-card rounded-2xl p-4 sm:p-5 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between border-b border-slate-800 light:border-slate-200 pb-2.5 mb-3">
              <h3 class="text-sm font-extrabold text-white light:text-slate-900 flex items-center gap-2">
                <i class="fa-solid fa-chart-pie text-brand-400"></i>
                هيكل الإنجاز المالي
              </h3>
              <span class="text-[10px] text-slate-400">المنفذ الفعلي</span>
            </div>
            <div class="relative h-60 flex items-center justify-center">
              <canvas id="financialDonutChart"></canvas>
            </div>
          </div>
          <div class="mt-3 pt-3 border-t border-slate-800 light:border-slate-200 text-[11px] text-slate-400 light:text-slate-600 space-y-1">
            <div class="flex justify-between items-center">
              <span class="flex items-center gap-1.5"><span class="w-2.5 h-2.5 rounded-full bg-brand-500"></span>أعمال التعاقد:</span>
              <span class="font-bold text-slate-200 light:text-slate-800">2,086.05 م.ج</span>
            </div>
            <div class="flex justify-between items-center">
              <span class="flex items-center gap-1.5"><span class="w-2.5 h-2.5 rounded-full bg-amber-500"></span>فروق الأسعار:</span>
              <span class="font-bold text-slate-200 light:text-slate-800">641.02 م.ج</span>
            </div>
            <div class="flex justify-between items-center">
              <span class="flex items-center gap-1.5"><span class="w-2.5 h-2.5 rounded-full bg-teal-500"></span>صافي التعويضات:</span>
              <span class="font-bold text-slate-200 light:text-slate-800">242.06 م.ج</span>
            </div>
          </div>
        </div>

      </div>

    </section>

    <!-- ======================================================================= -->
    <!-- TAB 2: التسليمات الجزئية والمحتجزات التعاقدية                           -->
    <!-- ======================================================================= -->
    <section id="tabHandovers" class="tab-content hidden space-y-6">
      
      <!-- Road Distances Handed Over Section -->
      <div class="glass-card rounded-2xl p-4 sm:p-5 space-y-4 avoid-break">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 light:border-slate-200 pb-3">
          <div>
            <h3 class="text-sm sm:text-base font-extrabold text-white light:text-slate-900 flex items-center gap-2">
              <i class="fa-solid fa-road text-emerald-400"></i>
              الموقف التراكمي للمسافات والأطوال المسلمة حتى التسليم الجزئي رقم (04)
            </h3>
            <p class="text-xs text-slate-400 light:text-slate-500 mt-0.5">تراكمي لجميع اتجاهات الطرق والأنفاق والبرابخ دون فصل كل تسليم على حدة</p>
          </div>
          <span class="text-xs font-black bg-emerald-500/15 text-emerald-400 light:text-emerald-700 border border-emerald-500/30 px-3 py-1 rounded-xl self-start sm:self-auto">
            إجمالي أطوال الطرق المسلمة: 197.40 كم من أصل 260 كم (75.92%)
          </span>
        </div>

        <!-- 4 Direction Cards Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-3 sm:gap-4" id="roadProgressCards">
          <!-- Rendered via JS -->
        </div>

        <!-- Structures Summary (3 Tunnels + 8 Culverts) -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 sm:gap-4 pt-1">
          <div class="bg-slate-900/80 light:bg-slate-50 p-3.5 rounded-xl border border-slate-800 light:border-slate-200 flex items-center gap-3.5">
            <div class="w-11 h-11 rounded-xl bg-purple-500/20 text-purple-400 flex items-center justify-center text-lg shrink-0">
              <i class="fa-solid fa-archway"></i>
            </div>
            <div>
              <div class="text-[11px] text-slate-400 light:text-slate-500">الأنفاق السطحية المسلمة (مسار العقد 65 كم)</div>
              <div class="text-base sm:text-lg font-black text-white light:text-slate-900 mt-0.5">3 من أصل 3 أنفاق <span class="text-xs font-bold text-emerald-400 light:text-emerald-700 bg-emerald-500/10 px-2 py-0.5 rounded mr-1.5">100% مسلمة</span></div>
              <div class="text-[10px] text-slate-400 light:text-slate-500 mt-0.5">نفق القوصية (290) + دوران للخلف (310) + منفلوط تنيدة (329)</div>
            </div>
          </div>

          <div class="bg-slate-900/80 light:bg-slate-50 p-3.5 rounded-xl border border-slate-800 light:border-slate-200 flex items-center gap-3.5">
            <div class="w-11 h-11 rounded-xl bg-blue-500/20 text-blue-400 flex items-center justify-center text-lg shrink-0">
              <i class="fa-solid fa-water"></i>
            </div>
            <div>
              <div class="text-[11px] text-slate-400 light:text-slate-500">برابخ تصريف السيول المسلمة (قطر 1 متر)</div>
              <div class="text-base sm:text-lg font-black text-white light:text-slate-900 mt-0.5">8 من أصل 9 مواقع <span class="text-xs font-bold text-blue-400 light:text-blue-700 bg-blue-500/10 px-2 py-0.5 rounded mr-1.5">88.89% مسلمة</span></div>
              <div class="text-[10px] text-slate-400 light:text-slate-500 mt-0.5">برابخ الكم: (5، 11، 13، 15، 20، 30، 40، 43) - متبقي بربخ كم 33.9</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Financial Handover Breakdown Cards -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3 sm:gap-4 avoid-break">
        <!-- Final Handovers -->
        <div class="glass-card stat-card rounded-2xl p-4 border-l-4 border-l-emerald-500">
          <div class="text-xs text-slate-400 light:text-slate-500 font-bold mb-1">المسلم تسليماً نهائياً (جزئي 1+2+3)</div>
          <div class="text-xl sm:text-2xl font-black text-white light:text-slate-900" id="hoFinalContract">1,236.68 <span class="text-xs font-normal text-slate-400">م.ج</span></div>
          <div class="mt-2 text-xs text-slate-400 light:text-slate-500 space-y-1">
            <div class="flex justify-between"><span>من المقايسة:</span><span class="text-emerald-400 light:text-emerald-700 font-bold">52.41%</span></div>
            <div class="flex justify-between"><span>من أمر الإسناد:</span><span class="text-slate-300 light:text-slate-700 font-bold">42.67%</span></div>
          </div>
        </div>

        <!-- Initial Handover 04 -->
        <div class="glass-card stat-card rounded-2xl p-4 border-l-4 border-l-brand-500">
          <div class="text-xs text-slate-400 light:text-slate-500 font-bold mb-1">المسلم ابتدائياً فقط (جزئي 04)</div>
          <div class="text-xl sm:text-2xl font-black text-brand-400 light:text-brand-600" id="hoInitialContract">531.19 <span class="text-xs font-normal text-slate-400">م.ج</span></div>
          <div class="mt-2 text-xs text-slate-400 light:text-slate-500 space-y-1">
            <div class="flex justify-between"><span>من المقايسة:</span><span class="text-brand-400 light:text-brand-600 font-bold">22.51%</span></div>
            <div class="flex justify-between"><span>من أمر الإسناد:</span><span class="text-slate-300 light:text-slate-700 font-bold">18.33%</span></div>
          </div>
        </div>

        <!-- Total Handed Over -->
        <div class="glass-card stat-card rounded-2xl p-4 border-l-4 border-l-purple-500">
          <div class="text-xs text-slate-400 light:text-slate-500 font-bold mb-1">إجمالي المسلم ابتدائياً (1 حتى 04)</div>
          <div class="text-xl sm:text-2xl font-black text-purple-400 light:text-purple-700" id="hoGrandContract">1,767.88 <span class="text-xs font-normal text-slate-400">م.ج</span></div>
          <div class="mt-2 text-xs text-slate-400 light:text-slate-500 space-y-1">
            <div class="flex justify-between"><span>من المقايسة:</span><span class="text-purple-400 light:text-purple-700 font-bold">74.92%</span></div>
            <div class="flex justify-between"><span>من المنفذ Approved:</span><span class="text-emerald-400 light:text-emerald-700 font-bold">84.75%</span></div>
          </div>
        </div>

        <!-- PV on Handovers -->
        <div class="glass-card stat-card rounded-2xl p-4 border-l-4 border-l-amber-500">
          <div class="text-xs text-slate-400 light:text-slate-500 font-bold mb-1">فروق أسعار التسليمات الجزئية</div>
          <div class="text-xl sm:text-2xl font-black text-amber-400 light:text-amber-600" id="hoGrandPv">471.63 <span class="text-xs font-normal text-slate-400">م.ج</span></div>
          <div class="mt-2 text-xs text-slate-400 light:text-slate-500 space-y-1">
            <div class="flex justify-between"><span>الإجمالي شامل الفروق:</span><span class="text-white light:text-slate-900 font-bold">2,239.51 م.ج</span></div>
            <div class="flex justify-between"><span>نهائي 1..3:</span><span class="text-slate-300 light:text-slate-700">147.71 م.ج</span></div>
          </div>
        </div>
      </div>

      <!-- Retentions Analysis: 5% Works Retention & 5% Final Bank Guarantee -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-4 sm:gap-6 avoid-break">
        
        <!-- Retentions Box 1: 5% Works Retention -->
        <div class="glass-card rounded-2xl p-4 sm:p-5 space-y-3.5 border-t-4 border-t-emerald-500">
          <div class="flex items-center justify-between border-b border-slate-800 light:border-slate-200 pb-2.5">
            <div>
              <h3 class="text-sm font-extrabold text-white light:text-slate-900 flex items-center gap-2">
                <i class="fa-solid fa-shield-halved text-emerald-400"></i>
                محتجز ضمان الأعمال (5% من المستخلصات المعتمدة)
              </h3>
              <p class="text-[11px] text-slate-400 light:text-slate-500 mt-0.5">يُخصم 5% من كل مستخلص جاري معتمد، ويُرد بموجب التسليم الابتدائي للأعمال</p>
            </div>
            <span class="text-xs font-bold text-emerald-400 light:text-emerald-700 bg-emerald-500/10 px-2.5 py-1 rounded-xl">صرف 89.84%</span>
          </div>

          <div class="grid grid-cols-3 gap-2.5 sm:gap-3 text-xs">
            <div class="bg-slate-900/80 light:bg-slate-50 p-2.5 sm:p-3 rounded-xl border border-slate-800 light:border-slate-200">
              <div class="text-slate-400 light:text-slate-500 text-[10px] sm:text-[11px]">المحتجز المخصوم (5%)</div>
              <div class="text-sm sm:text-base font-bold text-white light:text-slate-900 mt-1">98,384,801.11 <span class="text-[9px] text-slate-400">ج.م</span></div>
              <div class="text-[9px] text-slate-400 mt-0.5">5% × 1,967.70 م.ج</div>
            </div>

            <div class="bg-emerald-950/40 light:bg-emerald-50 p-2.5 sm:p-3 rounded-xl border border-emerald-500/30 light:border-emerald-200">
              <div class="text-emerald-300 light:text-emerald-800 text-[10px] sm:text-[11px]">المستحق رده وصرفه</div>
              <div class="text-sm sm:text-base font-black text-emerald-400 light:text-emerald-700 mt-1">88,393,816.83 <span class="text-[9px] text-slate-400">ج.م</span></div>
              <div class="text-[9px] text-emerald-400 light:text-emerald-700 font-bold mt-0.5">89.84% من المحتجز</div>
            </div>

            <div class="bg-slate-900/80 light:bg-slate-50 p-2.5 sm:p-3 rounded-xl border border-slate-800 light:border-slate-200">
              <div class="text-slate-400 light:text-slate-500 text-[10px] sm:text-[11px]">المتبقي لحين التسليم</div>
              <div class="text-sm sm:text-base font-bold text-amber-300 light:text-amber-700 mt-1">9,990,984.29 <span class="text-[9px] text-slate-400">ج.م</span></div>
              <div class="text-[9px] text-slate-400 mt-0.5">10.16% فقط</div>
            </div>
          </div>

          <div class="space-y-1 pt-1">
            <div class="flex justify-between text-xs">
              <span class="text-slate-400 light:text-slate-600">نسبة الصرف المستحقة بموجب التسليمات الابتدائية (جزئي 1..4):</span>
              <span class="font-extrabold text-emerald-400 light:text-emerald-700">89.84%</span>
            </div>
            <div class="w-full bg-slate-800 light:bg-slate-200 rounded-full h-2.5 overflow-hidden flex">
              <div class="bg-gradient-to-r from-emerald-600 to-teal-400 h-2.5" style="width: 89.84%"></div>
              <div class="bg-amber-500/40 h-2.5" style="width: 10.16%"></div>
            </div>
          </div>
        </div>

        <!-- Retentions Box 2: 5% Bank Guarantee -->
        <div class="glass-card rounded-2xl p-4 sm:p-5 space-y-3.5 border-t-4 border-t-purple-500">
          <div class="flex items-center justify-between border-b border-slate-800 light:border-slate-200 pb-2.5">
            <div>
              <h3 class="text-sm font-extrabold text-white light:text-slate-900 flex items-center gap-2">
                <i class="fa-solid fa-file-invoice text-purple-400"></i>
                خطاب الضمان البنكي للتأمين النهائي (5% من التعاقد)
              </h3>
              <p class="text-[11px] text-slate-400 light:text-slate-500 mt-0.5">يُخفض خطاب الضمان بفارق الحصر الفعلي + الأعمال المسلمة نهائياً</p>
            </div>
            <span class="text-xs font-bold text-purple-400 light:text-purple-700 bg-purple-500/10 px-2.5 py-1 rounded-xl">تخفيض 61.25%</span>
          </div>

          <div class="grid grid-cols-2 gap-2.5 sm:gap-3 text-xs">
            <div class="bg-slate-900/80 light:bg-slate-50 p-2.5 sm:p-3 rounded-xl border border-slate-800 light:border-slate-200">
              <div class="text-slate-400 light:text-slate-500 text-[10px] sm:text-[11px]">خطاب الضمان الأصلي (5% إسناد)</div>
              <div class="text-sm sm:text-base font-bold text-white light:text-slate-900 mt-1">144,900,000.00 <span class="text-[9px] text-slate-400">ج.م</span></div>
            </div>

            <div class="bg-purple-950/40 light:bg-purple-50 p-2.5 sm:p-3 rounded-xl border border-purple-500/30 light:border-purple-200">
              <div class="text-purple-300 light:text-purple-800 text-[10px] sm:text-[11px]">إجمالي التخفيض المستحق حالياً</div>
              <div class="text-sm sm:text-base font-black text-purple-400 light:text-purple-700 mt-1">88,747,909.53 <span class="text-[9px] text-slate-400">ج.م</span></div>
              <div class="text-[9px] text-purple-400 light:text-purple-700 font-bold mt-0.5">61.25% من الخطاب</div>
            </div>
          </div>

          <div class="space-y-1.5 text-xs pt-1">
            <div class="flex justify-between items-center p-2 rounded-lg bg-slate-900/50 light:bg-slate-50 border border-slate-800/60 light:border-slate-200">
              <span class="text-slate-300 light:text-slate-700">(أ) تخفيض فرق الحصر الفعلي عن الإسناد (5% × 538.28 م.ج):</span>
              <span class="font-bold text-slate-100 light:text-slate-900">26,913,803.21 ج.م (18.57%)</span>
            </div>
            <div class="flex justify-between items-center p-2 rounded-lg bg-slate-900/50 light:bg-slate-50 border border-slate-800/60 light:border-slate-200">
              <span class="text-slate-300 light:text-slate-700">(ب) تخفيض بموجب التسليم النهائي للأعمال (5% × 1,236.68 م.ج):</span>
              <span class="font-bold text-slate-100 light:text-slate-900">61,834,106.32 ج.م (42.67%)</span>
            </div>
            <div class="flex justify-between items-center p-2 rounded-lg bg-emerald-950/30 light:bg-emerald-50 border border-emerald-500/20 light:border-emerald-300 text-emerald-300 light:text-emerald-900 font-bold">
              <span>الرصيد المتبقي المفترض لسريان خطاب الضمان:</span>
              <span class="text-xs sm:text-sm text-emerald-400 light:text-emerald-700">56,152,090.47 ج.م (38.75%)</span>
            </div>
          </div>
        </div>

      </div>

      <!-- Individual Handovers Table -->
      <div class="glass-card rounded-2xl p-4 sm:p-5 space-y-3">
        <div class="flex items-center justify-between border-b border-slate-800 light:border-slate-200 pb-2.5">
          <h3 class="text-sm font-extrabold text-white light:text-slate-900 flex items-center gap-2">
            <i class="fa-solid fa-list-check text-brand-400"></i>
            جدول بيانات التسليمات الجزئية الفردية (جزئي 01 حتى جزئي 04)
          </h3>
          <span class="text-xs text-slate-400">محاضر التسليم المعتمدة</span>
        </div>

        <div class="overflow-x-auto table-responsive rounded-xl border border-slate-800 light:border-slate-200">
          <table class="w-full text-right text-xs">
            <thead class="bg-slate-900/90 light:bg-slate-100 text-slate-300 light:text-slate-800 font-bold border-b border-slate-800 light:border-slate-200">
              <tr>
                <th class="p-2.5">رقم التسليم</th>
                <th class="p-2.5">حالة التسليم</th>
                <th class="p-2.5">تواريخ التسليم الابتدائي والنهائي</th>
                <th class="p-2.5 text-left">قيمة بأسعار التعاقد (ج.م)</th>
                <th class="p-2.5 text-left">فروق الأسعار (ج.م)</th>
                <th class="p-2.5 text-left">الإجمالي شامل الفروق (ج.م)</th>
                <th class="p-2.5">نطاق الأعمال والمواقع المسلمة</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-800/60 light:divide-slate-200 font-medium text-slate-200 light:text-slate-700" id="individualHandoversTable">
              <!-- Rendered via JS -->
            </tbody>
          </table>
        </div>
      </div>

    </section>

    <!-- ======================================================================= -->
    <!-- TAB 3: مقايسة الأعمال معاد القياس (65 كم)                                -->
    <!-- ======================================================================= -->
    <section id="tabBoq" class="tab-content hidden space-y-6">
      
      <!-- 9 Main Work Categories Table -->
      <div class="glass-card rounded-2xl p-4 sm:p-5 space-y-3">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 light:border-slate-200 pb-3">
          <div>
            <h3 class="text-sm sm:text-base font-extrabold text-white light:text-slate-900 flex items-center gap-2">
              <i class="fa-solid fa-layer-group text-sky-400"></i>
              ملخص الأعمال الرئيسية ومقايسة الـ 65 كم معاد القياس (9 فئات رئيسية)
            </h3>
            <p class="text-xs text-slate-400 light:text-slate-500 mt-0.5">مقارنة القيمة التعاقدية والأوزان النسبية والمنفذ المعتمد والمنصرف بالمستخلصات لكل فئة</p>
          </div>
          <span class="text-xs font-bold bg-slate-800 light:bg-slate-100 text-slate-200 light:text-slate-800 px-3 py-1 rounded-xl self-start sm:self-auto border border-slate-700 light:border-slate-300">
            إجمالي المقايسة: 2,359,723,935.81 ج.م (74 بند)
          </span>
        </div>

        <div class="overflow-x-auto table-responsive rounded-xl border border-slate-800 light:border-slate-200">
          <table class="w-full text-right text-xs">
            <thead class="bg-slate-900/90 light:bg-slate-100 text-slate-300 light:text-slate-800 font-bold border-b border-slate-800 light:border-slate-200">
              <tr>
                <th class="p-2.5 text-center">م</th>
                <th class="p-2.5">الفئة الرئيسية للعمل</th>
                <th class="p-2.5 text-center">عدد البنود</th>
                <th class="p-2.5 text-left">قيمة المقايسة (ج.م)</th>
                <th class="p-2.5 text-center">الوزن النسبي %</th>
                <th class="p-2.5 text-left">المنفذ المعتمد Approved</th>
                <th class="p-2.5 text-left">المنصرف Billed</th>
                <th class="p-2.5 text-left">المتبقي (ج.م)</th>
                <th class="p-2.5 text-center">نسبة الإنجاز للفئة %</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-800/60 light:divide-slate-200 font-medium text-slate-200 light:text-slate-700" id="categoriesTableBody">
              <!-- Rendered via JS -->
            </tbody>
          </table>
        </div>
      </div>

      <!-- Detailed 74 Items Table with Live Filter & Search (Avoid break) -->
      <div class="glass-card rounded-2xl p-4 sm:p-5 space-y-3 ">
        <div class="flex flex-col lg:flex-row lg:items-center justify-between gap-3 border-b border-slate-800 light:border-slate-200 pb-3">
          <div>
            <h3 class="text-sm sm:text-base font-extrabold text-white light:text-slate-900 flex items-center gap-2">
              <i class="fa-solid fa-list text-brand-400"></i>
              جدول حصر بنود المقايسة التفصيلي (74 بنداً)
            </h3>
            <p class="text-xs text-slate-400 light:text-slate-500 mt-0.5">البحث والفلترة الفورية ومطابقة الكميات والأسعار والقيم مع شيت مقايسة الأعمال وشيت PROGRESS</p>
          </div>

          <!-- Search & Filter Controls (no-print) -->
          <div class="flex flex-wrap items-center gap-2.5 no-print">
            <div class="relative min-w-[220px]">
              <i class="fa-solid fa-search absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 text-xs"></i>
              <input type="text" id="itemSearchInput" placeholder="بحث بكود أو وصف البند..." class="w-full bg-slate-900 dark:bg-slate-900 light:bg-slate-100 border border-slate-700 dark:border-slate-700 light:border-slate-300 rounded-xl pr-8 pl-3 py-1.5 text-xs text-white light:text-slate-900 placeholder-slate-500 focus:outline-none focus:border-brand-500 transition">
            </div>

            <select id="categoryFilterSelect" class="bg-slate-900 dark:bg-slate-900 light:bg-slate-100 border border-slate-700 dark:border-slate-700 light:border-slate-300 rounded-xl px-3 py-1.5 text-xs text-slate-200 light:text-slate-800 focus:outline-none focus:border-brand-500 transition">
              <option value="ALL">جميع الفئات الرئيسية (9 فئات)</option>
            </select>
          </div>
        </div>

        <!-- Filter Metrics Bar -->
        <div class="flex flex-wrap items-center justify-between bg-slate-900/60 dark:bg-slate-900/60 light:bg-slate-100 p-2.5 rounded-xl border border-slate-800 dark:border-slate-800 light:border-slate-200 text-xs text-slate-400 light:text-slate-600 gap-2">
          <div>البنود المعروضة: <span class="font-bold text-white light:text-slate-900" id="filteredItemsCount">74</span> بند</div>
          <div>إجمالي المقايسة المحددة: <span class="font-bold text-brand-400 light:text-brand-700" id="filteredBoqVal">0.00</span> ج.م</div>
          <div>إجمالي المنفذ المعتمد: <span class="font-bold text-emerald-400 light:text-emerald-700" id="filteredAppVal">0.00</span> ج.م</div>
          <div>متوسط نسبة الإنجاز: <span class="font-bold text-purple-400 light:text-purple-700" id="filteredProgPct">0.00%</span></div>
        </div>

        <!-- Items Table -->
        <div class="overflow-x-auto table-responsive max-h-[600px] rounded-xl border border-slate-800 light:border-slate-200">
          <table class="w-full text-right text-xs">
            <thead class="bg-slate-900 dark:bg-slate-900 light:bg-slate-100 text-slate-300 light:text-slate-800 font-bold sticky top-0 z-10 shadow-sm border-b border-slate-800 light:border-slate-200">
              <tr>
                <th class="p-2.5 w-10 text-center">م</th>
                <th class="p-2.5 w-20">كود البند</th>
                <th class="p-2.5">بيان الأعمال (الوصف)</th>
                <th class="p-2.5 w-32">الفئة الرئيسية</th>
                <th class="p-2.5 w-12 text-center">الوحدة</th>
                <th class="p-2.5 text-left">الفئة التعاقدية</th>
                <th class="p-2.5 text-left">كمية المقايسة</th>
                <th class="p-2.5 text-left">قيمة المقايسة</th>
                <th class="p-2.5 text-left">الكمية المنفذة</th>
                <th class="p-2.5 text-left">القيمة المنفذة</th>
                <th class="p-2.5 text-center w-24">نسبة الإنجاز</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-800/60 light:divide-slate-200 font-medium text-slate-200 light:text-slate-700" id="boqItemsTableBody">
              <!-- Rendered via JS -->
            </tbody>
          </table>
        </div>
      </div>

    </section>

    <!-- ======================================================================= -->
    <!-- TAB 4: المستخلصات الجارية وفروق الأسعار والتعويضات                      -->
    <!-- ======================================================================= -->
    <section id="tabPayApps" class="tab-content hidden space-y-6">
      
      <!-- Pay Apps Summary Table -->
      <div class="glass-card rounded-2xl p-4 sm:p-5 space-y-3">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 light:border-slate-200 pb-3">
          <div>
            <h3 class="text-sm sm:text-base font-extrabold text-white light:text-slate-900 flex items-center gap-2">
              <i class="fa-solid fa-file-invoice-dollar text-purple-400"></i>
              بيان المستخلصات الجارية (Pay App-01 حتى Pay App-16) وفروق الأسعار وصافي التعويضات
            </h3>
            <p class="text-xs text-slate-400 light:text-slate-500 mt-0.5">تطبيق قاعدة مقارنة إجمالي تعويضات المستخلص مع إجمالي فروق أسعاره (=IF(Comp > PV, Comp - PV, 0))</p>
          </div>
          <span class="text-xs font-bold bg-slate-800 light:bg-slate-100 text-slate-200 light:text-slate-800 px-3 py-1 rounded-xl self-start sm:self-auto border border-slate-700 light:border-slate-300">
            16 مستخلص جاري
          </span>
        </div>

        <div class="overflow-x-auto table-responsive rounded-xl border border-slate-800 light:border-slate-200">
          <table class="w-full text-right text-xs">
            <thead class="bg-slate-900/90 light:bg-slate-100 text-slate-300 light:text-slate-800 font-bold border-b border-slate-800 light:border-slate-200">
              <tr>
                <th class="p-2.5">المستخلص</th>
                <th class="p-2.5 text-left">أعمال العقد المنفذة</th>
                <th class="p-2.5 text-left">فروق الأسعار للمستخلص</th>
                <th class="p-2.5 text-left">إجمالي التعويضات</th>
                <th class="p-2.5 text-left text-teal-400 light:text-teal-700">صافي التعويضات المقارن</th>
                <th class="p-2.5 text-left text-emerald-400 light:text-emerald-700">إجمالي المنفذ للمستخلص</th>
                <th class="p-2.5 text-left">العقد المعتمد Billed</th>
                <th class="p-2.5 text-left">فروق الأسعار Billed</th>
                <th class="p-2.5 text-left">صافي التعويضات Billed</th>
                <th class="p-2.5 text-center">حالة الاعتماد</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-800/60 light:divide-slate-200 font-medium text-slate-200 light:text-slate-700" id="payAppsTableBody">
              <!-- Rendered via JS -->
            </tbody>
          </table>
        </div>
      </div>

      <!-- Monthly Trend Line Chart (Avoid break) -->
      <div class="glass-card rounded-2xl p-4 sm:p-5 space-y-3 avoid-break">
        <div class="flex items-center justify-between border-b border-slate-800 light:border-slate-200 pb-2.5">
          <h3 class="text-sm font-extrabold text-white light:text-slate-900 flex items-center gap-2">
            <i class="fa-solid fa-chart-area text-brand-400"></i>
            منحنى تطور الأعمال المنفذة شهرياً (أسعار التعاقد + فروق الأسعار + التعويضات)
          </h3>
          <span class="text-xs text-slate-400">ملايين الجنيهات</span>
        </div>
        <div class="h-64 sm:h-72 w-full">
          <canvas id="monthlyTrendChart"></canvas>
        </div>
      </div>

    </section>

  </main>

  <!-- ========================================================================= -->
  <!-- A3 PRINT FIXED FOOTER (Visible only during Print)                         -->
  <!-- ========================================================================= -->
  <div class="print-only print-footer">
    <div>مشروع أعمال تطوير ورفع كفاءة طريق الصعيد الصحراوي الغربي (ديروط - أسيوط 65 كم) | المقاول: شركة إيماك للمقاولات</div>
    <div id="printPageNum">صفحة 1 من 1</div>
  </div>

  <!-- ========================================================================= -->
  <!-- DESKTOP FOOTER                                                            -->
  <!-- ========================================================================= -->
  <footer class="bg-navy-900 dark:bg-navy-900 light:bg-slate-100 border-t border-slate-800 dark:border-slate-800 light:border-slate-200 py-3 mt-6 text-xs text-slate-400 light:text-slate-600 no-print">
    <div class="max-w-[1750px] mx-auto px-3 sm:px-6 lg:px-8 flex flex-col sm:flex-row items-center justify-between gap-2">
      <div class="flex items-center gap-2">
        <span class="font-bold text-slate-200 light:text-slate-800">مشروع ديروط - أسيوط (65 كم)</span>
        <span>•</span>
        <span>الهيئة العامة للطرق والكباري</span>
        <span>•</span>
        <span>شركة إيماك للمقاولات</span>
      </div>
      <div>
        <span>البريد الإداري: <a href="mailto:MOHAMEDABORIZK@GMAIL.COM" class="text-brand-400 hover:underline">MOHAMEDABORIZK@GMAIL.COM</a></span>
      </div>
    </div>
  </footer>

  <!-- ========================================================================= -->
  <!-- LOGIN OVERLAY & MODAL                                                     -->
  <!-- ========================================================================= -->
  <div id="loginOverlay" class="fixed inset-0 z-50 bg-slate-950/90 backdrop-blur-md flex items-center justify-center p-4">
    <div class="bg-navy-900 dark:bg-navy-900 light:bg-white border border-slate-800 dark:border-slate-800 light:border-slate-200 rounded-3xl max-w-md w-full p-6 sm:p-8 shadow-2xl relative text-right">
      
      <!-- Brand Header -->
      <div class="text-center mb-6">
        <div class="w-16 h-16 rounded-2xl bg-gradient-to-tr from-brand-600 to-indigo-600 flex items-center justify-center mx-auto mb-3 shadow-lg shadow-brand-500/20 border border-white/10">
          <i class="fa-solid fa-road text-3xl text-white"></i>
        </div>
        <h2 class="text-lg sm:text-xl font-black text-white light:text-slate-900">تسجيل الدخول للنظام</h2>
        <p class="text-xs text-slate-400 light:text-slate-500 mt-1">مشروع ديروط - أسيوط 65 كم (لوحة المتابعة التنفيذية)</p>
      </div>

      <!-- Login Form -->
      <form onsubmit="handleLogin(event)" class="space-y-4 text-xs">
        <div>
          <label class="block text-slate-300 light:text-slate-700 font-bold mb-1">البريد الإلكتروني المسجل:</label>
          <div class="relative">
            <i class="fa-solid fa-envelope absolute right-3.5 top-1/2 -translate-y-1/2 text-slate-500"></i>
            <input type="email" id="loginEmail" required placeholder="name@domain.com" class="w-full bg-slate-950 dark:bg-slate-950 light:bg-slate-50 border border-slate-700 dark:border-slate-700 light:border-slate-300 rounded-xl pr-10 pl-4 py-2.5 text-white light:text-slate-900 placeholder-slate-500 focus:outline-none focus:border-brand-500 transition font-mono">
          </div>
        </div>

        <div>
          <label class="block text-slate-300 light:text-slate-700 font-bold mb-1">الرقم السري (كلمة المرور):</label>
          <div class="relative">
            <i class="fa-solid fa-lock absolute right-3.5 top-1/2 -translate-y-1/2 text-slate-500"></i>
            <input type="password" id="loginPassword" required placeholder="••••••••" class="w-full bg-slate-950 dark:bg-slate-950 light:bg-slate-50 border border-slate-700 dark:border-slate-700 light:border-slate-300 rounded-xl pr-10 pl-4 py-2.5 text-white light:text-slate-900 placeholder-slate-500 focus:outline-none focus:border-brand-500 transition font-mono">
          </div>
        </div>

        <div class="flex items-center justify-between text-slate-400 light:text-slate-600 text-[11px] pt-1">
          <label class="flex items-center gap-1.5 cursor-pointer">
            <input type="checkbox" id="rememberMeCheck" checked class="rounded border-slate-700 text-brand-600 focus:ring-0">
            <span>تذكر تسجيل الدخول على هذا الجهاز</span>
          </label>
        </div>

        <div id="loginErrorMsg" class="hidden p-2.5 rounded-xl bg-rose-500/15 border border-rose-500/30 text-rose-400 text-center font-bold text-[11px]">
          البريد الإلكتروني أو الرقم السري غير صحيح
        </div>

        <button type="submit" class="w-full py-3 rounded-xl bg-gradient-to-r from-brand-600 to-indigo-600 hover:from-brand-500 hover:to-indigo-500 text-white font-extrabold text-sm shadow-lg shadow-brand-600/30 transition flex items-center justify-center gap-2">
          <i class="fa-solid fa-right-to-bracket"></i>
          <span>دخول لوحة المتابعة</span>
        </button>
      </form>

      <!-- Quick Login Shortcuts for Registered Leaders -->
      <div class="mt-5 pt-3 border-t border-slate-800 dark:border-slate-800 light:border-slate-200">
        <div class="text-[11px] text-slate-400 light:text-slate-600 text-center mb-2.5 font-bold flex items-center justify-center gap-1.5">
          <i class="fa-solid fa-bolt text-amber-400"></i>
          <span>حسابات الدخول السريع المعتمدة (اضغط للدخول المباشر):</span>
        </div>
        <div class="grid grid-cols-2 gap-2 text-[10.5px]">
          
          <!-- 1. م. محمد أبو رزق -->
          <button type="button" onclick="fillDemoUser('MOHAMEDABORIZK@GMAIL.COM', 'admin')" class="p-2.5 rounded-xl bg-slate-800/80 dark:bg-slate-800/80 light:bg-slate-100 hover:bg-slate-700/80 border border-slate-700/60 dark:border-slate-700/60 light:border-slate-300 text-right transition flex flex-col justify-between">
            <div class="font-bold text-white light:text-slate-900">م. محمد أبو رزق</div>
            <div class="text-[9.5px] text-brand-400 font-semibold mt-0.5">مدير النظام (Admin)</div>
          </button>

          <!-- 2. م. سيد دسوقي -->
          <button type="button" onclick="fillDemoUser('sayed.desouky@kharafi-egypt.com', '123')" class="p-2.5 rounded-xl bg-slate-800/80 dark:bg-slate-800/80 light:bg-slate-100 hover:bg-slate-700/80 border border-slate-700/60 dark:border-slate-700/60 light:border-slate-300 text-right transition flex flex-col justify-between">
            <div class="font-bold text-white light:text-slate-900">م. سيد دسوقي</div>
            <div class="text-[9.5px] text-amber-400 font-semibold mt-0.5">رئيس مجلس الإدارة</div>
          </button>

          <!-- 3. م. محمد السيد -->
          <button type="button" onclick="fillDemoUser('mohamed.elsayed@kharafi-egypt.com', '123')" class="p-2.5 rounded-xl bg-slate-800/80 dark:bg-slate-800/80 light:bg-slate-100 hover:bg-slate-700/80 border border-slate-700/60 dark:border-slate-700/60 light:border-slate-300 text-right transition flex flex-col justify-between">
            <div class="font-bold text-white light:text-slate-900">م. محمد السيد</div>
            <div class="text-[9.5px] text-emerald-400 font-semibold mt-0.5">مدير الشئون الفنية</div>
          </button>

          <!-- 4. م. حاتم فريد -->
          <button type="button" onclick="fillDemoUser('hatem.farid@kharafi-egypt.com', '123')" class="p-2.5 rounded-xl bg-slate-800/80 dark:bg-slate-800/80 light:bg-slate-100 hover:bg-slate-700/80 border border-slate-700/60 dark:border-slate-700/60 light:border-slate-300 text-right transition flex flex-col justify-between">
            <div class="font-bold text-white light:text-slate-900">م. حاتم فريد</div>
            <div class="text-[9.5px] text-sky-400 font-semibold mt-0.5">مدير المشروعات</div>
          </button>

          <!-- 5. م. وليد مسلم -->
          <button type="button" onclick="fillDemoUser('waleed.musallam@kharafi-egypt.com', '123')" class="col-span-2 p-2.5 rounded-xl bg-slate-800/80 dark:bg-slate-800/80 light:bg-slate-100 hover:bg-slate-700/80 border border-slate-700/60 dark:border-slate-700/60 light:border-slate-300 text-right transition flex items-center justify-between">
            <div>
              <div class="font-bold text-white light:text-slate-900">م. وليد مسلم</div>
              <div class="text-[9.5px] text-teal-400 font-semibold mt-0.5">مدير المشروع</div>
            </div>
            <span class="text-[10px] bg-teal-500/10 text-teal-300 light:text-teal-700 px-2.5 py-1 rounded-lg border border-teal-500/20 font-bold">دخول مباشر</span>
          </button>

        </div>
      </div>

    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- USER ACCESS CONTROL MANAGEMENT MODAL (Admin Only)                         -->
  <!-- ========================================================================= -->
  <div id="userManageModal" class="fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-sm hidden items-center justify-center p-4">
    <div class="bg-navy-900 dark:bg-navy-900 light:bg-white border border-slate-800 dark:border-slate-800 light:border-slate-200 rounded-3xl max-w-2xl w-full p-6 shadow-2xl relative text-right">
      <div class="flex items-center justify-between border-b border-slate-800 light:border-slate-200 pb-3 mb-4">
        <h3 class="text-base font-black text-white light:text-slate-900 flex items-center gap-2">
          <i class="fa-solid fa-users-gear text-purple-400"></i>
          إدارة الصلاحيات والمستخدمين المصرح لهم
        </h3>
        <button onclick="closeUserManageModal()" class="text-slate-400 hover:text-white p-1 text-base">
          <i class="fa-solid fa-xmark"></i>
        </button>
      </div>

      <!-- Add New User Form -->
      <form onsubmit="handleAddNewUser(event)" class="bg-slate-950/60 light:bg-slate-50 p-3 rounded-2xl border border-slate-800 light:border-slate-200 mb-4 grid grid-cols-1 sm:grid-cols-4 gap-2 text-xs">
        <div>
          <label class="block text-slate-400 font-bold mb-1">الاسم:</label>
          <input type="text" id="newUserName" required placeholder="اسم المستخدم" class="w-full bg-slate-900 light:bg-white border border-slate-700 light:border-slate-300 rounded-lg px-2.5 py-1.5 text-white light:text-slate-900 text-xs">
        </div>
        <div>
          <label class="block text-slate-400 font-bold mb-1">البريد الإلكتروني:</label>
          <input type="email" id="newUserEmail" required placeholder="email@domain.com" class="w-full bg-slate-900 light:bg-white border border-slate-700 light:border-slate-300 rounded-lg px-2.5 py-1.5 text-white light:text-slate-900 font-mono text-xs">
        </div>
        <div>
          <label class="block text-slate-400 font-bold mb-1">الرقم السري:</label>
          <input type="text" id="newUserPass" required placeholder="رقم سري" class="w-full bg-slate-900 light:bg-white border border-slate-700 light:border-slate-300 rounded-lg px-2.5 py-1.5 text-white light:text-slate-900 font-mono text-xs">
        </div>
        <div class="flex items-end">
          <button type="submit" class="w-full py-1.5 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded-lg transition">
            <i class="fa-solid fa-user-plus ml-1"></i> إضافة مستخدم
          </button>
        </div>
      </form>

      <!-- Current Users List -->
      <div class="overflow-x-auto max-h-[300px] rounded-xl border border-slate-800 light:border-slate-200">
        <table class="w-full text-right text-xs">
          <thead class="bg-slate-950 light:bg-slate-100 text-slate-400 light:text-slate-700 font-bold">
            <tr>
              <th class="p-2.5">الاسم</th>
              <th class="p-2.5">البريد الإلكتروني</th>
              <th class="p-2.5">الرقم السري</th>
              <th class="p-2.5">الدور</th>
              <th class="p-2.5 text-center">إجراءات</th>
            </tr>
          </thead>
          <tbody id="usersListTableBody" class="divide-y divide-slate-800/60 light:divide-slate-200 text-slate-200 light:text-slate-800">
            <!-- Rendered via JS -->
          </tbody>
        </table>
      </div>

      <div class="mt-4 text-left">
        <button onclick="closeUserManageModal()" class="px-4 py-1.5 bg-slate-800 light:bg-slate-200 text-slate-200 light:text-slate-800 rounded-xl text-xs font-bold">إغلاق</button>
      </div>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- JAVASCRIPT APPLICATION CORE                                               -->
  <!-- ========================================================================= -->
  <script>
    // Embedded Data fallback ensures 100% functionality offline, locally, or on Vercel
    const EMBEDDED_DATA = {json_str};
    let projectData = EMBEDDED_DATA;
    let currentUser = null;
    let currentTabId = 'tabOverview';
    let currentTabTitle = 'الموقف التنفيذي والبيانات الأساسية للمشروع';

    // Formatters
    const formatMoney = (val) => {{
      if (val === undefined || val === null || isNaN(val)) return '0.00';
      return Number(val).toLocaleString('en-US', {{ minimumFractionDigits: 2, maximumFractionDigits: 2 }});
    }};

    const formatPct = (val) => {{
      if (val === undefined || val === null || isNaN(val)) return '0.00%';
      return (Number(val) * 100).toFixed(2) + '%';
    }};

    // =========================================================================
    // THEME MANAGEMENT (Day / Night Mode)
    // =========================================================================
    function initTheme() {{
      const savedTheme = localStorage.getItem('app_theme') || 'dark';
      applyTheme(savedTheme);
    }}

    function toggleTheme() {{
      const isDark = document.documentElement.classList.contains('dark');
      applyTheme(isDark ? 'light' : 'dark');
    }}

    function applyTheme(theme) {{
      const html = document.documentElement;
      const sunIcon = document.getElementById('themeSunIcon');
      const moonIcon = document.getElementById('themeMoonIcon');

      if (theme === 'light') {{
        html.classList.remove('dark');
        html.classList.add('light');
        localStorage.setItem('app_theme', 'light');
        if (sunIcon) sunIcon.classList.remove('hidden');
        if (moonIcon) moonIcon.classList.add('hidden');
      }} else {{
        html.classList.remove('light');
        html.classList.add('dark');
        localStorage.setItem('app_theme', 'dark');
        if (sunIcon) sunIcon.classList.add('hidden');
        if (moonIcon) moonIcon.classList.remove('hidden');
      }}

      // Update Chart.js color schemes dynamically if charts are initialized
      updateChartColors(theme);
    }}

    function updateChartColors(theme) {{
      const isDark = (theme === 'dark');
      const textColor = isDark ? '#94a3b8' : '#334155';
      const gridColor = isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)';

      if (window.donutChartInstance) {{
        window.donutChartInstance.options.plugins.legend.labels.color = textColor;
        window.donutChartInstance.update();
      }}
      if (window.trendChartInstance) {{
        window.trendChartInstance.options.scales.x.ticks.color = textColor;
        window.trendChartInstance.options.scales.y.ticks.color = textColor;
        window.trendChartInstance.options.scales.x.grid.color = gridColor;
        window.trendChartInstance.options.scales.y.grid.color = gridColor;
        window.trendChartInstance.options.plugins.legend.labels.color = textColor;
        window.trendChartInstance.update();
      }}
    }}

    // =========================================================================
    // AUTHENTICATION & ACCESS CONTROL
    // =========================================================================
    function initAuth() {{
      // Synchronize latest authorized users from projectData into localStorage
      const defaultUsers = projectData.authorized_users || [];
      let localUsers = [];
      try {{
        localUsers = JSON.parse(localStorage.getItem('registered_users') || '[]');
      }} catch(e) {{
        localUsers = [];
      }}

      defaultUsers.forEach(defU => {{
        const idx = localUsers.findIndex(u => u.email.toLowerCase() === defU.email.toLowerCase());
        if (idx === -1) {{
          localUsers.push(defU);
        }} else {{
          localUsers[idx].password = defU.password;
          localUsers[idx].name = defU.name;
          localUsers[idx].role = defU.role;
        }}
      }});

      localStorage.setItem('registered_users', JSON.stringify(localUsers));

      // Check session / remember me
      const savedUser = localStorage.getItem('logged_in_user') || sessionStorage.getItem('logged_in_user');
      if (savedUser) {{
        currentUser = JSON.parse(savedUser);
        onUserAuthenticated(currentUser);
      }} else {{
        showLoginOverlay();
      }}
    }}

    function showLoginOverlay() {{
      const overlay = document.getElementById('loginOverlay');
      if (overlay) overlay.classList.remove('hidden');
    }}

    function hideLoginOverlay() {{
      const overlay = document.getElementById('loginOverlay');
      if (overlay) overlay.classList.add('hidden');
    }}

    function handleLogin(event) {{
      event.preventDefault();
      const email = (document.getElementById('loginEmail').value || '').trim().toLowerCase();
      const pass = (document.getElementById('loginPassword').value || '').trim();
      const remember = document.getElementById('rememberMeCheck').checked;
      const errorMsg = document.getElementById('loginErrorMsg');

      const users = JSON.parse(localStorage.getItem('registered_users') || '[]');
      const user = users.find(u => u.email.toLowerCase() === email && u.password === pass);

      if (user) {{
        currentUser = user;
        if (remember) {{
          localStorage.setItem('logged_in_user', JSON.stringify(user));
        }} else {{
          sessionStorage.setItem('logged_in_user', JSON.stringify(user));
        }}
        if (errorMsg) errorMsg.classList.add('hidden');
        hideLoginOverlay();
        onUserAuthenticated(user);
      }} else {{
        if (errorMsg) errorMsg.classList.remove('hidden');
      }}
    }}

    function fillDemoUser(email, pass) {{
      const emailInput = document.getElementById('loginEmail');
      const passInput = document.getElementById('loginPassword');
      if (emailInput && passInput) {{
        emailInput.value = email;
        passInput.value = pass;
        handleLogin(new Event('submit'));
      }}
    }}

    function onUserAuthenticated(user) {{
      hideLoginOverlay();
      const badge = document.getElementById('userProfileBadge');
      const nameEl = document.getElementById('currentUserName');
      const roleEl = document.getElementById('currentUserRole');
      const manageBtn = document.getElementById('userManageBtn');

      if (badge && nameEl && roleEl) {{
        badge.classList.remove('hidden');
        badge.classList.add('flex');
        nameEl.textContent = user.name || user.email;
        roleEl.textContent = user.role || 'مستخدم مصرح له';
      }}

      // Show user management button only for Admin
      if (manageBtn) {{
        if (user.email.toLowerCase() === 'mohamedaborizk@gmail.com') {{
          manageBtn.classList.remove('hidden');
          manageBtn.classList.add('flex');
        }} else {{
          manageBtn.classList.add('hidden');
          manageBtn.classList.remove('flex');
        }}
      }}

      renderApp();
    }}

    function logout() {{
      localStorage.removeItem('logged_in_user');
      sessionStorage.removeItem('logged_in_user');
      currentUser = null;
      document.getElementById('userProfileBadge').classList.add('hidden');
      document.getElementById('userProfileBadge').classList.remove('flex');
      document.getElementById('userManageBtn').classList.add('hidden');
      showLoginOverlay();
    }}

    // User Management Modal functions
    function openUserManageModal() {{
      renderUsersTable();
      document.getElementById('userManageModal').classList.remove('hidden');
      document.getElementById('userManageModal').classList.add('flex');
    }}

    function closeUserManageModal() {{
      document.getElementById('userManageModal').classList.add('hidden');
      document.getElementById('userManageModal').classList.remove('flex');
    }}

    function renderUsersTable() {{
      const users = JSON.parse(localStorage.getItem('registered_users') || '[]');
      const tbody = document.getElementById('usersListTableBody');
      tbody.innerHTML = '';
      users.forEach((u, idx) => {{
        tbody.innerHTML += `
          <tr class="hover:bg-slate-900/40">
            <td class="p-2.5 font-bold">${{u.name}}</td>
            <td class="p-2.5 font-mono">${{u.email}}</td>
            <td class="p-2.5 font-mono text-slate-400">••••••</td>
            <td class="p-2.5">${{u.role}}</td>
            <td class="p-2.5 text-center">
              ${{u.email.toLowerCase() !== 'mohamedaborizk@gmail.com' ? `
                <button onclick="deleteUser('${{u.email}}')" class="text-rose-400 hover:text-rose-300 p-1" title="حذف المستخدم">
                  <i class="fa-solid fa-trash-can"></i>
                </button>
              ` : '<span class="text-[10px] text-slate-500">رئيسي</span>'}}
            </td>
          </tr>
        `;
      }});
    }}

    function handleAddNewUser(e) {{
      e.preventDefault();
      const name = document.getElementById('newUserName').value.trim();
      const email = document.getElementById('newUserEmail').value.trim();
      const pass = document.getElementById('newUserPass').value.trim();

      const users = JSON.parse(localStorage.getItem('registered_users') || '[]');
      if (users.some(u => u.email.toLowerCase() === email.toLowerCase())) {{
        alert('هذا البريد الإلكتروني مسجل بالفعل!');
        return;
      }}

      users.push({{
        email: email,
        password: pass,
        name: name,
        role: 'مستخدم مصرح له'
      }});

      localStorage.setItem('registered_users', JSON.stringify(users));
      document.getElementById('newUserName').value = '';
      document.getElementById('newUserEmail').value = '';
      document.getElementById('newUserPass').value = '';
      renderUsersTable();
    }}

    function deleteUser(email) {{
      if (!confirm('هل أنت متأكد من حذف هذا المستخدم؟')) return;
      let users = JSON.parse(localStorage.getItem('registered_users') || '[]');
      users = users.filter(u => u.email.toLowerCase() !== email.toLowerCase());
      localStorage.setItem('registered_users', JSON.stringify(users));
      renderUsersTable();
    }}

    // =========================================================================
    // A3 LANDSCAPE PRINT CONTROLLER
    // =========================================================================
    function triggerA3Print() {{
      // Update print header info
      const now = new Date();
      const dateStr = now.toLocaleDateString('ar-EG', {{ year: 'numeric', month: '2-digit', day: '2-digit' }}) + ' ' + now.toLocaleTimeString('ar-EG', {{ hour: '2-digit', minute: '2-digit' }});
      const titleEl = document.getElementById('printActiveTabTitle');
      const timeEl = document.getElementById('printTimestamp');

      if (titleEl) titleEl.textContent = currentTabTitle;
      if (timeEl) timeEl.textContent = 'تاريخ وساعة الطباعة: ' + dateStr;

      // Launch Native Print Dialog
      window.print();
    }}

    // =========================================================================
    // TAB SWITCHING CONTROLLER
    // =========================================================================
    function switchTab(tabId, tabTitle) {{
      currentTabId = tabId;
      if (tabTitle) currentTabTitle = tabTitle;

      // Desktop Tab Buttons
      document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
      document.querySelectorAll('.tab-btn').forEach(btn => {{
        btn.classList.remove('active', 'bg-brand-600', 'text-white', 'shadow-md', 'shadow-brand-600/20');
        btn.classList.add('text-slate-300');
      }});

      // Mobile Bottom Nav Buttons
      document.querySelectorAll('.mobile-nav-btn').forEach(btn => {{
        btn.classList.remove('active', 'text-brand-400');
        btn.classList.add('text-slate-400');
      }});

      const targetSection = document.getElementById(tabId);
      if (targetSection) targetSection.classList.remove('hidden');

      const targetDesktopBtn = document.querySelector(`.tab-btn[data-target="${{tabId}}"]`);
      if (targetDesktopBtn) {{
        targetDesktopBtn.classList.add('active', 'bg-brand-600', 'text-white', 'shadow-md', 'shadow-brand-600/20');
        targetDesktopBtn.classList.remove('text-slate-300');
      }}

      const targetMobileBtn = document.querySelector(`.mobile-nav-btn[data-target="${{tabId}}"]`);
      if (targetMobileBtn) {{
        targetMobileBtn.classList.add('active', 'text-brand-400');
        targetMobileBtn.classList.remove('text-slate-400');
      }}

      // Redraw charts
      if (tabId === 'tabOverview' && window.donutChartInstance) {{
        window.donutChartInstance.resize();
      }}
      if (tabId === 'tabPayApps' && window.trendChartInstance) {{
        window.trendChartInstance.resize();
      }}

      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    // =========================================================================
    // DATA RENDERING (DOM BINDING)
    // =========================================================================
    function renderApp() {{
      const d = projectData;
      const fin = d.financial_status;

      // 1. KPIs
      document.getElementById('kpiAwardVal').innerHTML = `${{(fin.award_value / 1e6).toFixed(2)}} <span class="text-xs font-normal text-slate-400">م.ج</span>`;
      document.getElementById('kpiBoqVal').innerHTML = `${{(fin.boq_value / 1e6).toFixed(2)}} <span class="text-xs font-normal text-slate-400">م.ج</span>`;
      document.getElementById('kpiBoqPct').textContent = formatPct(fin.boq_value / fin.award_value);

      document.getElementById('kpiAppContract').innerHTML = `${{(fin.app_contract / 1e6).toFixed(2)}} <span class="text-xs font-normal text-slate-400">م.ج</span>`;
      document.getElementById('kpiAppContractPct').textContent = formatPct(fin.app_contract / fin.boq_value);

      document.getElementById('kpiAppPv').innerHTML = `${{(fin.app_pv / 1e6).toFixed(2)}} <span class="text-xs font-normal text-slate-400">م.ج</span>`;
      document.getElementById('kpiAppPvPct').textContent = formatPct(fin.app_pv / fin.boq_value);

      document.getElementById('kpiAppComp').innerHTML = `${{(fin.app_net_comp / 1e6).toFixed(2)}} <span class="text-xs font-normal text-slate-400">م.ج</span>`;
      document.getElementById('kpiAppCompPct').textContent = formatPct(fin.app_net_comp / fin.boq_value);

      document.getElementById('kpiAppTotal').innerHTML = `${{(fin.app_total / 1e6).toFixed(2)}} <span class="text-xs font-normal text-slate-400">م.ج</span>`;
      document.getElementById('kpiAppTotalPct').textContent = formatPct(fin.app_total / fin.boq_value);

      // Billing stats
      document.getElementById('statBilledTotal').textContent = formatMoney(fin.billed_total);
      document.getElementById('statBilledContract').textContent = (fin.billed_contract / 1e6).toFixed(2) + ' م.ج';
      document.getElementById('statBilledPv').textContent = (fin.billed_pv / 1e6).toFixed(2) + ' م.ج';
      document.getElementById('statBilledComp').textContent = (fin.billed_net_comp / 1e6).toFixed(2) + ' م.ج';

      document.getElementById('statRemainingTotal').textContent = formatMoney(fin.rem_total);
      document.getElementById('statRemainingContract').textContent = (fin.rem_contract / 1e6).toFixed(2) + ' م.ج';
      document.getElementById('statRemainingPv').textContent = (fin.rem_pv / 1e6).toFixed(2) + ' م.ج';
      document.getElementById('statRemainingComp').textContent = (fin.rem_net_comp / 1e6).toFixed(2) + ' م.ج';

      // Quick header stats
      document.getElementById('quickBoqVal').textContent = (fin.boq_value / 1e6).toFixed(2) + ' م.ج';
      document.getElementById('quickApprovedVal').textContent = (fin.app_total / 1e6).toFixed(2) + ' م.ج';
      document.getElementById('quickBilledVal').textContent = (fin.billed_total / 1e6).toFixed(2) + ' م.ج';
      document.getElementById('quickRemainingVal').textContent = (fin.rem_total / 1e6).toFixed(2) + ' م.ج';

      // 2. Extensions List
      const extContainer = document.getElementById('extensionsContainer');
      extContainer.innerHTML = '';
      d.extensions.forEach(ext => {{
        const isApproved = ext.status.includes('موافقة') || ext.status.includes('معتمدة');
        const badgeClass = isApproved ? 'bg-emerald-500/10 text-emerald-400 border-emerald-500/30' : 'bg-rose-500/10 text-rose-400 border-rose-500/30';
        extContainer.innerHTML += `
          <div class="p-2 sm:p-2.5 rounded-xl bg-slate-900/60 light:bg-slate-50 border border-slate-800 light:border-slate-200">
            <div class="flex justify-between items-center mb-1">
              <span class="font-bold text-slate-200 light:text-slate-800">تمديد رقم (${{ext.no}})</span>
              <span class="px-2 py-0.5 rounded text-[10px] font-bold border ${{badgeClass}}">${{ext.status}}</span>
            </div>
            <div class="flex justify-between items-center text-[10px] sm:text-[11px] text-slate-400 light:text-slate-500">
              <span>المدة: <strong class="text-white light:text-slate-900">${{ext.months}} شهر</strong></span>
              <span>${{ext.ref_letters || ''}}</span>
            </div>
            <div class="text-[10px] sm:text-[11px] text-slate-300 light:text-slate-700 mt-1 leading-snug">${{ext.reasons}}</div>
          </div>
        `;
      }});

      // 3. Engineering Components Table
      const compBody = document.getElementById('componentsTableBody');
      compBody.innerHTML = '';
      d.engineering_components.forEach(comp => {{
        compBody.innerHTML += `
          <tr class="hover:bg-slate-900/40 light:hover:bg-slate-50 transition">
            <td class="p-2.5 sm:p-3 font-bold text-white light:text-slate-900">${{comp.category}}</td>
            <td class="p-2.5 sm:p-3 text-slate-300 light:text-slate-700">${{comp.type}}</td>
            <td class="p-2.5 sm:p-3 text-emerald-300 light:text-emerald-700 font-bold">${{comp.inside_contract}}</td>
            <td class="p-2.5 sm:p-3 text-amber-300 light:text-amber-700">${{comp.outside_contract}}</td>
            <td class="p-2.5 sm:p-3 font-bold text-white light:text-slate-900">${{comp.total_length}}</td>
            <td class="p-2.5 sm:p-3 text-slate-400 light:text-slate-500">${{comp.notes}}</td>
          </tr>
        `;
      }});

      // 4. Financial Status Table
      const finBody = document.getElementById('financialTableBody');
      const finRows = [
        {{ m: '1', title: 'قيمة التعاقد طبقاً لأمر الإسناد', val: fin.award_value, pctAward: 1.0, pctBoq: fin.award_value / fin.boq_value, ref: 'أمر الإسناد الأصلي' }},
        {{ m: '2', title: 'قيمة التعاقد طبقاً للحصر الفعلي (65 كم معاد القياس)', val: fin.boq_value, pctAward: fin.boq_value / fin.award_value, pctBoq: 1.0, ref: 'المقايسة المعتمدة (list!J1)' }},
        {{ m: '3', title: 'إجمالي قيمة الأعمال المنفذة بأسعار التعاقد (Approved Contract)', val: fin.app_contract, pctAward: fin.app_contract / fin.award_value, pctBoq: fin.app_contract / fin.boq_value, ref: 'المعتمد بشيت PROGRESS' }},
        {{ m: '4', title: 'إجمالي فروق الأسعار للأعمال المنفذة (Approved PV)', val: fin.app_pv, pctAward: fin.app_pv / fin.award_value, pctBoq: fin.app_pv / fin.boq_value, ref: 'المعتمد بشيت PROGRESS' }},
        {{ m: '5', title: 'صافي التعويضات للأعمال المنفذة (مقارنة كل مستخلص)', val: fin.app_net_comp, pctAward: fin.app_net_comp / fin.award_value, pctBoq: fin.app_net_comp / fin.boq_value, ref: 'مقارنة تعويضات وفروق المستخلص' }},
        {{ m: '6', title: 'إجمالي قيمة الأعمال المنفذة الشاملة (Approved Total)', val: fin.app_total, pctAward: fin.app_total / fin.award_value, pctBoq: fin.app_total / fin.boq_value, ref: 'أعمال العقد + فروق + صافي التعويضات', highlight: true }},
        {{ m: '7', title: 'إجمالي المستخلصات المعتمدة بأسعار التعاقد (Billed Contract)', val: fin.billed_contract, pctAward: fin.billed_contract / fin.award_value, pctBoq: fin.billed_contract / fin.boq_value, ref: 'مستخلصات 1..15 Locked' }},
        {{ m: '8', title: 'إجمالي مستخلصات فروق الأسعار المعتمدة (Billed PV)', val: fin.billed_pv, pctAward: fin.billed_pv / fin.award_value, pctBoq: fin.billed_pv / fin.boq_value, ref: 'مستخلصات فروق 1..14 Locked' }},
        {{ m: '9', title: 'صافي تعويضات المستخلصات المعتمدة (Billed Net Comp)', val: fin.billed_net_comp, pctAward: fin.billed_net_comp / fin.award_value, pctBoq: fin.billed_net_comp / fin.boq_value, ref: 'مستخلصات تعويضات 1..7 Locked' }},
        {{ m: '10', title: 'إجمالي المستخلصات المعتمدة الشاملة (Billed & Locked Total)', val: fin.billed_total, pctAward: fin.billed_total / fin.award_value, pctBoq: fin.billed_total / fin.boq_value, ref: 'مجموع ما تم اعتماده بالمستخلصات', highlight: true }},
        {{ m: '11', title: 'المستخلصات الجارية المستحقة والمتبقية بأسعار التعاقد', val: fin.rem_contract, pctAward: fin.rem_contract / fin.award_value, pctBoq: fin.rem_contract / fin.boq_value, ref: 'المنفذ المعتمد - المنصرف' }},
        {{ m: '12', title: 'مستخلصات فروق الأسعار المستحقة والمتبقية', val: fin.rem_pv, pctAward: fin.rem_pv / fin.award_value, pctBoq: fin.rem_pv / fin.boq_value, ref: 'فروق معتمدة - منصرف' }},
        {{ m: '13', title: 'صافي مستخلصات التعويضات المستحقة والمتبقية', val: fin.rem_net_comp, pctAward: fin.rem_net_comp / fin.award_value, pctBoq: fin.rem_net_comp / fin.boq_value, ref: 'تعويضات معتمدة - منصرف' }},
        {{ m: '14', title: 'إجمالي المستحقات المتبقية للمقاول عن الأعمال المنفذة', val: fin.rem_total, pctAward: fin.rem_total / fin.award_value, pctBoq: fin.rem_total / fin.boq_value, ref: 'إجمالي المستحق المتبقي', highlightAmber: true }}
      ];

      finBody.innerHTML = '';
      finRows.forEach(r => {{
        const rowClass = r.highlight ? 'bg-emerald-950/30 light:bg-emerald-50 font-bold text-emerald-300 light:text-emerald-900' : (r.highlightAmber ? 'bg-amber-950/30 light:bg-amber-50 font-bold text-amber-300 light:text-amber-900' : 'hover:bg-slate-900/40 light:hover:bg-slate-50');
        finBody.innerHTML += `
          <tr class="${{rowClass}}">
            <td class="p-2.5 text-center text-slate-400 font-bold">${{r.m}}</td>
            <td class="p-2.5 font-semibold">${{r.title}}</td>
            <td class="p-2.5 font-mono font-bold text-left">${{formatMoney(r.val)}}</td>
            <td class="p-2.5 font-mono text-center">${{formatPct(r.pctAward)}}</td>
            <td class="p-2.5 font-mono text-center">${{formatPct(r.pctBoq)}}</td>
            <td class="p-2.5 text-slate-400 light:text-slate-500 text-[11px]">${{r.ref}}</td>
          </tr>
        `;
      }});

      // 5. Handover Road Direction Cards
      const roadCards = document.getElementById('roadProgressCards');
      roadCards.innerHTML = '';
      d.handover_distances.forEach(item => {{
        const pct100 = (item.percentage * 100).toFixed(1);
        roadCards.innerHTML += `
          <div class="glass-card stat-card rounded-2xl p-4 flex flex-col justify-between">
            <div>
              <div class="flex justify-between items-center text-xs mb-1.5">
                <span class="font-bold text-white light:text-slate-900">${{item.name}}</span>
                <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-brand-500/10 text-brand-400 light:text-brand-700 border border-brand-500/20">${{pct100}}%</span>
              </div>
              <div class="text-[11px] text-slate-400 light:text-slate-500 mb-2">${{item.pave_type}}</div>
              <div class="space-y-1.5 my-2.5">
                <div class="w-full bg-slate-800 light:bg-slate-200 rounded-full h-2.5 overflow-hidden flex">
                  <div class="bg-emerald-500 h-2.5" style="width: ${{(item.final_km / item.scope_km * 100)}}%" title="مسلم نهائياً: ${{item.final_km}} كم"></div>
                  <div class="bg-brand-500 h-2.5" style="width: ${{(item.initial_km / item.scope_km * 100)}}%" title="مسلم ابتدائياً: ${{item.initial_km}} كم"></div>
                </div>
                <div class="flex justify-between text-[10px] text-slate-400 light:text-slate-600">
                  <span>المسلم: <strong class="text-white light:text-slate-900">${{item.total_km}} كم</strong></span>
                  <span>المتبقي: <strong class="text-amber-400 light:text-amber-700">${{item.remaining_km}} كم</strong></span>
                </div>
              </div>
            </div>
            <div class="text-[10px] text-slate-400 light:text-slate-500 border-t border-slate-800 light:border-slate-200 pt-2 leading-relaxed">
              ${{item.details}}
            </div>
          </div>
        `;
      }});

      // Handover Financial Cards
      const hof = d.handover_financials;
      document.getElementById('hoFinalContract').innerHTML = `${{(hof.final_contract / 1e6).toFixed(2)}} <span class="text-xs font-normal text-slate-400">م.ج</span>`;
      document.getElementById('hoInitialContract').innerHTML = `${{(hof.initial_contract / 1e6).toFixed(2)}} <span class="text-xs font-normal text-slate-400">م.ج</span>`;
      document.getElementById('hoGrandContract').innerHTML = `${{(hof.grand_contract / 1e6).toFixed(2)}} <span class="text-xs font-normal text-slate-400">م.ج</span>`;
      document.getElementById('hoGrandPv').innerHTML = `${{(hof.grand_pv / 1e6).toFixed(2)}} <span class="text-xs font-normal text-slate-400">م.ج</span>`;

      // Individual Handovers Table
      const hoBody = document.getElementById('individualHandoversTable');
      hoBody.innerHTML = '';
      d.handovers_list.forEach(item => {{
        hoBody.innerHTML += `
          <tr class="hover:bg-slate-900/40 light:hover:bg-slate-50 transition">
            <td class="p-2.5 font-bold text-white light:text-slate-900">${{item.title}}</td>
            <td class="p-2.5"><span class="px-2 py-0.5 rounded text-[10px] font-bold bg-slate-800 light:bg-slate-200 text-slate-300 light:text-slate-800">${{item.status}}</span></td>
            <td class="p-2.5 text-slate-300 light:text-slate-700 font-mono text-[11px]">${{item.dates}}</td>
            <td class="p-2.5 font-mono font-bold text-left text-white light:text-slate-900">${{formatMoney(item.contract_val)}}</td>
            <td class="p-2.5 font-mono text-left text-amber-300 light:text-amber-700">${{formatMoney(item.pv_val)}}</td>
            <td class="p-2.5 font-mono font-bold text-left text-emerald-400 light:text-emerald-700">${{formatMoney(item.total_val)}}</td>
            <td class="p-2.5 text-slate-400 light:text-slate-500 text-[11px] leading-relaxed">${{item.notes}}</td>
          </tr>
        `;
      }});

      // 6. Main Categories Table
      const catBody = document.getElementById('categoriesTableBody');
      const catSelect = document.getElementById('categoryFilterSelect');
      catBody.innerHTML = '';
      catSelect.innerHTML = '<option value="ALL">جميع الفئات الرئيسية (9 فئات)</option>';

      d.main_categories.forEach((cat, idx) => {{
        catSelect.innerHTML += `<option value="${{cat.name}}">${{cat.name}}</option>`;
        const pct100 = (cat.progress_pct * 100).toFixed(1);
        catBody.innerHTML += `
          <tr class="hover:bg-slate-900/40 light:hover:bg-slate-50 transition">
            <td class="p-2.5 text-center text-slate-400 font-bold">${{idx + 1}}</td>
            <td class="p-2.5 font-bold text-white light:text-slate-900">${{cat.name}}</td>
            <td class="p-2.5 text-center font-bold text-slate-300 light:text-slate-700">${{cat.items_count}}</td>
            <td class="p-2.5 font-mono font-bold text-left">${{formatMoney(cat.boq_val)}}</td>
            <td class="p-2.5 font-mono text-center text-slate-300 light:text-slate-700">${{formatPct(cat.weight_pct)}}</td>
            <td class="p-2.5 font-mono font-bold text-left text-emerald-400 light:text-emerald-700">${{formatMoney(cat.approved_val)}}</td>
            <td class="p-2.5 font-mono text-left text-sky-400 light:text-sky-700">${{formatMoney(cat.billed_val)}}</td>
            <td class="p-2.5 font-mono text-left text-amber-300 light:text-amber-700">${{formatMoney(cat.remaining_val)}}</td>
            <td class="p-2.5 text-center">
              <span class="px-2 py-0.5 rounded-lg text-[11px] font-extrabold bg-emerald-500/10 text-emerald-400 light:text-emerald-700 border border-emerald-500/20">${{pct100}}%</span>
            </td>
          </tr>
        `;
      }});

      // 7. Pay Apps Table
      const paBody = document.getElementById('payAppsTableBody');
      paBody.innerHTML = '';
      d.pay_apps.forEach(pa => {{
        const badge = pa.is_locked ? '<span class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/15 text-emerald-400 light:text-emerald-700 border border-emerald-500/30">معتمد ومقفل</span>' : '<span class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/15 text-amber-400 light:text-amber-700 border border-amber-500/30">جاري الاعتماد</span>';
        paBody.innerHTML += `
          <tr class="hover:bg-slate-900/40 light:hover:bg-slate-50 transition">
            <td class="p-2.5 font-bold text-white light:text-slate-900">${{pa.name}}</td>
            <td class="p-2.5 font-mono text-left">${{formatMoney(pa.app_contract)}}</td>
            <td class="p-2.5 font-mono text-left text-amber-300 light:text-amber-700">${{formatMoney(pa.app_pv)}}</td>
            <td class="p-2.5 font-mono text-left">${{formatMoney(pa.app_comp_gross)}}</td>
            <td class="p-2.5 font-mono font-bold text-left text-teal-300 light:text-teal-700">${{formatMoney(pa.app_comp_net)}}</td>
            <td class="p-2.5 font-mono font-bold text-left text-emerald-400 light:text-emerald-700">${{formatMoney(pa.app_total)}}</td>
            <td class="p-2.5 font-mono text-left text-sky-300 light:text-sky-700">${{formatMoney(pa.billed_contract)}}</td>
            <td class="p-2.5 font-mono text-left text-amber-200 light:text-amber-700">${{formatMoney(pa.billed_pv)}}</td>
            <td class="p-2.5 font-mono text-left text-teal-200 light:text-teal-700">${{formatMoney(pa.billed_comp_net)}}</td>
            <td class="p-2.5 text-center">${{badge}}</td>
          </tr>
        `;
      }});

      // 8. Render BOQ Items & Setup Filters
      renderBoqItems();
      document.getElementById('itemSearchInput').addEventListener('input', renderBoqItems);
      document.getElementById('categoryFilterSelect').addEventListener('change', renderBoqItems);

      // 9. Render Charts
      renderCharts();
    }}

    // Filter & Render BOQ Items
    function renderBoqItems() {{
      const query = (document.getElementById('itemSearchInput').value || '').trim().toLowerCase();
      const catFilter = document.getElementById('categoryFilterSelect').value;
      const tbody = document.getElementById('boqItemsTableBody');
      
      const filtered = projectData.boq_items.filter(item => {{
        const matchCat = (catFilter === 'ALL' || item.category === catFilter);
        const matchQuery = !query || 
          item.code.toLowerCase().includes(query) || 
          item.desc.toLowerCase().includes(query) || 
          item.category.toLowerCase().includes(query);
        return matchCat && matchQuery;
      }});

      tbody.innerHTML = '';
      let totBoq = 0, totApp = 0;

      filtered.forEach((it, idx) => {{
        totBoq += it.boq_val;
        totApp += it.approved_val;
        const pct = (it.progress_pct * 100).toFixed(1);
        const pctColor = it.progress_pct >= 0.8 ? 'text-emerald-400 light:text-emerald-700 bg-emerald-500/10' : (it.progress_pct >= 0.5 ? 'text-sky-400 light:text-sky-700 bg-sky-500/10' : 'text-amber-400 light:text-amber-700 bg-amber-500/10');
        
        tbody.innerHTML += `
          <tr class="hover:bg-slate-900/40 light:hover:bg-slate-50 transition">
            <td class="p-2.5 text-center text-slate-400 font-bold">${{idx + 1}}</td>
            <td class="p-2.5 font-mono font-bold text-white light:text-slate-900">${{it.code}}</td>
            <td class="p-2.5 text-slate-200 light:text-slate-800 leading-snug">${{it.desc}}</td>
            <td class="p-2.5 text-slate-300 light:text-slate-600 font-medium">${{it.category}}</td>
            <td class="p-2.5 text-center text-slate-400 light:text-slate-500">${{it.unit}}</td>
            <td class="p-2.5 font-mono text-left">${{formatMoney(it.rate)}}</td>
            <td class="p-2.5 font-mono text-left">${{formatMoney(it.boq_qty)}}</td>
            <td class="p-2.5 font-mono font-bold text-left">${{formatMoney(it.boq_val)}}</td>
            <td class="p-2.5 font-mono text-left text-emerald-300 light:text-emerald-700">${{formatMoney(it.approved_qty)}}</td>
            <td class="p-2.5 font-mono font-bold text-left text-emerald-400 light:text-emerald-700">${{formatMoney(it.approved_val)}}</td>
            <td class="p-2.5 text-center">
              <span class="px-2 py-0.5 rounded text-[11px] font-bold ${{pctColor}}">${{pct}}%</span>
            </td>
          </tr>
        `;
      }});

      document.getElementById('filteredItemsCount').textContent = filtered.length;
      document.getElementById('filteredBoqVal').textContent = formatMoney(totBoq);
      document.getElementById('filteredAppVal').textContent = formatMoney(totApp);
      document.getElementById('filteredProgPct').textContent = totBoq > 0 ? formatPct(totApp / totBoq) : '0.00%';
    }}

    // Charts Rendering
    function renderCharts() {{
      const fin = projectData.financial_status;
      const isDark = document.documentElement.classList.contains('dark');
      const textColor = isDark ? '#94a3b8' : '#334155';
      const gridColor = isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)';

      // Donut Chart: Breakdown of Executed Works
      const ctxDonut = document.getElementById('financialDonutChart').getContext('2d');
      if (window.donutChartInstance) window.donutChartInstance.destroy();

      window.donutChartInstance = new Chart(ctxDonut, {{
        type: 'doughnut',
        data: {{
          labels: ['أعمال التعاقد', 'فروق الأسعار', 'صافي التعويضات'],
          datasets: [{{
            data: [fin.app_contract, fin.app_pv, fin.app_net_comp],
            backgroundColor: ['#0284c7', '#f59e0b', '#14b8a6'],
            borderWidth: 2,
            borderColor: isDark ? '#0f172a' : '#ffffff'
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{
              position: 'bottom',
              labels: {{ color: textColor, font: {{ family: 'Cairo', size: 11 }} }}
            }},
            tooltip: {{
              callbacks: {{
                label: function(ctx) {{
                  const v = ctx.raw || 0;
                  return ' ' + ctx.label + ': ' + (v / 1e6).toFixed(2) + ' مليون ج.م';
                }}
              }}
            }}
          }},
          cutout: '68%'
        }}
      }});

      // Monthly Trend Chart
      const ctxTrend = document.getElementById('monthlyTrendChart').getContext('2d');
      if (window.trendChartInstance) window.trendChartInstance.destroy();

      const trendData = projectData.monthly_trend;
      window.trendChartInstance = new Chart(ctxTrend, {{
        type: 'line',
        data: {{
          labels: trendData.map(t => t.month),
          datasets: [
            {{
              label: 'أعمال التعاقد',
              data: trendData.map(t => t.contract / 1e6),
              borderColor: '#0284c7',
              backgroundColor: 'rgba(2, 132, 199, 0.1)',
              fill: true,
              tension: 0.3
            }},
            {{
              label: 'فروق الأسعار',
              data: trendData.map(t => t.pv / 1e6),
              borderColor: '#f59e0b',
              backgroundColor: 'rgba(245, 158, 11, 0.05)',
              fill: true,
              tension: 0.3
            }},
            {{
              label: 'التعويضات',
              data: trendData.map(t => t.comp / 1e6),
              borderColor: '#14b8a6',
              backgroundColor: 'transparent',
              tension: 0.3
            }}
          ]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          interaction: {{ mode: 'index', intersect: false }},
          scales: {{
            x: {{ grid: {{ color: gridColor }}, ticks: {{ color: textColor, font: {{ family: 'Cairo', size: 10 }} }} }},
            y: {{
              grid: {{ color: gridColor }},
              ticks: {{
                color: textColor,
                font: {{ family: 'Cairo', size: 10 }},
                callback: function(v) {{ return v + ' م.ج'; }}
              }}
            }}
          }},
          plugins: {{
            legend: {{
              position: 'top',
              labels: {{ color: textColor, font: {{ family: 'Cairo', size: 11 }} }}
            }}
          }}
        }}
      }});
    }}

    // =========================================================================
    // PWA SERVICE WORKER REGISTRATION
    // =========================================================================
    if ('serviceWorker' in navigator) {{
      window.addEventListener('load', () => {{
        navigator.serviceWorker.register('sw.js').catch(() => {{}});
      }});
    }}

    // Initialization on Page Load
    document.addEventListener('DOMContentLoaded', () => {{
      initTheme();
      initAuth();
    }});
  </script>
</body>
</html>
'''

out_html_path = os.path.join(app_dir, "index.html")
with open(out_html_path, "w", encoding="utf-8") as f:
    f.write(html_code)

print(f"Successfully generated full feature app/index.html ({len(html_code)} bytes)!")
