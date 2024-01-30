#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>

using namespace std;


int main()
{
    string line;
    ifstream file ("./example.txt");

    if (file.is_open())
    {
        while (getline(file, line))
        {
            int calory = 0;
            calory = stoi(line);
            // have a look at <vector>
            cout << calory << "\n";
        }
        file.close();
    }
    else cout << "File not opened.";

    return 0;
}



