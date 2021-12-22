## 📚 코딩테스트에 필요한 파이썬 문법 정리

### 수 자료형
#### 수 자료형의 연산
<pre><code>
# 나누기
a / b

# 몫
a // b

# 거듭연산자
a ** b # a의 b승
</code></pre>

### 리스트 자료형
#### 리스트 초기화
<pre><code>
# 빈 리스트 선언 방법
a = list()
a = []

# 크기가 N이고 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n
</code></pre>

#### 리스트 인덱싱과 슬라이싱
<pre><code>
a = [1,2,3,4,5,6,7,8,9]a[-1]   # 9
a[-3]   # 7
a[1:4]  # [2,3,4]
</code></pre>

#### 리스트 컴프리헨션
- 리스트를 초기화하는 방법 중 하나이다.   
- 대괄호안에 조건문과 반복문을 넣는 방식으로 리스트를 초기화할 수 있다.    
- **2차원 리스트를 초기화할 때 매우 효과적으로 사용된다.**    
<pre><code>
# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트

array = [i for i in range(20) if i % 2 == 1]

array = []
for i in range(20)
  if i % 2 == 1:
    array.append(i)

# 1부터 9까지의 수의 제곱값을 포함하는 리스트
array = [i*i for i in range(1, 10)]

# N * M 크기의 2차원 리스트 초기화
n = 3
m = 4
array = [ [0]* m for _ in range(n)] # [ [0,0,0,0],[0,0,0,0], [0,0,0,0] ]
</code></pre>

#### 특정 크기의 2차원 리스트를 초기화 할 때는 반드시 리스트 컴프리헨션을 사용 

#### 리스트 관련 기타 메서드
- append(): 리스트에 원소 삽입   
- sort(): 오름차순 정렬   
- reserve(): 내림차순 정렬 ```a.sort(reverse=True)```   
- insert(): 특정 인덱스에 데이터 추가 ```a.insert(2, 3) : 인덱스2에 3 추가```    
- count(): 특정값인 데이터 개수 세기    
- remove(): 특정 값 데이터 삭제 (인덱스가 낮은거 하나)
<pre><code>
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}
# remove_set에 포함되지 않는 값만을 저장
result = [i for i in a if i not in remove_set]
</code></pre>

### dictionary 자료형
#### dictionary 자료형 관련 함수
- 키 데이터만 뽑아서 리스트로 이용할 때는 keys()함수   
- 값 데이터만을 뽑아서 리스트로 이용할 때는 values() 함수
<pre><code>
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

# 키 데이터만 담은 리스트
key_list = data.keys()
value_list = data.values()

for key in key_list:
  print(data[key]) # Apple Banana Coconut
</code></pre>

### Set 자료형
#### Set 자료형 소개
- 중복을 허용하지 않는다.   
- 순서가 없다.   
- 특정한 데이터가 이미 등장한 적이 있는지 여부를 체크할 때 효과적이다.   
<pre><code>
# 집합 자료형 초기화 방법
data = set([1, 1, 2, 3, 4, 4, 5])
data = {1, 2, 3, 4, 5}
</code></pre>

#### Set 자료형의 연산
- 합집합, 교집합, 차집합 연산이 있다.
<pre><code>
# 집합 자료형 초기화 방법
a = set([1, 2, 3, 4, 5])
b = {3, 4, 5, 6, 7}

a | b # 합집합 {1, 2, 3, 4, 5, 6, 7}
a & b # 교집합 {3, 4, 5}
a - b # 차집합 {1, 2}
</code></pre>

#### Set 자료형 관련 함수
<pre><code>
data = set([1, 2, 3])
print(data)

# 새로운 원소 추가
data.add(4)

# 새로운 원소 여러개 추가
data.update([5, 6])

# 특정한 값을 갖는 원소 삭제
data.remove(3)

print(data)
</code></pre>

### 파이썬의 기타 연산자
- 파이썬에는 추가적으로 `in 연산자`와 `not in 연산자`를 제공한다.   
- 자료형(리스트, 튜플, 문자열, 딕셔너리)에 사용된다.    
- pass문 (조건문의 값이 참이라고 해도 아무것도 처리하고 싶지 않을 때)    
- 조건부 표현식을 이용하면 if~else문을 한줄에 작성해 사용할 수 있다.   
- 리스트에 있는 원소의 값을 변경해서 또 다른 리스트를 만들고자 할 때 매우 간결하게 사용 가능하다.

<pre><code>
x in 리스트 # 리ㅌ스트 안에 x가 있을때 참이다
x not in 문자열 # 문자열 안에 x가 들어가 있지 않을때 참이다

score = 85
if score >= 80:
  pass
else:
  print('성적이 80점 미만입니다.')

# 1줄일 경우 줄이기
if score >= 80: result = 'success'
else: result = 'fail'

# 조건부 표현식
result = 'success' if score >= 80 else 'fail'

# 3항 연산자
result = score >= 80 and 'success' or 'fail'

# 리스트에 있는 원소의 값을 변경해서 또다른 리스트를 만들고자 할 때 매우 간결하게 사용 가능

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = []
for i in a:
  if i not in result_set:
  result.append(i)

result = [i for i in a if i not in remove_set]
</code></pre>

### 람다 표현식
- 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있다.   
- 람다식은 파이썬의 정렬 라이브러리를 사용할 때, 정렬 기준(key)를 설정할 때에도 자주 사용한다.
<pre><code>
def add(a, b):
  return a + b
print(add(3, 4))

# 람다 표현식으로 구현한 add() 메서드
print((lambda a, b : a+ b)(3, 7))
</code></pre>

### 입출력
- map(): 해당리스트의 모든 원소에 int()함수를 적용한다.   
- sys.stdin.readline() : 입력을 최대한 빠르게 받아야하는 경우, readline() -> 엔터 줄바꿈 기호로 바뀜, rstrip() -> 공백문자 제거
<>