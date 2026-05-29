# =========================
# FINAL STRUKTUR DATA
# SILOG (Sistem Informasi Logistik)
# Sampai Menu 2.3
# =========================


# =====================================
# GRAPH : JARINGAN HUB DAN RUTE
# =====================================

class Graph:
    def __init__(self):
        self.graph = {}

    def tambah_hub(self, kota):
        if kota not in self.graph:
            self.graph[kota] = []
            print("Hub berhasil ditambahkan")
        else:
            print("Kota sudah ada")

    def tambah_rute(self, kota1, kota2, jarak):

        if kota1 not in self.graph or kota2 not in self.graph:
            print("Kota belum terdaftar")
            return

        # graph tidak berarah
        self.graph[kota1].append((kota2, jarak))
        self.graph[kota2].append((kota1, jarak))

        print("Rute berhasil ditambahkan")

    def cek_rute(self, asal, tujuan):

        if asal not in self.graph:
            return False, 0

        for tetangga, jarak in self.graph[asal]:
            if tetangga == tujuan:
                return True, jarak

        return False, 0

    def tampil_graph(self):
        for kota in self.graph:
            print(kota, "->", self.graph[kota])


# =====================================
# BST RESI PENGIRIMAN
# =====================================

class Node:
    def __init__(self, no_resi, pengirim, asal,
                 tujuan, berat, biaya):

        self.no_resi = no_resi
        self.pengirim = pengirim
        self.asal = asal
        self.tujuan = tujuan
        self.berat = berat
        self.biaya = biaya

        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, node):

        if root is None:
            return node

        if node.no_resi < root.no_resi:
            root.left = self.insert(root.left, node)

        elif node.no_resi > root.no_resi:
            root.right = self.insert(root.right, node)

        return root

    def tambah_resi(self, node):
        self.root = self.insert(self.root, node)

    # INORDER
    def inorder(self, root):

        if root is not None:

            self.inorder(root.left)

            print("======================")
            print("No Resi :", root.no_resi)
            print("Pengirim :", root.pengirim)
            print("Asal :", root.asal)
            print("Tujuan :", root.tujuan)
            print("Berat :", root.berat, "Kg")
            print("Biaya :", root.biaya)

            self.inorder(root.right)

    # pindahkan BST ke list
    def simpan_ke_list(self, root, data):

        if root is not None:
            self.simpan_ke_list(root.left, data)
            data.append(root)
            self.simpan_ke_list(root.right, data)


# =====================================
# PROGRAM UTAMA
# =====================================

hub = Graph()
resi_bst = BST()

# custom data awal
hub.tambah_hub("OKTAV")


while True:

    print("\n========== SILOG ==========")
    print("1. Kelola Jaringan Hub")
    print("2. Kelola Administrasi Resi")
    print("0. Exit")
    pilih = input("Pilih menu : ")

    # =====================================
    # MENU 1
    # =====================================

    if pilih == "1":

        while True:

            print("\n--- KELOLA HUB ---")
            print("1.1 Input Hub Kota Baru")
            print("1.2 Input Rute Antar Kota")
            print("0. Kembali")

            sub = input("Pilih menu : ")

            # MENU 1.1
            if sub == "1.1":

                kota = input("Masukkan nama kota : ")
                hub.tambah_hub(kota)

            # MENU 1.2
            elif sub == "1.2":

                kota1 = input("Kota asal : ")
                kota2 = input("Kota tujuan : ")
                jarak = int(input("Jarak KM : "))

                hub.tambah_rute(kota1, kota2, jarak)

            elif sub == "0":
                break

            else:
                print("Menu tidak tersedia")


    # =====================================
    # MENU 2
    # =====================================

    elif pilih == "2":

        while True:

            print("\n--- ADMINISTRASI RESI ---")
            print("2.1 Input Resi Baru")
            print("2.2 Lihat Seluruh Resi")
            print("2.3 Urutkan Berdasarkan Biaya")
            print("0. Kembali")

            sub2 = input("Pilih menu : ")

            # =====================================
            # MENU 2.1
            # =====================================

            if sub2 == "2.1":

                while True:

                    no_resi = input("No Resi : ")

                    # validasi no resi awal 2
                    if no_resi[0] != "2":
                        print("No resi harus diawali angka 2")
                        continue

                    pengirim = input("Nama Pengirim : ")
                    asal = input("Kota Asal : ")
                    tujuan = input("Kota Tujuan : ")
                    berat = int(input("Berat Paket : "))

                    ada_rute, jarak = hub.cek_rute(asal, tujuan)

                    if ada_rute == False:
                        print("Rute pengiriman belum tersedia")
                    else:

                        biaya = (jarak * 2000) + (berat * 5000)

                        node_baru = Node(
                            no_resi,
                            pengirim,
                            asal,
                            tujuan,
                            berat,
                            biaya
                        )

                        resi_bst.tambah_resi(node_baru)

                        print("Input Resi Berhasil")

                    lagi = input("Input lagi? (Y/N) : ")

                    if lagi.upper() == "N":
                        break

            # =====================================
            # MENU 2.2
            # =====================================

            elif sub2 == "2.2":

                print("\nDATA RESI TERDAFTAR")
                resi_bst.inorder(resi_bst.root)

            # =====================================
            # MENU 2.3
            # =====================================

            elif sub2 == "2.3":

                data = []

                resi_bst.simpan_ke_list(resi_bst.root, data)

                # SELECTION SORT
                n = len(data)

                for i in range(n):

                    max_index = i

                    for j in range(i + 1, n):

                        if data[j].biaya > data[max_index].biaya:
                            max_index = j

                    data[i], data[max_index] = \
                        data[max_index], data[i]

                print("\nURUTAN BIAYA TERBESAR")

                for item in data:

                    print("====================")
                    print("No Resi :", item.no_resi)
                    print("Pengirim :", item.pengirim)
                    print("Biaya :", item.biaya)

            elif sub2 == "0":
                break

            else:
                print("Menu tidak tersedia")


    # =====================================
    # EXIT
    # =====================================

    elif pilih == "0":

        print("Program selesai")
        break

    else:
        print("Menu tidak tersedia")