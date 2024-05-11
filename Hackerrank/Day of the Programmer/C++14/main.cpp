#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'dayOfProgrammer' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts INTEGER year as parameter.
 */

string dayOfProgrammer(int year) {
    string date;
    if (year == 1918) {
        // In 1918, Russia transitioned from Julian to Gregorian calendar, February had 14 days omitted.
        // So the 256th day is 26th September, not the usual 12th/13th.
        date = "26.09." + to_string(year);
    } else if ((year < 1918 && year % 4 == 0) || 
               // Julian calendar: Any year divisible by 4 is a leap year.
               (year > 1918 && (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0)))) {
        // Gregorian calendar: Leap years are either divisible by 400 or divisible by 4 but not by 100.
        // For leap years, the 256th day is 12th September.
        date = "12.09." + to_string(year);
    } else {
        // For non-leap years, the 256th day is 13th September.
        date = "13.09." + to_string(year);
    }
    return date;

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string year_temp;
    getline(cin, year_temp);

    int year = stoi(ltrim(rtrim(year_temp)));

    string result = dayOfProgrammer(year);

    fout << result << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
