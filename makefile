CC = gcc
CFLAGS = -Wall -g

all: mem_alloc

# mem_alloc
mem_alloc: source/mem_alloc.o
	$(CC) $(CFLAGS) $^ -o $@

source/mem_alloc.o: source/mem_alloc.c
	$(CC) $(CFLAGS) -c $< -o $@

# secret_santa
secret_santa:
	python source/secret_santa.py
#clean
c: 
	clear
	rm source/*.o



# $@ reffers to named before :
# $^ reffers to all named after :
# $< reffers to first after :
