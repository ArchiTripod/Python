import winreg as _winreg


hkcr = _winreg.OpenKey(_winreg.HKEY_CLASSES_ROOT, "")


with open("classes.txt", "w") as f:
    i = 0
    while True:
        try:
            ctype = _winreg.EnumKey(hkcr, i)
        except EnvironmentError:
            break
        else:
            f.write("%s -> %r\n" % (type(ctype), ctype))
        i += 1

