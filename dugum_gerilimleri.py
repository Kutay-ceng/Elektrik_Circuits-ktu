import numpy as np

def devre_cozumu(r1, r2, r3, r4, ig1, ig2):
    a = (1/r1) + (1/r2)
    b = -(1/r2)
    c = (1/r2) + (1/r3) + (1/r4)

    katsayi_matrisi = np.array([[a, b], 
                                [b, c]])
    
    akimlar = np.array([-ig1, ig2])

    gerilimler = np.linalg.solve(katsayi_matrisi, akimlar)
    
    return gerilimler[0], gerilimler[1]

if __name__ == "__main__":
    R1, R2, R3, R4 = 25.0, 5.0, 50.0, 75.0
    Ig1, Ig2 = 12.0, 16.0

    print("--- Gerilimler ---")
    v1, v2 = devre_cozumu(R1, R2, R3, R4, Ig1, Ig2)
    print(f"Hesaplanan V1: {v1:.4f} Volt")
    print(f"Hesaplanan V2: {v2:.4f} Volt")

    v1_yeni, v2_yeni = devre_cozumu(R1 * 1.1, R2, R3, R4, Ig1, Ig2)
    print(f"\nR1 %10 artinca yeni V1: {v1_yeni:.4f} V")
    print(f"V1'deki degisim: {v1_yeni - v1:.4f} V")
    print(f"\nR1 %10 artinca yeni V2: {v2_yeni:.4f} V")
    print(f"V2'deki degisim: {v2_yeni - v2:.4f} V")
