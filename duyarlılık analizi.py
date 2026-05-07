def duyarlilik_katsayilarini_hesapla(R1, R2, R3, R4, Ig1, Ig2, v1, v2):
    a = (1/R1) + (1/R2)
    b = -(1/R2)
    c = (1/R2) + (1/R3) + (1/R4)
    Delta = (a * c) - (b**2)
    
    S_Ig1_v1 = -c / Delta  
    S_Ig2_v1 = -b / Delta     
    S_Ig1_v2 = b / Delta     
    S_Ig2_v2 = a / Delta

    # Formül: dV/dR = -(Y^-1) * (dY/dR) * V
    S_R1_v1 = (c * v1) / (Delta * (R1**2))
    S_R1_v2 = (-b * v1) / (Delta * (R1**2))
    
    S_R2_v1 = ((c + b) * (v1 - v2)) / (Delta * (R2**2))
    S_R2_v2 = (-(a + b) * (v1 - v2)) / (Delta * (R2**2))
    
    return {
        "S_Ig1_v1": S_Ig1_v1, "S_Ig2_v1": S_Ig2_v1,
        "S_Ig1_v2": S_Ig1_v2, "S_Ig2_v2": S_Ig2_v2,
        "S_R1_v1": S_R1_v1, "S_R1_v2": S_R1_v2,
        "S_R2_v1": S_R2_v1, "S_R2_v2": S_R2_v2,
    }

if __name__ == "__main__":
    R1, R2, R3, R4 = 25.0, 5.0, 50.0, 75.0
    Ig1, Ig2 = 12.0, 16.0

    v1_nom = 25
    v2_nom = 90

    print("---- Gerçek Matematiksel Duyarlılık Katsayıları ----")
    sonuclar = duyarlilik_katsayilarini_hesapla(R1, R2, R3, R4, Ig1, Ig2, v1_nom, v2_nom)
    
    for duyarlilik, deger in sonuclar.items():
        print(f"{duyarlilik} = {deger:.4f}")
