import * as ResEdit from 'resedit';
import * as PE from 'pe-library';
import fs from 'fs';
const exePath = process.argv[2], ico = process.argv[3];
const exe = PE.NtExecutable.from(fs.readFileSync(exePath), { ignoreCert: true });
const res = PE.NtExecutableResource.from(exe);
const iconFile = ResEdit.Data.IconFile.from(fs.readFileSync(ico));
const groups = ResEdit.Resource.IconGroupEntry.fromEntries(res.entries);
const id = groups.length ? groups[0].id : 1, lang = groups.length ? groups[0].lang : 1033;
ResEdit.Resource.IconGroupEntry.replaceIconsForResource(res.entries, id, lang, iconFile.icons.map(i => i.data));
const vi = ResEdit.Resource.VersionInfo.fromEntries(res.entries)[0];
if (vi) {
  vi.setStringValues({ lang: 1033, codepage: 1200 }, { ProductName: 'C++ Yosh dasturchilar', FileDescription: 'C++ Yosh dasturchilar', CompanyName: 'Xayrullo Kulmatov', LegalCopyright: '© 2026 Xayrullo Kulmatov', Comments: 'Qizi Munisa Habibullayeva uchun' });
  vi.setFileVersion(2, 0, 1, 0); vi.setProductVersion(2, 0, 1, 0);
  vi.outputToResourceEntries(res.entries);
}
res.outputResource(exe);
fs.writeFileSync(exePath, Buffer.from(exe.generate()));
console.log('icon set, groups:', groups.length);
