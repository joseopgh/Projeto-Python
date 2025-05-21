mt = float(input('Uma distancia em metros :'))
km = mt/1000
hm = mt/100
dam = mt/10
dm = mt*10
cm = mt*100
mm = mt*1000
print('A medida de {}m corresponde a \n{:.3}km \n{:.2}hm \n{:.1}dam \n{}dm \n{}cm \n{}mm' .format(mt, km, hm, dam, dm, cm, mm))
