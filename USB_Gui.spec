# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['run_GUI.py'],
    pathex=['C:\\home\\sec\\misc\\UsbKeyboard_Mouse_Hacker_Gui-main'],
    binaries=[],
    datas=[('C:\\home\\sec\\misc\\UsbKeyboard_Mouse_Hacker_Gui-main\\css', 'css'),('C:\\home\\sec\\misc\\UsbKeyboard_Mouse_Hacker_Gui-main\\img', 'img')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='USB_Gui',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['img\\myico.ico'],
)
