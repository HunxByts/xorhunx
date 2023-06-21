#!/usr/bin/python
#Encode Decode XOR and burforce
#MAU RECODE ??? IZIN DULU LAH,  MINIMAL TAG AKUN GITHUB MIMIN YANG MENGARAH KE AKUN INI, LEBIH GAMPANG SI PAKE FORK
#KALAU DI ATAS TIDAK DI IKUTI MAKA AKAN MENDAPATKAN DOSA KARENA MIMIN GAK IKHLAS
#“Wahai orang-orang yang beriman! Janganlah kamu saling memakan harta sesamamu dengan jalan yang batil,” (QS. An Nisaa': 29). Rasulullah SAW juga melarang umatnya untuk mengambil hak orang lain tanpa izin.

# ############################
# #    TOOL CEYPTOGRAPHY     #
# #  BY FAISS || HUNXBYTS    #
# ############################

# import Module 
from sys import stderr
import platform
import os

# kondisi  Os yang di gunakan Linux atau Windows
jenis_system = platform.system()

if  jenis_system == 'Linux':
    os.system('clear')
elif jenis_system == 'Windows':
    os.system('cls')

# Variable Color
Bl='\033[30m' #black
Re='\033[1;31m' #red
Gr='\033[1;32m' #green
Ye='\033[1;33m' #yellow
Blu='\033[1;34m' #blue
Mage='\033[1;35m' #magenta
Cy='\033[1;36m' #cyan
Wh='\033[1;37m' #white

stderr.writelines(f"""{Cy}

██╗  ██╗ ██████╗ ██████╗       ██╗  ██╗██╗   ██╗███╗   ██╗██╗  ██╗
╚██╗██╔╝██╔═══██╗██╔══██╗      ██║  ██║██║   ██║████╗  ██║╚██╗██╔╝
 ╚███╔╝ ██║   ██║██████╔╝█████╗███████║██║   ██║██╔██╗ ██║ ╚███╔╝ 
 ██╔██╗ ██║   ██║██╔══██╗╚════╝██╔══██║██║   ██║██║╚██╗██║ ██╔██╗ 
██╔╝ ██╗╚██████╔╝██║  ██║      ██║  ██║╚██████╔╝██║ ╚████║██╔╝ ██╗
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝      ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝
                {Ye}TOOL XOR CRYPTOGRAPHY BY HUNXBYTS 
""")
#Menu Options
print(f"""
{Wh}----------------------------------------------------------------
{Wh}[{Ye}1{Wh}] {Ye}Tool Xor Encode
{Wh}[{Ye}2{Wh}] {Ye}Tool Xor Decode
{Wh}[{Ye}3{Wh}] {Ye}Tool xor Burtforce
{Wh}----------------------------------------------------------------
""")
user = input(f"{Ye}╰ > {Wh}xor-tool {Ye}⊚ > {Wh}")
print("----------------------------------------------------------------")

#Process Encode XOR
if user == '1':
    try:
        def encodeXOR(plaintext, getKey ):
            chipertext = ""
            for i in (plaintext):
                chipertext += chr(ord(i) ^ getKey)
            return chipertext

        plaintext = input(f"{Wh}[{Ye}+{Wh}] {Ye}Input Plaintext {Wh}: {Wh}")
        print("----------------------------------------------------------------")
        print(f"""
{Wh}Choice Key\n  
{Wh}[{Ye}1{Wh}] {Ye}Biner
{Wh}[{Ye}2{Wh}] {Ye}Decimal
{Wh}[{Ye}3{Wh}] {Ye}Hexadecimal
{Wh}[{Ye}4{Wh}] {Ye}Ascii\n
{Wh}[{Ye}!{Wh}] {Wh}Enter the number
    """)
        print("----------------------------------------------------------------")
        pilih = input(f"{Wh}[{Ye}+{Wh}] {Ye}Enter Key options {Wh}: {Wh}")
        print("----------------------------------------------------------------")
        key = input(f"{Wh}[{Ye}+{Wh}] {Ye}Input Key {Wh}: {Wh}")
        print("----------------------------------------------------------------")

        if pilih == '1':
            getKey = int(key, 2)
        elif pilih == '2':
            getKey = int(key)
        elif pilih == '3':
            getKey = int(key, 16)
        elif pilih == '4':
            getKey = int(''.join(str(ord(c)) for c in key))
        else:
            print(f'{Wh}[{Re}!{Wh}] {Wh}Incorrect key selection!')
    
        encode = encodeXOR(plaintext, getKey)
        print(f"{Wh}[{Ye}+{Wh}] {Ye}Chipertext {Wh}: {Wh}{encode}")
        print("----------------------------------------------------------------")
    except KeyboardInterrupt:
        print(f" {Wh}[{Re}!{Wh}] {Wh}Program Stoped...")
#End Process

#Star Process Decode XOR
elif user == '2':
    try:
        def encodeXOR2(chipertext2, Key2):
            plaintext2 = ""
            for i in chipertext2:
                plaintext2 += chr(ord(i) ^ Key2)
            return plaintext2

        chipertext2 = input(f"{Wh}[{Ye}+{Wh}] {Ye}Input Chipertext {Wh}: {Wh}")
        print("----------------------------------------------------------------")
        print(f"""
{Wh}Choice Key\n  
{Wh}[{Ye}1{Wh}] {Ye}Biner
{Wh}[{Ye}2{Wh}] {Ye}Decimal
{Wh}[{Ye}3{Wh}] {Ye}Hexadecimal
{Wh}[{Ye}4{Wh}] {Ye}Ascii\n
{Wh}[{Ye}!{Wh}] {Wh}Masukkan nomor pilihan
""")
        print("----------------------------------------------------------------")
        pilih = input(f"{Wh}[{Ye}+{Wh}] {Ye}Enter Key options {Wh}: {Wh}")
        print("----------------------------------------------------------------")
        key2 = input(f"{Wh}[{Ye}+{Wh}] {Ye}Input Key {Wh}: {Wh}")
        print("----------------------------------------------------------------")

        if pilih == '1':
            Key2 = int(key2, 2)
        elif pilih == '2':
            Key2 = int(key2)
        elif pilih == '3':
            Key2 = int(key2, 16)
        elif pilih == '4':
            Key2 = int(''.join(str(ord(c)) for c in key2))
        else:
            print(f'{Wh}[{Re}!{Wh}] {Wh}Incorrect key selection!')

        encode2 = encodeXOR2(chipertext2, Key2)
        print(f"{Wh}[{Ye}+{Wh}] {Ye}Plaintext {Wh}: {Wh}{encode2}")
        print("----------------------------------------------------------------")
    except KeyboardInterrupt:
        print(f"{Wh}[{Re}!{Wh}] {Wh}Program Stoped...")
#End Process

#Star Process Burtforce
elif user == '3':
    try:
        def encodeXOR3(chipertext3, key3):
            plaintext3 = ""
            for i in (chipertext3):
                plaintext3 += chr(ord(i) ^ key3)
            return plaintext3
            
        chipertext3 = input(f"{Wh}[{Ye}+{Wh}] {Ye}Input chipertext {Wh}: {Wh}")
        print(f" {Wh}[{Ye}!{Wh}] {Ye}Program Stoped...")

        for key in range(256):
            plain = (encodeXOR3(chipertext3, key))
        print("----------------------------------------------------------------")
        print(f"\n{Wh}[{Ye}+{Wh}] {Ye}Hasil burtforce key {Wh}[{Wh}{key}] {Wh}: {Wh}[ {Ye}{plain} {Wh}]")
    except KeyboardInterrupt:
        print(f" {Wh}[{Ye}!{Wh}] {Wh}Program Stoped...")
#End Process

#Proces Invalid 
else:
    print(f"{Wh}[{Re}!{Wh}] {Wh}Opsi not found!")

