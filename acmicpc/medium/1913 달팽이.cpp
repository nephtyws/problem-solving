/* from acmicpc.net, solved on 2015 */


#include <iostream>

using namespace std;

enum Case
{
    Left, Right, Up, Down
};

int main()
{
    int input;
    int target;

    cin >> input;

    cin >> target;

    int num = input * input;
    int temp = input;
    int temp2 = -1;
    int x = 0;
    int y = 0;
    int tarx, tary;
    Case dir = Down;

    int** snail = new int*[input];

    for (int i = 0; i < input; i++)
        snail[i] = new int[input];

    for (int i = 0; i < input; i++)
        for (int j = 0; j < input; j++)
            snail[i][j] = 0;

    for (int i = 0; i < input * input; i++)
    {
        snail[x][y] = num;
        if (num == target)
        {
            tarx = x + 1;
            tary = y + 1;
        }

        num--;

        switch (dir)
        {
            case Down:
                x++;
                break;
            case Right:
                y++;
                break;
            case Up:
                x--;
                break;
            case Left:
                y--;
                break;
        }

        if (dir == Down && x == temp)
        {
            dir = Right;
            x--;
            y++;
        }

        if (dir == Right && y == temp)
        {
            dir = Up;
            y--;
            x--;
        }

        if (dir == Up && x == temp2)
        {
            dir = Left;
            x++;
            y--;
            temp2++;
        }

        if (dir == Left && y == temp2)
        {
            dir = Down;
            y++;
            x++;
            temp--;
        }
    }

    for (int i = 0; i < input; i++)
    {
        for (int j = 0; j < input; j++)
            cout << snail[i][j] << " ";

        cout << endl;
    }

    cout << tarx << " " << tary << endl;
}
