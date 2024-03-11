class MenuItem:
    def __init__(self, NamaMenu, Harga):
        self.NamaMenu = NamaMenu
        self.Harga = Harga
        self.next = None

head = None
tail = None
current = None

def addMenuItem(NamaMenu, Harga):
    global head, tail, current
    new_item = MenuItem(NamaMenu, Harga)
    if head is None:
        head = new_item
        tail = new_item
        current = new_item
    else:
        tail.next = new_item
        tail = new_item

def DisplayMenu():
    global head
    current = head
    while current is not None:
        print(current.NamaMenu, "Rp.", current.Harga)
        current = current.next

# Main program
print("Selamat Datang di E-Order Warung D4 MIE")
print("Ice Cream dan Mie Pedas tersedia di warung ini!!\n")

print("DAFTAR MENU WARUNG D4 MIE\n")
addMenuItem("Mixue Ice Cream", 5000)
addMenuItem("Boba Shake", 16000)
addMenuItem("Mi Sundae", 14000)
addMenuItem("Mie Ganas", 11000)
addMenuItem("Creamy Mango Boba", 22000)
DisplayMenu()

# Take order
totalHarga = 0
MaxPesanan = 10
pesanan = ["" for i in range(MaxPesanan)]
harga = [0 for i in range(MaxPesanan)]
Jml_Pesanan = 0

while True:
    order = input("Silahkan ketik pesanan Anda: ")
    if order == "done":
        break
    print("------ (Ketik 'done' untuk step berikutnya) ------")
    print("==> " + order + " sudah ditambahkan ke keranjang <==")
    
    current = head
    while current is not None:
        if current.NamaMenu.lower() == order.lower():
            pesanan[Jml_Pesanan] = current.NamaMenu
            harga[Jml_Pesanan] = current.Harga
            Jml_Pesanan += 1
            totalHarga += current.Harga
            break
        current = current.next

print("\n|| Pesanan Anda ||")
for i in range(Jml_Pesanan):
    print(pesanan[i], "- Rp.", harga[i])
print("Total harga pesanan Anda: Rp.", totalHarga)
print("------ Terima Kasih telah E-Order di Warung Kami ------")