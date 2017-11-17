#*_* coding:utf-8 *_*
#!/usr/bin/python
import mysql
import time
from decimal import *
getcontext().prec=5

ism=mysql.insertMysql()

def initMysql(data):
    for i in range(len(data['rs'])):
        status = data['rs'][i]['status']
        Time = time.time()
        if status != u'未' and status != u'-1':
            recordid = int(data['rs'][i]['id'])
            ##########################
            league=data['rs'][i]['league']
            league_i = int(league['i'])
            league_n = league['n']
            league_sbn = league['sbn']
            league_stn = league['stn']
            # print league_i,league_n,league_sbn,league_stn
            ism.insertCompetition(league_i,league_n,league_sbn,league_stn,englishname='null',matchtime=0.0)
            ################################
            host = data['rs'][i]['host']
            host_i = int(host['i'])
            host_n = host['n']
            host_sbn = host['sbn']
            host_stn = host['stn']
            ism.insertTeam(host_i,host_n,host_sbn,host_stn,englishname='null')
            ################################
            guest = data['rs'][i]['guest']
            guest_i = int(guest['i'])
            guest_n = guest['n']
            guest_sbn = guest['sbn']
            guest_stn = guest['stn']
            ism.insertTeam(guest_i, guest_n, guest_sbn, guest_stn, englishname='null')

            #########################################
            rd = data['rs'][i]['rd']
            hostscore = int(rd['hg'])  # hostscore
            guestscore = int(rd['gg'])  # guestscore
            hostjiaoqiu = int(rd['hc'])  # hostjiaoqiu
            guestjiaoqiu = int(rd['gc'])  # guestjiaoqiu
            #######################################
            plus = data['rs'][i]['plus']
            hostattack = int(plus['ha'])  # hostattack
            guestattack = int(plus['ga'])  # guest进攻
            hostDattack = int(plus['hd'])  # host危险进攻
            guestDattack = int(plus['gd'])  # guest危险进攻
            hostshezheng = int(plus['hso'])  # host射正
            guestshezheng = int(plus['gso'])  # guest射正
            hostshebuzheng = int(plus['hsf'])  # host射不正
            guestshebuzheng = int(plus['gsf'])  # guest射不正
            hostkongqiulv = int(plus['hqq'])  # host控球率
            guestkongqiulv = int(plus['gqq'])  # guest控球率
            ###########################################
            f_ld=data['rs'][i]['f_ld']
            if f_ld['hrf']!=u'null'and f_ld['hrf']!=None:
                rangqiupankou=Decimal(f_ld['hrf'])*1000
                hostrangqiupeilv=Decimal(f_ld['hrfsp'])*1000
                objectrangqiupeilv=Decimal(f_ld['grfsp'])*1000
            else:
                rangqiupankou = Decimal(0)
                hostrangqiupeilv = Decimal(0)
                objectrangqiupeilv = Decimal(0)
            # print rangqiupankou,hostrangqiupeilv,objectrangqiupeilv

            if f_ld['hdx']!=u'null'and f_ld['hdx']!=None:
                daxiaopankou=float(f_ld['hdx'])*1000
                hostdaxiaopeilv=Decimal(f_ld['hdxsp'])*1000
                objectdaxiaopeilv=Decimal(f_ld['gdxsp'])*1000
                # print daxiaopankou,type(daxiaopankou)
            else:
                daxiaopankou =Decimal(0)
                hostdaxiaopeilv = Decimal(0)
                objectdaxiaopeilv = Decimal(0)
            # print daxiaopankou,hostdaxiaopeilv,objectdaxiaopeilv


            if hostattack > 0:
                hostweixianjingonglv =Decimal(hostDattack)*1000 / Decimal(hostattack)
            else:
                hostweixianjingonglv = Decimal(0)
            if hostDattack > 0:
                hostshemenlv = Decimal(hostshezheng + hostshebuzheng) *1000/ Decimal(hostDattack)
            else:
                hostshemenlv = Decimal(0)
            if (hostshezheng + hostshebuzheng) > 0:
                hostshezhenglv = Decimal(hostshezheng)*1000 / Decimal(hostshezheng + hostshebuzheng)
            else:
                hostshezhenglv = Decimal(0)
            if hostshezheng > 0:
                hostjinqiulv = Decimal(hostscore)*1000 / Decimal(hostshezheng)
            else:
                hostjinqiulv = Decimal(0)

            if guestattack > 0:
                guestweixianjingonglv = Decimal(guestDattack)*1000 / Decimal(guestattack)
            else:
                guestweixianjingonglv = Decimal(0)

            if guestDattack > 0:
                guestshemenlv = Decimal(guestshezheng + guestshebuzheng)*1000 / Decimal(guestDattack)
            else:
                guestshemenlv = Decimal(0)
            if (guestshezheng + guestshebuzheng) > 0:
                guestshezhenglv = Decimal(guestshezheng) *1000/ Decimal(guestshezheng + guestshebuzheng)
            else:
                guestshezhenglv = Decimal(0)
            if guestshezheng > 0:
                guestjinqiulv = Decimal(guestscore) *1000/ Decimal(guestshezheng)
            else:
                guestjinqiulv = Decimal(0)
            ##########################################################3
            Record=ism.querymysql.queryRecord(recordid)
            hostattack1 = Decimal(0)
            objectattack1 = Decimal(0)
            hostDattack1 = Decimal(0)
            guestDattack1 = Decimal(0)
            hostshemen1 = Decimal(0)
            objectshemen1 = Decimal(0)
            hostshezheng1 = Decimal(0)
            objectshezheng1 = Decimal(0)

            hostattack3 = Decimal(0)
            objectattack3 = Decimal(0)
            hostDattack3 = Decimal(0)
            guestDattack3 = Decimal(0)
            hostshemen3 = Decimal(0)
            objectshemen3 = Decimal(0)
            hostshezheng3 = Decimal(0)
            objectshezheng3 = Decimal(0)

            hostattack5 = Decimal(0)
            objectattack5 = Decimal(0)
            hostDattack5 = Decimal(0)
            guestDattack5 = Decimal(0)
            hostshemen5 = Decimal(0)
            objectshemen5 = Decimal(0)
            hostshezheng5 = Decimal(0)
            objectshezheng5 = Decimal(0)

            for j in range(len(Record)):
                if Time-60>=Record[j][5]>=Time-69:
                    hostattack1=Decimal(hostattack-Record[j][10])*1000
                    objectattack1=Decimal(guestattack-Record[j][11])*1000
                    hostDattack1=Decimal(hostDattack-Record[j][12])*1000
                    guestDattack1=Decimal(guestDattack-Record[j][13])*1000
                    hostshemen1=Decimal(hostshezheng+hostshebuzheng-Record[j][14]-Record[j][16])*1000
                    objectshemen1=Decimal(guestshezheng+guestshebuzheng-Record[j][15]-Record[j][17])*1000
                    hostshezheng1=Decimal(hostshezheng-Record[j][14])*1000
                    objectshezheng1=Decimal(guestshezheng-Record[j][15])*1000

                if Time - 180 >= Record[j][5] >= Time - 189:
                    hostattack3 = Decimal(hostattack - Record[j][10])*1000
                    objectattack3 = Decimal(guestattack - Record[j][11])*1000
                    hostDattack3 = Decimal(hostDattack - Record[j][12])*1000
                    guestDattack3 = Decimal(guestDattack - Record[j][13])*1000
                    hostshemen3 = Decimal(hostshezheng+hostshebuzheng-Record[j][14]-Record[j][16])*1000
                    objectshemen3 = Decimal(guestshezheng+guestshebuzheng-Record[j][15]-Record[j][17])*1000
                    hostshezheng3 = Decimal(hostshezheng - Record[j][14])*1000
                    objectshezheng3 = Decimal(guestshezheng - Record[j][15])*1000

                if Time - 300 >= Record[j][5] >= Time - 309:
                    hostattack5 = Decimal(hostattack - Record[j][10])*1000
                    objectattack5 = Decimal(guestattack - Record[j][11])*1000
                    hostDattack5 = Decimal(hostDattack - Record[j][12])*1000
                    guestDattack5 = Decimal(guestDattack - Record[j][13])*1000
                    hostshemen5 = Decimal(hostshezheng+hostshebuzheng-Record[j][14]-Record[j][16])*1000
                    objectshemen5 = Decimal(guestshezheng+guestshebuzheng-Record[j][15]-Record[j][17])*1000
                    hostshezheng5 = Decimal(hostshezheng - Record[j][14])*1000
                    objectshezheng5 = Decimal(guestshezheng - Record[j][15])*1000

            # print recordid,league_i,host_i,guest_i,status,Time,hostscore,guestscore,hostjiaoqiu,guestjiaoqiu,hostattack,guestattack,hostDattack,guestDattack,hostshezheng,guestshezheng,hostshebuzheng,guestshebuzheng,hostkongqiulv,guestkongqiulv,hostweixianjingonglv,hostshemenlv,hostshezhenglv,hostjinqiulv,guestweixianjingonglv,guestshemenlv,guestshezhenglv,guestjinqiulv,rangqiupankou,hostrangqiupeilv,objectrangqiupeilv,daxiaopankou,hostdaxiaopeilv,objectdaxiaopeilv,hostattack1,objectattack1,hostDattack1,guestDattack1,hostshemen1,objectshemen1,hostshezheng1,objectshezheng1,hostattack3,objectattack3,hostDattack3,guestDattack3,hostshemen3,objectshemen3,hostshezheng3,objectshezheng3,hostattack5,objectattack5,hostDattack5,guestDattack5,hostshemen5,objectshemen5 ,hostshezheng5,objectshezheng5

            ism.insertRecord(recordid,league_i,host_i,guest_i,status,Time,hostscore,guestscore,hostjiaoqiu,guestjiaoqiu,hostattack,guestattack,hostDattack,guestDattack,hostshezheng,guestshezheng,hostshebuzheng,guestshebuzheng,hostkongqiulv,guestkongqiulv,hostweixianjingonglv,hostshemenlv,hostshezhenglv,hostjinqiulv,guestweixianjingonglv,guestshemenlv,guestshezhenglv,guestjinqiulv,rangqiupankou,hostrangqiupeilv,objectrangqiupeilv,daxiaopankou,hostdaxiaopeilv,objectdaxiaopeilv,hostattack1,objectattack1,hostDattack1,guestDattack1,hostshemen1,objectshemen1,hostshezheng1,objectshezheng1,hostattack3,objectattack3,hostDattack3,guestDattack3,hostshemen3,objectshemen3,hostshezheng3,objectshezheng3,hostattack5,objectattack5,hostDattack5,guestDattack5,hostshemen5,objectshemen5 ,hostshezheng5,objectshezheng5)

