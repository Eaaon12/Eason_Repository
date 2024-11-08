import time, math
import sys



def caculation(oneYearS, excp):
    # 一個是正常的1-12月每月天數，一個是閏年的每月天數
    eachDayofMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    eachDayofMonthExcp = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # countDay代表當年已經過了多少天
    countDay = 0

    # onedayS代表一天的總秒數
    onedayS = 86400

    # indexOf代表第幾月
    indexOf = 0

    # 當年是閏年
    if(excp == 1):
        # 每跑一次月份+1，減掉當月月份天數的總秒數
        # 當傳進來的當年已過總秒數小於0，則停止，-1便可以得到當年過了幾個月
        # countDay再扣掉當月的天數便可以得到今年到上個月為止過了多少天
        for x in eachDayofMonthExcp:
            indexOf += 1
            oneYearS -= (x*onedayS)
            countDay += x
            if(oneYearS < 0):
                return[(indexOf-1), (countDay-x)]
    # 當年不是閏年
    else:
        # 每跑一次月份+1，減掉當月月份天數的總秒數
        # 當傳進來的當年已過總秒數小於0，則停止，-1便可以得到當年過了幾個月
        # countDay再扣掉當月的天數便可以得到今年到上個月為止過了多少天
        for x in eachDayofMonth:
            indexOf += 1
            oneYearS -= (x*onedayS)
            countDay += x
            if(oneYearS < 0):
                return[(indexOf-1), (countDay-x)]

def nowTime():
    #宣告閏年變數
    countExcpDay = 0
    #起始年份
    staring_year = 1970
    #取得1970到現在的時間
    nowTime = math.floor(time.time())
    #算出過了幾年
    year = math.floor(nowTime/31536000)
    #今年的年份
    current_year = staring_year + year
    #判斷每一年是不是閏年
    for each_year in range(staring_year,current_year):
        if each_year%4 == 0:
            countExcpDay = countExcpDay + 1
    #算出現在1970到現在的時間(減去閏年)
    nowTime = math.floor(time.time()) - (86400 * countExcpDay) 
    #算出過了幾年
    year = math.floor(nowTime/31536000)
    #現在的年份
    realYear = year + 1970 

    # 把今年到目前為止的總秒數和今年是否為閏年送去運算
    if(realYear%4 == 0):
        monthS = nowTime - (year*31536000)
        # monthS = nowTime - (year*31536000) - (countExcpDay*86400)
        print(monthS)
        MandDay = caculation(monthS, True)
    else:
        monthS = nowTime - (year*31536000)
        # monthS = nowTime - (year*31536000) - (countExcpDay*86400)
        print(monthS)
        MandDay = caculation(monthS, False)

    # 回傳回來過了多少個月+1就是當前月份，代表當前是第幾個月
    month = MandDay[0]
    realMonth = month +1

    # 到上個月為止今年過了多少天
    dayPass = MandDay[1]

    # 今年總秒數先扣掉今年到上個月為止過了多少天的總秒數，再除以一天的總秒數後再+1，最後再無條件捨去
    # 便可以得到今天是幾號，因為今天還沒過完所以要+1，第幾號的意思
    date = math.floor((monthS - (dayPass*86400)) / 86400)
    realDate = date + 1
    
    # 小時就是今年的總秒數扣掉已過天數的秒數和日的秒數後除一小時秒數再無條件捨去
    hour = math.floor((monthS - ((dayPass+date)*86400)) / (60*60))

    # 台北時差8小時
    localHour = hour + 8

    # 今年總秒數扣掉已過月秒數、日秒數、時秒數再除分秒數便可以得到第幾分
    minutes = math.floor((monthS - ((dayPass+date)*86400) - (hour*60*60)) / 60)

    # 今年總秒數扣掉已過月秒數、日秒數、時秒數、分秒數，剩下就是第幾秒了
    sec = monthS - ((dayPass+date)*86400) - (hour*60*60) - (minutes*60)

    weekList = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # 計算從1970到現在總共過了多少天
    allday = math.floor(time.time()/86400)
    
    # 1970/1/1號是星期四，所以非閏年index要+3，閏年index+2
    weekDay = (allday + 3) %7
        
    return "{}/{}/{} {}:{}:{} {}".format(realYear, realMonth, realDate, localHour, minutes, sec, weekList[weekDay])

if __name__ == '__main__':
    Now_time = nowTime()
    print(Now_time)
