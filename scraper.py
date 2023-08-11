from mylib import ar,ar_akhr,en
from time import sleep

chooser=input("""
choose :
1 - for famous arab community 
2 - for famous english community 
3 - for others arabic community 
""")

if chooser=="1":
    print("famous arabic community was choosed")
    ar()
    sleep(20)
elif chooser=="2":
    print("famous english community was choosed")
    en()
    sleep(20)
elif chooser=="3":
    print("others arab community was choosed")
    ar_akhr()
    sleep(20)
else:
    print("error ")