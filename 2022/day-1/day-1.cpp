#include <iostream>
#include <fstream>
#include <string>


using namespace std;


int max (int a, int b)
{
    if (a > b)
    {
        return a;
    } else {
        return b;
    }
}


int main ()
{
    ifstream file ("./input.txt");

    char new_char, last_char;
    int total_calories = 0, max_calories = 0;
    string number = "";

    if (file.is_open())
    {
        while (file.get(new_char))
        {
            if (new_char == '\n')
            {
                if (last_char == '\n'){
                    // keep max reset and continue 
                    max_calories = max(max_calories, total_calories);
                    total_calories = 0;
                } else {
                    // string to int update sum
                    total_calories += stoi(number);
                }
                number.clear();
            } else {
                number = number + new_char;
            }
            last_char = new_char;
        }
        file.close();
    }
    else cout << "File not opened.";

    cout << "Solution Part 1: " << max_calories << endl;

    return 0;
}
