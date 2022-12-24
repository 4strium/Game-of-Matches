
;--------------------------------
; Includes

  !include "MUI2.nsh"
  !include "logiclib.nsh"

;--------------------------------
; Custom defines
  !define NAME "Game of Matches"
  !define APPFILE "Game_matches_en.exe"
  !define VERSION "1.1.0"
  !define SLUG "${NAME} v${VERSION}"
  !define REGUNINSTKEY "dfe8613b-32a5-4670-b4af-e7b73fdb83de" ;Using a GUID here is not a bad idea
  !define REGHKEY HKLM ;Assuming RequestExecutionLevel admin AKA all user/machine install
  !define REGPATH_WINUNINST "Software\Microsoft\Windows\CurrentVersion\Uninstall"


;--------------------------------
; General

  Name "${NAME}"
  OutFile "${NAME} Installer.exe"
  InstallDir "$PROGRAMFILES\${NAME}"
  InstallDirRegKey HKCU "Software\${NAME}" ""
  RequestExecutionLevel admin
  BrandingText "The Game of Matches - 2022"

;--------------------------------
; UI
  
  !define MUI_ICON "app\icon\LOGO_v1.ico"
  !define MUI_UNICON "app\icon\Uninstaller_icon.ico"
  !define MUI_HEADERIMAGE
  !define MUI_WELCOMEFINISHPAGE_BITMAP "assets\welcome.bmp"
  !define MUI_HEADERIMAGE_BITMAP "assets\head.bmp"
  !define MUI_HEADERIMAGE_UNBITMAP "assets\head.bmp"
  !define MUI_ABORTWARNING
  !define MUI_WELCOMEPAGE_TITLE "${SLUG} Installation"
  !define MUI_FINISHPAGE_RUN ${APPFILE}

;--------------------------------
; Pages
  
  ; Installer pages
  !insertmacro MUI_PAGE_WELCOME
  !insertmacro MUI_PAGE_LICENSE "license.txt"
  !insertmacro MUI_PAGE_COMPONENTS
  !insertmacro MUI_PAGE_DIRECTORY
  !insertmacro MUI_PAGE_INSTFILES
  !insertmacro MUI_PAGE_FINISH

  ; Uninstaller pages
  !insertmacro MUI_UNPAGE_CONFIRM
  !insertmacro MUI_UNPAGE_INSTFILES


  ; Set UI language
  !insertmacro MUI_LANGUAGE "English"

;--------------------------------
; Section - Install App

  Section "-hidden app"
    SectionIn RO
    SetOutPath "$INSTDIR"
    File /r "app\*.*" 
    WriteRegStr ${REGHKEY} "Software\${NAME}" "" $INSTDIR
    WriteUninstaller "$INSTDIR\Uninstall.exe"
  SectionEnd
;--------------------------------
; Add the program in Windows program list
  Section
    WriteRegStr ${REGHKEY} "${REGPATH_WINUNINST}\${REGUNINSTKEY}" "DisplayName" "${NAME}"
    WriteRegStr ${REGHKEY} "${REGPATH_WINUNINST}\${REGUNINSTKEY}" "DisplayIcon" '"$INSTDIR\${APPFILE}"'
    WriteRegStr ${REGHKEY} "${REGPATH_WINUNINST}\${REGUNINSTKEY}" "UninstallString" '"$INSTDIR\Uninstall.exe"'
    WriteRegStr ${REGHKEY} "${REGPATH_WINUNINST}\${REGUNINSTKEY}" "Publisher" "Romain Mellaza"
    WriteRegStr ${REGHKEY} "${REGPATH_WINUNINST}\${REGUNINSTKEY}" "DisplayVersion" "${VERSION}"
  SectionEnd

;--------------------------------
; Section - Shortcut

  Section "Desktop Shortcut" DeskShort
    CreateShortCut "$DESKTOP\${NAME}.lnk" "$INSTDIR\${APPFILE}"
  SectionEnd

;--------------------------------
; Descriptions

  ;Language strings
  LangString DESC_DeskShort ${LANG_ENGLISH} "Create a desktop shortcut."

  ;Assign language strings to sections
  !insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
    !insertmacro MUI_DESCRIPTION_TEXT ${DeskShort} $(DESC_DeskShort)
  !insertmacro MUI_FUNCTION_DESCRIPTION_END

;--------------------------------
; Remove empty parent directories

  Function un.RMDirUP
    !define RMDirUP '!insertmacro RMDirUPCall'

    !macro RMDirUPCall _PATH
          push '${_PATH}'
          Call un.RMDirUP
    !macroend

    ; $0 - current folder
    ClearErrors

    Exch $0
    ;DetailPrint "ASDF - $0\.."
    RMDir "$0\.."

    IfErrors Skip
    ${RMDirUP} "$0\.."
    Skip:

    Pop $0

  FunctionEnd

;--------------------------------
; Section - Uninstaller

Section "Uninstall"

  ;Delete Shortcut
  Delete "$DESKTOP\${NAME}.lnk"

  ;Delete Uninstall
  Delete "$INSTDIR\Uninstall.exe"

  ;Delete Folder
  RMDir /r "$INSTDIR"
  ${RMDirUP} "$INSTDIR"

  DeleteRegKey /ifempty ${REGHKEY} "Software\${NAME}"

  DeleteRegKey ${REGHKEY} "${REGPATH_WINUNINST}\${REGUNINSTKEY}"


SectionEnd