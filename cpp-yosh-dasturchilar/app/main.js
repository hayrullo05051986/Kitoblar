// C++ Yosh dasturchilar — asosiy jarayon (Electron)
const { app, BrowserWindow, ipcMain, Menu, shell, dialog } = require('electron');
const path = require('path');
const fs = require('fs');

// ---------- Izohlar: foydalanuvchi papkasida JSON faylda saqlanadi ----------
const notesPath = () => path.join(app.getPath('userData'), 'izohlar.json');
function readNotes() { try { return JSON.parse(fs.readFileSync(notesPath(), 'utf8')); } catch (e) { return {}; } }
function writeNotes(n) {
  fs.mkdirSync(path.dirname(notesPath()), { recursive: true });
  const tmp = notesPath() + '.tmp';
  fs.writeFileSync(tmp, JSON.stringify(n, null, 1));
  fs.renameSync(tmp, notesPath());           // yarim yozilgan fayl qolmasligi uchun
}
ipcMain.handle('notes:get', () => readNotes());
ipcMain.handle('notes:set', (_e, key, text) => {
  const n = readNotes();
  if (text && text.trim()) n[key] = text; else delete n[key];
  writeNotes(n); return true;
});
ipcMain.handle('notes:export', async (e, text) => {
  const win = BrowserWindow.fromWebContents(e.sender);
  const r = await dialog.showSaveDialog(win, {
    title: 'Izohlarni saqlash',
    defaultPath: path.join(app.getPath('documents'), 'Mening_izohlarim.txt'),
    filters: [{ name: 'Matn fayli', extensions: ['txt'] }],
  });
  if (r.canceled || !r.filePath) return null;
  fs.writeFileSync(r.filePath, '﻿' + text, 'utf8');   // BOM — Bloknotda o'zbekcha harflar to'g'ri chiqadi
  return r.filePath;
});

function createWindow() {
  const win = new BrowserWindow({
    width: 1360, height: 880, minWidth: 980, minHeight: 600,
    title: 'C++ Yosh dasturchilar',
    icon: path.join(__dirname, 'renderer', 'icon.png'),
    backgroundColor: '#f6f7fb',
    webPreferences: { preload: path.join(__dirname, 'preload.js'), contextIsolation: true, nodeIntegration: false },
  });
  Menu.setApplicationMenu(null);
  win.loadFile(path.join(__dirname, 'renderer', 'index.html'));
  win.webContents.setWindowOpenHandler(({ url }) => { shell.openExternal(url); return { action: 'deny' }; });
  win.webContents.on('before-input-event', (e, input) => {
    if (input.key === 'F11' && input.type === 'keyDown') win.setFullScreen(!win.isFullScreen());
    if (input.key === 'F12' && input.type === 'keyDown') win.webContents.toggleDevTools();
  });
}

// Bitta nusxa: dastur ikkinchi marta ochilsa, avvalgi oyna oldinga chiqadi
if (!app.requestSingleInstanceLock()) app.quit();
else {
  app.on('second-instance', () => { const w = BrowserWindow.getAllWindows()[0]; if (w) { if (w.isMinimized()) w.restore(); w.focus(); } });
  app.whenReady().then(createWindow);
}
app.on('window-all-closed', () => app.quit());
