# 서버 안내용 API

이서비스는 그냥 팀원들이 할게 없다고해서
만든 서비스 API

## 문의 안내 형식

1. 버그 제보 형식
    - 이메일
    - 문제가 발생한 부분의 링크와 스크린샷 (파일 받거나 아니면 링크 받기)
    - 문제 설명

    json설계
    ```json
    {
        "User email":str,
        "Problem link":File,
        "Explanation":str
    } 
    ```

2. 문의 형식
    - 이메일
    - 문의 내용

    json설계
    ```json
    {
        "User email":str,
        "question":str
    } 
    ```

3. 신고 형식
    - 이메일
    - 신고 내용
    - 규칙 첨부를 이용한 타당한 근거를 통해 상황 설명

    json설계
    ```json
    {
        "User email":str,
        "Report contents":str,
        "Explanation":str
    } 
    ```

## 파트너쉽 신청

1. 파트너쉽 형식
    - 서버 이름
    - 서버 링크 (https://discord.gg/ 이 기본으로 되어야함)
    - 팀 서버 깃헙 (https://github.com/ 이 기본으로 되어야함)
    - 서버 소개 (50줄이상이여야함)
    - 서버 주인 태그 ("@" 있어야함)
    
    json설계
    ```json
    {
        "Server name":str,
        "Server link":str,
        "Server github":str,
        "Server introduction":str,
        "Server host tag":str
    } 
    ```
