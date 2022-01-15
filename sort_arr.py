class Sol:
    def sort_arr(self,arr):
        return [num for num in arr if num%2==0]+[num for num in arr if num%2==1]
if __name__ == '__main__':
    p = Sol()
    print(p.sort_arr(arr=[1,4,5,1]))
