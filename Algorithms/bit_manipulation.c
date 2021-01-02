//1. Count the no. of ones in the binary representation of the given number
int count_one(void)
{
    int n = 5;
    int count;
    while(n)
    {
        n = n&(n-1);
        count ++;
    }
    return count;
}

