# -*- mode: python -*-

block_cipher = None

added_files = [
         ( 'peru.ico', '.' ),
         ( 'peru_fisico.png', '.' )
         ]
a = Analysis(['input.py'],
             pathex=['D:\\JYUPANQUI\\PROYECTOS\\ConsultaDistrito'],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='input',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False, icon='icon.ico')
