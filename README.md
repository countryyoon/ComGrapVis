# ComGrapVis
# 컴퓨터 그래픽스 및 비젼

<2주차 Ex1>
- 루프 시작 전 파일 이름을 묻고 파일을 디스크에서 읽고 모니터에 디스플레이
- 각 동작 수행 후 키보드 입력 대기
- r : 영상의 적절한 위치에 파일명, 영상의 크기 및 깊이를 표시함
- g : 현재 디스플레이된 영상을 회색조 영상으로 변환하여 디스플레이 함
- c : 원래의 color 영상을 디스플레이 함
- m : 원래의 컬러 영상 위에 전체 화면 모자이크 처리
      1) 모자이크 블록수 (가로, 세로)를 사용자에게 입력 받고 모자이크 처리 수행
      2) 각 블록의 색 값을 블록화소의 평균값, 중앙값, 중심의 화소값으로 사용자가 모드를 선택할 수 있도록 함.
      3) 팀별 자유 선택으로 각 블록이 가장 선명하게 구별될 수 있는 모드를 제안하여 추가할 것
      4) 단 각 블록의 중앙에 적절한 크기로 블록 인덱스(열번호, 행번호) 를 텍스트로 표시
- q : 종료
- 각 기능에 대하여 함수를 구현하는 것을 추천함
- 기능의 잘못된 입력 등에 대하여 적절한 오류 표시를 해줄 것



<3주차 Ex2>
- 트랙바로 컬러 영상의 명도 및 채도를 조절
- 선형변환, s형변환 선택



<4주차>
- 백인과 흑인의 피부색을 검출하는 프로그램 작성
- 피부색 화소만 원래 화소색으로 나타내고 그 외에는 표시하지 않음
- 창을 사분할로 나누어 원본영상, 백인피부검출, 흑인피부검출, 두경우를모두검출 하는 경우를 띄운다
- 두 경우를 모두 검출하는 경우, 겹치는 범위는 빨간색으로 표시



<5주>



<6주>
- 웹캠 캡처 영상과 에지 영상을 blending 하여 디스플레이함
- 원본과 비교할수 있도록 원본, 에지, blending 된영 상을 가로, 또는 세로로 나란히 디스플레이
- 영상을 플레이 하며 트랙바로 alpha값을 [0, 1]의 범위에서 조절할 수 있도록 함
- 재생속도에 문제가 있을 경우 영상을 resize하여 처


<7주>
