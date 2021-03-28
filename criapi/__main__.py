import requests
from bs4 import BeautifulSoup
import re
class Cricbuzz():
    def scrape_url(self,url):
        r=requests.get(url)
        page=BeautifulSoup(r.content,'html.parser')
        return page
    def livescore(self):
        url="https://m.cricbuzz.com/"
        page=self.scrape_url(url)
        teams=page.find_all(href=re.compile("/cricket-commentary"))
        dicts=[]
        for team in teams:
            dict={}
            score=team.get_text(';')
            score=score.split(';')
            dict['id']=team.attrs['href'].split('/')[2]
            dict['batting']={}
            i=2
            try:
                dict['batting']['team']=score[i]
            except:
                continue
            dict['batting']['score']=[]
            batting={}
            dict['bowling']={}
            i+=1
            try:
                while 1:
                    batting={}
                    if score[i].split()[-1]=='&':
                        batting['runs']=score[i].split()[0].strip()
                        batting['wickets']='10'
                        dict['batting']['score'].append(batting)
                        i+=1
                    else:
                        batting['runs']=score[i].split('/')[0].strip()
                        try:
                            if score[i].split('/')[1].find("(f"):
                                batting['follow-on']=True
                            else:
                                batting['follow-on']=False

                            batting['wickets']=score[i].split('/')[1].replace('(f','').strip()
                        except:
                            batting['wickets']='10'
                        i+=1
                        batting['overs']=score[i][2:-1]
                        dict['batting']['score'].append(batting)
                        i+=1
                        break
                dict['bowling']['team']=score[i]

            except:
                try:
                    dict['bowling']['team']=score[i]
                except:
                    continue
            try:
                i+=1
                dict['bowling']['score']=[]
                while 1:
                    bowling={}
                    if score[i].split()[-1]=='&':
                        bowling['runs']=score[i].split()[0].strip()
                        bowling['wickets']='10'
                        dict['bowling']['score'].append(bowling)
                        i+=1
                    else:
                        bowling['runs']=score[i].split('/')[0].strip()
                        try:
                            if score[i].split('/')[1].find("(f"):
                                bowling['follow-on']=True
                            else:
                                bowling['follow-on']=False

                            bowling['wickets']=score[i].split('/')[1].replace('(f','').strip()
                        except:
                            bowling['wickets']='10'
                        i+=1
                        bowling['overs']=score[i][2:-1]
                        dict['bowling']['score'].append(bowling)
                        i+=1
                        break
            except:
                dict['bowling']['score']=[{}]
            dict['status']=score[-1]
            dicts.append(dict)
        return dicts
    def commentary(self,id):
        url='https://m.cricbuzz.com/cricket-commentary/'+str(id)
        page=self.scrape_url(url)
        tables=page.find_all('table')
        batsmen=[]
        bowler=[]
        try:
            batsmen_rows=tables[0].find_all('tr')
            for batsmen_row in batsmen_rows[1:]:
                dict={}
                columns=batsmen_row.get_text(';').split(';')
                dict['name']=columns[0]
                dict['runs']=columns[1]
                dict['balls']=columns[2][1:-1]
                dict['fours']=columns[3]
                dict['six']=columns[4]
                dict['sr']=columns[5]
                batsmen.append(dict)
            bowler_rows=tables[1].find_all('tr')
            for bowler_row in bowler_rows[1:]:
                dict={}
                columns=bowler_row.get_text(';').split(';')
                dict['name']=columns[0]
                dict['overs']=columns[1]
                dict['maidens']=columns[2]
                dict['runs']=columns[3]
                dict['wickets']=columns[4]
                bowler.append(dict)
        except:
            bowler=[]
            batsmen=[]
        score={}
        score['batsman']=batsmen
        score['bowler']=bowler
        comm=[]
        commentary=page.find_all('p')
        for comment in commentary:
            dict={}
            try:
                if len(comment.text.split()[0].split('.'))==2:
                    dict['over']=comment.encode_contents().decode('utf-8').split()[0]
                    dict['comm']=' '.join(comment.text.split()[1:])
                    comm.append(dict)
                else:
                    dict['over']=None
                    dict['comm']=comment.encode_contents().decode('utf-8')
                    comm.append(dict)
            except:
                continue
        score['comm']=comm
        return score
    def scorecard(self,id):
        url='https://m.cricbuzz.com/live-cricket-scorecard/'+str(id)
        page=self.scrape_url(url)
        tables=page.find_all('table')
        tables=tables[:-2]
        i=0
        scorecard=[]
        while i<len(tables):
            i+=1
            batsmen=[]
            while 1:
                if tables[i].get_text(';').split(';')[0]=='Bowler':
                    break
                batsmen_row=tables[i]
                dict={}
                columns=batsmen_row.get_text(';').split(';')
                dict['name']=columns[0]
                dict['runs']=columns[1]
                dict['balls']=columns[2][1:-1]
                dict['fours']=columns[3]
                dict['six']=columns[4]
                dict['sr']=columns[5]
                dict['dismissal']=columns[-1]
                batsmen.append(dict)
                i+=1
            bowler=[]
            bowler_rows=tables[i].find_all('tr')
            for bowler_row in bowler_rows[1:]:
                dict={}
                columns=bowler_row.get_text(';').split(';')
                dict['name']=columns[0]
                dict['overs']=columns[1]
                dict['maidens']=columns[2]
                dict['runs']=columns[3]
                dict['wickets']=columns[4]
                bowler.append(dict)
            i+=1
            try:
                fow_rows=tables[i].find_all('tr')
            except:
                fow_rows=[]
            fow=[]
            for fow_row in fow_rows[1:]:
                    dict={}
                    columns=fow_row.get_text(';').split(';')
                    dict['wkt_num']=columns[0]
                    dict['score']=columns[1]
                    dict['overs']=columns[2]
                    dict['name']=columns[3]
                    fow.append(dict)
                    continue
            i+=1
            score={}
            score['batcard']=batsmen
            score['bowlcard']=bowler
            score['fall_wickets']=fow
            scorecard.append(score)
        return scorecard
    





    

    
