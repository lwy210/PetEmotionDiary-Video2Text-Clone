<div align="center">📌 KT-Aivle에서 주관한 프로젝트의 권한이 KT에 있어, README.md만 복사하여 가져왔습니다.</div>
<br>
<div align="center"><img src="https://github.com/kawkmin/Pet_Emotion_diary_readme/assets/86940335/646dcd50-a43d-411c-982f-1fc59d766512" width="700" height="700"></div>

<br>

----

# <div align="center"><a href="https://petemotiondiary.site/"> https://petemotiondiary.site</a>

<div align="center"><img src="https://github.com/AIVLE-School-Third-Big-Project/PetEmotionDiary-Video2Text/assets/86940335/77933231-5d72-4f2a-93f1-763b5ffc3bd8"width="700" height="110"/></div>
<div align="center">AI 모델링을 통해 반려 동물 영상으로 일기 자동 생성 서비스입니다.</div>
<br>
<br>



### <a href="https://www.notion.so/AIVLE-School-AI-3-2-cb1d9e71ac54475c930b50d7ed0130d7">노션 정리 링크 </a>

<br>

## 프로젝트 구조
### <a href="https://www.notion.so/251e96bd8af04a0e8b1f87fb08a5dd28"> 인프라 구축 과정 노션 정리 링크 </a>
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
<a href="https://www.notion.so/AI-6b2e37d6ede6449a80bc7b7d063666e7?pvs=4"> AI 모델링 문서 링크 </a>

<br>
<br>

## ERD
<img src="https://github.com/AIVLE-School-Third-Big-Project/PetEmotionDiary-Video2Text/assets/86940335/30634fa1-7420-4609-a6f1-0b92fed9a54f">

<br>
<br>


## 홈페이지 구성


![KakaoTalk_20230713_173939080](https://github.com/AIVLE-School-Third-Big-Project/PetEmotionDiary-Video2Text/assets/86940335/87ab1de2-e0a3-4f30-b8eb-1f4bb5b78e81)
![KakaoTalk_20230713_173939080_01](https://github.com/AIVLE-School-Third-Big-Project/PetEmotionDiary-Video2Text/assets/86940335/cbc0300e-0d8b-4180-96f1-de7b94ce326c)

<br>
<br>

## 기타 설정

### .env 설정

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

### secrets.json 설정
```
{
    "kakao_key": 카카오 API key,
    "Open_Api_key": 챗 GPT Open ai key
}
```

### Settings.py
```
#로컬 환경 (DB = SQLite3, static = /static 폴더)
set DJANGO_SETTINGS_MODULE=config.settings.local

#서버 환경 (DB = RDS(MySQL), static = S3 클라우드)
set DJANGO_SETTINGS_MODULE=config.settings.prod
```

### models 디렉토리 트리
```
│  ├─models
│  │  ├─CatBoost
│  │  ├─ExtraTreesEntr
│  │  ├─ExtraTreesGini
│  │  ├─KNeighborsDist
│  │  ├─KNeighborsUnif
│  │  ├─LightGBM
│  │  ├─LightGBMLarge
│  │  ├─LightGBMXT
│  │  ├─NeuralNetFastAI
│  │  ├─NeuralNetTorch
│  │  ├─RandomForestEntr
│  │  ├─RandomForestGini
│  │  ├─WeightedEnsemble_L2
│  │  │  └─utils
│  │  └─XGBoost
│  └─utils
│      ├─attr
│      │  ├─CatBoost
│      │  ├─ExtraTreesEntr
│      │  ├─ExtraTreesGini
│      │  ├─KNeighborsDist
│      │  ├─KNeighborsUnif
│      │  ├─LightGBM
│      │  ├─LightGBMLarge
│      │  ├─LightGBMXT
│      │  ├─NeuralNetFastAI
│      │  ├─NeuralNetTorch
│      │  ├─RandomForestEntr
│      │  ├─RandomForestGini
│      │  └─XGBoost
│      └─data
├─cat_emotion_dir
│  ├─models
│  │  ├─CatBoost
│  │  ├─ExtraTreesEntr
│  │  ├─ExtraTreesGini
│  │  ├─KNeighborsDist
│  │  ├─KNeighborsUnif
│  │  ├─LightGBM
│  │  ├─LightGBMLarge
│  │  ├─LightGBMXT
│  │  ├─NeuralNetFastAI
│  │  ├─NeuralNetTorch
│  │  ├─RandomForestEntr
│  │  ├─RandomForestGini
│  │  ├─WeightedEnsemble_L2
│  │  │  └─utils
│  │  └─XGBoost
│  └─utils
│      ├─attr
│      │  ├─CatBoost
│      │  ├─ExtraTreesEntr
│      │  ├─ExtraTreesGini
│      │  ├─KNeighborsDist
│      │  ├─KNeighborsUnif
│      │  ├─LightGBM
│      │  ├─LightGBMLarge
│      │  ├─LightGBMXT
│      │  ├─NeuralNetFastAI
│      │  ├─NeuralNetTorch
│      │  ├─RandomForestEntr
│      │  ├─RandomForestGini
│      │  └─XGBoost
│      └─data
├─dog_action_dir
│  ├─models
│  │  ├─CatBoost
│  │  ├─ExtraTreesEntr
│  │  ├─ExtraTreesGini
│  │  ├─KNeighborsDist
│  │  ├─KNeighborsUnif
│  │  ├─LightGBM
│  │  ├─LightGBMLarge
│  │  ├─LightGBMXT
│  │  ├─NeuralNetFastAI
│  │  ├─NeuralNetTorch
│  │  ├─RandomForestEntr
│  │  ├─RandomForestGini
│  │  ├─WeightedEnsemble_L2
│  │  │  └─utils
│  │  └─XGBoost
│  └─utils
│      ├─attr
│      │  ├─CatBoost
│      │  ├─ExtraTreesEntr
│      │  ├─ExtraTreesGini
│      │  ├─KNeighborsDist
│      │  ├─KNeighborsUnif
│      │  ├─LightGBM
│      │  ├─LightGBMLarge
│      │  ├─LightGBMXT
│      │  ├─NeuralNetFastAI
│      │  ├─NeuralNetTorch
│      │  ├─RandomForestEntr
│      │  ├─RandomForestGini
│      │  └─XGBoost
│      └─data
├─dog_emotion_dir
│  ├─models
│  │  ├─CatBoost
│  │  ├─ExtraTreesEntr
│  │  ├─ExtraTreesGini
│  │  ├─KNeighborsDist
│  │  ├─KNeighborsUnif
│  │  ├─LightGBM
│  │  ├─LightGBMLarge
│  │  ├─LightGBMXT
│  │  ├─NeuralNetFastAI
│  │  ├─NeuralNetTorch
│  │  ├─RandomForestEntr
│  │  ├─RandomForestGini
│  │  ├─WeightedEnsemble_L2
│  │  │  └─utils
│  │  └─XGBoost
│  └─utils
│      ├─attr
│      │  ├─CatBoost
│      │  ├─ExtraTreesEntr
│      │  ├─ExtraTreesGini
│      │  ├─KNeighborsDist
│      │  ├─KNeighborsUnif
│      │  ├─LightGBM
│      │  ├─LightGBMLarge
│      │  ├─LightGBMXT
│      │  ├─NeuralNetFastAI
│      │  ├─NeuralNetTorch
│      │  ├─RandomForestEntr
│      │  ├─RandomForestGini
│      │  └─XGBoost
│      └─data
├─split_imgs
└─yolov5
    ├─.git
    │  ├─branches
    │  ├─hooks
    │  ├─info
    │  ├─logs
    │  │  └─refs
    │  │      ├─heads
    │  │      └─remotes
    │  │          └─origin
    │  ├─objects
    │  │  ├─info
    │  │  └─pack
    │  └─refs
    │      ├─heads
    │      ├─remotes
    │      │  └─origin
    │      └─tags
    ├─classify
    ├─data
    │  ├─hyps
    │  ├─images
    │  └─scripts
    ├─models
    │  ├─hub
    │  ├─segment
    │  └─__pycache__
    ├─segment
    ├─utils
    │  ├─aws
    │  ├─docker
    │  ├─flask_rest_api
    │  ├─google_app_engine
    │  ├─loggers
    │  │  ├─clearml
    │  │  ├─comet
    │  │  └─wandb
    │  ├─segment
    │  │  └─__pycache__
    │  └─__pycache__
    └─__pycache__
```
