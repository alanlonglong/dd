# *_* coding:utf-8 *_*
#!/usr/bin/python
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='******', db='ds', charset='utf8')
cur = conn.cursor()


class insertMysql:

    def __init__(self):
        self.querymysql=queryMysql()
        self.updatemysqlall=updateMysqlAll()

    def insertTeam(self,teamid,name='null',name1='null',name2='null',englishname='null'):
        aa=self.querymysql.queryTeam(teamid)
        bb=(teamid,name,name1,name2,englishname)
        if aa:
            if aa==bb:
                self.updatemysqlall.updateTeamAll(teamid,name,name1,name2,englishname)
                # cur.execute("insert into team values('%d','%s','%s','%s','%s')"%(teamid,name,name1,name2,englishname))
        else:
            cur.execute("insert into team values('%d','%s','%s','%s','%s')" % (teamid, name, name1, name2, englishname))
        conn.commit()

    def insertCompetition(self,competitionid,name='null',name1='null',name2='null',englishname='null',matchtime=0.0):
        aa=self.querymysql.queryCompetition(competitionid)
        bb=(competitionid,name,name1,name2,englishname,matchtime)
        if aa:
            if aa!=bb:
                self.updatemysqlall.updateCompetitionAll(competitionid,name,name1,name2,englishname,matchtime)
                # cur.execute("insert into competition values('%d','%s','%s','%s','%s','%f')"%(competitionid,name,name1,name2,englishname,matchtime))
        else:
            cur.execute("insert into competition values('%d','%s','%s','%s','%s','%f')" % (competitionid, name, name1, name2, englishname, matchtime))

        conn.commit()

    def insertRecord(self,recordid,competitionid ,hostid ,guestid ,status,Time ,hostscore ,guestscore ,hostjiaoqiu ,guestjiaoqiu ,hostattack ,guestattack ,hostDattack ,guestDattack ,hostshezheng ,guestshezheng ,hostshebuzheng ,guestshebuzheng ,hostkongqiulv ,guestkongqiulv ,hostweixianjingonglv ,hostshemenlv ,hostshezhenglv ,hostjinqiulv ,guestweixianjingonglv ,guestshemenlv ,guestshezhenglv ,guestjinqiulv ,rangqiupankou,hostrangqiupeilv,objectrangqiupeilv,daxiaopankou,hostdaxiaopeilv,objectdaxiaopeilv,hostattack1,objectattack1,hostDattack1,guestDattack1,hostshemen1,objectshemen1,hostshezheng1,objectshezheng1,hostattack3,objectattack3,hostDattack3,guestDattack3,hostshemen3,objectshemen3,hostshezheng3,objectshezheng3,hostattack5,objectattack5,hostDattack5,guestDattack5,hostshemen5,objectshemen5 ,hostshezheng5,objectshezheng5):
        # aa=self.querymysql.queryRecord(recordid,Time)
        # bb=(recordid,competitionid ,hostid ,guestid ,status,Time ,hostscore ,guestscore ,hostjiaoqiu ,guestjiaoqiu ,hostattack ,guestattack ,hostDattack ,guestDattack ,hostshezheng ,guestshezheng ,hostshebuzheng ,guestshebuzheng ,hostkongqiulv ,guestkongqiulv ,hostweixianjingonglv ,hostshemenlv ,hostshezhenglv ,hostjinqiulv ,guestweixianjingonglv ,guestshemenlv ,guestshezhenglv ,guestjinqiulv )
        # if aa:
        #     if aa!=bb:
        #         self.updatemysqlall.updateRecordAll(recordid,competitionid ,hostid ,guestid ,status,Time ,hostscore ,guestscore ,hostjiaoqiu ,guestjiaoqiu ,hostattack ,guestattack ,hostDattack ,guestDattack ,hostshezheng ,guestshezheng ,hostshebuzheng ,guestshebuzheng ,hostkongqiulv ,guestkongqiulv ,hostweixianjingonglv ,hostshemenlv ,hostshezhenglv ,hostjinqiulv ,guestweixianjingonglv ,guestshemenlv ,guestshezhenglv ,guestjinqiulv )
        #         cur.execute("insert into record values('%d','%d','%d','%d','%s','%f','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%f','%f','%f','%f','%f','%f','%f','%f'"%(recordid,competitionid ,hostid ,guestid ,status,Time ,hostscore ,guestscore ,hostjiaoqiu ,guestjiaoqiu ,hostattack ,guestattack ,hostDattack ,guestDattack ,hostshezheng ,guestshezheng ,hostshebuzheng ,guestshebuzheng ,hostkongqiulv ,guestkongqiulv ,hostweixianjingonglv ,hostshemenlv ,hostshezhenglv ,hostjinqiulv ,guestweixianjingonglv ,guestshemenlv ,guestshezhenglv ,guestjinqiulv ))
        # else:
        cur.execute("insert into record values('%d','%d','%d','%d','%s','%63.5f','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d')" % (recordid, competitionid, hostid, guestid, status, Time, hostscore, guestscore, hostjiaoqiu,guestjiaoqiu, hostattack, guestattack, hostDattack, guestDattack, hostshezheng, guestshezheng,hostshebuzheng, guestshebuzheng, hostkongqiulv, guestkongqiulv, hostweixianjingonglv, hostshemenlv,hostshezhenglv, hostjinqiulv, guestweixianjingonglv, guestshemenlv, guestshezhenglv, guestjinqiulv,rangqiupankou,hostrangqiupeilv,objectrangqiupeilv,daxiaopankou,hostdaxiaopeilv,objectdaxiaopeilv,hostattack1,objectattack1,hostDattack1,guestDattack1,hostshemen1,objectshemen1,hostshezheng1,objectshezheng1,hostattack3,objectattack3,hostDattack3,guestDattack3,hostshemen3,objectshemen3,hostshezheng3,objectshezheng3,hostattack5,objectattack5,hostDattack5,guestDattack5,hostshemen5,objectshemen5 ,hostshezheng5,objectshezheng5))
        # print 'mysql',recordid, competitionid, hostid, guestid, status, Time, hostscore, guestscore, hostjiaoqiu,guestjiaoqiu, hostattack, guestattack, hostDattack, guestDattack, hostshezheng, guestshezheng,hostshebuzheng, guestshebuzheng, hostkongqiulv, guestkongqiulv, hostweixianjingonglv, hostshemenlv,hostshezhenglv, hostjinqiulv, guestweixianjingonglv, guestshemenlv, guestshezhenglv, guestjinqiulv,rangqiupankou,hostrangqiupeilv,objectrangqiupeilv,daxiaopankou,hostdaxiaopeilv,objectdaxiaopeilv,hostattack1,objectattack1,hostDattack1,guestDattack1,hostshemen1,objectshemen1,hostshezheng1,objectshezheng1,hostattack3,objectattack3,hostDattack3,guestDattack3,hostshemen3,objectshemen3,hostshezheng3,objectshezheng3,hostattack5,objectattack5,hostDattack5,guestDattack5,hostshemen5,objectshemen5 ,hostshezheng5,objectshezheng5
        conn.commit()




class queryMysql:

    def queryTeam(self,teamid):
        cur.execute("select * from team where teamid={}".format(teamid))
        return cur.fetchall()
    def queryCompetition(self,competitionid):
        cur.execute("select * from competition where competitionid={}".format(competitionid))
        return cur.fetchall()
    def queryRecord(self,recordid):
        cur.execute("select * from record where recordid={}".format(recordid))
        return cur.fetchall()



class updateMysqlAll:
    def updateTeamAll(self,teamid,name,name1,name2,englishname):
        cur.execute("update team set name='{}',name1='{}',name2='{}',englishname='{}' where teamid={}".format(name,name1,name2,englishname,teamid))
        conn.commit()

    def updateCompetitionAll(self,competitionid,name,name1,name2,englishname,matchtime):
        cur.execute("update competition set name='{}',name1='{}',name2='{}',englishname='{}' ,matchtime={} where competitionid={}".format(name, name1, name2,englishname,matchtime, competitionid))
        conn.commit()

    def updateRecordAll(self,recordid,competitionid ,hostid ,guestid ,status,Time ,hostscore ,guestscore ,hostjiaoqiu ,guestjiaoqiu ,hostattack ,guestattack ,hostDattack ,guestDattack ,hostshezheng ,guestshezheng ,hostshebuzheng ,guestshebuzheng ,hostkongqiulv ,guestkongqiulv ,hostweixianjingonglv ,hostshemenlv ,hostshezhenglv ,hostjinqiulv ,guestweixianjingonglv ,guestshemenlv ,guestshezhenglv ,guestjinqiulv ):
        cur.execute("SET SQL_SAFT_UPDATES=0")
        cur.execute("update record set competitionid={} ,hostid={} ,guestid={} ,status='{}',Time={} ,hostscore={} ,guestscore={} ,hostjiaoqiu={} ,guestjiaoqiu={} ,hostattack={} ,guestattack={} ,hostDattack={} ,guestDattack={} ,hostshezheng={} ,guestshezheng={} ,hostshebuzheng={} ,guestshebuzheng={} ,hostkongqiulv={} ,guestkongqiulv={} ,hostweixianjingonglv={} ,hostshemenlv={} ,hostshezhenglv={} ,hostjinqiulv={} ,guestweixianjingonglv={} ,guestshemenlv={} ,guestshezhenglv={} ,guestjinqiulv={} where recordid={} ".format(competitionid ,hostid ,guestid ,status,Time ,hostscore ,guestscore ,hostjiaoqiu ,guestjiaoqiu ,hostattack ,guestattack ,hostDattack ,guestDattack ,hostshezheng ,guestshezheng ,hostshebuzheng ,guestshebuzheng ,hostkongqiulv ,guestkongqiulv ,hostweixianjingonglv ,hostshemenlv ,hostshezhenglv ,hostjinqiulv ,guestweixianjingonglv ,guestshemenlv ,guestshezhenglv ,guestjinqiulv ,recordid))
        cur.execute("SET SQL_SAFT_UPDATES=1")
        conn.commit()
