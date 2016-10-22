"""This is for the file with memory management."""
from Queue import Queue
from math import *
def main():
    num_test_cases = input()
    for test_case in range(0,3):
        case_stats_line = raw_input()
        num_pages = case_stats_line.split()[0]
        page_size = case_stats_line.split()[1]
        num_accesses = case_stats_line.split()[2]

        fifo_replacements = 0
        lru_replacements = 0

        access_addr = []
        for cycle in range(0,num_accesses):
            access_addr.append(input())

        fifo = Queue(num_pages)
        for addr in access_addr:
            if not fifo.full():
                fifo.put(addr/page_size)
            else:
                curr_page = fifo.get()
                if(addr/page_size!=curr_page):
                    fifo_replacements+=1

        lru = []
        for addr in access_addr:
            pass


    pass

if __name__=="__main__":
    main()