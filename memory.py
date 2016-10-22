"""This is for the file with memory management."""
from Queue import Queue
from collections import deque
from math import *
def main():
    num_test_cases = input()
    for test_case in range(0,num_test_cases):
        case_stats_line = raw_input()
        num_pages = int(case_stats_line.split()[0])
        page_size = int(case_stats_line.split()[1])
        num_accesses = int(case_stats_line.split()[2])

        fifo_replacements = 0
        lru_replacements = 0

        access_addr = []
        for cycle in range(0,num_accesses):
            access_addr.append(input())

        fifo = deque([],num_pages)
        for addr in access_addr:
            page = addr/page_size
            if page not in fifo:
                if len(fifo)>=fifo.maxlen:
                    fifo.popleft()#Remove the least recently added page.
                    fifo_replacements+=1
                fifo.append(page)#Always add the page/add it back.

        lru = deque([],num_pages)
        for addr in access_addr:
            page = addr/page_size
            if page in lru:
                lru.remove(page)
            else:
                if len(lru)>=lru.maxlen:
                    lru.popleft()# Removes least recently used.
                    lru_replacements+=1
            lru.append(page)#No matter what, page should be added to most recent place.

        if fifo_replacements>lru_replacements:
            print("yes"),#Comma to prevent new line.
        else:
            print("no"),
        print(str(fifo_replacements)+" "+str(lru_replacements))

if __name__=="__main__":
    main()