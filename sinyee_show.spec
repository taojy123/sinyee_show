# -*- mode: python -*-
a = Analysis([os.path.join(HOMEPATH,'support\\_mountzlib.py'), os.path.join(HOMEPATH,'support\\useUnicode.py'), 'sinyee_show.py'],
             pathex=['E:\\Workspace\\GitHub\\sinyee_show'])
pyz = PYZ(a.pure)
exe = EXE( pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'sinyee_show.exe'),
          debug=False,
          strip=False,
          upx=True,
          console=False )
app = BUNDLE(exe,
             name=os.path.join('dist', 'sinyee_show.exe.app'))
