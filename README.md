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


## 프로젝트 개요 
### 프로젝트 선정 배경 및 필요성 
내에서 음원 스트리밍을 이용하는 수가 1520만명이 넘으면서 그에 따른 음원 추천 알고리즘도 개발되고 있다. 그중 감정에 따른 음원 추천 알고리즘도 개발 되고 있다. 감정을 구분하는 연구는 주로 음성인식, 표정 인식, 심박수등의 생리학적 요소로 판별하는 알고리즘의 연구가 대부분이다. 한국 컨텐츠 진흥원에서 발표한 2023년 음악 이용자 실태 조사에 따르면 출, 퇴근시나 도보 산책 등 보행시 음원을 이용하는 숫자는 전체 이용자 수의 45%로 걸으면서 음원을 재생하는 경우가 많다. 이때 얻을 수 있는 정보는 보행 정보이다. 보행 정보를 통해서 감정을 분류 하고 음원을 추천 하면 실시간으로 사용자의 감정에 맞게 추천 할 수 있다. 그래서 보행 분석을 통한 감정 분류에 따른 노래 추천 알고리즘을 개발 하고자 한다. 
### 최종 결과물의 목표 
STEP: Spatial Temporal Graph Convolutional Networks for Emotion Perception from Gaits 논문을 기반해서 보행분석으로 감정 분류하는 모델의 구조를 변경후 분석을 통해 논문이 제시한 성능 보다 향상 시키는 것이 목표이다. 

## 과제 수행방법 
1. 데이터 셋
   본 프로젝트에서 사용한 데이터는 Emotion-Gait이다. Emotion-Gait는 실제 수집 데이터와 STEP-Gen을 토대로 만든 데이터로 구성된다. 실제 데이터는 STEP의 저자들이 직접 수집한 342개의 데이터와 Edinburgh Locomtion MOCAP 데이터 베이스에 있는 1,835개로 총 2,177개 이다. STEP-Gen을 통해 새롭게 1000개의 생성된 데이터를 더해 총 3,177개로 구성된다.

2. 모델 학습
   모델 학습을 위해서 Training, validation testing set을 7 :2 :1 비율로 나눴다. 배치 크기는 8, 에포크는 180으로 모델 학습 했으며 초기 학습률은 0.1로 Adam optimizer를 사용하여 최적화를 진행했다. 모멘텀은 0.9, 가중치 감쇠는 1e-4로 한 nestrerov 모멘텀을 사용하였다. 모델 학습 시 사용한 GPU는 NVIDIA GeForce RTX 3090dlek.

3. 평가 지표
   데이터 셋에서 라벨링된 감정과 모델이 에측한 감정을 비교해서 정확도를 측정했다.
   ![image](https://github.com/hoyoonchoi/STEP_by_STEP/assets/132192963/322b831a-44b0-479e-a921-afae69ecb651)

   학습을 진행 할때마다 test를 진행했으며 그 중 TOP-1 accuracy를 선택하였다.

## 실험
   실험은 총 2가지로 진행하였으며 실험 1에 대한 추가 실험으로 실험 2를 진행하게 되었다.
   STGCN layer의 구조를 변경해서 성능을 개선하고, 최적화하였다. 그래프 컨볼루션 네트워크의 공간 및 시간 축 층 개수와 채널 수에 따른 인식 성능을 비교했다. 그래프 컨볼루션 네트워크층을 추가했을 때와 공간과 시간 축 채널을 늘렸을 때로 나누어서 모델 학습을 진행했다.

### 보행자 행동 인식 모델
![image](https://github.com/hoyoonchoi/STEP_by_STEP/assets/132192963/98c91865-8b28-49fa-965d-80223baa7df5)

STEP 분류 모델은 3개의 STGCN layer와 AvgPool2D layer, Conv2D layer를 지난 후 affective feature와 함께 softmax 함수를 거쳐 결과 값을 내는 구조로 이루어져 있다.

### 실험 1 (layer 추가 및 channel 증가) 
STGCN 구조의 layer를 추가하는 실험과 STGCN 구조의 channel을 추가하는 실험을 진행한다. 
![image](https://github.com/hoyoonchoi/STEP_by_STEP/assets/132192963/506e0fac-9ccf-43b4-9fb4-c1705a296275)
![image](https://github.com/hoyoonchoi/STEP_by_STEP/assets/132192963/d90306ce-03c2-4f4a-a0d2-abdcc0c4ff9b)

 STEP의 그래프 컨볼루션층이 3개인 것을 한 층씩 늘려가면서 5개 층까지 진행하였다.
 STEP + layer 1은 3개의 층에 아웃풋 채널이 64인 층을  추가한 것이다. STEP + layer 1-1은 아웃풋 채널이 32인 층을 추가한 것이다. STEP +layer 2는 아웃풋 채널이 64인 층을 2개 추가한 것이다.

![image](https://github.com/hoyoonchoi/STEP_by_STEP/assets/132192963/1c4f9043-92f8-4192-a528-f1eb54997200)
![image](https://github.com/hoyoonchoi/STEP_by_STEP/assets/132192963/4b2a66d7-20b4-446e-9534-0324cc349454)

공간 및 시간 축 층의 마지막 아웃풋 채널이 64인 것을 128, 256채널로 변경하면서 실험을 진행하였다.
 STEP + channel 1은 3개의 층에서 마지막 아웃풋 채널을 128로 변경한 것이다. STEP + channel 2은 4개의 층에서 마지막 아웃풋 채널을 256으로 변경한 것이고 STEP + channel 3은 4개의 층에서 마지막 아웃풋 채널을 128로 변경한 것이다. 


### 실험 2 
실험 1에서 얻은 결과를 토대로 STGCN의 구조를 변경 했다. 
실험 1에서는 Channel 수를 늘리는 것은 효과가 좋지 않으며 그래프의 층을 더 쌓는 구족가 성능이 좋으나 연속해서 계속 쌓으면 오버피팅이 나타나는 현상을 가져 왔다. 이를 토대로 실험 2에서는 layer에서 layer로 이동 할때 node에 weight를 주었고 layer1, layer2, layer 3를 concatenation 하는 구조를 변경해서 실험을 진행 하였다. 
![image](https://github.com/hoyoonchoi/STEP_by_STEP/assets/132192963/275cfd2d-ceba-4e69-847c-deb95cbf1c79)


##결과 
### 실험 1 수행 결과 
![image](https://github.com/hoyoonchoi/STEP_by_STEP/assets/132192963/7d903704-1020-4c21-84e4-c87f685bbd3b)
![image](https://github.com/hoyoonchoi/STEP_by_STEP/assets/132192963/9835db47-82d9-424c-960f-a99c83624237)

층을 추가 했을 때 기존에 3개의 구조일 때 보다 4개일 때 성능이 좋게 나왔으며 64채널 층을 추가 했을 때(+layer1)  89.13%로 가장 높은 성능을 보여주었다. 하지만 층 개수가 5개일 때 오버피팅의 문제 때문에 정확도가 4개일 때보다 줄어들었다. 층은 유지한 채 채널만 늘렸을 때는 오히려 성능이 하락하였다. 특히 층을 늘렸음에도 채널을 늘리면 늘릴수록 성능이 하락하였다.
 skeleton의 관계성을 통해 행동을 인식하는 방식이기 때문에 그래프의 층을 더 쌓는 구조가 채널을 늘려 모델의 복잡도를 높이는 구조보다 더 효과적임을 확인하였다.

### 실험 2 수행 결과 
 concatenation를 진행한 결과 분류 결과과 86.96%의 결과를 나타내었다. layer를 증가했을 때 보다 좋은 성능을 보여주지 못했는데 결과 분석을 진행했다. concatenation은 새로운 특징을 학습하거나 추출 하지 않기 때문에 더 나은 성능을 보여주지 못했다. 두 번째로 특징을 통합하거나 정제하지 않지 때문에 그래프 간의 연관성을 토대로 학습을 진행하는 STGCN 구조에는 맞지 않는 다는 것을 입증 하였다. 

 ### 최종결과물 주요 특징 및 설명 
 인간의 보행 분석을 한 후 감정을 인식하는 STEP 모델에서 ST-GCN의 구조를 변경해 가며 분류 성능을 높이는 방법을 연구했다. 기존의 3개 층보다 4개의 층일때 더 높은 성능을 보여주었으며 특히 아웃풋 채널이 64인 층을 추가했을 때 가장 높은 성능을 보여주었다. 하지만 ST-GCN의 채널을 추가했을 때는 오히려 성능이 줄어드는 것을 확인 할 수 있었다. 
 이를 통해 보행자의 행동 분석 시 관절 사이의 관계를 추출하는 그래프 구조의 반복이 시공간 축의 채널 확장보다 효과적임을 실험을 통해 입증하였다. 




 

 

   

   



