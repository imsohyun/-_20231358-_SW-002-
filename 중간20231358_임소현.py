class Book:
    def __init__(self, book_id, title, author, year): #도서 정보 초기화
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year

    def __str__(self): #도서 정보를 문자열로 반환
        return f"[책 번호: {self.book_id}, 제목: {self.title}, 저자: {self.author}, 출판 연도: {self.year}]"

# Node 클래스 코드는 수정 없이 사용해야 함
class Node: #단순 연결 리스트를 위한 노드 클래스
    def __init__(self, elem, next=None):
        self.data = elem
        self.link = next

    def append(self, node): #현재 노드 다음에 node를 삽입
        if node is not None:
            node.link = self.link
            self.link = node

    def popNext(self): #현재 노드의 다음 노드를 삭제
        next_node = self.link
        if next_node is not None: self.link = next_node.link
        return next_node

class LinkedList: #단순 연결 리스트 클래스
    def __init__(self):
        self.head = None

    def isEmpty(self): #리스트 공백 확인
        return self.head is None

    def insert(self, elem): #새 노드를 리스트에 삽입
        if self.find_by_id(elem.book_id) is not None:
            print(f"오류: 책 번호 '{elem.book_id}'는 이미 존재합니다.")
            return False

        new_node = Node(elem) #삽입할 새로운 노드를 생성

        #머리 노드로 삽입하거나 리스트 정렬 유지하며 삽입
        if self.isEmpty() or int(self.head.data.book_id) > int(elem.book_id):
            new_node.link = self.head
            self.head = new_node
            print(f"도서 '{elem.title}'가 추가되었습니다.")
            return True

        ptr = self.head
        while ptr.link is not None and int(ptr.link.data.book_id) < int(elem.book_id):
            ptr = ptr.link

        new_node.link = ptr.link
        ptr.link = new_node
        print(f"도서 '{elem.title}'가 추가되었습니다.")
        return True

    #도서 번호로 도서를 찾기
    def find_by_id(self, book_id): # 주어진 책 번호로 도서 찾기
        ptr = self.head
        while ptr is not None:
            if ptr.data.book_id == book_id:
                return ptr.data
            ptr = ptr.link
        return None
        
    #도서 제목으로 도서를 찾기
    def find_by_title(self, title):
        ptr = self.head
        while ptr is not None:
            if ptr.data.title == title:
                return ptr.data
            ptr = ptr.link
        return None

    #도서 제목을 기반으로 리스트에서 도서의 위치(pos)를 찾기
    def find_pos_by_title(self, title):
        pos = 0
        ptr = self.head
        while ptr is not None:
            if ptr.data.title == title:
                return pos
            ptr = ptr.link
            pos += 1
        return -1    

    #프로그램 요구 사항 2,3 : 사용자가 입력한 책 제목으로 삭제 및 조회, 책 번호를 기준으로 도서 삭제 및 조회, 책 번호 존재하지 않으면 오류 메시지 출력
    def delete_by_title(self, title):  
        if self.isEmpty():
            print("등록된 도서가 없습니다.")
            return False

        if self.head.data.title == title:
            book_id = self.head.data.book_id
            self.head = self.head.link
            print(f"책 제목 '{title}'에 해당하는 책 번호 '{book_id}'의 도서가 삭제되었습니다.")
            return True

        ptr = self.head
        while ptr.link is not None:
            if ptr.link.data.title == title:
                book_id = ptr.link.data.book_id
                ptr.popNext()
                print(f"책 제목 '{title}'에 해당하는 책 번호 '{book_id}'의 도서가 삭제되었습니다.")
                return True
            ptr = ptr.link

        print(f"오류: 책 제목 '{title}'에 해당하는 도서를 찾을 수 없습니다.")
        return False

    def getNode(self, pos): #주어진 위치의 노드 반환
        if pos < 0:
            return None
        ptr = self.head
        for i in range(pos):
            if ptr is None:
                return None
            ptr = ptr.link
        return ptr

    def size(self): #리스트 크기 반환
        count = 0
        ptr = self.head
        while ptr is not None:
            count += 1
            ptr = ptr.link
        return count
        
    def display(self):  # 리스트의 모든 도서 정보 출력
        if self.isEmpty():  # 리스트가 비어 있을 경우
            print("등록된 도서가 없습니다.")
            return

        # 리스트에 도서가 있는 경우
        print("현재 등록된 도서 목록:")
        ptr = self.head
        while ptr is not None:
            print(ptr.data)
            ptr = ptr.link

class BookManagementSystem:
    def __init__(self): #도서 관리 시스템 생성자
        self.books = LinkedList()

    def add_book(self, book_id, title, author, year): #새로운 도서 추가
        #책 번호 중복 검사
        if self.books.find_by_id(book_id) is not None:
            print(f"오류: 책 번호 '{book_id}'는 이미 존재합니다.")
            return False
        #책 제목 중복 검사
        if self.books.find_by_title(title) is not None:
            print(f"오류: 책 제목 '{title}'는 이미 존재합니다.")
            return False

        #출판연도 정수로 제한
        try:
            year = int(year)
        except ValueError:
            print("오류: 출판 연도는 정수여야 합니다.")
            return False

        # 중복 없으면 도서 추가
        book = Book(book_id, title, author, year)
        self.books.insert(book)
        return True

    def remove_book(self, title): #도서 제목을 기준으로 삭제
        self.books.delete_by_title(title)

    def search_book(self, title): #도서 제목을 기준으로 조회
        book = self.books.find_by_title(title)
        if book:
            print(book)
        else:
            print(f"오류: 책 제목 '{title}'을 찾을 수 없습니다.")

    def display_books(self): #모든 도서 정보 출력
        self.books.display()

    def main(self): #사용자 입력
        while True:
            print("\n=== 도서 관리 프로그램 ===")
            print("1. 도서 추가")
            print("2. 도서 삭제 (책 제목으로 삭제)")
            print("3. 도서 조회 (책 제목으로 조회)")
            print("4. 전체 도서 목록 출력")
            print("5. 종료")
            choice = input("메뉴를 선택하세요: ")
            
            if choice == '1': 
                try:
                    book_id = int(input("책 번호를 입력하세요: "))  # 책 번호 정수로 제한
                except ValueError:
                    print("오류: 책 번호는 정수여야 합니다.")
                    continue

                #추가 기능에서 책 번호가 중복되면 바로 오류 메시지 출력
                if self.books.find_by_id(book_id) is not None:
                    print(f"오류: 책 번호 '{book_id}'는 이미 존재합니다.")
                    continue
    
                title = input("책 제목을 입력하세요: ")

                #추가 기능에서 책 제목이 중복되면 바로 오류 메시지 출력
                if self.books.find_by_title(title) is not None:
                    print(f"오류: 책 제목 '{title}'는 이미 존재합니다.")
                    continue

                #책 번호와 책 제목이 중복되지 않을 때만 나머지 정보 입력 받기
                author = input("저자를 입력하세요: ")
                year = input("출판 연도를 입력하세요: ")
                self.add_book(book_id, title, author, year)
            elif choice == '2':
                title = input("삭제할 책 제목을 입력하세요: ")
                self.remove_book(title)
            elif choice == '3':
                title = input("조회할 책 제목을 입력하세요: ")
                self.search_book(title)
            elif choice == '4':
                self.display_books()
            elif choice == '5':
                print("프로그램을 종료합니다.")
                break
            else:
                print("오류: 잘못된 입력입니다. 다시 선택해 주세요.")

if __name__ == "__main__": #프로그램 실행
    system = BookManagementSystem()
    system.main()
