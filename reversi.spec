# -*- mode: python -*-

block_cipher = None


a = Analysis(['reversi.py'],
             pathex=['D:\\reversi'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
a.datas += [('black.png', '.\\black.png', 'DATA')]
a.datas += [('white.png', '.\\white.png', 'DATA')]
a.datas += [('candidate.png', '.\\candidate.png', 'DATA')]
a.datas += [('board.png', '.\\board.png', 'DATA')]
a.datas += [('empty.png', '.\\empty.png', 'DATA')]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.datas,
          [],
          name='reversi',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='reversi')
