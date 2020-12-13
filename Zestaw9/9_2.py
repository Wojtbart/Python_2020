class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogólnie


class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0   # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        # return self.length == 0
        return self.head is None

    def count(self):   # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.head:   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):   # klasy O(N)
        if self.head:   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):          # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None   # czyszczenie łącza
        self.length -= 1
        return node   # zwracamy usuwany node

# pozostałe metody

    def remove_tail(self):   # klasy O(N)
        # Zwraca cały węzeł, skraca listę.
        # Dla pustej listy rzuca wyjątek ValueError.
        if self.is_empty():
            raise ValueError("Pusta lista!!!")
        node = self.tail
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next.next:  # patrzymy na kolejny
                temp = temp.next  # dajemy mu nastepny
            self.tail = temp
            temp.next = None

        self.length -= 1
        return node   # zwracamy usuwany node

    def merge(self, other):    # klasy O(1)
        # Węzły z listy other są przepinane do listy self na jej koniec.
        # Po zakończeniu operacji lista other ma być pusta.
        if self.is_empty() or other.is_empty():
            raise ValueError("Pusta lista!!!")
        if self != other:
            self.tail.next = other.head
            self.tail = other.tail
            self.length += other.length
            other.clear()

    def clear(self):     # czyszczenie listy
        self.length = 0
        self.head = None
        self.tail = None

    def search(self, data):    # klasy O(N)
        # Zwraca łącze do węzła o podanym kluczu lub None.
        if self.is_empty():
            return None
        else:
            temp = self.head

            while temp != None:
                if temp.data == data:
                    return temp.data
                else:
                    temp = temp.next
            return None

    def find_min(self):    # klasy O(N)
        # Zwraca łącze do węzła z najmniejszym kluczem lub None dla pustej listy.
        if self.is_empty():
            return None
        mini = self.head
        temp = self.head
        while temp != None:
            if temp.data < mini.data:
                mini = temp
            else:
                temp = temp.next
        return mini

    def find_max(self):  # klasy O(N)
        # Zwraca łącze do węzła z największym kluczem lub None dla pustej listy.
        if self.is_empty():
            return None
        maxi = self.head
        temp = self.head
        while temp != None:
            if temp.data > maxi.data:
                maxi = temp
            else:
                temp = temp.next
        return maxi

    # def reverse(self):   # klasy O(N)
    #     # Odwracanie kolejności węzłów na liście.
    #     node = self.head
    #     temp = self.head
    #     if node:
    #         while temp.next:
    #             node = temp.next
    #             temp.next = node.next
    #             node.next = self.head
    #             self.head = node


if __name__ == '__main__':

    alist = SingleList()
    alist.insert_head(Node(11))  # [11]
    alist.insert_tail(Node(22))  # [11, 22]
    alist.insert_tail(Node(33))  # [11, 22, 33]
    print("Dlugosc a listy:", alist.count())

    blist = SingleList()
    blist.insert_head(Node(33))  # [33]
    blist.insert_tail(Node(44))  # [33, 44]
    blist.insert_tail(Node(55))  # [33, 44, 55]
    print("Dlugosc b listy:", blist.count())

    print("Usuwam z listy a ogon o wartosci:", alist.remove_tail())

    alist.merge(blist)  # merge 2 list
    print("Po polaczeniu listy a oraz listy b lista a ma dlugosc:", alist.count())

    print("szukam elementu 33 w liscie a =>", alist.search(33))
    print("szukam elementu 55 w liscie a =>", alist.search(55))
    print("szukam elementu 66 w liscie a =>", alist.search(66))

    print("Najmniejszy element w liście a to:", alist.find_min())
    print("Najwiekszy element w liście a to:", alist.find_max())

    blist.clear()
    print("Dlugosc b listy po wyczyszczeniu to:", blist.count())

    # print("Odwracam liste a")
    # alist.reverse()  # [55,44,33,22,11]

    while not alist.is_empty():
        print("Usuwam głowe:", alist.remove_head())
