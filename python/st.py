from datetime import datetime
# pre defined vars
dt = datetime.now()
# hackers below
st = input('st\n')
print(f'"{st}"', "is what you wrote!\n")


if st == 'about':
    print("""
    ###HELP GUIDE###
    Q: !!! what is this project?
    A: noone knows. one night at 1/7/2026, a someone decided to make this for no reason.

    some useful trix
    1. do current date (dt)
    2. ? (about)
    3. my ip (ipadr)
    4. author (au)
    thats it for now
    """)
if st == 'dt':
    print(f"!!!{dt}!!!\n")
if st == 'ipadr':
    print(f"!!!12.0.0.1!!!")
if st == 'au':
    print('!!! ajm19826 !!!')
try:
    int(st)
    print("!!! integer detected !!!")
except Exception as e:        
    print("not a integer")
    print("oh no a error, unhandled", e, "!!! try again")


