#!/usr/bin/env python
import gammu
import smtplib

SMTPSERVER = 'smtp.yourdomain.com'
TO_EMAIL = 'you@yourdomain.com'

sm = gammu.StateMachine()
sm.ReadConfig()
sm.Init()


def sms_getall(sm):
    status = sm.GetSMSStatus()
    remain = status['SIMUsed'] + status['PhoneUsed'] + status['TemplatesUsed']
    sms = []
    start = True
    
    while remain > 0:
        if start:
            cursms = sm.GetNextSMS(Start = True, Folder = 0)
            start = False
        else:
            cursms = sm.GetNextSMS(Location = cursms[0]['Location'], Folder = 0)
        remain = remain - len(cursms)
        sms.append(cursms)
    
    data = gammu.LinkSMS(sms)
    
    for x in data:
        v = gammu.DecodeSMS(x)
        m = x[0]
        subj = '[SMS] %s' % (str(m['Text']).replace('\n',' '))
        loc = []
        for m in x:
            loc.append(str(m['Location']))
        if v == None:
            body = m['Text']
        else:
            body = ''
            for e in v['Entries']:
                if e['Bitmap'] != None:
                    for bmp in e['Bitmap']:
                        body = body + 'Bitmap:'
                        for row in bmp['XPM'][3:]:
                            body = body + row
                    print
                if e['Buffer'] != None:
                    body = body+'Text:'
                    body = body+e['Buffer']
        mail_send(subj,body,m['Number'])
        for l in loc:
             sms_del(sm,l,1)

def sms_del(sm,loc,folder):
    sm.DeleteSMS(folder, loc)
    #print('del %s from folder %s'%(loc,folder))

def mail_send(subj,body,sender='sms'):
    message = 'From: %s\nSubject: %s\n\nSms from:%s\n%s' % (sender,subj,sender,body)
    server = smtplib.SMTP(SMTP_SERVER, 25)
    server.sendmail(sender, TO_EMAIL, message)

sms_getall(sm)

