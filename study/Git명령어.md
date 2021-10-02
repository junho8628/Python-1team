### git init
    해당 폴더에 .git폴더 생성하여 git과 통신할 수 있는 폴더로 만듭니다.
    
### git config --list
    우선 경로를 cd C:/로 이동합니다.  
    그 이후 git config --list 명령어를 입력하여 user.name과 user.email이 있는지, 있다면 본인인지 확인합니다.
    
### git config --global user.name "username"
    본인이 아니라면 본인으로 변경해줍니다.
### git config --global user.email "useremail@ ...."
    본인이 아니라면 본인 이메일로 변경해줍니다.  
    
### git remote add (이름) (저장소 주소)
    로컬과 git을 연결합니다. 
    이름과 저장소 주소로 원격 저장소를 추가합니다.
    ex) git remote add test https://github.com/Ottere/kaldea.git

### git remote remove (이름) 
    해당 명령어를 통해 remote를 삭제 할 수 있습니다.
    ex ) git remote remove test

### git remote rename (이름) (바꿀이름)
    해당 명령어를 통해 remote의 이름을 바꿀 수 있습니다.
    git remote rename test changetest

### git remote -v 
    해당 명령어로 remote의 이름과 주소를 확인 할 수 있습니다.  
     
### git status 
    현재 git 저장소의 상태를 확인합니다.  
    수정, 삭제, 추가 등의 데이터를 확인 가능합니다.
    
### git add (staying)
    git add . 을 할 경우 init을 한 폴더의 모든 파일 및 폴더가 저장소에 올라갑니다.
    git add [파일 이름]을 할 경우 적은 한개의 파일만 저장소에 올라갑니다.

### git commit -m "설명"
    add를 한 이후 commit을 하여 내용을 확정짓습니다.  
    commit을 하지 않으면 push가 불가능합니다.
    
### git push (remote 이름) (브랜치명)
    ex) git push test master
    해당 명령어로 원격 저장소(git)에 commit 된 파일들을 올릴 수 있습니다.
