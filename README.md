# <div align="center"><a href="https://petemotiondiary.site/"> https://petemotiondiary.site</a>

<div align="center"><img src="https://github.com/AIVLE-School-Third-Big-Project/PetEmotionDiary-Video2Text/assets/86940335/77933231-5d72-4f2a-93f1-763b5ffc3bd8"width="700" height="110"/></div>
<div align="center">AI 모델링을 통해 반려 동물 영상으로 일기 자동 생성 서비스입니다.</div>
<br>
<br>



### <a href="https://www.notion.so/AIVLE-School-AI-3-2-cb1d9e71ac54475c930b50d7ed0130d7">노션 정리 링크 </a>

<br>

## 프로젝트 구조

<div align="center"><img src=https://github.com/AIVLE-School-Third-Big-Project/PetEmotionDiary-Video2Text/assets/86940335/07fa66aa-fa46-4f1e-85ad-bfc4c2cc0a89/></div>

- Django의 내장 서버는 배포에 알맞지 않아, Gunicorn과 Nginx로 서버를 구축하였습니다.
- EC2를 사용해서 서비스 서버를 배포하였습니다.
- 정적 파일들을 클라우드 서비스인 S3로 관리합니다.
- MySQL을 RDS로 관리하도록 하였습니다.

<br>
<br>

## 팀 구성원

<table>
<tr>
    <td align="center"><a href="https://github.com/kawkmin"><img src="https://avatars.githubusercontent.com/u/86940335?v=4" width="100px;"/>         <br /><sub><b>kawkmin</b></a><br>PM / BackEnd
    <td align="center"><a href="https://github.com/lwy210"><img src="https://avatars.githubusercontent.com/u/33020581?v=44" width="100px;" />         <br /><sub><b>lwy210</b></a><br>BackEnd
    <td align="center"><a href="https://github.com/dohyun-99"><img src="https://avatars.githubusercontent.com/u/104931224?v=4" width="100px;" />         <br /><sub><b>Dohyun</b></a><br>Front / Ai
    <td align="center"><a href="https://github.com/bokkuembab"><img src="https://avatars.githubusercontent.com/u/88229105?v=4" width="100px;" />         <br /><sub><b>bokkuembab</b></a><br>Front / Ai
    <td align="center"><a href="https://github.com/EunchanJeong"><img src="https://avatars.githubusercontent.com/u/89077219?v=4" width="100px;" />         <br /><sub><b>Eunchan Jeong</b></a><br>Ai
    <td align="center"><a href="https://github.com/Yongtato"><img src="https://avatars.githubusercontent.com/u/113650809?v=4" width="100px"/>         <br /><sub><b>Yongtato</b></a><br>Ai 
</tr>
</table>

<br>
<br>

## 서비스 소개

### 반려동물과 소중한 추억을 쉽고,특별하고 기록할 수 있습니다!
- AI 영상 분석 모델링을 사용하여, 사용자가 영상만 올리면 자동으로 일기를 작성해 줍니다.
- 날짜별로 정리하여, 반려동물 마다 소중한 일기장을 만들 수 있도록 하였습니다.
### 자신의 반려동물을 자랑해보세요!
- 게시판을 통해 자신의 반려동물을 올려, 자랑할 수 있습니다.

<br>
<br>

## AI 모델링
<a href="https://www.notion.so/5b5666b4316a4be68d4ccd4f9613b06c?v=50b641aecf9644f6915778f383801829"> AI 모델링 문서 링크 </a>

<br>
<br>

## ERD
<img src="https://github.com/AIVLE-School-Third-Big-Project/PetEmotionDiary-Video2Text/assets/86940335/c7c675f0-6cdb-424b-b726-3ce0034458cc">

<br>
<br>


## 홈페이지 구성

### (추후 업데이트)
<br>
<br>

## .env 설정

```
#RDS
DB_NAME= 이름
DB_USER= 유저
DB_HOST= 호스트 주소
DB_PASSWORD= 비밀번호

#S3
S3_KEY= S3 키
S3_SECRET_KEY= S3 시크릿 키
```

## secrets.json 설정
```
{
    "kakao_key": 카카오 API key
}
```

## Settings.py
```
#로컬 환경 (DB = SQLite3, static = /static 폴더)
set DJANGO_SETTINGS_MODULE=config.settings.local

#서버 환경 (DB = RDS(MySQL), static = S3 클라우드)
set DJANGO_SETTINGS_MODULE=config.settings.prod
```
