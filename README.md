# algorithm_practice

알고리즘 문제풀이

## [사다리 타기](https://github.com/ljiwoo59/algorithm_practice/tree/main/laddergame)
입력 :
* 테스트 번호
* 100 \* 100 사이즈의 0, 1, 2 로 구성된 맵
* 1 은 사다리, 2 는 목적지를 뜻함

출력 :
* #테스트 번호와 목적지에 도달하는 시작지점의 x 좌표

목적지로 부터 시작지점을 찾아가는 백트래킹을 이용하지 않고 완전 탐색을 이용하여 시작지점으로 부터 목적지를 찾아감

## [길이 존재하는가](https://github.com/ljiwoo59/algorithm_practice/tree/main/findpath)

0 에서 99로 가는 길이 존재하는지 알아내기

입력 :
* 테스트 번호와 길의 총 개수
* 순서쌍으로 이루어진 숫자 나열 (순서쌍은 길을 의미한다)

출력 :
* #테스트 번호와 존재 여부 (0 은 없음, 1 은 있음)

제약 사항 :
* 한가지 길이라도 존재한다면 길이 존재하는 것이다
* 방향을 거슬러 돌아갈 수는 없다
* 출발점과 도착점을 제외한 정점의 개수는 98개를 넘어가지 않으며, 한 정점에서 선택할 수 있는 길의 개수도 2개를 넘어가지 않는다

길의 개수는 최대 2개, 정점의 개수는 최대 100개 이기 때문에 size[100]의 정적 배열 두개를 선언한뒤, DFS를 이용하여 길의 존재 여부를 찾음

## [미로찾기](https://github.com/ljiwoo59/algorithm_practice/tree/main/mazepath)

16 * 16 미로 길이 있는지 판단하기

입력 :
* 테스트 번호
* 0(길), 1(벽), 2(출발점), 3(도착점) 으 이루어진 16 * 16 맵

출력 :
* #테스트 번호와 도달 가능 여부

DFS를 이용하여 도달 가능 여부를 찾음

## [숫자 바꾸기](https://github.com/ljiwoo59/algorithm_practice/tree/main/changenum)

주어진 횟수로 숫자의 자리를 서로 교환 하였을 때 구할 수 있는 숫자의 최대 값을 구하라

입력 :
* 테스트 개수
* 숫자와 바꿀 수 있는 횟수

출력 :
* #테스트 번호와 바뀐 숫자

## [주사위 굴리기](https://github.com/ljiwoo59/algorithm_practice/tree/main/rolling_dice)

[백준 14499](https://www.acmicpc.net/problem/14499)

deque를 이용하여 양방향에서 입력 및 출력을 이용함

## [퇴사](https://github.com/ljiwoo59/algorithm_practice/tree/main/retirement_benefit)

[백준 14501](https://www.acmicpc.net/problem/14501)

동적 계획법을 이용하여 날마다의 최대 값을 넘겨받아 총 최대 금액의 값을 구함

## [평범한 배낭](https://github.com/ljiwoo59/algorithm_practice/tree/main/napsack)

[백준 12865](https://www.acmicpc.net/problem/12865)

동적 계획법을 이용하여 짊어들 수 있는 최대의 무게 안에서 최대 가치값 구함

## [정수 삼각형](https://github.com/ljiwoo59/algorithm_practice/tree/main/int_triangle)

[백준 1932](https://www.acmicpc.net/problem/1932)

동적 계획법을 이용하여 아래층 부터 위층으로 올라가며 최대값 계산

## [소풍](https://github.com/ljiwoo59/algorithm_practice/tree/main/picnic)

From 알고리즘 문제해결 전략 

각 학생들의 쌍에 대해 이들이 서로 친구인지 여부가 주어질 때, 학생들을 짝지을 수 있는 방법의 수 계산
짝이 되는 학생들이 일부만 다르더라도 다른 방법

입력 :
* 테스트 케이수의 수 C (C < 50)
* 학생의 수 n (2 <= n <= 10) 와 친구 쌍의 수 m (0 <= m <= (n(n - 1) / 2))
* m 개의 정수 쌍으로 서로 친구인 두 학생의 번호 (번호는 0 부터 n - 1)

출력 :
* 짝지어줄 수 있는 방법의 수

재귀 함수를 이용하여 배열의 콤비네이션을 중복되지 않도록 완전 탐색



