# python3
# import numpy as np

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    # arr = np.zeros((1, n), dtype=bool)
    arr = [[False for j in range(n)] for i in range(1)]
    time=0
    i=0
    # # while True:
    # #     if (m<=0):
    # #         break
    # #     for th in range(n):
    # #         if not (arr[th][time]): # if its not taken up
    # #             print(th, time)
    # #             for work in range(data[i]):
    # #                 if (work>=arr[th].size):
    # #                     for tmp in range(n):
    # #                         arr[th].append(False) # adding time
    # #                 arr[th][work] = True # taking up
    # #                 m=m-1
    # #                 i=i+1
    # for el in data:
    #     # if not enough threads, search another time
    #     for th in range(n): # add beark
    #         if not (arr[time][th]): # if its not taken up
    #             print(th, time)
    #             # if not enough time, append
    #             for work in range(el):
    #                 arr[time+work][th] = True
    while True:
        if (i>=m):
            break
        for th in range(n):
            if not (arr[time][th]): # if its not taken up
                print(th, time)
                while (len(arr)<(time+data[i])):
                    # arr_1d = np.zeros(n, dtype=bool)
                    arr_1d = [False for i in range(n)]
                    # arr = np.append(arr, [arr_1d], axis=0)
                    arr.append(arr_1d)
                for work in range(data[i]):
                    tmp = time+work
                    # print(tmp)
                    # if(tmp<len(arr)):
                    #     if (th<len(arr[tmp])):
                    arr[tmp][th] = True
                i+=1
        time = time +1



    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    text = input()
    if 'I' in text:
        line1 = input()
        line2 = input()
    elif 'F' in text:
        name = input()
        if not 'a' in name: 
            name = "test/"+name
            f = open(name, "r")
            line1 = f.readline()
            line2 = f.readline()
            # text = f.read()
            # raise Exception(text)
    n,m = line1.split(" ")
    n = int(n)
    m = int(m)
    Sdata = line2.split(" ")
    data = []
    for i in Sdata:
        data.append(int(i))
    # n = 0
    # m = 0
    
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    # data = []

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
