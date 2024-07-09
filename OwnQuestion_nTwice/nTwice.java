
public class Main
{
    public static String nTwice(String str, int num){
        if (num*2 > str.length()) return "-1";
        if (num*2 == str.length()) return str;
        return str.substring(0,num) + str.substring(str.length()-num);
    }
	public static void main(String[] args) {
	    String[][] testcases = {{"Hello","2"},
	                  {"Chocolate","3"},
	                  {"Chocolate","1"}};
	    for(String[] test : testcases){
	        System.out.println(nTwice(test[0],Integer.parseInt(test[1])));
	    }
	}
}
