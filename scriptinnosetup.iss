; Script generado por Inno Setup Script Wizard.
; Ver el archivo de ayuda de Inno Setup para más información sobre la creación de scripts de Inno Setup.

[Setup]
; Título del instalador
AppName=Conversor de MKV a MP3
; Versión del instalador
AppVersion=1.0
; Directorio de salida del instalador
DefaultDirName={pf}\Conversor de MKV a MP3
; Nombre del archivo de salida del instalador
OutputBaseFilename=Instalador_Conversor_MKV_a_MP3
; Icono del instalador
SetupIconFile=icono.ico
; Privilegios de administrador
PrivilegesRequired=admin
; Cierra las aplicaciones antes de la instalación
CloseApplications=yes
; Reinicia después de la instalación si es necesario
AlwaysRestart=no

[Files]
; Archivos a incluir en el instalador
Source: "dist\main.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "CONVIRTIENDO.gif"; DestDir: "{app}"; Flags: ignoreversion
Source: "icono.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
; Crear un acceso directo en el menú de inicio
Name: "{group}\Conversor de MKV a MP3"; Filename: "{app}\main.exe"; WorkingDir: "{app}"; IconFilename: "{app}\icono.ico"
; Crear un acceso directo en el escritorio
Name: "{commondesktop}\Conversor de MKV a MP3"; Filename: "{app}\main.exe"; WorkingDir: "{app}"; IconFilename: "{app}\icono.ico"

[Run]
; Ejecutar el programa después de la instalación
Filename: "{app}\main.exe"; Description: "Ejecutar Conversor de MKV a MP3"; Flags: nowait postinstall skipifsilent
