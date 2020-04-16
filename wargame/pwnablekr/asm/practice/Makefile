LD=/usr/bin/ld
NASM=/usr/bin/nasm

OBJS=sh.o
TARGET=sh

all: $(TARGET)
clean: $(TARGET) $(OBJS)
	rm -rf $^

$(TARGET): $(OBJS)
	$(LD) -m elf_x86_64 $^ -o $@

$(OBJS): sh.a
	$(NASM) -f elf64 $^ -o $@
