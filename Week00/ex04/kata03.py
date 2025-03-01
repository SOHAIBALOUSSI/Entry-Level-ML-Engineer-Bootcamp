kata = "aaaaaaaaaaaaaaaaaaaaaaaaThe right formattta"

if len(kata) > 42: print('too loong kata string'), exit()

print(f"{kata:{'-'}>{42}}",end='')