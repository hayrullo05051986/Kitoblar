// Markup -> Word builder for the C++ book
const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, ImageRun,
  Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle, LevelFormat,
  PageBreak, TableOfContents, Footer, PageNumber, Header,
  Bookmark, InternalHyperlink, Tab, TabStopType, LeaderType, PositionalTab, PositionalTabAlignment, PositionalTabRelativeTo, PositionalTabLeader,
} = require('docx');
const sizeOf = (f) => {
  const b = fs.readFileSync(f); // PNG only
  return { w: b.readUInt32BE(16), h: b.readUInt32BE(20) };
};

const ROOT = __dirname;
const NEW = process.env.ALIFBO === 'new';
const T = (old, nw) => NEW ? nw : old;
const SUF = NEW ? '_new' : '';
const FONT = 'Times New Roman';
const MONO = 'Consolas';
const PAGE_W = 11906, MARGIN = 1134; // A4, 2 cm top/bottom
const M_LEFT = 1701, M_RIGHT = 851;  // chap 3 sm (pereplot uchun), o'ng 1.5 sm
const CONTENT_W = PAGE_W - M_LEFT - M_RIGHT; // 9354 DXA

const NOTE = {
  eslatma:  { label: 'ESLATMA',          fill: 'FFF4D6', bar: 'F2A900' },
  fakt:     { label: 'QIZIQARLI FAKT',   fill: 'E6F4FF', bar: '2D8CFF' },
  maslahat: { label: 'MASLAHAT',         fill: 'E8F8EC', bar: '2EAD5B' },
  mashq:    { label: T('O\'ZING SINAB KO\'R', 'ÖZING SINAB KÖR'), fill: 'F3ECFF', bar: '8A5CF6' },
  diqqat:   { label: 'DIQQAT',           fill: 'FFE9E9', bar: 'E5484D' },
};

function inline(text, base = {}) {
  // **bold**, *italic*, `code`
  const runs = [];
  const re = /(\*\*[^*]+\*\*|`[^`]+`|\*[^*]+\*)/g;
  let last = 0, m;
  while ((m = re.exec(text))) {
    if (m.index > last) runs.push(new TextRun({ text: text.slice(last, m.index), ...base }));
    const t = m[0];
    if (t.startsWith('**')) runs.push(new TextRun({ text: t.slice(2, -2), bold: true, ...base }));
    else if (t.startsWith('`')) runs.push(new TextRun({ text: t.slice(1, -1), font: MONO, color: 'C7254E', ...base, shading: { type: ShadingType.CLEAR, fill: 'F4F4F4', color: 'auto' } }));
    else runs.push(new TextRun({ text: t.slice(1, -1), italics: true, ...base }));
    last = m.index + t.length;
  }
  if (last < text.length) runs.push(new TextRun({ text: text.slice(last), ...base }));
  return runs;
}

const thin = { style: BorderStyle.SINGLE, size: 4, color: 'BFC7D5' };

function codeBlock(lines, kind) {
  const isOut = kind === 'output' || kind === 'terminal';
  const fill = isOut ? '1E1E1E' : 'F6F8FA';
  const color = isOut ? 'E8E8E8' : '1F2328';
  const label = kind === 'terminal' ? 'Terminal:' : (isOut ? 'Natija (ekranda):' : null);
  const children = [];
  if (label) children.push(new Paragraph({ spacing: { before: 0, after: 40 }, children: [new TextRun({ text: label, font: FONT, size: 18, bold: true, color: '9CDCFE' })] }));
  for (const l of lines) {
    const lead = l.match(/^ */)[0].length;
    const body = l.slice(lead);
    const runs = [];
    if (lead) runs.push(new TextRun({ text: ' '.repeat(lead), font: MONO, size: 19 }));
    // comments in green
    const ci = isOut ? -1 : body.indexOf('//');
    if (ci >= 0) {
      if (ci > 0) runs.push(new TextRun({ text: body.slice(0, ci), font: MONO, size: 19, color }));
      runs.push(new TextRun({ text: body.slice(ci), font: MONO, size: 19, color: '2E8B57', italics: true }));
    } else runs.push(new TextRun({ text: body || ' ', font: MONO, size: 19, color }));
    children.push(new Paragraph({ spacing: { before: 0, after: 0, line: 260 }, children: runs }));
  }
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: [CONTENT_W],
    rows: [new TableRow({ cantSplit: lines.length < 25, children: [new TableCell({
      width: { size: CONTENT_W, type: WidthType.DXA },
      shading: { type: ShadingType.CLEAR, fill, color: 'auto' },
      margins: { top: 100, bottom: 100, left: 160, right: 160 },
      borders: { top: thin, bottom: thin, left: { style: BorderStyle.SINGLE, size: 24, color: isOut ? '569CD6' : '4F8EF7' }, right: thin },
      children,
    })] })],
  });
}

function noteBox(type, text) {
  const n = NOTE[type] || NOTE.eslatma;
  const paras = text.split('\\n').map((t, i) => new Paragraph({
    alignment: AlignmentType.JUSTIFIED, spacing: { before: i ? 60 : 0, after: 0, line: 300 },
    children: [ ...(i === 0 ? [new TextRun({ text: n.label + ': ', bold: true, color: n.bar, font: FONT, size: 26 })] : []), ...inline(t, { font: FONT, size: 26 }) ],
  }));
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: [CONTENT_W],
    rows: [new TableRow({ cantSplit: true, children: [new TableCell({
      width: { size: CONTENT_W, type: WidthType.DXA },
      shading: { type: ShadingType.CLEAR, fill: n.fill, color: 'auto' },
      margins: { top: 120, bottom: 120, left: 200, right: 200 },
      borders: { top: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' }, bottom: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' }, right: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' }, left: { style: BorderStyle.SINGLE, size: 36, color: n.bar } },
      children: paras,
    })] })],
  });
}

function table(rows) {
  const cols = rows[0].length;
  const colW = Math.floor(CONTENT_W / cols);
  const widths = Array(cols).fill(colW); widths[cols - 1] = CONTENT_W - colW * (cols - 1);
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: widths,
    rows: rows.map((r, ri) => new TableRow({ tableHeader: ri === 0, children: r.map((c, ci) => new TableCell({
      width: { size: widths[ci], type: WidthType.DXA },
      shading: { type: ShadingType.CLEAR, fill: ri === 0 ? '3B5BDB' : (ri % 2 ? 'FFFFFF' : 'EEF2FF'), color: 'auto' },
      margins: { top: 70, bottom: 70, left: 110, right: 110 },
      borders: { top: thin, bottom: thin, left: thin, right: thin },
      children: [new Paragraph({ spacing: { before: 0, after: 0 }, children: inline(c, ri === 0 ? { bold: true, color: 'FFFFFF', font: FONT, size: 24 } : { font: FONT, size: 24 }) })],
    })) })),
  });
}

function image(file, caption, widthIn) {
  const p = path.join(ROOT, NEW ? 'img_new' : 'img', file);
  const { w, h } = sizeOf(p);
  const wpx = Math.round((widthIn || 6) * 96);
  const hpx = Math.round(wpx * h / w);
  const out = [new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 120, after: 40 }, keepNext: !!caption,
    children: [new ImageRun({ type: 'png', data: fs.readFileSync(p), transformation: { width: wpx, height: hpx }, altText: { title: caption || file, description: caption || file, name: file } })] })];
  if (caption) out.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 0, after: 160 }, children: [new TextRun({ text: caption, italics: true, size: 24, color: '5A6270', font: FONT })] }));
  return out;
}

let listInstance = 0;
const heads = [];
function bm(level, t) { t = t.replace(/`/g, ''); const id = 'toc' + heads.length; heads.push({ level, t, id }); return new Bookmark({ id, children: [new TextRun(t)] }); }
function parse(src) {
  const out = [];
  const lines = src.replace(/\r/g, '').split('\n');
  let i = 0, firstH1 = true;
  let lastList = null;
  const spacer = () => new Paragraph({ spacing: { before: 0, after: 80 }, children: [] });
  while (i < lines.length) {
    let l = lines[i];
    if (!/^(- |\d+\. )/.test(l)) lastList = null;
    if (l.startsWith('```')) {
      const kind = l.slice(3).trim();
      const buf = []; i++;
      while (i < lines.length && !lines[i].startsWith('```')) buf.push(lines[i++]);
      i++;
      out.push(codeBlock(buf, kind)); out.push(spacer());
      continue;
    }
    if (l.startsWith('# ')) {
      out.push(new Paragraph({ heading: HeadingLevel.HEADING_1, pageBreakBefore: true, children: [bm(1, l.slice(2))] }));
    } else if (l.startsWith('## ')) {
      out.push(new Paragraph({ heading: HeadingLevel.HEADING_2, children: [bm(2, l.slice(3))] }));
    } else if (l.startsWith('### ')) {
      out.push(new Paragraph({ heading: HeadingLevel.HEADING_3, children: [new TextRun(l.slice(4))] }));
    } else if (l.startsWith('!img ')) {
      const [f, cap, w] = l.slice(5).split('|').map(s => s.trim());
      out.push(...image(f, cap, w ? parseFloat(w) : 6));
    } else if (l.startsWith('!')) {
      const m = l.match(/^!(\w+)\s+(.*)$/);
      out.push(noteBox(m[1], m[2])); out.push(spacer());
    } else if (l.startsWith('|')) {
      const rows = [];
      while (i < lines.length && lines[i].startsWith('|')) {
        const r = lines[i].trim().replace(/\\\|/g, '\u0001').replace(/^\||\|$/g, '').split('|').map(s => s.trim().replace(/\u0001/g, '|'));
        if (!r.every(c => /^:?-+:?$/.test(c))) rows.push(r);
        i++;
      }
      out.push(table(rows)); out.push(spacer());
      continue;
    } else if (/^- /.test(l)) {
      out.push(new Paragraph({ style: 'Royxat', numbering: { reference: 'bullets', level: 0 }, children: inline(l.slice(2)) }));
    } else if (/^\d+\. /.test(l)) {
      if (lastList !== 'num') { listInstance++; }
      lastList = 'num';
      out.push(new Paragraph({ style: 'Royxat', numbering: { reference: 'numbers', level: 0, instance: listInstance }, children: inline(l.replace(/^\d+\. /, '')) }));
      i++; continue;
    } else if (l.trim() === '') {
      // nothing
    } else {
      out.push(new Paragraph({ style: 'Matn', children: inline(l) }));
    }
    if (l.trim() !== '') out._justH1 = l.startsWith('# ');
    if (/^- /.test(l)) lastList = 'bul';
    i++;
  }
  return out;
}

// ---- assemble ----
const SRC = process.env.SRC || 'merged';
const order = fs.readFileSync(path.join(ROOT, 'src', 'ORDER'), 'utf8').split('\n').map(s => s.trim()).filter(Boolean);
const body = [];
for (const f of order) body.push(...parse(fs.readFileSync(path.join(ROOT, SRC, f), 'utf8')));

function front() {
  const f = path.join(ROOT, SRC, 'front.md');
  if (!fs.existsSync(f)) return [];
  const out = [];
  for (const l of fs.readFileSync(f, 'utf8').split('\n')) {
    if (!l.trim()) continue;
    if (l.startsWith('%%title ')) out.push(new Paragraph({ pageBreakBefore: true, alignment: AlignmentType.CENTER, spacing: { before: 400, after: 360 }, children: [new TextRun({ text: l.slice(8), font: FONT, size: 40, bold: true, color: '3B5BDB' })] }));
    else if (l.startsWith('%%sign ')) out.push(new Paragraph({ alignment: AlignmentType.RIGHT, spacing: { before: 0, after: 0, line: 300 }, children: inline(l.slice(7), { italics: true, font: FONT, size: 28 }) }));
    else out.push(new Paragraph({ alignment: AlignmentType.JUSTIFIED, spacing: { before: 0, after: 200, line: 360 }, indent: { firstLine: 567 }, children: inline(l, { font: FONT, size: 28 }) }));
  }
  return out;
}
const cover = [
  new Paragraph({ spacing: { before: 600, after: 200 }, alignment: AlignmentType.CENTER, children: [new TextRun({ text: T('C++ DASTURLASH TILI', 'C++ DASTURLAŞ TILI'), font: FONT, size: 60, bold: true, color: '3B5BDB' })] }),
  new Paragraph({ spacing: { before: 0, after: 300 }, alignment: AlignmentType.CENTER, children: [new TextRun({ text: T('Yosh dasturchilar uchun qiziqarli qo\'llanma', 'Yoş dasturçilar uçun qiziqarli qöllanma'), font: FONT, size: 32, color: '495057' })] }),
  ...image('cover.png', null, 5.2),
  new Paragraph({ spacing: { before: 300, after: 80 }, alignment: AlignmentType.CENTER, children: [new TextRun({ text: T('Kodi va Malika bilan birga: algoritmlashdan OOP va STL gacha — 15 ta modul, 86 ta mavzu', 'Kodi va Malika bilan birga: algoritmlaşdan OOP va STL gaça — 15 ta modul, 86 ta mavzu'), font: FONT, size: 26, color: '495057' })] }),
  new Paragraph({ spacing: { before: 200, after: 40 }, alignment: AlignmentType.CENTER, children: [new TextRun({ text: T('Muallif: ', 'Muallif: '), font: FONT, size: 28, color: '495057' }), new TextRun({ text: 'Xayrullo Kulmatov', font: FONT, size: 28, bold: true, color: '1C3FAA' })] }),
  new Paragraph({ spacing: { before: 0, after: 200 }, alignment: AlignmentType.CENTER, children: [new TextRun({ text: T('Qizim Munisa Habibullayeva uchun', 'Qizim Munisa Habibullayeva uçun'), font: FONT, size: 26, italics: true, color: '8A5CF6' })] }),
  new Paragraph({ spacing: { before: 0, after: 0 }, alignment: AlignmentType.CENTER, children: [new TextRun({ text: T('Toshkent, 2026', 'Yangi alifbo (Ö, Ğ, Ş, Ç) nashri · Toşkent, 2026'), font: FONT, size: 22, color: '868E96' })] }),
  ...front(),
  new Paragraph({ pageBreakBefore: true, spacing: { after: 200 }, children: [new TextRun({ text: 'Mundarija', font: FONT, size: 36, bold: true, color: '3B5BDB' })] }),
];
const pages = fs.existsSync(path.join(ROOT, 'tocpages' + SUF + '.json')) ? JSON.parse(fs.readFileSync(path.join(ROOT, 'tocpages' + SUF + '.json'), 'utf8')) : {};
for (let k = 0; k < heads.length; k++) {
  const h = heads[k];
  const pg = String(pages[h.id] || '000');
  const top = h.level === 1;
  cover.push(new Paragraph({
    keepNext: top,
    tabStops: [{ type: TabStopType.RIGHT, position: CONTENT_W, leader: LeaderType.DOT }],
    spacing: { before: top ? 160 : 0, after: top ? 40 : 20 },
    indent: { left: top ? 0 : 400 },
    children: [
      new InternalHyperlink({ anchor: h.id, children: [new TextRun({ text: h.t, bold: top, size: top ? 22 : 20, color: top ? '1C3FAA' : '1F2328', font: FONT })] }),
      new TextRun({ children: [new Tab()], size: top ? 22 : 20 }),
      new TextRun({ text: pg, bold: top, size: top ? 22 : 20, font: FONT }),
    ],
  }));
}
fs.writeFileSync(path.join(ROOT, 'heads' + SUF + '.json'), JSON.stringify(heads));

const doc = new Document({
  creator: 'C++ qo\'llanma', title: 'C++ dasturlash tili — yosh dasturchilar uchun',
  
  styles: {
    default: { document: { run: { font: FONT, size: 28 } } },
    paragraphStyles: [
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true,
        run: { font: FONT, size: 44, bold: true, color: 'FFFFFF' },
        paragraph: { spacing: { before: 0, after: 240 }, keepNext: true, outlineLevel: 0, shading: { type: ShadingType.CLEAR, fill: '3B5BDB', color: 'auto' }, indent: { left: 0 }, border: { top: { style: BorderStyle.SINGLE, size: 6, color: '3B5BDB', space: 8 }, bottom: { style: BorderStyle.SINGLE, size: 6, color: '3B5BDB', space: 8 } } } },
      { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true,
        run: { font: FONT, size: 36, bold: true, color: '1C3FAA' },
        paragraph: { spacing: { before: 360, after: 200 }, keepNext: true, outlineLevel: 1, border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: 'F2A900', space: 4 } } } },
      { id: 'Heading3', name: 'Heading 3', basedOn: 'Normal', next: 'Normal', quickFormat: true,
        run: { font: FONT, size: 30, bold: true, color: '2B2D42' },
        paragraph: { spacing: { before: 240, after: 120 }, keepNext: true, outlineLevel: 2 } },
      // Asosiy matn: Times New Roman 14, oldin/keyin 0 pt, qatorlar orasi 1.25, chapdan 0.8 sm
      { id: 'Matn', name: 'Matn (asosiy)', basedOn: 'Normal', next: 'Matn', quickFormat: true,
        run: { font: FONT, size: 28 },
        paragraph: { alignment: AlignmentType.JUSTIFIED, spacing: { before: 0, after: 0, line: 300 }, indent: { left: 454, right: 0 } } },
      { id: 'Royxat', name: 'Royxat', basedOn: 'Normal', next: 'Royxat', quickFormat: true,
        run: { font: FONT, size: 28 },
        paragraph: { alignment: AlignmentType.JUSTIFIED, spacing: { before: 0, after: 0, line: 300 } } },
    ],
  },
  numbering: { config: [
    { reference: 'bullets', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 794, hanging: 340 } } } }] },
    { reference: 'numbers', levels: [{ level: 0, format: LevelFormat.DECIMAL, text: '%1.', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 794, hanging: 340 } } } }] },
  ] },
  sections: [{
    properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: MARGIN, bottom: MARGIN, left: M_LEFT, right: M_RIGHT } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ children: [PageNumber.CURRENT], size: 18, color: '868E96' })] })] }) },
    children: [...cover, ...body],
  }],
});

Packer.toBuffer(doc).then(b => { fs.writeFileSync(path.join(ROOT, process.argv[2] || 'out.docx'), b); console.log('written'); });
