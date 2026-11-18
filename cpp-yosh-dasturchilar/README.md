# C++ Yosh dasturchilar

Kodi va Malika bilan birga: algoritmlashdan OOP va STL gacha — 12 yoshli bolalar uchun
o'zbek tilidagi C++ qo'llanmasi (kitob va Windows dasturi).

**Muallif:** Xayrullo Kulmatov — qizi Munisa Habibullayeva uchun yaratilgan.

## Tarkib

| Papka | Nima bor |
|---|---|
| `app/` | Windows uchun o'quvchi dasturi (Electron): mundarija, qidiruv, to'xtagan joydan davom etish, izohlar, shrift va o'lcham tanlash, joriy/yangi alifbo |
| `book/` | Kitob manbalari: `src/` (asosiy matn), `addons/`, `deep/` (chuqurlashtirilgan bo'limlar), rasm skriptlari va Word kitobni yig'uvchi `build.js` |

## Dasturni o'rnatish

Tayyor o'rnatish faylini **Releases** bo'limidan yuklab oling: `CPP_Yosh_dasturchilar_Setup_<versiya>.exe`.

## Manbadan yig'ish

Kitob (Word):

```bash
cd book
python3 merge.py            # src + addons + deep -> merged/
node build.js kitob.docx    # joriy alifbo
ALIFBO=new SRC=merged_new node build.js kitob_yangi.docx   # yangi alifbo (avval merged_new yarating)
```

Dastur:

```bash
cd book && python3 make_app_content.py ../app/renderer
cd ../app && npm install && npm start      # sinash
npx electron-builder --win dir --x64       # Windows papkasi; o'rnatish fayli installer.nsi orqali (makensis)
```

## Mualliflik huquqi

© 2026 Xayrullo Kulmatov. Barcha huquqlar himoyalangan — [LICENSE.md](LICENSE.md).
