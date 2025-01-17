[![SSinsa](https://img.shields.io/static/v1?logo=GitHub&label=Cteator&message=SSinsa&color=blue)](https://github.com/SSinsa)

[![laziness](https://img.shields.io/static/v1?logo=GitHub&label=Cteator&message=laziness&color=blue)](https://github.com/sonwonrak92)

[![JuNu](https://img.shields.io/static/v1?logo=GitHub&label=Cteator&message=JuNu&color=blue)](https://github.com/mike6321)

[![bbubbush](https://img.shields.io/static/v1?logo=GitHub&label=Cteator&message=bbubbush&color=lightgrey)](https://github.com/bbubbush) :: java

# dataStructure_algorithm
자료구조 및 알고리즘 공부


## 1. Linear Array(선형배열)
- 흔히 일반적으로 생각하는 Array(이하 배열)를 말하며, 별 다른 말이 없을 경우에는 동일한 데이터 타입의 집합으로 간주한다.
- 별도의 특별한 자료구조는 아니나 시간복잡도가 O(1)인 메서드와 O(N)인 메서드의 차이를 구분할 수 있어야 한다.  예를 들어 배열 안에 특정 값을 찾는 기능은 O(N)만큼의 시간복잡도가 걸린다. 왜인지는 본인이 생각해보길 바란다.

## 2. Sorting(정렬)
- 중요하다. 각 정렬간의 방법, 시간복잡도, 특징 정도는 필히 암기해 두어야 한다. 프로그래밍 언어에 내장되어있는 정렬 기능이 어떤 방법으로 진행하는지 확인한다면 플러스 1점!

#### 1) Selection Sort(선택정렬)
- 시간복잡도 : O(N^2)
- 장점 : 구현이 쉽다.
- 단점 : 느리다. 따라서 정렬방식으로 채택되는일이 없다.

#### 2) Insertion Sort(삽입정렬)
- 시간복잡도 : O(N) ~ O(N^2)
- 장점 : 구현이 쉽고 준수한 성능을 보여준다.
- 단점 : 그럼에도 불구하고 퀵, 병합정렬에 비해 상대적으로 매우 느리다.

#### 3) Bubble Sort(버블정렬)
- 시간복잡도 : O(N^2)
- 장점 : 구현이 아주 쉽다. 또한 코드가 직관적이기 때문에 초보개발자가 봐도 이해할 수 있다.
- 단점 : 얘도 느리다. 안쓴다.

#### 4) Merge Sort(병합정렬)
- 시간복잡도 : O(N log N)
- 장점 : 빠르고 안정적인 정렬방법이다. 즉, 데이터의 분포에 상관없이 비슷한 성능을 보여준다.
- 단점 : 구현이 복잡하다. 

#### 5) Quick Sort(퀵정렬)
- 시간복잡도 : O(N log N) ~ O(N^2) 
- 장점 : 속도가 빠르다. 시간복잡도가 동일한 병합정렬에 비해서도 기대성능이 더 좋은 편이다.
- 단점 : Pivot point에 따라 Best practice와 Worst practice가 확연하게 차이가 난다. 

## 3. Searching(탐색)
#### 1) Linear Searching(선형탐색)
- 시간복잡도 : O(N)
- 일반적으로 자료를 탐색하는 방법.
- 앞에서부터 순차적으로 원하는 값에 도달할 때 까지 반복한다.
- 정렬도 필요없고 구현도 쉬워 빠르게 구현하여 테스트할 수 있다.
- 하지만 느리다.

#### 2) Binary Searching(이진탐색)
- 시간복잡도 : O(N log N)
- 정렬이 되어있어야 한다는 조건이 붙지만, 빠른 탐색속도를 자랑하는 방법이다.
- 탐색할 데이터가 많은 경우 속도가 **(정렬 + 이진탐색 방법) > 탐색방법** 보다 빠르면 사용한다.

## 4. Recursive Algorithm(재귀 알고리즘) feat 재귀주누
- 순환참조라고도 하며 알고리즘 내에 본인을 다시 호출하는 부분이 포함된다는 특징이 있다.
- 코드가 간결해진다는 장점이 있지만, 자칫 무한히 본인을 호출하여 Stack Overflow를 발생시킬 수 있다.
- 구현 시 크게 두 가지만 명심하여 개발하면 비교적 헷갈리지 않게 구현할 수 있다. 첫 번째는 종료조건, 두 번째는 재귀호출조건 및 파라미터 이다.
- 어렵다고 생각된다면 작은 단위의 샘플(Base Case)를 만들어 놓고 조금씩 확장해 가면서 적용시키면 보다 쉽게 구현할 수 있다.


#[5주차 정리]

## 1. Binary Search Tree(이진탐색트리)
- 시간복잡도 : O(N log N) ~ O(N)
- 이진탐색의 특성을 활용한 자료구조. 특징은 아래와 같다.
- 1) 어떤 노드(N) 기준으로 왼쪽 서브트리의 모든 값은 N보다 작아야 한다.
- 2) 어떤 노드(N) 기준으로 오른쪽 서브트리의 모든 값은 N보다 커야 한다.
- 3) 중복된 키는 존재하지 않는다.

- 특히 어려운 부분은 노드의 삭제. 삭제할 노드의 자식노드 수에 따라 로직이 달라야 한다. 

## 2. Heap(힙)
- 시간복잡도 : O(N log N)
- 부모는 자식보다 큰 값을 갖고, 완전이진트리의 형태를 따르는 자료구조.
- Max Heap 혹은 Min Heap에 따라 root의 값을 가장 큰 값 혹은 가장 작은 값으로 갖는다.
- 힙에서는 이진탐색트리와 다르게 중복된 키를 허용한다.

