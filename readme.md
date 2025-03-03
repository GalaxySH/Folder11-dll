# Folder11 Ico

Automated repo for [Folder11](https://github.com/icon11-community/Folder11).

## Bundling the icons to `.dll`

Compile the `.rc` file to a RES file with the VS Native Tools Command Prompt:
```
rc.exe Folder11Icons.rc
```

Convert `.res` to `.dll`:
```
link.exe /DLL /NOENTRY /OUT:Folder11Icons.dll Folder11Icons.res
```

Open `.dll` directly in the properties>customize prompt and select from all icons
