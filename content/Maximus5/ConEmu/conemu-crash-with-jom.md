Title: Crash only within ConEmu when running jom.exe
Date: 2021-08-20 18:00
Modified: 2010-12-05 19:30
Tags: Maximus5, ConEmu, Jom
Slug: conemu-crash-with-jom
Authors: alberthdev
Summary: Crash occurs within ConEmu when running jom.exe in special cases

{! colorbox.html !}

# Gist
When using Jom v1.1.3 to try and build a nmake Makefile in ConEmu via cmd, Jom will crash. Repeating the same exact commands in the Windows Command Prompt yields no crash.

# Extra Information
## Crash Screenshots

**Crash repro w/ConEmu hook:**

[![Crash Repro]({attach}/images/Maximus5/ConEmu/conemu-crash-with-jom/crash-repro.png){: width=300px}]({attach}/images/Maximus5/ConEmu/conemu-crash-with-jom/crash-repro.png "Crash repro w/ConEmu hook"){: class="imgbox" width=600px}

**Crash info (pasted below):**

[![Crash Repro]({attach}/images/Maximus5/ConEmu/conemu-crash-with-jom/crash-info.png){: width=300px}]({attach}/images/Maximus5/ConEmu/conemu-crash-with-jom/crash-info.png "Crash info w/ConEmu hook"){: class="imgbox" width=600px}

**Works in CMD:**

[![Same Command Working in CMD]({attach}/images/Maximus5/ConEmu/conemu-crash-with-jom/cmd-run.png){: width=300px}]({attach}/images/Maximus5/ConEmu/conemu-crash-with-jom/cmd-run.png "Same Command Working in CMD"){: class="imgbox" width=600px}

## Crash Info from PowerShell/Event Log

```
:::pwsh-session
C:\JomCrashRepro>powershell
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\JomCrashRepro> Get-EventLog -LogName Application -Newest 1 -EntryType Error | Select-Object -Property *


EventID            : 1000
MachineName        : WIN-VJH6V04CD8M
Data               : {}
Index              : 3542
Category           : Application Crashing Events
CategoryNumber     : 100
EntryType          : Error
Message            : Faulting application name: jom.exe, version: 0.0.0.0, time stamp: 0x5c110064
                     Faulting module name: ConEmuHk.dll, version: 21.8.16.0, time stamp: 0x611ae490
                     Exception code: 0xc0000005
                     Fault offset: 0x0001f950
                     Faulting process id: 0xb2c
                     Faulting application start time: 0x01d7965af35b5631
                     Faulting application path: C:\staging\jom-1.1.3\jom.exe
                     Faulting module path: C:\vagrant\ConEmuAlpha\App\ConEmu\ConEmu\ConEmuHk.dll
                     Report Id: 0e6ab4a3-47f2-4688-9f05-08a54e16b271
                     Faulting package full name:
                     Faulting package-relative application ID:
Source             : Application Error
ReplacementStrings : {jom.exe, 0.0.0.0, 5c110064, ConEmuHk.dll...}
InstanceId         : 1000
TimeGenerated      : 8/21/2021 7:06:26 AM
TimeWritten        : 8/21/2021 7:06:26 AM
UserName           :
Site               :
Container          :
```

## ConEmu's Help > About/Help > SysInfo tab 
```
:::text
ConEmu 210816 [32] Startup Info
  OsVer: 10.0.17763.x64, Product: server, SP: 0.0, Suite: 0x110
  Build: 1809, UBR: 1637, ReactOS: 0, Rsrv: 0, WINE: 0, PE: 0, R2: 0
  DBCS: 0, IMM: 1, Remote: 0, ACP: 1252, OEMCP: 437, Admin: 1
  StartTime: 2021-08-21 07:04:23.317
  AppID: 46198a6229d66711fa3aa2958e1da614::169
  Desktop: `Winsta0\Default`, SessionId: 1, ConsoleSessionId: 1, Theming: 1, DWM: 0
  Title: `C:\vagrant\ConEmuAlpha\App\ConEmu\ConEmu.exe`
  Size: {0,0},{0,0}
  Flags: 0x00000000, ShowWindow: 0, ConHWnd: 0x00000000
  char: 1, short: 2, int: 4, long: 4, u64: 8
  Handles: 0x00000000, 0x00000000, 0x00000000
  StdFlags: In=x0 (Mode=-1) Out=x0 (Mode=-1) Err=x0 (Mode=-1)
  Current PID: 1708, TID: 2780
  Active HKL: 0x04090409
  GetKeyboardLayoutList: 0x04090409
CmdLine: "C:\vagrant\ConEmuAlpha\App\ConEmu\ConEmu.exe" /LoadCfgFile "C:\vagrant\ConEmuAlpha\Data\settings\ConEmu.xml" -log
ExecMod: C:\vagrant\ConEmuAlpha\App\ConEmu\ConEmu.exe
WorkDir: C:\vagrant\ConEmuAlpha
PathEnv: C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Windows\System32\OpenSSH\;C:\ProgramData\chocolatey\bin;C:\opscode\chef\bin\;C:\Program Files\OpenSSH-Win64;C:\Program Files\dotnet\;C:\Strawberry\c\bin;C:\Strawberry\perl\site\bin;C:\Strawberry\perl\bin;C:\Users\vagrant\AppData\Local\Microsoft\WindowsApps;C:\Users\vagrant\.dotnet\tools
ConFont: 0	Lucida Console	00	Consolas
CMD's AutoRuns: {not defined}
Foreground: x00040076 {-8,-8}-{1032,776} 'VirtualConsoleClass' - cmd - powershell (Admin)
MouseCursor: {563,428} MouseMonitor: 00010001 StartMonitor: 00000000
Display: bpp=32, planes=1, align=1, vrefr=64, shade=x00000000, rast=x00007E99, dpi=96x96, per-mon-dpi=1
Monitors (dpi: WholeDesktop, Effective, Angular, RAW):
  00010001: {0,0}-{1024,768} (1024x768), Working: {0,0}-{1024,768} (1024x768), dpi: {96,96};{96,96};{96,96};{96,96} `\\.\DISPLAY1` <<== Primary
Modules:
  00340000-005B2FFF   273000 C:\vagrant\ConEmuAlpha\App\ConEmu\ConEmu.exe
  77E60000-77FFBFFF   19C000 C:\Windows\SYSTEM32\ntdll.dll
  779B0000-77A8FFFF    E0000 C:\Windows\System32\KERNEL32.DLL
  75780000-7597AFFF   1FB000 C:\Windows\System32\KERNELBASE.dll
  77250000-77293FFF    44000 C:\Windows\System32\SHLWAPI.dll
  77D30000-77DEFFFF    C0000 C:\Windows\System32\msvcrt.dll
  75AC0000-75D36FFF   277000 C:\Windows\System32\combase.dll
  76BC0000-76CE2FFF   123000 C:\Windows\System32\ucrtbase.dll
  75A00000-75ABEFFF    BF000 C:\Windows\System32\RPCRT4.dll
  75620000-7563FFFF    20000 C:\Windows\System32\SspiCli.dll
  75610000-75619FFF     A000 C:\Windows\System32\CRYPTBASE.dll
  75E20000-75E81FFF    62000 C:\Windows\System32\bcryptPrimitives.dll
  766C0000-76738FFF    79000 C:\Windows\System32\sechost.dll
  76880000-768A2FFF    23000 C:\Windows\System32\GDI32.dll
  76A40000-76BA7FFF   168000 C:\Windows\System32\gdi32full.dll
  75980000-759FFFFF    80000 C:\Windows\System32\msvcp_win.dll
  77B90000-77D28FFF   199000 C:\Windows\System32\USER32.dll
  75D40000-75D56FFF    17000 C:\Windows\System32\win32u.dll
  76940000-76A39FFF    FA000 C:\Windows\System32\COMDLG32.dll
  76140000-761C8FFF    89000 C:\Windows\System32\shcore.dll
  76CF0000-77245FFF   556000 C:\Windows\System32\SHELL32.dll
  75DE0000-75E1AFFF    3B000 C:\Windows\System32\cfgmgr32.dll
  772F0000-778F1FFF   602000 C:\Windows\System32\windows.storage.dll
  75D60000-75DDDFFF    7E000 C:\Windows\System32\advapi32.dll
  75F60000-75F7BFFF    1C000 C:\Windows\System32\profapi.dll
  77DF0000-77E43FFF    54000 C:\Windows\System32\powrprof.dll
  76800000-7680EFFF     F000 C:\Windows\System32\kernel.appcore.dll
  76640000-76651FFF    12000 C:\Windows\System32\cryptsp.dll
  77A90000-77B8BFFF    FC000 C:\Windows\System32\ole32.dll
  77910000-779A5FFF    96000 C:\Windows\System32\OLEAUT32.dll
  753F0000-753F7FFF     8000 C:\Windows\SYSTEM32\VERSION.dll
  74D10000-74D22FFF    13000 C:\Windows\SYSTEM32\NETAPI32.dll
  75400000-7560EFFF   20F000 C:\Windows\WinSxS\x86_microsoft.windows.common-controls_6595b64144ccf1df_6.0.17763.1637_none_261d79df67c867cb\COMCTL32.dll
  75170000-75193FFF    24000 C:\Windows\SYSTEM32\WINMM.dll
  75140000-75162FFF    23000 C:\Windows\SYSTEM32\WINMMBASE.dll
  74D00000-74D0AFFF     B000 C:\Windows\SYSTEM32\NETUTILS.DLL
  74CE0000-74CF4FFF    15000 C:\Windows\SYSTEM32\SAMCLI.DLL
  75F30000-75F54FFF    25000 C:\Windows\System32\IMM32.DLL
  75370000-753EAFFF    7B000 C:\Windows\system32\uxtheme.dll
  74CB0000-74CD5FFF    26000 C:\Windows\SYSTEM32\dwmapi.dll
  75F80000-76117FFF   198000 C:\Windows\System32\CRYPT32.dll
  76BB0000-76BBDFFF     E000 C:\Windows\System32\MSASN1.dll
  75640000-7577BFFF   13C000 C:\Windows\System32\MSCTF.dll
  6F780000-6F84CFFF    CD000 C:\vagrant\ConEmuAlpha\App\ConEmu\ConEmu\ConEmuCD.dll
  768B0000-76930FFF    81000 C:\Windows\System32\clbcatq.dll
  74CA0000-74CAEFFF     F000 C:\Windows\SYSTEM32\Wtsapi32.dll
  74C50000-74C92FFF    43000 C:\Windows\SYSTEM32\WINSTA.dll
```

## Windows Version Info
```
:::pwsh-session
PS C:\JomCrashRepro> Get-ComputerInfo OsName,OsVersion,OsBuildNumber,OsHardwareAbstractionLayer,WindowsVersion


OsName                     : Microsoft Windows Server 2019 Standard Evaluation
OsVersion                  : 10.0.17763
OsBuildNumber              : 17763
OsHardwareAbstractionLayer : 10.0.17763.1432
WindowsVersion             : 1809
```

```
:::batch
C:\JomCrashRepro>ver

Microsoft Windows [Version 10.0.17763.1637]
```