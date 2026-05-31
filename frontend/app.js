const I18N = {
  ar: {
    heroKicker: 'منصة دعم القرار الطبي',
    heroSubtitle: 'تحليل أشعة الصدر، دمج التحاليل، ومحادثة طبية مبنية على سياق المريض.',
    doctorPortalTitle: 'بوابة الطبيب',
    doctorPortalSubtitle: 'مساحة عمل سريرية منظمة لتحليل صور الأشعة ودمج التحاليل ومراجعة سياق المريض.',
    authAccessNote: 'يرجى تسجيل الدخول بحساب الطبيب للوصول إلى مساحة العمل الطبية.',
    loginTab: 'تسجيل الدخول', registerTab: 'إنشاء حساب',
    loginTitle: 'تسجيل دخول الطبيب', registerTitle: 'إنشاء حساب طبيب',
    doctorName: 'اسم الطبيب', doctorEmail: 'البريد الإلكتروني', doctorPassword: 'كلمة المرور', doctorPasswordConfirm: 'تأكيد كلمة المرور',
    loginButton: 'دخول', registerButton: 'إنشاء الحساب', logout: 'تسجيل الخروج',
    loggedInAs: 'تم الدخول باسم', accountCreated: 'تم إنشاء الحساب وتسجيل الدخول بنجاح.', loginSuccess: 'تم تسجيل الدخول بنجاح.',
    invalidCredentials: 'البريد الإلكتروني أو كلمة المرور غير صحيحة.', passwordsDoNotMatch: 'كلمتا المرور غير متطابقتين.', accountExists: 'يوجد حساب مسجل بهذا البريد الإلكتروني.', weakPassword: 'يجب أن تكون كلمة المرور 6 أحرف على الأقل.',
    themeDark: 'الوضع الليلي', themeLight: 'الوضع النهاري', showPassword: 'إظهار', hidePassword: 'إخفاء',
    workspaceReady: 'جاهز لبدء سير العمل',
    noActivePatient: 'لا يوجد مريض نشط',
    patientBadge: 'المريض',
    chatNotReady: 'المحادثة غير مفعلة',
    chatReady: 'المحادثة جاهزة',
    stepPatientTitle: 'المريض', stepPatientSub: 'إنشاء أو تحميل ملف المريض',
    stepXrayTitle: 'الأشعة', stepXraySub: 'رفع وتحليل الصورة',
    stepLabTitle: 'التحاليل', stepLabSub: 'دمج اختياري',
    stepChatTitle: 'المساعد', stepChatSub: 'أسئلة مبنية على السياق',
    patientKicker: 'بيانات المريض', patientTitle: '1. المريض', required: 'مطلوب',
    patientName: 'اسم المريض', patientNamePlaceholder: 'مثال: سارة أحمد', patientId: 'معرّف المريض', patientIdPlaceholder: 'اكتب معرّف مريض موجود أو اتركه بعد الإنشاء', age: 'العمر', agePlaceholder: 'مثال: 45', sex: 'الجنس', sexUnknown: 'غير محدد', sexFemale: 'أنثى', sexMale: 'ذكر', phone: 'رقم الهاتف', optional: 'اختياري', notes: 'ملاحظات سريرية',
    notesPlaceholder: 'الأعراض، القصة المرضية، الحرارة، السعال، تشبع الأكسجين، أمراض سابقة...',
    createPatient: 'إنشاء مريض', useExisting: 'استخدام مريض موجود',
    xrayKicker: 'الخطوة الأساسية', xrayTitle: '2. تحليل صورة الأشعة', mainStep: 'خطوة رئيسية', xrayImage: 'صورة أشعة الصدر', noXrayPreview: 'لا توجد معاينة للأشعة بعد', uploadXray: 'رفع الأشعة', analyzeXray: 'تحليل الأشعة',
    labKicker: 'بيانات داعمة اختيارية', labTitle: '3. تقرير التحاليل', optionalStep: 'اختياري', labHint: 'يمكن إضافة صورة التحليل بعد تحليل الأشعة لتحديث التقرير وسياق المحادثة.', labImage: 'صورة تقرير التحليل', noLabPreview: 'لا توجد معاينة للتحليل بعد', uploadLab: 'رفع التحليل', analyzeLab: 'تحليل ودمج التحاليل',
    legendTitle: 'دليل ألوان الإشعارات الطبية',
    xrayResultKicker: 'نتيجة التصوير', xrayResultTitle: 'تفسير صورة الأشعة', notAnalyzed: 'لم يتم التحليل', xrayEmpty: 'قم بتحليل صورة الأشعة لعرض الملخص المهم والإشعارات الطبية هنا.',
    labResultKicker: 'نتيجة التحاليل', labResultTitle: 'ملخص التحليل المخبري', notAdded: 'لم تتم الإضافة', labEmpty: 'بعد رفع التحليل ستظهر القيم المهمة فقط، دون عرض نص OCR الطويل.',
    integratedKicker: 'الملخص السريري', integratedTitle: 'السياق الطبي المتكامل', refreshReports: 'تحديث التقارير', integratedEmpty: 'لا يوجد ملخص متكامل بعد. أكمل تحليل الأشعة أولًا، ثم أضف التحاليل اختياريًا.',
    chatKicker: 'مساعد يعتمد على سياق المريض', chatTitle: '4. المساعد الطبي', waitingContext: 'بانتظار السياق', chatWelcome: 'قم بتحليل صورة الأشعة أولًا، ثم اسأل عن سياق المريض المحفوظ. هذا المساعد للدعم التعليمي فقط وليس تشخيصًا نهائيًا.',
    chatPlaceholder: 'اسأل عن حالة المريض والسياق المحفوظ...', send: 'إرسال',
    quickInitial: 'الانطباع الأولي', quickSummary: 'ملخص الأشعة والتحاليل', quickChecks: 'الفحوصات التالية', quickTeaching: 'التوضيح والشرح',
    status: 'الحالة', source: 'المصدر', xrayFiles: 'ملفات الأشعة', labFiles: 'ملفات التحاليل',
    success: 'نجاح', fallback: 'وضع احتياطي', failed: 'فشل', error: 'خطأ', pending: 'قيد المعالجة',
    remoteXray: 'ذكاء اصطناعي خارجي - الأشعة', remoteLab: 'ذكاء اصطناعي خارجي - دمج التحاليل', remoteAi: 'ذكاء اصطناعي خارجي', partialRemote: 'ذكاء اصطناعي جزئي', localFallback: 'احتياطي محلي', local: 'سياق محلي', cache: 'نتيجة محفوظة', unknown: 'غير معروف',
    critical: 'أحمر: أولوية عالية/خطر', high: 'برتقالي: يحتاج انتباه', moderate: 'أصفر: متوسط', normal: 'أخضر: مطمئن', info: 'أزرق: معلومة',
    attentionRequired: 'تنبيه يحتاج انتباه الطبيب', monitorClosely: 'نتائج تحتاج متابعة', moderateConcern: 'ملاحظة متوسطة الأهمية', stableSummary: 'لا توجد إشارات خطورة واضحة', infoSummary: 'معلومة سياقية',
    xrayCompleted: 'اكتمل تحليل الأشعة', labCompleted: 'اكتمل دمج التحاليل',
    importantSummary: 'الملخص المهم', importantFindings: 'النقاط المهمة', clinicalAlert: 'الإشعار السريري',
    imageQuality: 'جودة الصورة', severity: 'تقدير الشدة', findings: 'النتائج', impression: 'الانطباع', recommendations: 'التوصيات', alerts: 'التنبيهات',
    labImportantValues: 'القيم المخبرية المهمة', labInterpretation: 'تفسير التحاليل', noAbnormalLab: 'لم يتم تمييز قيم مخبرية شاذة بوضوح.', rawHidden: 'تم إخفاء نص OCR الكامل لإبقاء الواجهة مختصرة. يمكن مراجعة التقرير الكامل عند الحاجة.',
    integratedInterpretation: 'التفسير المتكامل', medicalExplanation: 'شرح طبي مختصر', openReport: 'فتح التقرير', downloadReport: 'تحميل التقرير', openLatestReport: 'فتح أحدث تقرير', downloadLatestReport: 'تحميل أحدث تقرير',
    warnings: 'تحذيرات', noWarnings: 'لا توجد تحذيرات', reportLoading: 'جاري تحميل ملخص التقرير...', reportLoadFailed: 'تعذر تحميل ملخص التقرير تلقائيًا. استخدم زر فتح التقرير.',
    creatingPatient: 'جاري إنشاء المريض...', patientNameRequired: 'اسم المريض مطلوب.', patientCreated: 'تم إنشاء المريض', enterPatientId: 'أدخل رقم المريض أولًا.', loadingPatient: 'جاري تحميل بيانات المريض...', usingPatient: 'يتم استخدام المريض',
    createOrLoadFirst: 'أنشئ مريضًا أو حمّل مريضًا موجودًا أولًا.', chooseFileFirst: 'اختر صورة أولًا.', uploading: 'جاري الرفع...', uploadSuccess: 'تم رفع الملف بنجاح.', fileMissingAfterUpload: 'اكتمل طلب الرفع، لكن الملف لم يظهر ضمن ملفات المريض.', noUploadedFile: 'لا يوجد ملف مرفوع لهذا المريض. اختر الملف وارفعه أولًا.',
    analyzingXray: 'جاري تحليل الأشعة...', checkingXray: 'جاري التحقق من رفع صورة الأشعة...', xrayMayTake: 'جاري تحليل الأشعة بواسطة خدمة الذكاء الاصطناعي. قد يستغرق الطلب الأول وقتًا أطول...', xrayFallback: 'عاد تحليل الأشعة بوضع احتياطي. راجع التحذيرات.', xrayDone: 'اكتمل تحليل الأشعة. أصبحت المحادثة متاحة الآن.',
    analyzingLab: 'جاري تحليل المختبر ودمج السياق...', checkingLab: 'جاري التحقق من رفع صورة التحليل...', labMayTake: 'جاري تحليل تقرير المختبر ودمجه مع سياق الأشعة المحفوظ...', labDoneWarnings: 'اكتمل دمج التحاليل مع وجود تحذيرات.', labDone: 'اكتمل دمج التحاليل.',
    contextReady: 'السياق جاهز', askingAssistant: 'جاري سؤال المساعد...', sendingQuestion: 'جاري إرسال السؤال...', answerReceived: 'تم استلام الإجابة.', sourceLabel: 'المصدر', refreshedReport: 'تم تحميل أحدث تقرير', noReports: 'لا توجد تقارير لهذا المريض.', refreshingReports: 'جاري تحديث أحدث تقرير...', actionFailed: 'فشل الإجراء', chatFailed: 'فشلت المحادثة',
    tableTest: 'التحليل', tableValue: 'القيمة', tableUnit: 'الوحدة', tableStatus: 'الحالة', tableRange: 'المدى المرجعي',
  },
  en: {
    heroKicker: 'Clinical decision support workspace',
    heroSubtitle: 'Chest X-ray analysis, optional lab merging, and a patient-context medical assistant.',
    doctorPortalTitle: 'Doctor portal',
    doctorPortalSubtitle: 'A structured clinical workspace for X-ray analysis, lab merging, and patient-context review.',
    authAccessNote: 'Sign in with a doctor account to access the clinical workspace.',
    loginTab: 'Sign in', registerTab: 'Create account',
    loginTitle: 'Doctor sign in', registerTitle: 'Create doctor account',
    doctorName: 'Doctor name', doctorEmail: 'Email', doctorPassword: 'Password', doctorPasswordConfirm: 'Confirm password',
    loginButton: 'Sign in', registerButton: 'Create account', logout: 'Sign out',
    loggedInAs: 'Signed in as', accountCreated: 'Account created and signed in successfully.', loginSuccess: 'Signed in successfully.',
    invalidCredentials: 'Incorrect email or password.', passwordsDoNotMatch: 'Passwords do not match.', accountExists: 'An account already exists with this email.', weakPassword: 'Password must be at least 6 characters.',
    themeDark: 'Dark mode', themeLight: 'Light mode', showPassword: 'Show', hidePassword: 'Hide',
    workspaceReady: 'Ready to start the workflow',
    noActivePatient: 'No active patient',
    patientBadge: 'Patient',
    chatNotReady: 'Chat not ready',
    chatReady: 'Chat ready',
    stepPatientTitle: 'Patient', stepPatientSub: 'Create or load a patient',
    stepXrayTitle: 'X-ray', stepXraySub: 'Upload and analyze image',
    stepLabTitle: 'Lab', stepLabSub: 'Optional merge',
    stepChatTitle: 'Assistant', stepChatSub: 'Context-based questions',
    patientKicker: 'Patient data', patientTitle: '1. Patient', required: 'Required',
    patientName: 'Patient name', patientNamePlaceholder: 'Example: Sara Ahmed', patientId: 'Patient ID', patientIdPlaceholder: 'Use an existing ID or create a new patient', agePlaceholder: 'Example: 45',
    age: 'Age', sex: 'Sex', sexUnknown: 'Unknown', sexFemale: 'Female', sexMale: 'Male', phone: 'Phone', optional: 'Optional', notes: 'Clinical notes',
    notesPlaceholder: 'Symptoms, history, fever, cough, oxygen saturation, comorbidities...',
    createPatient: 'Create Patient', useExisting: 'Use Existing Patient',
    xrayKicker: 'Core step', xrayTitle: '2. X-ray Analysis', mainStep: 'Main step', xrayImage: 'Chest X-ray image', noXrayPreview: 'No X-ray preview yet', uploadXray: 'Upload X-ray', analyzeXray: 'Analyze X-ray',
    labKicker: 'Optional supporting data', labTitle: '3. Lab Report', optionalStep: 'Optional', labHint: 'Add a lab image after X-ray analysis to update the report and chat context.', labImage: 'Lab report image', noLabPreview: 'No lab preview yet', uploadLab: 'Upload Lab', analyzeLab: 'Analyze Lab & Merge',
    legendTitle: 'Clinical alert color guide',
    xrayResultKicker: 'Imaging result', xrayResultTitle: 'Chest X-ray interpretation', notAnalyzed: 'Not analyzed', xrayEmpty: 'Analyze the X-ray to show the concise summary and clinical alerts here.',
    labResultKicker: 'Lab result', labResultTitle: 'Lab summary', notAdded: 'Not added', labEmpty: 'After lab upload, only important values will appear here without long OCR text.',
    integratedKicker: 'Clinical summary', integratedTitle: 'Integrated patient context', refreshReports: 'Refresh reports', integratedEmpty: 'No integrated summary yet. Complete X-ray analysis first, then optionally add labs.',
    chatKicker: 'Patient-context assistant', chatTitle: '4. Medical Assistant', waitingContext: 'Waiting for context', chatWelcome: 'Analyze the X-ray first, then ask about the saved patient context. Educational support only, not a final diagnosis.',
    chatPlaceholder: 'Ask about the saved patient context...', send: 'Send',
    quickInitial: 'Initial impression', quickSummary: 'X-ray + lab summary', quickChecks: 'Next checks', quickTeaching: 'Teaching explanation',
    status: 'Status', source: 'Source', xrayFiles: 'X-ray files', labFiles: 'Lab files',
    success: 'Success', fallback: 'Fallback', failed: 'Failed', error: 'Error', pending: 'Pending',
    remoteXray: 'Remote AI - X-ray', remoteLab: 'Remote AI - lab merge', remoteAi: 'Remote AI', partialRemote: 'Partial remote AI', localFallback: 'Local fallback', local: 'Local context', cache: 'Cached result', unknown: 'Unknown',
    critical: 'Red: urgent/high risk', high: 'Orange: needs attention', moderate: 'Yellow: moderate', normal: 'Green: reassuring', info: 'Blue: information',
    attentionRequired: 'Clinician attention required', monitorClosely: 'Findings need follow-up', moderateConcern: 'Moderate-priority note', stableSummary: 'No clear high-risk signal', infoSummary: 'Context information',
    xrayCompleted: 'X-ray analysis completed', labCompleted: 'Lab merge completed',
    importantSummary: 'Key summary', importantFindings: 'Important points', clinicalAlert: 'Clinical alert',
    imageQuality: 'Image quality', severity: 'Estimated severity', findings: 'Findings', impression: 'Impression', recommendations: 'Recommendations', alerts: 'Alerts',
    labImportantValues: 'Important lab values', labInterpretation: 'Lab interpretation', noAbnormalLab: 'No clearly flagged abnormal lab values.', rawHidden: 'Full OCR text is hidden to keep the interface concise. Open the full report if needed.',
    integratedInterpretation: 'Integrated interpretation', medicalExplanation: 'Brief medical explanation', openReport: 'Open Report', downloadReport: 'Download Report', openLatestReport: 'Open Latest Report', downloadLatestReport: 'Download Latest Report',
    warnings: 'Warnings', noWarnings: 'No warnings', reportLoading: 'Loading report summary...', reportLoadFailed: 'Could not load report summary automatically. Use the open report button.',
    creatingPatient: 'Creating patient...', patientNameRequired: 'Patient name is required.', patientCreated: 'Patient created', enterPatientId: 'Enter patient ID first.', loadingPatient: 'Loading patient...', usingPatient: 'Using patient',
    createOrLoadFirst: 'Create or load a patient first.', chooseFileFirst: 'Choose an image first.', uploading: 'Uploading...', uploadSuccess: 'File uploaded successfully.', fileMissingAfterUpload: 'Upload request finished, but the file did not appear in patient files.', noUploadedFile: 'No uploaded file exists for this patient. Choose and upload the file first.',
    analyzingXray: 'Analyzing X-ray...', checkingXray: 'Checking X-ray upload...', xrayMayTake: 'Analyzing X-ray with the AI service. The first request may take longer...', xrayFallback: 'X-ray analysis returned fallback. Check warnings.', xrayDone: 'X-ray analysis completed. Chat is now available.',
    analyzingLab: 'Analyzing lab and merging context...', checkingLab: 'Checking lab image upload...', labMayTake: 'Analyzing lab report and merging it with saved X-ray context...', labDoneWarnings: 'Lab merge completed with warnings.', labDone: 'Lab merge completed.',
    contextReady: 'Context ready', askingAssistant: 'Asking assistant...', sendingQuestion: 'Sending question...', answerReceived: 'Answer received.', sourceLabel: 'Source', refreshedReport: 'Loaded latest report', noReports: 'No reports for this patient.', refreshingReports: 'Refreshing latest report...', actionFailed: 'Action failed', chatFailed: 'Chat failed',
    tableTest: 'Test', tableValue: 'Value', tableUnit: 'Unit', tableStatus: 'Status', tableRange: 'Reference range',
  }
};

const state = {
  apiBase: localStorage.getItem('ai_doctor_api_base') || 'https://ai-doctor-helper.onrender.com/api',
  lang: localStorage.getItem('ai_doctor_lang') || 'ar',
  theme: localStorage.getItem('ai_doctor_theme') || 'light',
  patientId: '',
  latestReportUrl: '',
  chatReady: false,
  xrayParsed: null,
  labParsed: null,
};

const $ = (id) => document.getElementById(id);
const t = (key) => (I18N[state.lang] && I18N[state.lang][key]) || I18N.ar[key] || key;

function escapeHtml(value) {
  return String(value ?? '')
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#039;');
}

function compactText(value, max = 520) {
  const text = String(value || '').replace(/\s+/g, ' ').trim();
  if (!text) return '';
  if (text.length <= max) return text;
  const cut = text.slice(0, max);
  const lastDot = Math.max(cut.lastIndexOf('.'), cut.lastIndexOf('،'), cut.lastIndexOf(';'));
  return (lastDot > 180 ? cut.slice(0, lastDot + 1) : cut.trim()) + '…';
}

function splitImportantPoints(text, limit = 4) {
  const cleaned = String(text || '').replace(/\s+/g, ' ').trim();
  if (!cleaned) return [];
  const parts = cleaned
    .split(/(?:\.\s+|;\s+|،\s+|\n+)/)
    .map((x) => x.trim())
    .filter(Boolean);
  return parts.slice(0, limit).map((x) => compactText(x, 170));
}

function prettyStatus(status) {
  const map = { success: t('success'), fallback: t('fallback'), failed: t('failed'), error: t('error'), pending: t('pending') };
  return map[String(status || '').toLowerCase()] || status || '-';
}

function prettySource(source) {
  const map = {
    xray_remote_ai: t('remoteXray'),
    lab_merged_remote_ai: t('remoteLab'),
    remote_ai: t('remoteAi'),
    partial_remote_ai: t('partialRemote'),
    local_fallback: t('localFallback'),
    local: t('local'),
    cache: t('cache'),
    fallback: t('fallback'),
    unknown: t('unknown'),
  };
  return map[source] || source || '-';
}

function setLanguage(lang) {
  state.lang = lang === 'en' ? 'en' : 'ar';
  localStorage.setItem('ai_doctor_lang', state.lang);
  document.documentElement.lang = state.lang;
  document.documentElement.dir = state.lang === 'ar' ? 'rtl' : 'ltr';

  document.querySelectorAll('[data-i18n]').forEach((el) => {
    const key = el.dataset.i18n;
    if (key && I18N[state.lang][key]) el.textContent = t(key);
  });
  document.querySelectorAll('[data-i18n-placeholder]').forEach((el) => {
    const key = el.dataset.i18nPlaceholder;
    if (key && I18N[state.lang][key]) el.placeholder = t(key);
  });

  $('langArBtn')?.classList.toggle('is-active', state.lang === 'ar');
  $('langEnBtn')?.classList.toggle('is-active', state.lang === 'en');
  renderSeverityLegend();
  updatePatientBadges();
  updateAuthVisibility();
}

function setStatus(id, text, type = '') {
  const el = $(id);
  if (!el) return;
  el.textContent = text || '';
  el.classList.toggle('error', type === 'error' || type === true);
  el.classList.toggle('success', type === 'success');
}

function setBusy(isBusy, text = '') {
  const stateText = $('workspaceState');
  const dot = document.querySelector('.system-card .dot');
  if (stateText) stateText.textContent = text || (isBusy ? t('pending') : t('workspaceReady'));
  if (dot) {
    dot.classList.toggle('dot--busy', Boolean(isBusy));
    dot.classList.toggle('dot--ready', !isBusy);
    dot.classList.remove('dot--error');
  }
}

function setSystemError(text) {
  const stateText = $('workspaceState');
  const dot = document.querySelector('.system-card .dot');
  if (stateText) stateText.textContent = text || t('actionFailed');
  if (dot) {
    dot.classList.remove('dot--ready', 'dot--busy');
    dot.classList.add('dot--error');
  }
}

function setWorkflowStep(id, status) {
  const el = $(id);
  if (!el) return;
  el.classList.toggle('is-active', status === 'active');
  el.classList.toggle('is-done', status === 'done');
}

function updatePatientBadges() {
  const patientBadge = $('activePatientBadge');
  const chatBadge = $('chatReadyBadge');
  if (patientBadge) patientBadge.textContent = state.patientId ? `${t('patientBadge')}: ${state.patientId}` : t('noActivePatient');
  if (chatBadge) chatBadge.textContent = state.chatReady ? t('chatReady') : t('chatNotReady');
}

function updateResultBadge(id, result) {
  const el = $(id);
  if (!el) return;
  const status = String(result?.status || '').toLowerCase();
  const source = String(result?.source || '').toLowerCase();
  el.classList.remove('state-pill--idle', 'state-pill--success', 'state-pill--warning', 'state-pill--danger');
  if (status === 'success' && source !== 'fallback') {
    el.textContent = t('success');
    el.classList.add('state-pill--success');
  } else if (source === 'fallback' || status === 'fallback') {
    el.textContent = t('fallback');
    el.classList.add('state-pill--danger');
  } else if ((result?.warnings || []).length) {
    el.textContent = t('warnings');
    el.classList.add('state-pill--warning');
  } else {
    el.textContent = t('pending');
    el.classList.add('state-pill--idle');
  }
}

function getApiBase() { return state.apiBase.replace(/\/$/, ''); }
function getPatientId() { return $('patientId').value.trim(); }
function setPatientId(patientId) { state.patientId = patientId; $('patientId').value = patientId; updatePatientBadges(); }
function getReportUrl(reportDownloadUrl) {
  if (!reportDownloadUrl) return '';
  if (reportDownloadUrl.startsWith('http')) return reportDownloadUrl;
  const origin = getApiBase().replace(/\/api$/, '');
  return `${origin}${reportDownloadUrl}`;
}

async function requestJson(url, options = {}) {
  const response = await fetch(url, options);
  const text = await response.text();
  let payload = null;
  try { payload = text ? JSON.parse(text) : null; }
  catch { payload = { raw: text }; }
  if (!response.ok) {
    const message = payload?.detail || payload?.message || response.statusText || 'Request failed';
    throw new Error(typeof message === 'string' ? message : JSON.stringify(message));
  }
  return payload;
}

function metric(label, value) {
  return `<div class="metric"><span>${escapeHtml(label)}</span><strong>${escapeHtml(value || '-')}</strong></div>`;
}

function warningsHtml(warnings) {
  if (!warnings || !warnings.length) return '';
  return `<div class="warning-list"><strong>${escapeHtml(t('warnings'))}</strong><ul>${warnings.map((w) => `<li>${escapeHtml(w)}</li>`).join('')}</ul></div>`;
}

function reportButtonsHtml(reportUrl, latest = false) {
  if (!reportUrl) return '';
  return `
    <div class="report-actions">
      <a class="report-link" href="${escapeHtml(reportUrl)}" target="_blank" rel="noopener">${escapeHtml(latest ? t('openLatestReport') : t('openReport'))}</a>
      <a class="report-link secondary-link" href="${escapeHtml(reportUrl)}" download>${escapeHtml(latest ? t('downloadLatestReport') : t('downloadReport'))}</a>
    </div>
  `;
}

function severityLegendHtml() {
  const items = [
    ['critical', t('critical')], ['high', t('high')], ['moderate', t('moderate')], ['normal', t('normal')], ['info', t('info')]
  ];
  return items.map(([level, label]) => `<span class="legend-item"><span class="severity-dot severity-dot--${level}"></span>${escapeHtml(label)}</span>`).join('');
}
function renderSeverityLegend() { const el = $('severityLegend'); if (el) el.innerHTML = severityLegendHtml(); }

function classifySeverity(text, explicitSeverity = '', warnings = []) {
  const blob = `${text || ''} ${explicitSeverity || ''} ${(warnings || []).join(' ')}`.toLowerCase();
  if (/critical|severe|urgent|emergency|life[- ]?threat|respiratory failure|tension|large pneumothorax|massive|marked/i.test(blob)) return 'critical';
  if (/moderate|high|pneumonia|consolidation|effusion|cardiomegaly|opacity|infiltrate|abnormal|elevated crp|high wbc|low platelet|thrombocytopenia/i.test(blob)) return 'high';
  if (/mild|limited|follow|low|borderline|possible|small/i.test(blob)) return 'moderate';
  if (/normal|no acute|clear|unremarkable|no abnormal/i.test(blob)) return 'normal';
  return 'info';
}

function alertCopy(level, context = '') {
  const byLevel = {
    critical: [t('attentionRequired'), state.lang === 'ar' ? 'توجد مؤشرات قد تكون عالية الخطورة وتحتاج مراجعة فورية.' : 'Potential high-risk findings require urgent review.'],
    high: [t('monitorClosely'), state.lang === 'ar' ? 'النتائج غير مطمئنة بالكامل وتحتاج ربطًا سريريًا ومتابعة الطبيب.' : 'Findings are not fully reassuring and need clinical correlation.'],
    moderate: [t('moderateConcern'), state.lang === 'ar' ? 'توجد ملاحظة تحتاج متابعة دون اعتبارها تشخيصًا نهائيًا.' : 'There is a note that needs follow-up; not a final diagnosis.'],
    normal: [t('stableSummary'), state.lang === 'ar' ? 'لا تظهر مؤشرات خطورة واضحة ضمن الملخص المتاح.' : 'No clear high-risk signal in the available summary.'],
    info: [t('infoSummary'), state.lang === 'ar' ? 'تتوفر معلومات داعمة تحتاج قراءة الطبيب.' : 'Supportive context information is available.'],
  };
  const [title, fallback] = byLevel[level] || byLevel.info;
  return [title, compactText(context, 180) || fallback];
}

function alertCard(level, title, summary) {
  return `
    <div class="clinical-alert clinical-alert--${escapeHtml(level)}">
      <span class="severity-dot severity-dot--${escapeHtml(level)}"></span>
      <div>
        <p class="alert-title">${escapeHtml(title)}</p>
        <p class="alert-summary">${escapeHtml(summary)}</p>
      </div>
    </div>
  `;
}

function importantList(points) {
  const clean = (points || []).filter(Boolean).slice(0, 5);
  if (!clean.length) return '';
  return `<ul class="compact-list">${clean.map((p) => `<li>${escapeHtml(p)}</li>`).join('')}</ul>`;
}

function chips(items, abnormal = false) {
  const clean = (items || []).filter(Boolean).slice(0, 8);
  if (!clean.length) return '';
  return `<div class="finding-chips">${clean.map((item) => `<span class="finding-chip ${abnormal ? 'finding-chip--abnormal' : ''}">${escapeHtml(item)}</span>`).join('')}</div>`;
}

function textAfterLabel(text, label) {
  const escaped = label.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const nextLabels = ['Status:', 'Image quality:', 'Estimated severity:', 'Findings:', 'Impression:', 'Detected findings:', 'Alerts:', 'Recommendations:', 'Lab interpretation:', 'Flagged values:', 'Integrated Interpretation', 'Medical Explanation', 'Extracted OCR Text'];
  const pattern = new RegExp(`${escaped}\\s*([\\s\\S]*?)(?=${nextLabels.filter((x) => x !== label).map((x) => x.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('|')}|$)`, 'i');
  const match = text.match(pattern);
  return match ? match[1].replace(/\s+/g, ' ').trim() : '';
}

function getSectionNodes(doc, headingText) {
  const headings = Array.from(doc.querySelectorAll('h2'));
  const heading = headings.find((h) => h.textContent.trim().toLowerCase().includes(headingText.toLowerCase()));
  if (!heading) return [];
  const nodes = [];
  let current = heading.nextElementSibling;
  while (current && current.tagName.toLowerCase() !== 'h2') {
    nodes.push(current);
    current = current.nextElementSibling;
  }
  return nodes;
}

function getSectionText(doc, headingText) {
  return getSectionNodes(doc, headingText)
    .map((node) => node.textContent || '')
    .join('\n')
    .replace(/Extracted OCR Text[\s\S]*$/i, '')
    .replace(/\n{3,}/g, '\n\n')
    .trim();
}

function parseHtmlTable(doc, headingText) {
  const nodes = getSectionNodes(doc, headingText);
  const table = nodes.map((node) => node.querySelector ? node.querySelector('table') : null).find(Boolean);
  if (!table) return [];
  const rows = Array.from(table.querySelectorAll('tr')).map((row) => Array.from(row.children).map((cell) => cell.textContent.trim()));
  if (rows.length < 2) return [];
  return rows.slice(1).map((r) => ({ test: r[0] || '', value: r[1] || '', unit: r[2] || '', status: r[3] || '', range: r[4] || '' })).filter((x) => x.test);
}

function isAbnormalStatus(status) {
  return /high|low|abnormal|elevated|decreased|critical/i.test(String(status || ''));
}

function renderLabTable(rows) {
  const selected = rows.filter((r) => isAbnormalStatus(r.status)).slice(0, 8);
  const data = selected.length ? selected : rows.slice(0, 6);
  if (!data.length) return '';
  return `
    <div class="lab-table-wrap">
      <table class="lab-table">
        <thead><tr><th>${escapeHtml(t('tableTest'))}</th><th>${escapeHtml(t('tableValue'))}</th><th>${escapeHtml(t('tableUnit'))}</th><th>${escapeHtml(t('tableStatus'))}</th><th>${escapeHtml(t('tableRange'))}</th></tr></thead>
        <tbody>${data.map((r) => `<tr class="${isAbnormalStatus(r.status) ? 'is-abnormal' : ''}"><td>${escapeHtml(r.test)}</td><td>${escapeHtml(r.value)}</td><td>${escapeHtml(r.unit)}</td><td>${escapeHtml(r.status)}</td><td>${escapeHtml(r.range)}</td></tr>`).join('')}</tbody>
      </table>
    </div>
  `;
}

function renderAnalysisShell(result, targetId, kind) {
  const reportUrl = getReportUrl(result.report_download_url);
  if (reportUrl) state.latestReportUrl = reportUrl;
  const title = kind === 'xray' ? t('xrayCompleted') : t('labCompleted');
  const html = `
    <div class="result-overview">
      ${metric(t('status'), prettyStatus(result.status))}
      ${metric(t('source'), prettySource(result.source))}
      ${metric(t('xrayFiles'), result.available_xray_files ?? '-')}
    </div>
    ${warningsHtml(result.warnings || [])}
    ${reportButtonsHtml(reportUrl)}
    <div class="section-card" id="${kind}ReportDetails">
      <h3>${escapeHtml(title)}</h3>
      <p>${escapeHtml(t('reportLoading'))}</p>
    </div>
  `;
  const el = $(targetId);
  if (el) { el.classList.remove('empty-state'); el.innerHTML = html; }
  renderReportActions(reportUrl);
  return reportUrl;
}

async function loadReportHtml(reportUrl) {
  if (!reportUrl) return null;
  const response = await fetch(reportUrl, { method: 'GET' });
  if (!response.ok) throw new Error(`Could not load report details (${response.status}).`);
  return await response.text();
}

function parseReport(reportHtml) {
  const doc = new DOMParser().parseFromString(reportHtml, 'text/html');
  const xrayText = getSectionText(doc, 'Chest X-ray Analysis');
  const labText = getSectionText(doc, 'Lab Report OCR and Context');
  const integratedText = getSectionText(doc, 'Integrated Interpretation');
  const explanationText = getSectionText(doc, 'Medical Explanation').replace(/Extracted OCR Text[\s\S]*$/i, '').trim();

  const xray = {
    text: xrayText,
    findings: textAfterLabel(xrayText, 'Findings:'),
    impression: textAfterLabel(xrayText, 'Impression:'),
    severity: textAfterLabel(xrayText, 'Estimated severity:'),
    quality: textAfterLabel(xrayText, 'Image quality:'),
    recommendations: textAfterLabel(xrayText, 'Recommendations:'),
    detected: textAfterLabel(xrayText, 'Detected findings:'),
    alerts: textAfterLabel(xrayText, 'Alerts:'),
  };
  const labRows = parseHtmlTable(doc, 'Lab Report OCR and Context');
  const lab = {
    text: labText,
    status: textAfterLabel(labText, 'Status:'),
    interpretation: textAfterLabel(labText, 'Lab interpretation:'),
    rows: labRows,
    abnormalRows: labRows.filter((r) => isAbnormalStatus(r.status)),
  };
  return { xray, lab, integratedText, explanationText };
}

function renderXrayDetails(parsed, result = {}) {
  const details = $('xrayReportDetails');
  if (!details) return;
  const x = parsed.xray;
  const context = x.impression || x.findings || x.text;
  const level = classifySeverity(`${x.findings} ${x.impression} ${x.detected} ${x.alerts}`, x.severity, result.warnings);
  const [title, summary] = alertCopy(level, context);
  const points = [
    x.quality ? `${t('imageQuality')}: ${x.quality}` : '',
    x.severity ? `${t('severity')}: ${x.severity}` : '',
    ...splitImportantPoints(x.findings || x.impression || x.text, 3),
  ];

  details.innerHTML = `
    ${alertCard(level, title, summary)}
    <div class="section-card">
      <h3>${escapeHtml(t('importantSummary'))}</h3>
      ${importantList(points)}
    </div>
    ${x.impression ? `<div class="section-card"><h3>${escapeHtml(t('impression'))}</h3><p>${escapeHtml(compactText(x.impression, 430))}</p></div>` : ''}
    ${x.findings ? `<div class="section-card"><h3>${escapeHtml(t('findings'))}</h3><p>${escapeHtml(compactText(x.findings, 430))}</p></div>` : ''}
    ${x.detected ? `<div class="section-card"><h3>${escapeHtml(t('importantFindings'))}</h3>${chips(splitImportantPoints(x.detected, 8), level !== 'normal')}</div>` : ''}
    ${x.recommendations ? `<div class="section-card"><h3>${escapeHtml(t('recommendations'))}</h3>${importantList(splitImportantPoints(x.recommendations, 4))}</div>` : ''}
  `;
}

function renderLabDetails(parsed, result = {}) {
  const details = $('labReportDetails');
  if (!details) return;
  const lab = parsed.lab;
  const abnormalNames = lab.abnormalRows.map((r) => `${r.test}: ${r.value}${r.unit ? ' ' + r.unit : ''} (${r.status})`);
  const context = lab.interpretation || abnormalNames.join('; ') || lab.text;
  const level = classifySeverity(`${lab.interpretation} ${abnormalNames.join(' ')}`, '', result.warnings);
  const [title, summary] = alertCopy(level, context);
  const labPoints = abnormalNames.length ? abnormalNames.slice(0, 6) : splitImportantPoints(lab.interpretation || lab.text, 4);

  details.innerHTML = `
    ${alertCard(level, title, summary)}
    <div class="section-card">
      <h3>${escapeHtml(t('labImportantValues'))}</h3>
      ${labPoints.length ? importantList(labPoints) : `<p>${escapeHtml(t('noAbnormalLab'))}</p>`}
      ${renderLabTable(lab.rows)}
      <p class="no-raw-note">${escapeHtml(t('rawHidden'))}</p>
    </div>
    ${lab.interpretation ? `<div class="section-card"><h3>${escapeHtml(t('labInterpretation'))}</h3><p>${escapeHtml(compactText(lab.interpretation, 520))}</p></div>` : ''}
  `;
}

function renderIntegratedSummary(parsed) {
  const el = $('integratedSummary');
  if (!el) return;
  const integrated = compactText(parsed.integratedText, 640);
  const explanation = compactText(parsed.explanationText, 480);
  const labAbnormal = parsed.lab?.abnormalRows?.map((r) => `${r.test} ${r.status}`).join(', ') || '';
  const level = classifySeverity(`${parsed.xray?.impression || ''} ${parsed.xray?.findings || ''} ${integrated} ${labAbnormal}`, parsed.xray?.severity || '');
  const [title, summary] = alertCopy(level, integrated || parsed.xray?.impression || labAbnormal);

  el.classList.remove('empty-state');
  el.innerHTML = `
    ${alertCard(level, title, summary)}
    <div class="section-card">
      <h3>${escapeHtml(t('integratedInterpretation'))}</h3>
      <p>${escapeHtml(integrated || t('integratedEmpty'))}</p>
    </div>
    ${explanation ? `<div class="section-card"><h3>${escapeHtml(t('medicalExplanation'))}</h3><p>${escapeHtml(explanation)}</p></div>` : ''}
  `;
}

function renderParsedReport(kind, reportHtml, result = {}) {
  const parsed = parseReport(reportHtml);
  if (kind === 'xray') {
    state.xrayParsed = parsed.xray;
    renderXrayDetails(parsed, result);
  }
  if (kind === 'lab') {
    state.labParsed = parsed.lab;
    renderLabDetails(parsed, result);
  }
  renderIntegratedSummary(parsed);
}

function renderReportActions(reportUrl) {
  const el = $('reportActions');
  if (!el) return;
  el.innerHTML = reportUrl ? reportButtonsHtml(reportUrl, true) : '';
}

async function renderAnalysisResult(result, targetId, kind) {
  const reportUrl = renderAnalysisShell(result, targetId, kind);
  updateResultBadge(kind === 'xray' ? 'xrayResultBadge' : 'labResultBadge', result);
  if (reportUrl) {
    try {
      const html = await loadReportHtml(reportUrl);
      renderParsedReport(kind, html, result);
    } catch (err) {
      const details = $(`${kind}ReportDetails`);
      if (details) details.innerHTML = `<h3>${escapeHtml(kind === 'xray' ? t('xrayCompleted') : t('labCompleted'))}</h3><p>${escapeHtml(t('reportLoadFailed'))} ${escapeHtml(err.message || '')}</p>`;
    }
  }
}

async function createPatient() {
  setBusy(true, t('creatingPatient'));
  setStatus('patientStatus', t('creatingPatient'));
  const body = {
    patient_name: $('patientName').value.trim(),
    age: $('age').value ? Number($('age').value) : null,
    sex: $('sex').value || null,
    phone: null,
    symptoms_or_notes: $('notes').value.trim() || null,
  };
  if (!body.patient_name) throw new Error(t('patientNameRequired'));
  const patient = await requestJson(`${getApiBase()}/patients`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) });
  setPatientId(patient.patient_id);
  setWorkflowStep('stepPatient', 'done');
  setWorkflowStep('stepXray', 'active');
  setStatus('patientStatus', `${t('patientCreated')}: ${patient.patient_id}`, 'success');
  setBusy(false);
  return patient;
}

async function useExistingPatient() {
  const patientId = getPatientId();
  if (!patientId) throw new Error(t('enterPatientId'));
  setBusy(true, t('loadingPatient'));
  setStatus('patientStatus', t('loadingPatient'));
  const patient = await requestJson(`${getApiBase()}/patients/${encodeURIComponent(patientId)}`);
  setPatientId(patient.patient_id);
  $('patientName').value = patient.patient_name || '';
  $('age').value = patient.age ?? '';
  $('sex').value = patient.sex || '';

  $('notes').value = patient.symptoms_or_notes || '';
  setWorkflowStep('stepPatient', 'done');
  setWorkflowStep('stepXray', 'active');
  setStatus('patientStatus', `${t('usingPatient')}: ${patient.patient_id}`, 'success');
  await loadExistingContext(patient.patient_id);
  setBusy(false);
}

async function getPatientFiles(patientId) { return await requestJson(`${getApiBase()}/patients/${encodeURIComponent(patientId)}/files`, { method: 'GET' }); }
function hasFileType(files, kind) { return Array.isArray(files) && files.some((item) => String(item.file_type || '').toLowerCase() === kind); }

async function uploadFile(kind) {
  const patientId = getPatientId();
  if (!patientId) throw new Error(t('createOrLoadFirst'));
  const input = kind === 'xray' ? $('xrayFile') : $('labFile');
  const statusId = kind === 'xray' ? 'xrayStatus' : 'labStatus';
  if (!input || !input.files || !input.files.length) throw new Error(t('chooseFileFirst'));
  const form = new FormData();
  form.append('file', input.files[0]);
  const endpoint = kind === 'xray' ? 'xray' : 'lab';
  setBusy(true, t('uploading'));
  setStatus(statusId, t('uploading'));
  const result = await requestJson(`${getApiBase()}/patients/${encodeURIComponent(patientId)}/files/${endpoint}`, { method: 'POST', body: form });
  const files = await getPatientFiles(patientId);
  if (!hasFileType(files, kind)) throw new Error(t('fileMissingAfterUpload'));
  setStatus(statusId, t('uploadSuccess'), 'success');
  setBusy(false);
  return result;
}

async function ensureFileUploaded(kind) {
  const patientId = getPatientId();
  if (!patientId) throw new Error(t('createOrLoadFirst'));
  const input = kind === 'xray' ? $('xrayFile') : $('labFile');
  const existingFiles = await getPatientFiles(patientId);
  if (hasFileType(existingFiles, kind)) return true;
  if (input && input.files && input.files.length) {
    await uploadFile(kind);
    return true;
  }
  throw new Error(t('noUploadedFile'));
}

async function analyzeXray() {
  const patientId = getPatientId();
  if (!patientId) throw new Error(t('createOrLoadFirst'));
  setBusy(true, t('analyzingXray'));
  setStatus('xrayStatus', t('checkingXray'));
  await ensureFileUploaded('xray');
  setStatus('xrayStatus', t('xrayMayTake'));
  const result = await requestJson(`${getApiBase()}/patients/${encodeURIComponent(patientId)}/analysis/xray`, { method: 'POST' });
  await renderAnalysisResult(result, 'xrayResult', 'xray');
  if (result.status === 'fallback' || result.source === 'fallback') {
    setStatus('xrayStatus', t('xrayFallback'), 'error');
  } else {
    state.chatReady = true;
    updatePatientBadges();
    setWorkflowStep('stepXray', 'done');
    setWorkflowStep('stepLab', 'active');
    setWorkflowStep('stepChat', 'active');
    $('chatSourceBadge').textContent = t('contextReady');
    $('chatSourceBadge').className = 'state-pill state-pill--success';
    setStatus('xrayStatus', t('xrayDone'), 'success');
  }
  setBusy(false);
}

async function analyzeLab() {
  const patientId = getPatientId();
  if (!patientId) throw new Error(t('createOrLoadFirst'));
  setBusy(true, t('analyzingLab'));
  setStatus('labStatus', t('checkingLab'));
  await ensureFileUploaded('lab');
  setStatus('labStatus', t('labMayTake'));
  const result = await requestJson(`${getApiBase()}/patients/${encodeURIComponent(patientId)}/analysis/lab`, { method: 'POST' });
  await renderAnalysisResult(result, 'labResult', 'lab');
  if ((result.warnings || []).length) setStatus('labStatus', t('labDoneWarnings'), 'error');
  else { setWorkflowStep('stepLab', 'done'); setStatus('labStatus', t('labDone'), 'success'); }
  setBusy(false);
}

function addChatMessage(role, text, source = '') {
  const wrap = $('chatMessages');
  if (!wrap) return;
  const div = document.createElement('div');
  div.className = `message ${role}`;
  const content = document.createElement('div');
  content.textContent = text;
  div.appendChild(content);
  if (source) {
    const badge = document.createElement('span');
    badge.className = 'message__source';
    badge.textContent = `${t('sourceLabel')}: ${prettySource(source)}`;
    div.appendChild(badge);
  }
  wrap.appendChild(div);
  wrap.scrollTop = wrap.scrollHeight;
}

async function sendChat() {
  const patientId = getPatientId();
  if (!patientId) throw new Error(t('createOrLoadFirst'));
  const question = $('chatQuestion').value.trim();
  if (!question) return;
  addChatMessage('user', question);
  $('chatQuestion').value = '';
  setBusy(true, t('askingAssistant'));
  setStatus('chatStatus', t('sendingQuestion'));
  const result = await requestJson(`${getApiBase()}/patients/${encodeURIComponent(patientId)}/chat`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ question }) });
  addChatMessage('assistant', result.answer, result.source || 'unknown');
  $('chatSourceBadge').textContent = prettySource(result.source || 'unknown');
  $('chatSourceBadge').className = result.source === 'remote_ai' ? 'state-pill state-pill--success' : 'state-pill state-pill--warning';
  setWorkflowStep('stepChat', 'done');
  setStatus('chatStatus', result.note || t('answerReceived'), 'success');
  setBusy(false);
}

async function loadChatHistory(patientId) {
  try {
    const messages = await requestJson(`${getApiBase()}/patients/${encodeURIComponent(patientId)}/chat/history`);
    const wrap = $('chatMessages');
    if (!wrap || !Array.isArray(messages) || !messages.length) return;
    wrap.innerHTML = '';
    messages.forEach((msg) => addChatMessage(msg.role === 'user' ? 'user' : 'assistant', msg.content));
    state.chatReady = true;
    updatePatientBadges();
    $('chatSourceBadge').textContent = t('contextReady');
    $('chatSourceBadge').className = 'state-pill state-pill--success';
  } catch { /* optional */ }
}

async function loadLatestReport(patientId) {
  const reports = await requestJson(`${getApiBase()}/patients/${encodeURIComponent(patientId)}/reports`);
  if (!Array.isArray(reports) || !reports.length) return null;
  const latest = reports[0];
  const reportUrl = getReportUrl(`/api/patients/${patientId}/reports/${latest.id}/download`);
  state.latestReportUrl = reportUrl;
  renderReportActions(reportUrl);
  const html = await loadReportHtml(reportUrl);
  renderParsedReport('xray', html);
  renderParsedReport('lab', html);
  return latest;
}

async function loadExistingContext(patientId) { await Promise.allSettled([loadLatestReport(patientId), loadChatHistory(patientId)]); }

async function refreshReports() {
  const patientId = getPatientId();
  if (!patientId) throw new Error(t('createOrLoadFirst'));
  setStatus('patientStatus', t('refreshingReports'));
  const latest = await loadLatestReport(patientId);
  setStatus('patientStatus', latest ? `${t('refreshedReport')}: ${latest.filename}` : t('noReports'), latest ? 'success' : '');
}

function previewSelectedImage(inputId, previewId) {
  const input = $(inputId);
  const preview = $(previewId);
  if (!input || !preview) return;
  input.addEventListener('change', () => {
    const file = input.files && input.files[0];
    if (!file) { preview.innerHTML = `<span>${escapeHtml(inputId === 'xrayFile' ? t('noXrayPreview') : t('noLabPreview'))}</span>`; return; }
    const url = URL.createObjectURL(file);
    preview.innerHTML = `<img src="${url}" alt="preview" />`;
  });
}

function bindClick(id, handler, statusId) {
  const el = $(id);
  if (!el) return;
  el.addEventListener('click', async () => {
    try { el.disabled = true; await handler(); }
    catch (err) { setSystemError(t('actionFailed')); setStatus(statusId, err.message || String(err), 'error'); }
    finally {
      el.disabled = false;
      if (document.querySelector('.system-card .dot')?.classList.contains('dot--error')) setTimeout(() => setBusy(false), 1800);
    }
  });
}



function applyTheme(theme) {
  state.theme = theme === 'dark' ? 'dark' : 'light';
  localStorage.setItem('ai_doctor_theme', state.theme);
  document.documentElement.dataset.theme = state.theme;
  updateThemeButtons();
}

function toggleTheme() {
  applyTheme(state.theme === 'dark' ? 'light' : 'dark');
}

function updateThemeButtons() {
  const label = state.theme === 'dark' ? t('themeLight') : t('themeDark');
  ['themeToggleBtn', 'authThemeToggleBtn'].forEach((id) => {
    const button = $(id);
    if (button) button.textContent = label;
  });
}

function updatePasswordToggleLabels() {
  document.querySelectorAll('[data-toggle-password]').forEach((button) => {
    const target = $(button.dataset.togglePassword);
    const isVisible = target?.type === 'text';
    button.textContent = isVisible ? t('hidePassword') : t('showPassword');
  });
}

function initializeDisplayControls() {
  applyTheme(state.theme);
  $('themeToggleBtn')?.addEventListener('click', toggleTheme);
  $('authThemeToggleBtn')?.addEventListener('click', toggleTheme);
  $('authArBtn')?.addEventListener('click', () => setLanguage('ar'));
  $('authEnBtn')?.addEventListener('click', () => setLanguage('en'));

  document.querySelectorAll('[data-toggle-password]').forEach((button) => {
    button.addEventListener('click', () => {
      const input = $(button.dataset.togglePassword);
      if (!input) return;
      input.type = input.type === 'password' ? 'text' : 'password';
      updatePasswordToggleLabels();
      input.focus();
    });
  });

  const scrollButton = $('scrollTopBtn');
  if (scrollButton) {
    const updateScrollButton = () => scrollButton.classList.toggle('is-visible', window.scrollY > 420);
    window.addEventListener('scroll', updateScrollButton, { passive: true });
    scrollButton.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
    updateScrollButton();
  }
}

const AUTH_ACCOUNTS_KEY = 'ai_doctor_doctor_accounts_v1';
const AUTH_SESSION_KEY = 'ai_doctor_current_doctor_session_v2';

function getDoctorAccounts() {
  try {
    const raw = localStorage.getItem(AUTH_ACCOUNTS_KEY);
    const parsed = raw ? JSON.parse(raw) : [];
    return Array.isArray(parsed) ? parsed : [];
  } catch {
    return [];
  }
}

function saveDoctorAccounts(accounts) {
  localStorage.setItem(AUTH_ACCOUNTS_KEY, JSON.stringify(accounts));
}

function normalizeEmail(email) {
  return String(email || '').trim().toLowerCase();
}

async function hashPassword(password) {
  const value = String(password || '');
  if (window.crypto?.subtle && window.TextEncoder) {
    const data = new TextEncoder().encode(value);
    const digest = await crypto.subtle.digest('SHA-256', data);
    return Array.from(new Uint8Array(digest)).map((byte) => byte.toString(16).padStart(2, '0')).join('');
  }
  return btoa(unescape(encodeURIComponent(value)));
}

function getCurrentDoctor() {
  try {
    const raw = sessionStorage.getItem(AUTH_SESSION_KEY);
    return raw ? JSON.parse(raw) : null;
  } catch {
    return null;
  }
}

function setAuthStatus(text, type = '') {
  const el = $('authStatus');
  if (!el) return;
  el.textContent = text || '';
  el.classList.toggle('error', type === 'error');
  el.classList.toggle('success', type === 'success');
}

function showAuthMode(mode) {
  const isRegister = mode === 'register';
  $('loginForm')?.classList.toggle('is-hidden', isRegister);
  $('registerForm')?.classList.toggle('is-hidden', !isRegister);
  $('loginTabBtn')?.classList.toggle('is-active', !isRegister);
  $('registerTabBtn')?.classList.toggle('is-active', isRegister);
  setAuthStatus('');
}

function updateAuthVisibility() {
  const doctor = getCurrentDoctor();
  const isAuthenticated = Boolean(doctor?.email);

  $('authScreen')?.classList.toggle('is-hidden', isAuthenticated);
  document.querySelectorAll('.app-protected').forEach((el) => el.classList.toggle('is-hidden', !isAuthenticated));

  const badge = $('doctorSessionBadge');
  if (badge) {
    badge.classList.toggle('is-hidden', !isAuthenticated);
    badge.textContent = isAuthenticated ? `${t('loggedInAs')}: ${doctor.name || doctor.email}` : '';
  }

  $('logoutBtn')?.classList.toggle('is-hidden', !isAuthenticated);
}

async function registerDoctor(event) {
  event.preventDefault();
  const name = $('registerName')?.value.trim() || '';
  const email = normalizeEmail($('registerEmail')?.value);
  const password = $('registerPassword')?.value || '';
  const confirm = $('registerPasswordConfirm')?.value || '';

  if (password.length < 6) {
    setAuthStatus(t('weakPassword'), 'error');
    return;
  }
  if (password !== confirm) {
    setAuthStatus(t('passwordsDoNotMatch'), 'error');
    return;
  }

  const accounts = getDoctorAccounts();
  if (accounts.some((account) => account.email === email)) {
    setAuthStatus(t('accountExists'), 'error');
    return;
  }

  const password_hash = await hashPassword(password);
  const account = {
    id: `doctor_${Date.now()}`,
    name,
    email,
    password_hash,
    created_at: new Date().toISOString(),
  };

  accounts.push(account);
  saveDoctorAccounts(accounts);
  sessionStorage.setItem(AUTH_SESSION_KEY, JSON.stringify({ id: account.id, name: account.name, email: account.email }));
  setAuthStatus(t('accountCreated'), 'success');
  updateAuthVisibility();
}

async function loginDoctor(event) {
  event.preventDefault();
  const email = normalizeEmail($('loginEmail')?.value);
  const password = $('loginPassword')?.value || '';
  const password_hash = await hashPassword(password);
  const account = getDoctorAccounts().find((item) => item.email === email && item.password_hash === password_hash);

  if (!account) {
    setAuthStatus(t('invalidCredentials'), 'error');
    return;
  }

  sessionStorage.setItem(AUTH_SESSION_KEY, JSON.stringify({ id: account.id, name: account.name, email: account.email }));
  setAuthStatus(t('loginSuccess'), 'success');
  updateAuthVisibility();
}

function logoutDoctor() {
  sessionStorage.removeItem(AUTH_SESSION_KEY);
  localStorage.removeItem('ai_doctor_current_doctor_v1');
  state.patientId = '';
  state.latestReportUrl = '';
  state.chatReady = false;
  updatePatientBadges();
  updateAuthVisibility();
  showAuthMode('login');
}

function initializeAuth() {
  $('loginTabBtn')?.addEventListener('click', () => showAuthMode('login'));
  $('registerTabBtn')?.addEventListener('click', () => showAuthMode('register'));
  $('loginForm')?.addEventListener('submit', loginDoctor);
  $('registerForm')?.addEventListener('submit', registerDoctor);
  $('logoutBtn')?.addEventListener('click', logoutDoctor);
  updateAuthVisibility();
}


function initializeFrontend() {
  initializeDisplayControls();
  setLanguage(state.lang);
  initializeAuth();
  renderSeverityLegend();
  updatePatientBadges();
  previewSelectedImage('xrayFile', 'xrayPreview');
  previewSelectedImage('labFile', 'labPreview');
  bindClick('createPatientBtn', createPatient, 'patientStatus');
  bindClick('loadPatientBtn', useExistingPatient, 'patientStatus');
  bindClick('uploadXrayBtn', async () => uploadFile('xray'), 'xrayStatus');
  bindClick('uploadLabBtn', async () => uploadFile('lab'), 'labStatus');
  bindClick('analyzeXrayBtn', analyzeXray, 'xrayStatus');
  bindClick('analyzeLabBtn', analyzeLab, 'labStatus');
  bindClick('sendChatBtn', sendChat, 'chatStatus');
  bindClick('refreshReportsBtn', refreshReports, 'patientStatus');
  $('langArBtn')?.addEventListener('click', () => setLanguage('ar'));
  $('langEnBtn')?.addEventListener('click', () => setLanguage('en'));

  const chatQuestion = $('chatQuestion');
  if (chatQuestion) {
    chatQuestion.addEventListener('keydown', async (event) => {
      if (event.key === 'Enter') {
        event.preventDefault();
        try { await sendChat(); }
        catch (err) { setSystemError(t('chatFailed')); setStatus('chatStatus', err.message || String(err), 'error'); }
      }
    });
  }

  document.querySelectorAll('.quick-prompt').forEach((button) => {
    button.addEventListener('click', () => {
      const question = state.lang === 'ar' ? button.dataset.questionAr : button.dataset.questionEn;
      $('chatQuestion').value = question || '';
      $('chatQuestion').focus();
    });
  });
}

initializeFrontend();
