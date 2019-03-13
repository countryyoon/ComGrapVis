# ComGrapVis
# 컴퓨터 그래픽스 및 비젼

<2주차 Ex1>
1, 아래의 기능을 포함하는 프로그램 작성
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