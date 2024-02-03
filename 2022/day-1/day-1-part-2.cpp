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


void bubble_sort(vector <int>& vector_reference)
{
    // highly inefficient but appropriate for our
    // c++ journy beginins
    int aux;
    
    for (int i=0; i < vector_reference.size(); i++)
    {
        for (int j = 0; j < vector_reference.size()-1; j++)
        {
            if (vector_reference.at(j) < vector_reference.at(j+1))
            {
                aux = vector_reference.at(j+1);
                vector_reference.at(j+1) = vector_reference.at(j);
                vector_reference.at(j) = aux;
            }
        }
    }


}


int main ()
{
    ifstream file ("./input.txt");

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

        // push back extra last number: 
        elf_calories.push_back(total_calories + stoi(number));

        file.close();
    }
    else cout << "File not opened.";
    
    // for (int i=0; i < elf_calories.size(); i++)
    // {
    //     cout << elf_calories[i] << endl;
    // }

    bubble_sort(elf_calories);
    
    cout << "Solution Part 2: " << (elf_calories[0] +
                                    elf_calories[1] +
                                    elf_calories[2]) << endl; 

}