// T - O(?) where ? is ...
// S - O(?) where ? is ...

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Main {

    public void wordBreak(String input, Set wordDict)
    {

    }


    public static void main(String[] args) {
        Main m = new Main();
        String [] a = { "i", "like", "sam", "sung", "samsung", "mobile", "ice",
                "cream", "icecream", "man", "go", "mango"};
        Set<String> dict = new HashSet<>(Arrays.asList(a));
        m.wordBreak("ilikesamsungmobile", dict);
    }
}