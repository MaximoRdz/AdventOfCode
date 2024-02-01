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
        char new_char, last_char;
        int total_calories = 0;
        string number = "";

        while (file.get(new_char))
        {
            if (new_char == '\n')
            {
                if (last_char == '\n'){
                    // keep max and continue 
                    cout << "total: " << total_calories << endl;
                    number.clear();
                    continue;
                }
                // string to int update sum
                total_calories += stoi(number);
                cout << stoi(number) << endl;
                number.clear();
            } else {
                number = number + new_char;
                last_char = new_char;
            }
        }
        file.close();
    }
    else cout << "File not opened.";

    return 0;
}



