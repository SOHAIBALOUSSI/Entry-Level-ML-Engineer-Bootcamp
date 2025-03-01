kata = (0, 4, 132.42222, 10000, 12345.67)


# $> python3 kata04.py
# module_00, ex_04 : 132.42, 1.00e+04, 1.23e+04
# $> python3 kata04.py | cut -c 10,18
# ,:

module, ex, decimal1, integer ,decimal2 = kata

if module<0 or module>99 or ex<0 or ex>99:print('bad arguments'), exit()

print(f"module_{module:02}, ex_{ex:02} : {decimal1:.02f}, {integer :.2e}, {decimal2:.2e}", end='')