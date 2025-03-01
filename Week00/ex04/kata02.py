kata = (2019, 9, 25, 3, 30)
# $> python3 kata02.py | cat -e
# 09/25/2019 03:30$
# $> python3 kata02.py | wc -c
# 17
# $>
count = 0
for x in kata:
    count+=1
    if x<0: print('negative value detected, Abort'), exit()

if count!=5: print('bad number of arguments, Abort'), exit()

year, month, day, hour, minutes = kata
print(f"{month:02}/{day:02}/{year:04} {hour:02}:{minutes:02}", end='')
