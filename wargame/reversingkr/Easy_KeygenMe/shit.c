#include <stdio.h>
#include <stdint.h>
#include <string.h>

const char key[3] = { 0x10, 0x20, 0x30 };

int encrypt();
int decrypt();

int encrypt()
{
  char name[32];
  char serialKey[32];

  memset(name, (void *)0x00, sizeof(char) * 32);
  memset(serialKey, (void *)0x00, sizeof(char) * 32);

  printf("input name: ");
  scanf("%s", name);

  int v1 = 0;
  for (unsigned int v0 = 0; v1 < strlen(&name); v0++) {
    if (v0 >= 3) v0 = 0;
    sprintf(&serialKey, "%s%02x", &serialKey, name[v1++] ^ key[v0]);
  }
  printf("%s", serialKey);
  return 0;
}

int decrypt()
{
  unsigned char name[32];
  unsigned char serialKey[32] = {0x5B,0x13,0x49,0x77,0x13,0x5E,0x7D,0x13};
  unsigned int v0 = 0;

  memset(name, (void *)0x00, sizeof(char) * 32);

  for (unsigned int v1 = 0; v1 < strlen(serialKey); v1++, v0++) {
    if (v0 >= 3) v0 = 0;
    sprintf(&name, "%s%x", &name, serialKey[v1] ^ key[v0]);
  }
  printf("%s\n", &name);
  return 0;
}

int main(int argc, char** argv)
{
  printf("[e]ncrypt\n[d]ecrypt\n>");
  switch (getchar()) {
    case 'e':
      encrypt();
      break;
    case 'd':
      decrypt();
      break;
  }
  return 0;
}
