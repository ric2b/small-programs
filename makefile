CC = gcc
CFLAGS = -Wall -g

all: mem_alloc

# mem_alloc
mem_alloc: mem_alloc.o
	$(CC) $(CFLAGS) $^ -o $@
	rm mem_alloc.o

mem_alloc.o: mem_alloc.c
	$(CC) $(CFLAGS) -c $< -o $@

c: 
	clear
	rm *.o



# $@ reffers to named before :
# $^ reffers to all named after :
# $< reffers to first after :
