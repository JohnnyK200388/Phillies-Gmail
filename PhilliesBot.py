import http.client
import json
import datetime
import smtplib
 
now = datetime.datetime.now()
date_string = now.strftime('%Y-%m-%d')      
 
conn = http.client.HTTPSConnection("statsapi.mlb.com")
 
conn.request("GET", f"/api/v1/schedule?sportId=1&date={date_string}&teamId=143")
res = conn.getresponse()
 
print(f"API call status: {res.status}")
 
if res.status == 200:
    data = res.read()
    games = json.loads(data.decode("utf-8"))["dates"][0]["games"]
    print(f"Number of games: {len(games)}")
  
    if len(games) > 0:
      
        game = games[0]
        opponent = game['teams']['away']['team']['name'] if game['teams']['home']['team']['id'] == '143' else game['teams']['home']['team']['name']
      
        print(f"The Phillies are playing {opponent}")
        toaddrs = 'finalprojecttu@gmail.com'
        fromaddrs= 'finalprojecttu@gmail.com'
        message = f"The Phils are playing {opponent}. Tune in now or your a fake fan!"
      
        with smtplib.SMTP('smtp.gmail.com','587') as smtpserver:
            smtpserver.ehlo()
            smtpserver.starttls()
            smtpserver.ehlo()
            print("Email server login successful")
            smtpserver.login('finalprojecttu@gmail.com', 'khzhifuokcctotoc')
          
            for i in range(1):

              
                smtpserver.sendmail(fromaddrs,toaddrs,message)
                print("Phil email is sent!!!!")
    else:
        print("No games found for today.")
else:
    print("Error: could not retrieve schedule from the MLB API")
