LD=/usr/bin/ld
NASM=/usr/bin/nasm

OBJS=asm.o
TARGET=asm

all: $(TARGET)
clean: $(TARGET) $(OBJS)
	rm -rf $^

$(TARGET): $(OBJS)
	$(LD) -m elf_i386 $^ -o $@

$(OBJS): asm.a
	$(NASM) -f elf32 $^ -o $@
