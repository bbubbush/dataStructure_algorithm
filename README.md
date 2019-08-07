# dataStructure_algorithm
자료구조 및 알고리즘 공부

## 1. Linear Array(선형배열)
- 흔히 일반적으로 생각하는 Array(이하 배열)를 말하며, 별 다른 말이 없을 경우에는 동일한 데이터 타입의 집합으로 간주한다.
- 별도의 특별한 자료구조는 아니나 시간복잡도가 O(1)인 메서드와 O(N)인 메서드의 차이를 구분할 수 있어야 한다.  예를 들어 배열 안에 특정 값을 찾는 기능은 O(N)만큼의 시간복잡도가 걸린다. 왜냐고 물어본다면 배열안에 특정 값이 있는지 확인하려면 적어도 처음부터 끝까지 한번은 확인을 해봐야 답을 해줄수 있기 때문이다.

## 2. Sorting(정렬)
- 중요하다. 각 정렬간의 방법도 구분할 수 있어야 하고, 시간복잡도, 특징 정도는 필히 암기해 두어야 한다. 프로그래밍 언어에 내장되어있는 정렬 기능이 어떤 방법으로 진행하는지 확인한다면 플러스 1점!

#### 1) Selection Sort(선택정렬)
- 시간복잡도 : O(N^2)

#### 2) Insertion Sort(삽입정렬)
- 시간복잡도 : O(N^2)

#### 3) Bubble Sort(버블정렬)
- 시간복잡도 : O(N^2)

#### 4) Merge Sort(병합정렬)
- 시간복잡도 : O(N log N)

#### 5) Quick Sort(퀵정렬)
- 시간복잡도 : O(N log N) ~ O(N^2) 

## 3. Searching(탐색)
#### 1) Linear Searching(선형탐색)
- 
#### 2) Binary Searching(이진탐색)
- 정렬이 되어있어야 한다는 조건이 붙지만, 빠른 탐색속도를 자랑하는 방법이다.
- 

## 4. Recursive Algorithm(재귀 알고리즘)
- 순환참조라고도 하며 알고리즘 내에 본인을 다시 호출하는 부분이 포함된다는 특징이 있다.
- 코드가 간결해진다는 장점이 있지만, 자칫 무한히 본인을 호출하여 Stack Overflow를 발생시킬 수 있다.
- 구현 시 크게 두 가지만 명심하여 개발하면 비교적 헷갈리지 않게 구현할 수 있다. 첫 번째는 종료조건, 두 번째는 재귀호출조건 및 파라미터 이다.
- 어렵다고 생각된다면 작은 단위의 샘플(Base Case)를 만들어 놓고 조금씩 확장해 가면서 적용시키면 보다 쉽게 구현할 수 있다.
