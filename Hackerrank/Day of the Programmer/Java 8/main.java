import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'dayOfProgrammer' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts INTEGER year as parameter.
     */

    public static String dayOfProgrammer(int year) {
    // Write your code here
        // The day of the programmer is the 256th day of the year.
        // Normally, in the Gregorian calendar, it falls on September 12th on leap years and September 13th on non-leap years.
        // In the Julian calendar, which was used in Russia until 1918, leap years are any year divisible by 4.
        // After Russia's switch to the Gregorian calendar, leap years are years that are either divisible by 400,
        // or divisible by 4 but not by 100.

        if (year == 1918) {
            // Special case for the year 1918, because Russia transitioned from the Julian to the Gregorian calendar,
            // so the February 14th was the 32nd day of the year in Russia.
            // That means the 256th day is calculated by adding 215 days to February 14, landing on September 26.
            return "26.09." + year;
        } else if ((year < 1918 && year % 4 == 0) ||
                   (year > 1918 && (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0)))) {
            // Leap year calculation for both calendars.
            // If it is a leap year, the 256th day of the year is September 12th.
            return "12.09." + year;
        } else {
            // For non-leap years, the 256th day of the year is September 13th.
            return "13.09." + year;
        }

    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int year = Integer.parseInt(bufferedReader.readLine().trim());

        String result = Result.dayOfProgrammer(year);

        bufferedWriter.write(result);
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
