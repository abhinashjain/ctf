//gcc -c -fPIC libutil.c -o libutil.o
//gcc libutil.o -shared -o libutil.so

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void execute(const char *s)
{
    printf("Execute this! %s\n", s);
    if (strstr(s,"cvfP")) {
        printf("Not creating backup.tar! Make your own!\n");
    } else {
        system(s);
    }
}

