const { contextBridge, ipcRenderer } = require('electron');
contextBridge.exposeInMainWorld('api', {
  notesGet: () => ipcRenderer.invoke('notes:get'),
  notesSet: (key, text) => ipcRenderer.invoke('notes:set', key, text),
  notesExport: (text) => ipcRenderer.invoke('notes:export', text),
});
