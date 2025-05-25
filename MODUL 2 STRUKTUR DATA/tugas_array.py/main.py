class Node:
    def _init_(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def _init_(self):
        self.head = None

    # Menambahkan node di akhir list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    # Menampilkan isi list
    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=' <-> ')
            curr = curr.next
        print("None")

    # 1. Menghapus node awal
    def delete_from_beginning(self):
        if self.head is None:
            print("List kosong.")
            return
        print(f"Menghapus node awal: {self.head.data}")
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    # 2. Menghapus node akhir
    def delete_from_end(self):
        if self.head is None:
            print("List kosong.")
            return
        curr = self.head
        if curr.next is None:
            print(f"Menghapus node akhir (tunggal): {curr.data}")
            self.head = None
            return
        while curr.next:
            curr = curr.next
        print(f"Menghapus node akhir: {curr.data}")
        curr.prev.next = None

    # 3. Menghapus node berdasarkan nilai data
    def delete_by_value(self, value):
        curr = self.head
        while curr:
            if curr.data == value:
                print(f"Menghapus node dengan nilai: {value}")
                # Node di awal
                if curr.prev is None:
                    self.head = curr.next
                    if self.head:
                        self.head.prev = None
                # Node di tengah atau akhir
                else:
                    curr.prev.next = curr.next
                    if curr.next:
                        curr.next.prev = curr.prev
                return
            curr = curr.next
        print(f"Node dengan nilai {value} tidak ditemukan.")

# === Contoh penggunaan ===

dll = DoubleLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)

print("Isi awal linked list:")
dll.display()

dll.delete_from_beginning()
dll.display()

dll.delete_from_end()
dll.display()

dll.delete_by_value(20)
dll.display()

dll.delete_by_value(99)  # Coba hapus data yang tidak ada