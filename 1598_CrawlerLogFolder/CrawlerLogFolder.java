
class Solution {
    public int minOperations(String[] logs) {
        // own effeciant
        int need = 0;
        for (String s : logs) {
            if (s.equals("../")) {
                if (need == 0)
                    continue;
                need--;
                continue;
            } else if (s.equals("./"))
                continue;
            else if (s.contains("/"))
                need++;
        }
        return need;
    }
}
