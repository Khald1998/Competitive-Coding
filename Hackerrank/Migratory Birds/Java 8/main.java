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
     * Complete the 'migratoryBirds' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts INTEGER_ARRAY arr as parameter.
     */

    public static int migratoryBirds(List<Integer> arr) {
        Map<Integer, Integer> typeCount = new HashMap<>();
        for (int birdType : arr) {
            typeCount.put(birdType, typeCount.getOrDefault(birdType, 0) + 1);
        }

        int maxCount = Collections.max(typeCount.values());
        int mostCommonType = Integer.MAX_VALUE;

        for (Map.Entry<Integer, Integer> entry : typeCount.entrySet()) {
            int birdType = entry.getKey();
            int count = entry.getValue();
            if (count == maxCount && birdType < mostCommonType) {
                mostCommonType = birdType;
            }
        }

        return mostCommonType;

    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int arrCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> arr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Integer::parseInt)
            .collect(toList());

        int result = Result.migratoryBirds(arr);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
