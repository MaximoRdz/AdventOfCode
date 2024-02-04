/**
 * Now the second column means how the round 
 * needs to end: 
 * X: lose
 * Y: draw
 * Z: win
*/

#include <iostream>
#include <fstream>
#include <string>

using namespace std;


char char_to_win(char play)
{
    if (play == 'A')
    {
        return 'B';
    } else if (play == 'B')
    {
        return 'C';
    } else
    {
        return 'A';
    }
}


char char_to_lose(char play)
{
    if (play == 'A')
    {
        return 'C';
    } else if (play == 'B')
    {
        return 'A';
    } else
    {
        return 'B';
    }
}


char char_to_draw(char play)
{
    return play;
}


char response(char play, char need)
{
    if (need == 'X')
    {
        return char_to_lose(play);
    } else if (need == 'Y')
    {
        return char_to_draw(play);
    } else 
    {
        return char_to_win(play);
    }
}


int response_value(char a)
{
    if (a == 'A')
    {
        return 1;
    } else if (a == 'B')
    {
        return 2;
    } else{
        return 3;
    }
}


int play_result(char need)
{
    if (need == 'Z')
    {
        return 6;
    } else if (need == 'X')
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
    char play, need;
    int ans = 0;

    if (file.is_open())
    {
        while (getline(file, line))
        {   
            play = line[0];
            need = line[2];

            ans += play_result(need) + response_value(response(play, need));

        }
    }
    cout << "Solution Part 1: " << ans << endl;
}
