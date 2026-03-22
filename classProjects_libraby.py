class BookNode:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True
        self.next = None

class BookLinkedList:
    def __init__(self):
        self.head = None

    def add_book(self, title, author):
        new_book = BookNode(title, author)
        if not self.head:
            self.head = new_book
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_book
        print(f"  [Library] Book added: '{title}' by {author}")

    def find_book(self, title):
        current = self.head
        while current:
            if current.title == title:
                return current
            current = current.next
        return None

    def show_all_books(self):
        print("\n  All Books in Library:")
        current = self.head
        if not current:
            print("    No books available.")
            return
        while current:
            status = "Available" if current.is_available else "Issued"
            print(f"    - '{current.title}' by {current.author} [{status}]")
            current = current.next

class QueueNode:
    def __init__(self, member_name):
        self.member_name = member_name
        self.next = None

class WaitingQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, member_name):
        new_node = QueueNode(member_name)
        if not self.rear:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
        print(f"  [Queue] '{member_name}' added to waiting list (Position: {self.size})")

    def dequeue(self):
        if not self.front:
            return None
        member = self.front.member_name
        self.front = self.front.next
        if not self.front:
            self.rear = None
        self.size -= 1
        return member

    def is_empty(self):
        return self.front is None

    def show_waiting(self):
        print("  Waiting List:")
        current = self.front
        pos = 1
        if not current:
            print("    (No one waiting)")
            return
        while current:
            print(f"    {pos}. {current.member_name}")
            current = current.next
            pos += 1

class LibrarySystem:
    def __init__(self):
        self.books = BookLinkedList()
        self.waiting_lists = {}

    def add_book(self, title, author):
        self.books.add_book(title, author)
        self.waiting_lists[title] = WaitingQueue()

    def issue_book(self, title, member_name):
        print(f"\n'{member_name}' wants to borrow: '{title}'")
        book = self.books.find_book(title)
        if not book:
            print(f"  Book '{title}' not found in library.")
            return
        if book.is_available:
            book.is_available = False
            print(f"  Book issued to '{member_name}' successfully!")
        else:
            print(f"  Book not available. Adding to waiting list...")
            self.waiting_lists[title].enqueue(member_name)

    def return_book(self, title, member_name):
        print(f"\n'{member_name}' is returning: '{title}'")
        book = self.books.find_book(title)
        if not book:
            print(f"  Book '{title}' not found.")
            return
        waiting = self.waiting_lists[title]
        if waiting.is_empty():
            book.is_available = True
            print(f"  Book returned. Now available for anyone.")
        else:
            next_member = waiting.dequeue()
            print(f"  Book auto-issued to next in line: '{next_member}'")

    def show_waiting_list(self, title):
        print(f"\nWaiting List for '{title}':")
        if title in self.waiting_lists:
            self.waiting_lists[title].show_waiting()
        else:
            print("  Book not found.")


# ── DEMO ────────────────────────────────────
print("=" * 50)
print("   COLLEGE LIBRARY MANAGEMENT SYSTEM")
print("=" * 50)

lib = LibrarySystem()

print("\n--- Adding Books ---")
lib.add_book("Python Basics", "Guido van Rossum")
lib.add_book("Data Structures", "Mark Allen Weiss")

lib.books.show_all_books()

lib.issue_book("Python Basics", "Rahul")
lib.issue_book("Python Basics", "Priya")
lib.issue_book("Python Basics", "Amit")
lib.issue_book("Python Basics", "Sneha")

lib.show_waiting_list("Python Basics")

lib.return_book("Python Basics", "Rahul")

lib.show_waiting_list("Python Basics")

lib.books.show_all_books()