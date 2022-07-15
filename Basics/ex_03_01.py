sh = input('Enter hours: ')
sr = input('Enter rate: ')
fh = float(sh)
fr = float(sr)

if fh > 40:
    print('overtime')
    reg = fh * fr
    otp = (fh - 40) * fr * 1.5
    print('Reg = ',reg,'OTP = ',otp)
    xp = reg + otp
else:
    print('Regular')
    xp = fh * fr

print('Pay: ', xp)
