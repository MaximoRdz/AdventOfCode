/**
 * Rock, paper, scissors
 * A: Rock      1
 * B: Paper     2
 * C: Scissors  3
 * 
 * Loss:        0
 * Draw:        3
 * Win:         6
 * 
 * Second column is response:
 * X: Rock
 * Y: Paper
 * Z: Scissors
*/

#include <iostream>
#include <fstream>
#include <string>

using namespace std;


int response_value(char a)
{
    if (a == 'X')
    {
        return 1;
    } else if (a == 'Y')
    {
        return 2;
    } else{
        return 3;
    }
}


char defeats (char hand)
{
    if (hand == 'X')
    {
        return 'C';
    } else if (hand == 'Y')
    {
        return 'A';
    } else if (hand == 'Z')
    {
        return 'B';
    } else if (hand == 'C')
    {
        return 'Y';
    } else if (hand == 'A')
    {
        return 'Z';
    } else if (hand == 'B')
    {
        return 'X';
    } else
    {
        return ' ';
    }
}

int play_result(char play, char response)
{
    if (defeats(response) == play)
    {
        return 6;
    } else if (defeats(play) == response)
    {
        return 0;
    } else
    { 
        return 3;
    }
}

int main()
{
    ifstream file("./input.txt");
    string line;
    char play, response;
    int ans = 0;

    if (file.is_open())
    {
        while (getline(file, line))
        {   
            play = line[0];
            response = line[2];

            ans += play_result(play, response) + response_value(response);
        }
    }
    cout << "Solution Part 1: " << ans << endl;
}
