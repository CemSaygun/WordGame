

film_ismi=input("Film ismi giriniz: ")

yıldız=[]

for i in range(0,len(film_ismi)):
    if film_ismi[i]==" ":
        yıldız.append(" ")
    else:
        yıldız.append("*")

print("""
      
      1) oyundan çıkmak için 'q' yazınız
      2) tahmin yapmak için 'tahmin' yazınız
      3) küçük harf kullanınız
      
      """)



while(True):
    harf=input("harf giriniz: ")
    if harf =="q":
        break
    elif harf=="tahmin":
        tahmin=input("tahmininiz: ")
        if tahmin==film_ismi:
            print("BRAVOO")
            break
        else:
            print("DADAAANTT")
            continue
    
    if harf in film_ismi:
        for i in range(0,len(film_ismi)):
            if film_ismi[i]==harf:
                    yıldız[i]=harf
        print("".join(yıldız))
    else:
        print("DADAAANTT")
  
            
    
