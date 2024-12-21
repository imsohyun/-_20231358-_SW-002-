import random

# 1. 학생 정보
def info_students(num_students=30):
    students = []
    for i in range(num_students):
        name = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2))  # 이름 : 알파벳 대문자 두 글자
        age = random.randint(18, 22)  # 나이 : 18 ~ 22 사이의 정수
        score = random.randint(0, 100)  # 성적 : 0 ~ 100 사이의 정수
        students.append({"이름": ''.join(name), "나이": age, "성적": score})
    return students

# 2. 파일에 학생 정보를 저장
def generate_students_to_file(filename, students):
    with open(filename, 'w') as file:
        for student in students:
            file.write(f"{student['이름']},{student['나이']},{student['성적']}\n")

# 3. 파일에서 학생 정보를 읽기
def read_students_from_file(filename):
    students = []
    with open(filename, 'r') as file:
        for line in file:
            name, age, score = line.strip().split(',')
            students.append({"이름": name, "나이": int(age), "성적": int(score)})
    return students

# 4. 선택 정렬 (Selection Sort)
def selection_sort(A, field, order):
    n = len(A)
    for i in range(n - 1):
        least = i
        for j in range(i + 1, n):
            if order == '오름차순': # 오름차순 정렬
                if A[j][field] < A[least][field]:
                    least = j
            elif order == '내림차순': # 내림차순 정렬
                if A[j][field] > A[least][field]:
                    least = j
        A[i], A[least] = A[least], A[i]  
    return A

# 5. 삽입 정렬 (Insertion Sort)
def insertion_sort(A, field, order):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0:
            if order == '오름차순': # 오름차순 정렬
                if A[j][field] > key[field]:
                    A[j + 1] = A[j]
                    j -= 1
                else:
                    break
            elif order == '내림차순': # 내림차순 정렬
                if A[j][field] < key[field]:
                    A[j + 1] = A[j]
                    j -= 1
                else:
                    break
        A[j + 1] = key
    return A

# 6. 퀵 정렬 (Quick Sort)
def quick_sort(A, left, right, field, order):
    if left < right:
        q = partition(A, left, right, field, order)  # 좌우로 분할
        quick_sort(A, left, q - 1, field, order)  # 왼쪽 부분리스트를 퀵 정렬
        quick_sort(A, q + 1, right, field, order)  # 오른쪽 부분리스트를 퀵 정렬

def partition(A, left, right, field, order):
    low = left + 1
    high = right
    pivot = A[left][field]  # 피벗 설정

    while low <= high:
        if order == '오름차순':
            while low <= right and A[low][field] <= pivot: # 피벗보다 큰 요소를 찾음
                low += 1
            while high >= left and A[high][field] > pivot: # 피벗보다 작은 요소를 찾음
                high -= 1
        elif order == '내림차순':
            while low <= right and A[low][field] >= pivot:
                low += 1
            while high >= left and A[high][field] < pivot:
                high -= 1

        if low < high: #요소 교환
            A[low], A[high] = A[high], A[low]

    A[left], A[high] = A[high], A[left]
    return high

# 7. 기수 정렬 (Radix Sort) + 계수 정렬 (Counting Sort)
class ArrayQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return self.front == (self.rear + 1) % self.capacity

    def enqueue(self, item):
        if not self.is_full():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item

    def dequeue(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.capacity
            item = self.array[self.front]
            self.array[self.front] = None  # 삭제된 자리 초기화
            return item
        return None

def radix_sort(A):
    Buckets = 10  # 10진법을 사용
    Digit = 3  # 정렬할 숫자의 최대 자릿수

    # 버킷 개수의 원형 큐 생성
    queues = [ArrayQueue(len(A)) for _ in range(Buckets)]

    n = len(A)
    factor = 1

    for d in range(Digit):
        # 1. 각 자릿수에 대해 정렬
        for i in range(n):
            digit = (A[i] // factor) % Buckets
            queues[digit].enqueue(A[i])  # 자리수에 해당하는 큐에 삽입

        # 2. 큐에서 다시 배열로 값을 꺼내어 정렬된 상태로 재배열
        i = 0
        for b in range(Buckets):
            while not queues[b].is_empty():
                A[i] = queues[b].dequeue()
                i += 1

        # 3. 다음 자릿수로 이동
        factor *= Buckets

def counting_sort(arr):
    # 1. 입력 배열에서 가장 큰 값을 찾음
    max_val = max(arr)

    # 2. 카운트 배열 초기화 (0으로 채워진 배열)
    count = [0] * (max_val + 1)

    # 3. 카운트 배열 : 입력 배열의 값을 카운트 배열에 기록 (빈도 계산)
    for num in arr:
        count[num] += 1

    # 4. 누적 카운트 배열 : 카운트 배열에서 누적합 계산 (누적 카운트)
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # 5. 출력 배열 생성
    output = [0] * len(arr)

    # 6. 입력 배열을 역순으로 순회하면서, 각 요소를 출력 배열의 올바른 위치에 삽입
    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1  # 사용한 숫자의 위치를 감소

    return output

# 7. 학생 정렬
def main():
    input_filename = 'C:\\Users\\User\\Desktop\\새 폴더\\students.txt'  
    output_filename = 'C:\\Users\\User\\Desktop\\새 폴더\\sorted_students.txt'  

    students = info_students()

    while True:
        save_option = input("학생 정보를 리스트에 저장하거나 파일로 저장하시겠습니까? (리스트/파일): ") # 학생 정보 저장 형식 지정
        if save_option in ["리스트", "파일"]:
            break
        print("잘못된 입력입니다. '리스트' 또는 '파일' 중 하나를 선택해주세요.") # 리스트/파일 외 입력 시 오류 처리

    if save_option == "파일":
        generate_students_to_file(input_filename, students)
        print(f"학생 정보를 {input_filename} 파일에 저장했습니다.")

        print("\n--- 파일에서 학생 정보 로드 ---")
        students = read_students_from_file(input_filename)
    elif save_option == "리스트":
        print("학생 정보를 리스트에 저장했습니다.")

    while True:
        print("\n--- 메뉴 ---")
        print("1. 이름을 기준으로 정렬")
        print("2. 나이를 기준으로 정렬")
        print("3. 성적을 기준으로 정렬")
        print("4. 프로그램 종료")

        choice = input("정렬 기준을 선택하세요 (1, 2, 3, 4): ")
        if choice not in ['1', '2', '3', '4']: # 1/2/3/4 외 입력 시 오류 처리
            print("잘못된 입력입니다. 1, 2, 3, 4 중 하나를 선택해주세요.")
            continue

        if choice == '4':
            print("프로그램을 종료합니다.")
            break

        field = '이름' if choice == '1' else '나이' if choice == '2' else '성적'

        while True:
            order = input(f"{field} 기준으로 정렬할 방향을 선택하세요 (오름차순/내림차순): ") # 오름차순/내림차순 정렬 방식 지정
            if order in ['오름차순', '내림차순']:
                break
            print("잘못된 입력입니다. '오름차순' 또는 '내림차순' 중 하나를 선택해주세요.") # 오름차순/내림차순 외 입력 시 오류 처리

        if choice == '1':
            sorted_students = selection_sort(students, field, order)
        elif choice == '2':
            sorted_students = insertion_sort(students, field, order)
        elif choice == '3':
            quick_sort(students, 0, len(students) - 1, field, order)
            sorted_students = students

        print(f"\n--- {field} 기준으로 정렬된 학생 정보 ({order}) ---")
        for student in sorted_students:
            print(student)

        if save_option == "파일":
            generate_students_to_file(output_filename, sorted_students) # 정렬된 학생 정보를 파일에 저장
            print(f"\n정렬된 학생 정보를 {output_filename} 파일에 저장했습니다.") 

if __name__ == "__main__":
    main()