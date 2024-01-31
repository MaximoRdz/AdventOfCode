#include <iostream>
#include <fstream>
#include <string>


using namespace std;


int main()
{
    string line;
    ifstream file ("./example.txt");

    if (file.is_open())
    {
        char c;
        while (file.get(c))
        {
            if (c == '\n')
            {
                cout << "hola";
            }
            cout << c;
        }
        file.close();
    }
    else cout << "File not opened.";

    return 0;
}



