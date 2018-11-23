//     https://www.codeabbey.com/index/task_view/micro-life


#include <iostream>


int array1[8][8] = {

    {0, 1, 1, 0, 1, 0, 0, 0},
    {0, 1, 1, 0, 1, 0, 0, 1},
    {0, 0, 0, 0, 1, 1, 0, 1},
    {0, 0, 0, 0, 0, 1, 0, 1},
    {1, 1, 1, 0, 0, 0, 1, 0},
    {1, 0, 1, 1, 1, 1, 0, 1},
    {0, 1, 0, 0, 1, 0, 0, 0},
    {1, 1, 0, 1, 0, 0 ,1 ,0}

};  //row then column

const int row_1 = 8;
const int column_1 = 8;

void find_neighbors(int array1[row_1][column_1]){

int neighbors = 0;
for (int array_x = 0; array_x < 8; array_x++){
        for (int array_y = 0; array_y < 8; array_y++){
                for (int i = 0; i < 3; i++){
                    for (int j= 0; j < 3; j++){
                        int checking_x;
                        int checking_y;
                        if (array_x + (i - 1) < 0){
                                checking_x = 7;
                        }
                        else if (array_x + (i - 1) > 7){
                            checking_x = 0;
                        }
                        else{
                            checking_x = array_x + (i-1);
                        };

                        if (array_y + (j - 1) < 0){
                                checking_y = 7;
                        }
                        else if (array_y + (j - 1) > 7){
                            checking_y = 0;
                        }
                        else{
                            checking_y = array_y + (j-1);
                        };

                        if (checking_x != 0 && checking_y != 0){
                                if ((array1[checking_x][checking_y]) = 1){
                                    neighbors = neighbors + 1;
                                }
                        }
                }
        }

    switch (neighbors){
            case 2:
                //if 0 stays 0, if 1 stays 1
                break;
            case 3:
                //becomes 1
                array1[array_x][array_y] = 1;
                break;
            default:
                // becomes 0
                array1[array_x][array_y] = 0;
                break;
            }
        }
    }

}



void print_array(int x[row_1][column_1]){
    for (int a = 0; a < 8; a++){
                for (int b = 0; b < 8; b++){
                    std::cout << x[a][b];
            }
            std::cout << " ";
    }

}

int main()
{
find_neighbors(array1);

print_array(array1);




    return 0;
}
