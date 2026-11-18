Unicode true
SetCompressor /SOLID lzma
!include "MUI2.nsh"

!define APPNAME "C++ Yosh dasturchilar"
!define EXENAME "C++ Yosh dasturchilar.exe"
!define VERSION "2.0.1"
!define UNKEY "Software\Microsoft\Windows\CurrentVersion\Uninstall\CppYoshDasturchilar"

Name "${APPNAME}"
OutFile "dist\CPP_Yosh_dasturchilar_Setup_${VERSION}.exe"
InstallDir "$LOCALAPPDATA\Programs\CppYoshDasturchilar"
InstallDirRegKey HKCU "${UNKEY}" "InstallLocation"
RequestExecutionLevel user
BrandingText "${APPNAME} ${VERSION} — Xayrullo Kulmatov"

VIProductVersion "2.0.1.0"
VIAddVersionKey "ProductName" "${APPNAME}"
VIAddVersionKey "FileDescription" "${APPNAME} - o'rnatish dasturi"
VIAddVersionKey "FileVersion" "${VERSION}"
VIAddVersionKey "LegalCopyright" "© 2026 Xayrullo Kulmatov"
VIAddVersionKey "CompanyName" "Xayrullo Kulmatov"
VIAddVersionKey "Comments" "Qizi Munisa Habibullayeva uchun"

!define MUI_ICON "build\icon.ico"
!define MUI_UNICON "build\icon.ico"
!define MUI_WELCOMEPAGE_TITLE "C++ Yosh dasturchilar"
!define MUI_WELCOMEPAGE_TEXT "Kodi va Malika bilan C++ dasturlashni o'rganamiz!$\r$\n$\r$\nMuallif: Xayrullo Kulmatov.$\r$\nQizi Munisa Habibullayeva uchun yaratilgan.$\r$\n$\r$\nBu dastur kitobni kompyuteringizga o'rnatadi. Mavzularni o'qish, o'z izohlaringizni yozish va to'xtagan joydan davom ettirish mumkin.$\r$\n$\r$\nDavom etish uchun $\"Keyingi$\" tugmasini bosing."
!define MUI_FINISHPAGE_RUN "$INSTDIR\${EXENAME}"
!define MUI_FINISHPAGE_RUN_TEXT "Dasturni hozir ishga tushirish"
!define MUI_ABORTWARNING

!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_LANGUAGE "Uzbek"

Section "Install"
  SetOutPath "$INSTDIR"
  File /r "dist\win-unpacked\*.*"
  WriteUninstaller "$INSTDIR\Uninstall.exe"
  CreateShortCut "$DESKTOP\${APPNAME}.lnk" "$INSTDIR\${EXENAME}" "" "$INSTDIR\${EXENAME}" 0
  CreateDirectory "$SMPROGRAMS\${APPNAME}"
  CreateShortCut "$SMPROGRAMS\${APPNAME}\${APPNAME}.lnk" "$INSTDIR\${EXENAME}" "" "$INSTDIR\${EXENAME}" 0
  CreateShortCut "$SMPROGRAMS\${APPNAME}\O'chirish (Uninstall).lnk" "$INSTDIR\Uninstall.exe"
  WriteRegStr HKCU "${UNKEY}" "DisplayName" "${APPNAME}"
  WriteRegStr HKCU "${UNKEY}" "DisplayVersion" "${VERSION}"
  WriteRegStr HKCU "${UNKEY}" "Publisher" "Xayrullo Kulmatov"
  WriteRegStr HKCU "${UNKEY}" "DisplayIcon" "$INSTDIR\${EXENAME}"
  WriteRegStr HKCU "${UNKEY}" "InstallLocation" "$INSTDIR"
  WriteRegStr HKCU "${UNKEY}" "UninstallString" "$\"$INSTDIR\Uninstall.exe$\""
  WriteRegDWORD HKCU "${UNKEY}" "NoModify" 1
  WriteRegDWORD HKCU "${UNKEY}" "NoRepair" 1
SectionEnd

Section "Uninstall"
  Delete "$DESKTOP\${APPNAME}.lnk"
  RMDir /r "$SMPROGRAMS\${APPNAME}"
  RMDir /r "$INSTDIR"
  DeleteRegKey HKCU "${UNKEY}"
SectionEnd
