#include <stdio.h>


int max(int a, int b)
{
    if (a >= b){
        return a;
    } else {
        return b;
    }
}


int main()
{ 
    FILE *file;

    file = fopen("./example.txt", "r");

    if (file == NULL)
    {
        printf("Error opening file.\n");
        return 1;
    }

    fclose(file);

    return 0;
}










/*
int main()
{
    FILE *fh;

    fh = fopen("./example.txt", "r");

    if (fh != NULL)
    {
        char c;
        while ( (c = fgetc(fh)) != EOF )
        {
            putchar(c);
        }
        fclose(fh);
    } else printf("Error opening file.\n");

    return 0;
}
*/



/*
int y = 0;

int main(){
    int x = 4;
    printf("x is stored at %p\n", &x);
    printf("y is stored at %p\n", &y);

    return 0;
}
*/