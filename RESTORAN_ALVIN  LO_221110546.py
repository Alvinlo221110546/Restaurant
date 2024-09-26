from abc import ABC, abstractmethod

class OrderObserver(ABC):
    @abstractmethod
    def update(self, order: 'Order') -> None:
        pass

class CustomerObserver(OrderObserver):
    def update(self, order: 'Order') -> None:
        print("Pesanan Anda telah diproses.")

class OrderSubject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer: OrderObserver) -> None:
        self._observers.append(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update(self)

class PaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> None:
        pass

    @abstractmethod
    def choose_payment_method(self) -> str:
        pass

class CreditCardPayment(PaymentStrategy):
    def process_payment(self, amount: float) -> None:
        print(f"Processing credit card payment: ${amount}")

    def choose_payment_method(self) -> str:
        return "Credit Card"

class CashPayment(PaymentStrategy):
    def process_payment(self, amount: float) -> None:
        print(f"Processing cash payment: ${amount}")

    def choose_payment_method(self) -> str:
        return "Cash"

class OrderProcessingTemplate(ABC):
    def process_order(self, order: 'Order') -> None:
        self.display_order(order)
        self.handle_payment(order)
        self.notify_customer(order)

    @abstractmethod
    def display_order(self, order: 'Order') -> None:
        pass

    @abstractmethod
    def handle_payment(self, order: 'Order') -> None:
        pass

    @abstractmethod
    def notify_customer(self, order: 'Order') -> None:
        pass

class CashierOrderProcessing(OrderProcessingTemplate):
    def display_order(self, order: 'Order') -> None:
        order.display_order()

    def handle_payment(self, order: 'Order') -> None:
        total_price = order.get_total_price(menu)
        payment.process_payment(total_price)
        print("Order processed by Cashier.")

    def notify_customer(self, order: 'Order') -> None:
        print("Customer notified about the order.")

class ChefOrderProcessing(OrderProcessingTemplate):
    def display_order(self, order: 'Order') -> None:
        order.display_order()

    def handle_payment(self, order: 'Order') -> None:
        pass

    def notify_customer(self, order: 'Order') -> None:
        print("Order is being prepared by Chef.")

class Menu:
    def __init__(self):
        self._items = {}

    def add_item(self, item_name, price):
        self._items[item_name] = price

    def display_menu(self):
        print("Menu:")
        for item, price in self._items.items():
            print(f"{item}: ${price}")

    def get_item_price(self, item_name):
        return self._items.get(item_name, None)

class Order:
    def __init__(self):
        self._items = {}

    def display_order(self):
        print("Order:")
        for item, quantity in self._items.items():
            print(f"{item} x{quantity}")

    def add_item(self, item_name, quantity):
        if item_name not in menu._items:
            raise ValueError(f"{item_name} tidak ada dalam menu.")
        if quantity <= 0:
            raise ValueError("Jumlah pesanan harus lebih dari 0.")

        if item_name in self._items:
            self._items[item_name] += quantity
        else:
            self._items[item_name] = quantity

    def get_total_price(self, menu):
        return sum([menu.get_item_price(item) * quantity for item, quantity in self._items.items()])

class Payment:
    def process_payment(self, amount):
        if amount <= 0:
            raise ValueError("Jumlah pembayaran harus lebih dari 0.")
        print(f"Payment processed: ${amount}")

class Reservation:
    def __init__(self):
        self._reservations = []

    def add_reservation(self, name, time):
        self._reservations.append({'name': name, 'time': time})
        print(f"Reservasi untuk {name} pada pukul {time} berhasil dilakukan.")

    def display_reservations(self):
        print("\nDaftar Reservasi:")
        for reservation in self._reservations:
            print(f"{reservation['name']} - {reservation['time']}")

class ReservationHandler:
    def __init__(self):
        self._reservation = Reservation()

    def make_reservation(self):
        name = input("Masukkan nama untuk reservasi: ")
        time = input("Masukkan waktu reservasi (HH:MM): ")
        if self.is_valid_time(time):
            self._reservation.add_reservation(name, time)
        else:
            print("Format waktu tidak valid. Gunakan format HH:MM.")

    def display_reservations(self):
        self._reservation.display_reservations()

    def is_valid_time(self, time):
        try:
            hours, minutes = map(int, time.split(':'))
            return 0 <= hours < 24 and 0 <= minutes < 60
        except ValueError:
            return False

menu = Menu()
menu.add_item("Nasi Goreng", 10)
menu.add_item("Soto Ayam", 8)
menu.add_item("Mie Goreng", 9)
menu.add_item("Ifumie Goreng", 11)
menu.add_item("Lontong Sayur", 14)
menu.add_item("Sate Ayam", 7)

order = Order()
payment = Payment()

customer_observer = CustomerObserver()
order_subject = OrderSubject()
order_subject.add_observer(customer_observer)

cashier_order_processing = CashierOrderProcessing()
chef_order_processing = ChefOrderProcessing()

reservation_handler = ReservationHandler()

while True:
    print("\n====== Restoran HOME FOOD ======")
    print("1. Menampilkan Menu")
    print("2. Menambah Pesanan")
    print("3. Menghapus Pesanan")
    print("4. Melakukan Reservasi")
    print("5. Melihat Daftar Pesanan")
    print("6. Melakukan Pembayaran")
    print("7. Keluar")

    choice = input("Masukkan pilihan Anda (1-7): ")

    if choice == "1":
        menu.display_menu()
    elif choice == "2":
        item_name = input("Masukkan nama menu yang ingin dipesan: ")
        quantity = int(input("Masukkan jumlah yang ingin dipesan: "))
        try:
            order.add_item(item_name, quantity)
            print(f"{quantity} {item_name}(s) ditambahkan ke dalam pesanan.")
        except ValueError as e:
            print(e)
    elif choice == "3":
        item_name = input("Masukkan nama menu yang ingin dihapus dari pesanan: ")
        if item_name in order._items:
            del order._items[item_name]
            print(f"{item_name} dihapus dari pesanan.")
        else:
            print(f"{item_name} tidak ditemukan dalam pesanan.")
    elif choice == "4":
        reservation_handler.make_reservation()
    elif choice == "5":
        order.display_order()
    elif choice == "6":
        total_price = order.get_total_price(menu)
        print("Pilih metode pembayaran:\n1. Credit Card\n2. Cash")
        payment_choice = input("Masukkan pilihan metode pembayaran (1/2): ")
        payment_strategy = CreditCardPayment() if payment_choice == "1" else CashPayment()
        payment_strategy.process_payment(total_price)
        order_subject.notify_observers()
        if total_price > 50:
            chef_order_processing.process_order(order)
        else:
            cashier_order_processing.process_order(order)
        print(f"Pembayaran berhasil dengan metode {payment_strategy.choose_payment_method()}.")
    elif choice == "7":
        print("Terima kasih telah menggunakan layanan Restoran HOME FOOD. Sampai jumpa lagi!")
        break
    else:
        print("Pilihan tidak valid.")
