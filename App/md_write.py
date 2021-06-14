import datetime

class main:
    def partnership_md(title,link,tag,github,into):
        with open("./MDFILE/partnership/"+title+".md",'w',encoding='UTF-8',newline="") as file:        
            file.write("# "+title+"\n---\n\n")
            file.write("> 서버 링크\n   - "+link+"\n\n")
            file.write("> 서버 주인 태그\n   - "+tag+"\n\n")
            file.write("> 팀 서버 깃허브\n   - "+github+"\n\n")
            file.write("> 서버 소개\n   - "+into)
            print("CLEAR")

    def ask_md(email,question):
        now = datetime.datetime.now()
        time_s = str(now.strftime("%Y년 %m월 %d일 %H시 %M분 %S초"))

        with open("./MDFILE/ask/"+email+"`s_ask.md",'w',encoding='UTF-8',newline="") as file:        
            file.write("# "+email+"\n---\n\n")
            file.write("> 문의 시각\n   - "+time_s+"\n\n")
            file.write("> 사용자 이메일\n   - "+email+"\n\n")
            file.write("> 문의 내용\n   - "+question)
            print("CLEAR")

    def report(email,contents,explanation):
        now = datetime.datetime.now()
        time_s = str(now.strftime("%Y년 %m월 %d일 %H시 %M분 %S초"))

        with open("./MDFILE/report/"+email+"`s_report.md",'w',encoding='UTF-8',newline="") as file:        
            file.write("# "+email+"\n---\n\n")
            file.write("> 신고 시각\n   - "+time_s+"\n\n")
            file.write("> 신고 내용\n   - "+contents+"\n\n")
            file.write("> 신고 내용 상황 설명\n   - "+explanation)
            print("CLEAR")

    def bugreport(email,contents,explanation):
        now = datetime.datetime.now()
        time_s = str(now.strftime("%Y년 %m월 %d일 %H시 %M분 %S초"))

        with open("./MDFILE/bugreport/"+email+"`s_bugreport.md",'w',encoding='UTF-8',newline="") as file:        
            file.write("# "+email+"\n---\n\n")
            file.write("> 에러제보 시각\n   - "+time_s+"\n\n")
            file.write("> 에러 내용\n   - "+contents+"\n\n")
            file.write("> 에러 설명\n   - "+explanation)


#버그 코드
# bugreport(email="alfmalfm1214@gmail.com",contents="자세한내용은 생략한다",explanation="자세한내용은 생략한다")

#신고 코드
# report(email="alfmalfm1214@gmail.com",contents="자세한내용은 생략한다",explanation="자세한내용은 생략한다")

#문의 코드
# ask_md(email="alfmalfm1214@gmail.com",question="자세한내용은 생략한다")

#파트너쉽 코드
# partnership_md(title="Team Sirius",link="https://www.teamsirius.xyz",tag="Mireu / 미르#0257",github="https://github.com/Mireu-Labcon",into="자세한내용은 생략한다")