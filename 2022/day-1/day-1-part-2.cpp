#include <iostream> 
#include <fstream>
#include <string>
#include <vector>

using namespace std;


int max (int a, int b)
{
    if (a > b)
    {
        return a;
    } else 
    {
        return b;
    }
}


void bubble_sort(vector <int>& vector_address)
{
    // highly inefficient but appropriate for our
    // c++ journy beginins
    vector_address[2] = 42;
    cout << vector_address[0] << endl;
    cout << vector_address.size();


}


int main ()
{
    ifstream file ("./example.txt");

    char new_char, last_char;
    int total_calories = 0; 
    vector <int> elf_calories;
    string number = "";

    if (file.is_open())
    {
        while (file.get(new_char))
        {
            if (new_char == '\n')
            {
                if (last_char == '\n'){
                    // keep max reset and continue 
                    elf_calories.push_back(total_calories);
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

    for (int i=0; i < elf_calories.size(); i++)
    {
        cout << elf_calories[i] << "\n\b";
    }
    
    cout << "pass to bubble: " << endl; 
    
    bubble_sort(elf_calories);
    
    for (int i=0; i < elf_calories.size(); i++)
    {
        cout << elf_calories[i] << "\n\b";
    }

}