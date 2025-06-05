# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['music-player.py'],
    pathex=[],
    binaries=[('/usr/lib/libgstreamer-1.0.so', '.'), ('/usr/lib/libgstbase-1.0.so', '.'), ('/usr/lib/libgstapp-1.0.so', '.')],
    datas=[('/usr/lib/qt/plugins/mediaservice', 'PyQt5/Qt/plugins/mediaservice'), ('/usr/lib/qt/plugins/platforms', 'PyQt5/Qt/plugins/platforms'), ('/usr/lib/gstreamer-1.0', 'gstreamer-1.0')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='music-player',
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
)
