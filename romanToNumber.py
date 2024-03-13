def to_number(roman):
    numbers = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000,
    }

    total = 0
    #döngü için index temsil eden 'i' değişkenini 0-sıfır olarak tanımladım
    #amaç: Roma rakamı içinde index değerine göre karakterin karşılığını getirmek
    i = 0

    # while döngüsü i+1 olarak başlattım. 'Index out of range' hatası almamak için i+1 den başlattım
    while i+1 < len(roman):

        #val = 'numbers' sözlüğündeki çağırılacak ilk/çağırılması gereken mevcut değer
        val = numbers[roman[i]]
        #next_val = 'numbers' sözlüğündeki çağırılacak bir sonraki değer
        next_val = numbers[roman[i+1]]

        if next_val > val :  
            #Örneğin; val=100 , next_val=1000 diyelim. next_val, val den büyük olduğu için, toplam değer [ next_val - val ] olacak. [1000 - 100 => 900]
            x = next_val - val
            total += x
            i+=1
        else:
            total += val

        # YUKARIDAKİ KOŞULLAR:
        # Eğer bir sonraki değer(next_val), mevcut değerden(val) büyükse:
            # bir sonraki değerden mevcut değeri çıkart ve 'x' değişkenine ata
            # 'x' değerini 'total' değişkenine ekle
            # 'i' yi BİR arttır. Bunu yapmadığımız zaman fazladan değer eklemesi yapar. 
            
            ## Bu koşuldaki amaç: Mevcut değerden küçük olan değer, büyük olan bir sonraki değerden farkı alınarak eklenir. 
            ## Koşul içinde artırma yapmadığımız zaman ise bir sonraki değeri de eklemiş olur, dönüştürülmesi gereken sayı sonucu fazla çıkar.
            
        #DEĞİLSE:
            #mevcut değeri olduğu gibi total değişkenine ekle

        i+=1 #Burada döngü için artırıyoruz

    if next_val > val : 
         #Döngüden sonra eğer bir sonraki değer, mevcut değerden büyükse, olduğu gibi sonucu(total) döndür.
         return total
    else:
        #Değilse, bir sonraki değeri de sonuca(total) ekle ondan sonra döndür.
        total+= next_val
        return total
        

print(to_number('MCMVII')) #1907
print(to_number('MMXI')) #2011
print(to_number('XC')) #90
print(to_number('MCMXC')) #1990