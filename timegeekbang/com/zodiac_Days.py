# Tuple元祖（）元祖嵌套 unchangable
# List ["1","2"]
zodiac_name = ("1",u"水瓶座","3")
zodiac_days = ((1,20),(2,19),(3,21))
china_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
#m = 2
#d = 15
(m,d) = (2,15)
zodiacDay = filter(lambda x:x<=(m,d),zodiac_days)
zodiac_len = len(list(zodiacDay))
#print(zodiac_name[zodiac_len])
#years = input("input a string:")
#intY = int(years)
#print(years)
# For loop
for z in china_zodiac:
    print(z)
for y in range(2000,2020):
    print("%s is %s Year" %(y,china_zodiac[y%12]))

