// C++ Yosh dasturchilar — o'quvchi oynasi
(function () {
  const B = window.BOOK;
  const $ = (s) => document.querySelector(s);
  const store = {
    get(k, d) { try { const v = localStorage.getItem(k); return v === null ? d : JSON.parse(v); } catch (e) { return d; } },
    set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} },
  };

  // Interfeys yozuvlari: [joriy alifbo, yangi alifbo]
  const UI = {
    sub: ['Yosh dasturchilar uchun', 'Yoş dasturçilar uçun'],
    search: ['Kitobdan qidirish...', 'Kitobdan qidiriş...'],
    alpha: ['Alifbo:', 'Alifbo:'], a0: ['Joriy', 'Joriy'], a1: ['Yangi', 'Yangi'],
    font: ['Shrift:', 'Şrift:'],
    toc: ['Mundarijani yashirish/ko\'rsatish', 'Mundarijani yaşiriş/körsatiş'],
    smaller: ['Harfni kichraytirish', 'Harfni kiçraytiriş'], bigger: ['Harfni kattalashtirish', 'Harfni kattalaştiriş'],
    theme: ['Tungi / kunduzgi rejim', 'Tungi / kunduzgi rejim'],
    notes: ['Izohlar', 'Izohlar'], myNotes: ['📝 Mening izohlarim', '📝 Mening izohlarim'],
    notesHint: ['Bu yerga shu mavzu bo\'yicha o\'zingga kerakli izohlarni yoz: tushunmagan joylaring, savollaring, eslab qolish kerak bo\'lgan narsalar. Izohlar avtomatik saqlanadi.',
                'Bu yerga şu mavzu böyiça özingga kerakli izohlarni yoz: tuşunmagan joylaring, savollaring, eslab qoliş kerak bölgan narsalar. Izohlar avtomatik saqlanadi.'],
    notesPh: ['Masalan: "for tsikli 3 qismdan iborat — boshlanish; shart; qadam"', 'Masalan: "for tsikli 3 qismdan iborat — boşlaniş; şart; qadam"'],
    saved: ['✓ saqlandi', '✓ saqlandi'], saving: ['saqlanmoqda...', 'saqlanmoqda...'],
    allNotes: ['📚 Barcha izohlarim', '📚 Barcha izohlarim'], export: ['💾 Faylga saqlash', '💾 Faylga saqlaş'],
    noNotes: ['Hali izoh yozilmagan.', 'Hali izoh yozilmagan.'], open: ['Ochish →', 'Ochiş →'],
    exported: ['Izohlar saqlandi: ', 'Izohlar saqlandi: '],
    close: ['Yopish', 'Yopiş'],
    prev: ['← Oldingi', '← Oldingi'], next: ['Keyingi →', 'Keyingi →'],
    done: ['✓ O\'qib bo\'ldim', '✓ Öqib böldim'], undone: ['○ O\'qilmagan', '○ Öqilmagan'],
    read: ['o\'qildi', 'öqildi'], copied: ['Kod nusxalandi', 'Kod nusxalandi'],
    welcomeBack: ['Xush kelibsan!', 'Xuş kelibsan!'],
    resumeQ: ['Oxirgi marta «{t}» mavzusida to\'xtagan eding. O\'qilgan joydan davom etaymi?', 'Oxirgi marta «{t}» mavzusida töxtagan eding. Öqilgan joydan davom etaymi?'],
    yes: ['Ha, davom etamiz', 'Ha, davom etamiz'], no: ['Yo\'q, boshidan boshlayman', 'Yöq, boşidan boşlayman'],
    here: ['📍 Shu yerda to\'xtagan eding', '📍 Şu yerda töxtagan eding'],
    found: ['ta mavzuda topildi', 'ta mavzuda topildi'],
    credit: ['Muallif: Xayrullo Kulmatov\nQizi Munisa Habibullayeva uchun yaratilgan', 'Muallif: Xayrullo Kulmatov\nQizi Munisa Habibullayeva uçun yaratilgan'],
    dedic: ['💜 Bu dastur <b>Xayrullo Kulmatov</b> tomonidan qizi <b>Munisa Habibullayeva</b> uchun yaratildi.', '💜 Bu dastur <b>Xayrullo Kulmatov</b> tomonidan qizi <b>Munisa Habibullayeva</b> uçun yaratildi.'],
    autoDone: ['Mavzu oxiriga yetding — «O\'qib bo\'ldim» deb belgilandi 🎉', 'Mavzu oxiriga yetding — «Öqib böldim» deb belgilandi 🎉'],
  };
  const FONTS = {
    segoe: '"Segoe UI", "Nunito", Arial, sans-serif',
    arial: 'Arial, Helvetica, sans-serif',
    times: '"Times New Roman", Times, serif',
    verdana: 'Verdana, Geneva, sans-serif',
  };

  const flat = [];
  B.forEach((m, mi) => m.topics.forEach((t, ti) => flat.push({ mi, ti, m, t, key: m.t[0] + ' › ' + t.t[0] })));
  const keyIdx = Object.fromEntries(flat.map((f, i) => [f.key, i]));

  let A = store.get('alpha', 0);              // 0 = joriy, 1 = yangi
  let cur = 0;
  let done = store.get('done2', {});          // mavzu kaliti -> true
  let pos = store.get('pos', {});             // mavzu kaliti -> {i: element, o: siljish}
  let last = store.get('last', null);         // oxirgi mavzu kaliti
  let fs = store.get('fs', 19);
  let font = store.get('font', 'segoe');
  let notes = {};
  const u = (k) => (UI[k] || [k, k])[A];
  const plainText = (h) => h.replace(/<[^>]+>/g, ' ').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&').replace(/\s+/g, ' ').toLowerCase();
  const textCache = {};
  const topicText = (i) => textCache[i] || (textCache[i] = plainText(flat[i].t.h[0] + ' ' + flat[i].t.h[1] + ' ' + flat[i].t.t.join(' ')));

  // ---------- Mundarija va qidiruv ----------
  function buildToc() {
    const q = $('#search').value.trim().toLowerCase();
    const toc = $('#toc'); toc.innerHTML = '';
    const open = store.get('open', {});
    let hits = 0;
    B.forEach((m, mi) => {
      const items = flat.map((f, i) => ({ f, i })).filter(x => x.f.mi === mi)
        .filter(x => !q || topicText(x.i).includes(q));
      if (q && !items.length) return;
      hits += items.length;
      const d = document.createElement('div');
      d.className = 'mod' + (open[mi] || q || flat[cur].mi === mi ? ' open' : '');
      const nDone = flat.filter(f => f.mi === mi && done[f.key]).length;
      const total = flat.filter(f => f.mi === mi).length;
      d.innerHTML = `<div class="mt"><span class="arr">▸</span><span>${m.t[A]} <small>${nDone}/${total}</small></span></div><div class="tl"></div>`;
      d.querySelector('.mt').onclick = () => { d.classList.toggle('open'); const o = store.get('open', {}); o[mi] = d.classList.contains('open'); store.set('open', o); };
      const tl = d.querySelector('.tl');
      items.forEach(({ f, i }) => {
        const e = document.createElement('div');
        e.className = 'tp' + (i === cur ? ' cur' : '');
        const nt = notes[f.key] && notes[f.key].trim() ? '<span class="nt" title="Izoh bor">📝</span>' : '';
        e.innerHTML = `<span class="ck">${done[f.key] ? '✓' : ''}</span><span class="tt">${f.t.t[A]}</span>${nt}`;
        e.onclick = () => go(i, true);
        tl.appendChild(e);
      });
      toc.appendChild(d);
    });
    if (q) { const h = document.createElement('div'); h.className = 'hits'; h.textContent = hits + ' ' + u('found'); toc.prepend(h); }
    const n = flat.filter(f => done[f.key]).length;
    $('#pbar').style.width = (100 * n / flat.length) + '%';
    $('#ptext').textContent = `${n} / ${flat.length} ${u('read')}`;
    const c = toc.querySelector('.tp.cur'); if (c) c.scrollIntoView({ block: 'nearest' });
  }

  // ---------- Sahifa ----------
  function highlight(root, q) {
    if (!q || q.length < 2) return null;
    let first = null;
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
    const nodes = []; while (walker.nextNode()) nodes.push(walker.currentNode);
    for (const n of nodes) {
      const low = n.nodeValue.toLowerCase(); let k = low.indexOf(q);
      if (k < 0) continue;
      const frag = document.createDocumentFragment(); let s = 0;
      while (k >= 0) {
        frag.append(n.nodeValue.slice(s, k));
        const mk = document.createElement('mark'); mk.textContent = n.nodeValue.slice(k, k + q.length); frag.append(mk);
        if (!first) first = mk;
        s = k + q.length; k = low.indexOf(q, s);
      }
      frag.append(n.nodeValue.slice(s)); n.replaceWith(frag);
    }
    return first;
  }

  function render() {
    const f = flat[cur];
    const head = f.t.t[0] === 'Kirish' && f.ti === 0 ? `<h1>${f.m.t[A]}</h1>` : `<h2>${f.t.t[A]}</h2>`;
    const page = $('#page');
    page.innerHTML = (cur === 0 ? `<div class="dedic">${u('dedic')}</div>` : '') + head + f.t.h[A] + '<div id="endmark"></div>';
    page.querySelectorAll('.copy').forEach(b => b.onclick = () => {
      navigator.clipboard.writeText(b.parentElement.querySelector('pre').innerText); toast(u('copied'));
    });
    page.querySelectorAll('figure img').forEach(img => img.onclick = () => { $('#imgBig').src = img.src; $('#imgDlg').classList.remove('hidden'); });
    $('#prevBtn').disabled = cur === 0; $('#nextBtn').disabled = cur === flat.length - 1;
    $('#doneBtn').textContent = done[f.key] ? u('done') : u('undone');
    $('#doneBtn').classList.toggle('on', !!done[f.key]);
    document.title = f.t.t[A] + ' — C++ Yosh dasturchilar';
    $('#ntopic').textContent = f.t.t[A];
    $('#ntext').value = notes[f.key] || '';
    $('#ntext').placeholder = u('notesPh');
    $('#nsaved').textContent = '';
    const q = $('#search').value.trim().toLowerCase();
    const mk = highlight(page, q);
    return mk;
  }

  // Joriy o'qish joyini saqlash: ekranda ko'rinayotgan birinchi abzas
  function anchorNow() {
    const page = $('#page'); const top = page.getBoundingClientRect().top;
    const els = page.querySelectorAll('[data-s], h2, h1, figure, .code, .tbl');
    for (let k = 0; k < els.length; k++) {
      const r = els[k].getBoundingClientRect();
      if (r.bottom > top + 10) return { i: k, o: Math.round(top - r.top) };
    }
    return { i: 0, o: 0 };
  }
  function restoreAnchor(p, mark) {
    const page = $('#page');
    const els = page.querySelectorAll('[data-s], h2, h1, figure, .code, .tbl');
    const el = els[p.i];
    if (!el) { page.scrollTop = 0; return; }
    page.scrollTop = el.offsetTop - page.offsetTop + (p.o || 0);
    if (mark && p.i > 0) {
      el.classList.add('resume');
      const tag = document.createElement('div'); tag.className = 'here'; tag.textContent = u('here');
      el.before(tag);
      setTimeout(() => { el.classList.remove('resume'); tag.remove(); }, 6000);
    }
  }
  let saveT = null;
  const asking = () => !$('#resumeDlg').classList.contains('hidden');
  function savePos() {
    if (asking()) return;
    clearTimeout(saveT);
    saveT = setTimeout(() => {
      const f = flat[cur]; pos[f.key] = anchorNow(); store.set('pos', pos);
      last = f.key; store.set('last', last);
    }, 300);
  }

  let rendered = false;
  function go(i, keepPlace, opts) {
    if (rendered && flat[cur]) { pos[flat[cur].key] = anchorNow(); store.set('pos', pos); }
    cur = Math.max(0, Math.min(flat.length - 1, i));
    if (!(opts && opts.noSave)) { last = flat[cur].key; store.set('last', last); }
    const mk = render(); buildToc(); rendered = true;
    const page = $('#page');
    if (opts && opts.anchor) restoreAnchor(opts.anchor, opts.mark);
    else if (mk) mk.scrollIntoView({ block: 'center' });
    else if (opts && opts.top) page.scrollTop = 0;
    else if (keepPlace && pos[flat[cur].key]) restoreAnchor(pos[flat[cur].key], opts && opts.mark);
    else page.scrollTop = 0;
    updateReadbar();
  }

  function applyUI() {
    document.querySelectorAll('[data-ui]').forEach(e => e.textContent = u(e.dataset.ui));
    document.querySelectorAll('[data-tip]').forEach(e => e.title = u(e.dataset.tip));
    $('#search').placeholder = u('search');
    $('#prevBtn').textContent = u('prev'); $('#nextBtn').textContent = u('next');
    $('#alpha').children[0].textContent = u('a0'); $('#alpha').children[1].textContent = u('a1');
    [...$('#alpha').children].forEach(b => b.classList.toggle('on', Number(b.dataset.a) === A));
    document.documentElement.style.setProperty('--fs', fs + 'px');
    document.documentElement.style.setProperty('--font', FONTS[font] || FONTS.segoe);
    $('#fontSel').value = font; $('#fsVal').textContent = fs + 'px';
  }

  function toast(t, ms) {
    const d = document.createElement('div'); d.className = 'toast'; d.textContent = t;
    document.body.appendChild(d); setTimeout(() => d.remove(), ms || 1800);
  }

  // ---------- O'qish chizig'i va avtomatik belgilash ----------
  function updateReadbar() {
    const p = $('#page');
    const max = p.scrollHeight - p.clientHeight;
    const r = max <= 0 ? 1 : p.scrollTop / max;
    $('#readfill').style.width = (r * 100) + '%';
    const f = flat[cur];
    if (r > 0.985 && max > 200 && !done[f.key]) {
      done[f.key] = true; store.set('done2', done);
      $('#doneBtn').textContent = u('done'); $('#doneBtn').classList.add('on');
      buildToc(); toast(u('autoDone'), 2600);
    }
  }
  $('#page').addEventListener('scroll', () => { updateReadbar(); savePos(); }, { passive: true });

  // ---------- Izohlar ----------
  let noteT = null;
  $('#ntext').addEventListener('input', () => {
    const key = flat[cur].key; notes[key] = $('#ntext').value;
    $('#nsaved').textContent = u('saving');
    clearTimeout(noteT);
    noteT = setTimeout(async () => {
      await window.api.notesSet(key, notes[key]);
      $('#nsaved').textContent = u('saved');
      const had = !!document.querySelector('.tp.cur .nt'), has = !!notes[key].trim();
      if (had !== has) buildToc();
    }, 500);
  });
  function notesText() {
    const out = ['C++ Yosh dasturchilar — Mening izohlarim', '='.repeat(42), ''];
    flat.forEach(f => { const t = (notes[f.key] || '').trim(); if (t) out.push('■ ' + f.m.t[A], '  ' + f.t.t[A], '', t, '', '-'.repeat(42), ''); });
    return out.join('\r\n');
  }
  async function exportNotes() {
    const p = await window.api.notesExport(notesText());
    if (p) toast(u('exported') + p, 4000);
  }
  function showAll() {
    const list = $('#allList'); list.innerHTML = '';
    const items = flat.map((f, i) => ({ f, i })).filter(x => (notes[x.f.key] || '').trim());
    if (!items.length) list.innerHTML = `<p class="hint">${u('noNotes')}</p>`;
    items.forEach(({ f, i }) => {
      const d = document.createElement('div'); d.className = 'nitem';
      d.innerHTML = `<div class="nh"><span><small>${f.m.t[A]}</small><br><b></b></span><button></button></div><pre></pre>`;
      d.querySelector('b').textContent = f.t.t[A];
      d.querySelector('pre').textContent = notes[f.key];
      const b = d.querySelector('button'); b.textContent = u('open');
      b.onclick = () => { $('#allDlg').classList.add('hidden'); go(i, true); };
      list.appendChild(d);
    });
    $('#allDlg').classList.remove('hidden');
  }
  $('#nAll').onclick = showAll;
  $('#nExport').onclick = exportNotes;
  $('#allExport').onclick = exportNotes;
  $('#allClose').onclick = () => $('#allDlg').classList.add('hidden');
  $('#notesBtn').onclick = () => {
    const hid = document.body.classList.toggle('nonotes'); store.set('nonotes', hid);
    $('#notesBtn').classList.toggle('on', !hid);
  };

  // ---------- Boshqa tugmalar ----------
  $('#prevBtn').onclick = () => go(cur - 1, false, { top: true });
  $('#nextBtn').onclick = () => go(cur + 1, false, { top: true });
  $('#doneBtn').onclick = () => { const k = flat[cur].key; done[k] = !done[k]; store.set('done2', done); render(); buildToc(); restoreAnchor(anchorNowSafe(), false); };
  function anchorNowSafe() { return pos[flat[cur].key] || { i: 0, o: 0 }; }
  $('#alpha').onclick = (e) => {
    const a = e.target.dataset.a; if (a === undefined) return;
    const p = anchorNow(); A = Number(a); store.set('alpha', A); applyUI(); render(); buildToc(); restoreAnchor(p, false);
  };
  function refont(fn) { const p = anchorNow(); fn(); applyUI(); restoreAnchor(p, false); }
  $('#fontPlus').onclick = () => refont(() => { fs = Math.min(32, fs + 1); store.set('fs', fs); });
  $('#fontMinus').onclick = () => refont(() => { fs = Math.max(13, fs - 1); store.set('fs', fs); });
  $('#fontSel').onchange = () => refont(() => { font = $('#fontSel').value; store.set('font', font); });
  $('#themeBtn').onclick = () => { document.body.classList.toggle('dark'); store.set('dark', document.body.classList.contains('dark')); };
  $('#menuBtn').onclick = () => document.body.classList.toggle('noside');
  let qT = null;
  $('#search').oninput = () => { clearTimeout(qT); qT = setTimeout(() => { buildToc(); const mk = render(); if (mk) mk.scrollIntoView({ block: 'center' }); }, 250); };
  $('#imgDlg').onclick = () => $('#imgDlg').classList.add('hidden');
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') document.querySelectorAll('.dlg').forEach(d => { if (d.id !== 'resumeDlg') d.classList.add('hidden'); });
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA' || e.target.tagName === 'SELECT') return;
    if (e.key === 'ArrowRight' && e.altKey) go(cur + 1, false, { top: true });
    else if (e.key === 'ArrowLeft' && e.altKey) go(cur - 1, false, { top: true });
    else if ((e.key === '+' || e.key === '=') && e.ctrlKey) { e.preventDefault(); $('#fontPlus').click(); }
    else if (e.key === '-' && e.ctrlKey) { e.preventDefault(); $('#fontMinus').click(); }
  });
  window.addEventListener('beforeunload', () => { if (rendered && flat[cur] && !asking()) { pos[flat[cur].key] = anchorNow(); store.set('pos', pos); store.set('last', flat[cur].key); } });

  // ---------- Ishga tushish ----------
  async function start() {
    if (store.get('dark', false)) document.body.classList.add('dark');
    if (store.get('nonotes', false)) { document.body.classList.add('nonotes'); $('#notesBtn').classList.remove('on'); }
    try { notes = await window.api.notesGet() || {}; } catch (e) { notes = {}; }
    applyUI();
    const li = last && keyIdx[last] !== undefined ? keyIdx[last] : -1;
    const lp = li >= 0 ? pos[last] : null;
    go(0, false, { top: true, noSave: true });
    if (li > 0 || (lp && lp.i > 0)) {
      $('#resumeText').textContent = u('resumeQ').replace('{t}', flat[li].t.t[A]);
      $('#resumeYes').textContent = u('yes'); $('#resumeNo').textContent = u('no');
      $('#resumeDlg').classList.remove('hidden');
      $('#resumeYes').focus();
      $('#resumeYes').onclick = () => { $('#resumeDlg').classList.add('hidden'); go(li, false, { anchor: lp || { i: 0, o: 0 }, mark: true }); };
      $('#resumeNo').onclick = () => { $('#resumeDlg').classList.add('hidden'); pos = {}; store.set('pos', pos); go(0, false, { top: true }); };
    }
  }
  start();
})();
