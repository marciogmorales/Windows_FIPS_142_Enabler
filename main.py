import winreg as wrg

location = wrg.HKEY_LOCAL_MACHINE
reg_path = wrg.OpenKeyEx(location, r"SYSTEM\CurrentControlSet\Control\Lsa\\")
reg_path_read = wrg.OpenKeyEx(location, r"SYSTEM\CurrentControlSet\Control\Lsa\FipsAlgorithmPolicy\\")

print("Checking if FIPS more is already enabled...")
if wrg.QueryValueEx(reg_path_read,"FipsAlgorithmPolicy") == (1, 4):
    print("FIPS mode is already enabled")
    exit()

else:
    if input('Do you want to enable FIPS mode? Press (y/n): ') == "y":
        print("Enabling FIPS mode")
        key_1 = wrg.CreateKey(reg_path, "FipsAlgorithmPolicy")
        wrg.SetValueEx(key_1, "FipsAlgorithmPolicy", 0, wrg.REG_DWORD, 0x00000001)
        print("FIPS mode enabled")
        (wrg.CloseKey(key_1))

    else:
        print("FIPS mode not enabled")
        exit()