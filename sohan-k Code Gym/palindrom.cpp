//Important 1381114114111831

#include<iostream>
#include<bits/stdc++.h> 
using namespace std;

#include <string>
#include <sstream>

namespace patch
{
    template < typename T > std::string to_string( const T& n )
    {
        std::ostringstream stm ;
        stm << n ;
        return stm.str() ;
    }
}

string findSum(string str1, string str2) 
{ 
  
    // Take an empty string for storing result 
    string str = ""; 
  
    // Calculate length of both string 
    int n1 = str1.length(), n2 = str2.length(); 
    int diff = n2 - n1; 
  
    // Initially take carry zero 
    int carry = 0; 
  
    // Traverse from end of both strings 
    for (int i=n1-1; i>=0; i--) 
    { 

        int sum = ((str1[i]-'0') + 
                   (str2[i+diff]-'0') + 
                   carry); 
        str.push_back(sum%10 + '0'); 
        carry = sum/10; 
    } 
  

    for (int i=n2-n1-1; i>=0; i--) 
    { 
        int sum = ((str2[i]-'0')+carry); 
        str.push_back(sum%10 + '0'); 
        carry = sum/10; 
    } 
  
    // Add remaining carry 
    if (carry) 
        str.push_back(carry+'0'); 
  
    // reverse resultant string 
    reverse(str.begin(), str.end()); 
    return str; 
}  	

string multiply(string num1, string num2) 
{ 
    int len1 = num1.size(); 
    int len2 = num2.size(); 
    if (len1 == 0 || len2 == 0) 
    return "0"; 
  
    // will keep the result number in vector 
    // in reverse order 
    vector<int> result(len1 + len2, 0); 
  
    // Below two indexes are used to find positions 
    // in result.  
    int i_n1 = 0;  
    int i_n2 = 0;  
      
    // Go from right to left in num1 
    for (int i=len1-1; i>=0; i--) 
    { 
        int carry = 0; 
        int n1 = num1[i] - '0'; 
  

        i_n2 = 0;  
          
        // Go from right to left in num2              
        for (int j=len2-1; j>=0; j--) 
        { 
            // Take current digit of second number 
            int n2 = num2[j] - '0'; 
  
            int sum = n1*n2 + result[i_n1 + i_n2] + carry; 
  
            // Carry for next iteration 
            carry = sum/10; 
  
            // Store result 
            result[i_n1 + i_n2] = sum % 10; 
  
            i_n2++; 
        } 
  
        // store carry in next cell 
        if (carry > 0) 
            result[i_n1 + i_n2] += carry; 
  
        // To shift position to left after every 
        // multiplication of a digit in num1. 
        i_n1++; 
    } 
  
    // ignore '0's from the right 
    int i = result.size() - 1; 
    while (i>=0 && result[i] == 0) 
    i--; 
  
    // If all were '0's - means either both or 
    // one of num1 or num2 were '0' 
    if (i == -1) 
    return "0"; 
  
    // generate the result string 
    string s = ""; 
      
    while (i >= 0) 
        s += patch::to_string(result[i--]); 
  
    /*delete(&len1);
    delete(&len2);
    delete(&i_n1);
    delete(&i_n2);
    delete(&i);*/

    return s; 
}

int isPalindrome(string str) 
{ 
    // Start from leftmost and rightmost corners of str 
    int l = 0; 
    int h = str.length() - 1; 
  
    // Keep comparing characters while they are same 
    while (h > l) 
    { 
        if (str[l++] != str[h--]) 
        { 
            return 0; 
        } 
    } 
/*    delete(&h);
    delete(&l);*/
    return 1;
}

//100000000000000000000000000000000
//10000000000000000000000000
int main(){
	
	cout<<"jhsr"<<endl;
	cout<<"iesjf"<<endl;
    cout<<"starting......"<<endl;
    string i = "138111149";
    string prime = "10000019";
    string  ans;
    int counter = 0;

    while( i != "10000000000000000000000000" ){
        ans = multiply(i, prime);
        if(isPalindrome(ans)){
            cout<<ans<<endl;
            counter++;
        }
        i = findSum("1",i);
    }
    cout<<endl<<"Total freaking palindroms are "<<counter<<endl;

	return 0;
}