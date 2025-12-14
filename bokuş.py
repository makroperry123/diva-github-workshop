#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Basit bir Python programı

def merhaba():
    """Merhaba mesajı yazdır"""
    print("Merhaba, Dünya!")
    print("Bu basit bir Python programıdır.")

def hesaplama():
    """Basit bir hesaplama yap"""
    sayi1 = 10
    sayi2 = 20
    toplam = sayi1 + sayi2
    print(f"{sayi1} + {sayi2} = {toplam}")

if __name__ == "__main__":
    merhaba()
    hesaplama()
