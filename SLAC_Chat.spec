# -*- mode: python -*-

block_cipher = None


a = Analysis(['SLAC_Chat.py'],
             pathex=['/home/jacob/Documents/SLAC_Chat/source'],
             binaries=[],
             datas=[],
             hiddenimports=['PyQt5.sip'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

a.datas += [('icon.ico','../assets/icon.ico','DATA'),
	    ('icon.png','../assets/icon.png','DATA'),]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

if sys.platform == 'linux':
	exe = EXE(pyz,
		  a.scripts,
		  a.binaries,
		  a.zipfiles,
		  a.datas,
		  name='SLAC_Chat',
		  debug=False,
		  strip=False,
		  upx=True,
		  runtime_tmpdir=None,
		  console=False,
		  clean=True,
		  onefile=True,
		  hidden_import='PyQt5.sip',
		  icon='../assets/icon.png')

if sys.platform == 'darwin':
	exe = EXE(pyz,
		  a.scripts,
		  a.binaries,
		  a.zipfiles,
		  a.datas,
		  name='SLAC_Chat',
		  debug=False,
		  strip=False,
		  upx=True,
		  runtime_tmpdir=None,
		  console=True,
		  clean=True,
		  onefile=True,
		  hidden_import='PyQt5.sip',
		  icon='../assets/icon.ico')

if sys.platform == 'darwin':
	app = BUNDLE(exe,
		     name='SLAC_Chat.app',
		     info_plist={
		     	'NSHighResolutionCapable': 'True',
			'UIRequiresPersistentWiFi': 'True'
		     },
		     icon='../assets/icon.ico')

if sys.platform == 'win32' or sys.platform == 'win64':
	exe = EXE(pyz,
		  a.scripts,
		  a.binaries,
		  a.zipfiles,
		  a.datas,
		  name='SLAC_Chat.exe',
		  debug=False,
		  strip=False,
		  upx=True,
		  runtime_tmpdir=None,
		  console=False,
		  clean=True,
		  onefile=True,
		  hidden_import='PyQt5.sip',
		  icon='../assets/icon.ico')

