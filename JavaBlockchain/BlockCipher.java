import java.util.*;

public class BlockCipher {
    public static void main(String[] args) {
        
        //demo of hash function
        String statement1 = "CTEC 445";
        int hashvalue = statement1.hashCode();
        
        System.out.println("Statement is: " + statement1 + " whose hash value is: " + hashvalue);
        
        //hashing arrays
        String [] list1 = {"Mecahel", "Zack", "Cel"};
        String [] list2 = {"Mecahel", "Zack", "Cel"};
        
        int hash1 = Arrays.hashCode(list1);
        int hash2 = Arrays.hashCode(list2);
        
        System.out.println("hash 1 is : " + hash1 + " hash 2 is: " + hash2);
       
        //demonstrate a series of blocks in a chain
        ArrayList<Block> blockChain = new ArrayList<Block>();
        
        String[] initialValues = {"Mecahel has $326", "Zack has $57"};
        Block firstBlock = new Block(initialValues, 0);
        blockChain.add(firstBlock);
        System.out.println("First block is: " + firstBlock.toString());
        System.out.println("The block chain is: " + blockChain.toString());
       
        //block two
        String[] transactions = {"Mecahel spends $35", "Zack spends $56"};
        Block secondBlock = new Block(transactions, firstBlock.getBlockHash());
        blockChain.add(secondBlock);
        System.out.println("Second block is: " + secondBlock.toString());
        System.out.println("The block chain is: " + blockChain.toString());
        }
    }
