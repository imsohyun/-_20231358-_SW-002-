import random

# 1. 학생 정보 생성 및 저장
def info_students(num_students=30):
    students = []
    for i in range(num_students):
        name = random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 2)  # 두 글자 대문자
        age = random.randint(18, 22)  # 나이 범위 18~22
        score = random.randint(0, 100)  # 성적 범위 0~100
        students.append({"이름": ''.join(name), "나이": age, "성적": score})
    return students

# 2. 파일에 학생 정보를 저장
def save_students_to_file(filename, students):
    with open(filename, 'w') as file:
        for student in students:
            file.write(f"{student['이름']},{student['나이']},{student['성적']}\n")

# 3. 파일에서 학생 정보를 읽기
def load_students_from_file(filename):
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
            if order == '오름차순':
                if A[j][field] < A[least][field]:
                    least = j
            elif order == '내림차순':
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
            if order == '오름차순':
                if A[j][field] > key[field]:
                    A[j + 1] = A[j]
                    j -= 1
                else:
                    break
            elif order == '내림차순':
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
        quick_sort(A, left, q - 1, field, order)     # 왼쪽 부분리스트를 퀵 정렬
        quick_sort(A, q + 1, right, field, order)    # 오른쪽 부분리스트를 퀵 정렬

def partition(A, left, right, field, order):
    low = left + 1
    high = right
    pivot = A[left][field]  # 기준 필드에 따라 피벗 설정

    while low <= high:
        if order == '오름차순':
            while low <= right and A[low][field] <= pivot:
                low += 1
            while high >= left and A[high][field] > pivot:
                high -= 1
        elif order == '내림차순':
            while low <= right and A[low][field] >= pivot:
                low += 1
            while high >= left and A[high][field] < pivot:
                high -= 1

        if low < high:
            A[low], A[high] = A[high], A[low]

    A[left], A[high] = A[high], A[left]
    return high

# 7. 학생 정렬
def main():
    filename = 'students.txt'
    print("학생 정보를 생성 중...")
    students = info_students()
    save_students_to_file(filename, students)
    print(f"학생 정보를 {filename} 파일에 저장했습니다.")

    print("\n--- 파일에서 학생 정보 로드 ---")
    students = load_students_from_file(filename)

    while True:
        print("\n--- 메뉴 ---")
        print("1. 이름을 기준으로 정렬 (선택 정렬)")
        print("2. 나이를 기준으로 정렬 (삽입 정렬)")
        print("3. 성적을 기준으로 정렬 (퀵 정렬)")
        print("4. 프로그램 종료")
        choice = input("정렬 기준을 선택하세요 (1, 2, 3, 4): ")

        if choice in ['1', '2', '3']:
            field = '이름' if choice == '1' else '나이' if choice == '2' else '성적'
            order = input(f"{field} 기준으로 정렬할 방향을 선택하세요 (오름차순/내림차순): ")
            
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
        elif choice == '4':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 선택해주세요.")

if __name__ == "__main__":
    main()
