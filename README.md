# STEP_by_STEP
소프트웨어융합캡스톤디자인 수업의 일환으로 진행된 프로젝트 입니다.


# 프로젝트 구성 
이 프로젝트는 STEP 논문에서 제시한 보행분석을 통한 감정 인식 분류 모델의 성능을 높이기 위해서 진행된 실험 들이며 
STEP 논문에서 제시한 모델의 정확도인 86.41%를 실험을 통해서 89.13% 까지 2.72%의 성능을 향상 시킨 실험을 진행한 프로젝트 입니다.  

## 참고한 프로젝트 및 논문 
<STEP: Spatial Temporal Graph Convolutional Networks for Emotion Perception from Gaits.>
```
@inproceedings{bhattacharya2020step,
author = {Bhattacharya, Uttaran and Mittal, Trisha and Chandra, Rohan and Randhavane, Tanmay and Bera, Aniket and Manocha, Dinesh},
title = {STEP: Spatial Temporal Graph Convolutional Networks for Emotion Perception from Gaits},
year = {2020},
publisher = {AAAI Press},
booktitle = {Proceedings of the Thirty-Fourth AAAI Conference on Artificial Intelligence},
pages = {1342–1350},
numpages = {9},
series = {AAAI’20}
}
```
<https://github.com/UttaranB127/STEP.git>


# 프로젝트 개요 
### 프로젝트 선정 배경 및 필요성 
내에서 음원 스트리밍을 이용하는 수가 1520만명이 넘으면서 그에 따른 음원 추천 알고리즘도 개발되고 있다. 그중 감정에 따른 음원 추천 알고리즘도 개발 되고 있다. 감정을 구분하는 연구는 주로 음성인식, 표정 인식, 심박수등의 생리학적 요소로 판별하는 알고리즘의 연구가 대부분이다. 한국 컨텐츠 진흥원에서 발표한 2023년 음악 이용자 실태 조사에 따르면 출, 퇴근시나 도보 산책 등 보행시 음원을 이용하는 숫자는 전체 이용자 수의 45%로 걸으면서 음원을 재생하는 경우가 많다. 이때 얻을 수 있는 정보는 보행 정보이다. 보행 정보를 통해서 감정을 분류 하고 음원을 추천 하면 실시간으로 사용자의 감정에 맞게 추천 할 수 있다. 그래서 보행 분석을 통한 감정 분류에 따른 노래 추천 알고리즘을 개발 하고자 한다. 
### 최종 결과물의 목표 
STEP: Spatial Temporal Graph Convolutional Networks for Emotion Perception from Gaits 논문을 기반해서 보행분석으로 감정 분류하는 모델의 구조를 변경후 분석을 통해 논문이 제시한 성능 보다 향상 시키는 것이 목표이다. 



