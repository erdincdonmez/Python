# merge sort

def mergeSort(dizi):
   if len(dizi) > 1:
        mid = len(dizi) // 2
        left = dizi[:mid]
        right = dizi[mid:]

        # Yarılanmışı çağır
        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        
        # Ana yineleyici
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              dizi[k] = left[i]
              i += 1
            else:
                dizi[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            dizi[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            dizi[k]=right[j]
            j += 1
            k += 1
   return dizi  

dizi = [16,21,11,8,12,22]
print(mergeSort(dizi))