#include <iostream>
#include <set>
#include <math.h>
#include <list>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;
#define rep(i, n) for (int i = 0; i < n; i++)

int gcd(int a, int b)
{
    // greatest common divisor
    int la = max(a, b);
    int sm = min(a, b);
    if (la % sm == 0)
        return sm;
    else
        return gcd(sm, la - sm);
}

int lcm(int a, int b)
{
    // least common multiple
    return a * b / gcd(a, b);
}

bool findCharInString(string str, char c)
{
    // if c not in str, str.find(c) return string::npos
    return str.find(c) != string::npos;
}

// string S
// length S.length()

// map<string, int> mp;
// loop for (auto x : mp)