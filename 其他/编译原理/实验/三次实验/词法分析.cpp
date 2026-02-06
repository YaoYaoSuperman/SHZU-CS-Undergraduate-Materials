#include<iostream>
#include<stdio.h>
//#include<conio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>

int i, row = 0, line = 0; //
char test[1000];  //test文件中的字符(逐个字符存取)
int number[100];	//常数表 
char mark[100][5];   //标识符表


using namespace std;

//词法分析
int wordanalysis()
{
	//标识符和保留字，以大写字母和小写字母开头
    if ((test[i] >= 'A'&&test[i] <= 'Z')||(test[i]>='a'&&test[i]<='z'))  
    {
        char word[10];  //当前识别的
        //保留字表
        char pro[100][100] = { "PROGRAM", "BEGIN", "END", "VAR", "INTEGER", "WHILE",
								 "IF", "THEN", "ELSE", "DO", "PROCEDURE" ,"char",
                                "int","if","else","var" ,"return","break",
								"do","while","for","double","float","short"}; 

        int n = 0;
        word[n++] = test[i++];
        while ((test[i] >= 'A'&&test[i] <= 'Z') || (test[i] >= '0' && test[i] <= '9')||(test[i]>='a'&&test[i]<='z'))
        {
            word[n++] = test[i++];
        }
        word[n] = '\0';
        i--;

        //判断该标识符是否为保留字
        for (n = 0; n < 100; n++)
        {
            if (strcmp(word, pro[n]) == 0)
            {
                printf(">> %s\t(%d,-) 保留字\n", pro[n], n + 1);
                return 3;
            }
        }

        //判断该标识符是否在标识符表中
        int m = 0;
        if (line != 0)
        {
            int q = 0;
            while (q<line)
            {
                if (strcmp(word, mark[q++]) == 0)
                {
                    printf(">> %s\t(25,%d) 标识符\n", word, q);
                    return 3;
                }
            }
        }

        //将该标识符保存到标识符表中
        strcpy(mark[line], word);
        
        printf(">> %s\t(25, %d) 标识符\n", word, line + 1);
        line++;
        return 3;

    }
	//数字 
    else if (test[i] >= '0' && test[i] <= '9')  
    {
        char x[100];
        int n = 0;
        x[n++] = test[i++];
        
        while (test[i] >= '0' && test[i] <= '9')
        {
            x[n++] = test[i++];
        }
        x[n] = '\0';
        i--;
        int num = atoi(x); //将字符串转换成int型
        
        //判断该常数是否存在于常数表中
        if (row != 0)
        {   
            
            for(int y=0;y<row;y++)
            {
            	if(number[y]==num)
            	{
            		printf(">> %d\t(26,%d)\n", num, y + 1);
                    return 3;
				}
			}
        }
        
        //将该常数保存到标识符表中
        number[row]=num;
        

        int line = row;
        printf(">> %d\t(26,%d)\n", num, line + 1);
        row++;

        return 3;
    }
	
	//各种符号，
    else                      
    	switch (test[i])
    {
        case ' ':
        case '\n': //一行结束
            return -1;
        case '#': return 0;
        case '=':
            i++;
            if(test[i] == '=')
            {
                printf(">> ==\t(26,-)\n"); return 3;
            }else {
                i--;
                printf(">> =\t(27,-)\n"); return 3;
            }
            
        case '<':
            i++;
            if (test[i] == '=')
            {
                printf(">> <= \t(28,-)\n");
                return 3;
            }
            else if (test[i] == '>')
            {
                printf(">> <>\t(29,-)\n");
                return 3;
            }
            else
            {
                i--;
                printf(">> <\t(30,-)\n");
                return 3;
            }
        case '>':
            i++;
            if (test[i] == '=')
            {
                printf(">> >=\t(31,-)\n");
                return 3;
            }
            else
            {
                i--;
                printf(">> >\t(32,-)\n");
                return 3;
            }
        case '+': 
            i++;
            if(test[i] == '='){
                printf(">> +=\t(33,-)\n"); //00
                return 3;
            }   
            else if(test[i] == '+')
            {    
                printf(">> ++\t(37,-)\n"); //00
                return 3;
            }else
            {
                i--;
                printf(">> +\t(38,-)\n");  //00
                return 3;
            }
            return 3;
//          printf(">> +\t(33,-)\n"); return 3;
        case '-': 
            if((test[i - 1] >= '0' && test[i - 1] <= '9') || test[i+1] == '=')
            {
                cout << "'-'代表减法运算" << endl; 
            }else if(test[i-1] == '=' || test[i-1] == '(' || test[i-1] == ')' || test[i-1] == 
                ',' || test[i-1] == ';' || test[i-1] == '"' ){ 
                printf("'-'代表当前字符是负数\n");
            }else if(test[i+1] !=  '-' && test[i+1] != '=') //
                printf("'-'代表当前字符是负数\n");
            i++;
            if(test[i] == '='){
                printf(">> -=\t(36,-)\n"); //00
                return 3;
            }   
            else if(test[i] == '-')
            {    
                printf(">> --\t(37,-)\n"); //00
                return 3;
            }else
            {
                i--;
                printf(">> -\t(38,-)\n");  //00
                return 3;
            }
            return 3;
        case '*':
            i++;
            if(test[i] == '*') 
            {
                printf(">> **\t(39,-)\n"); return 3;
            }else {
                i--;
                printf(">> *\t(35,-)\n"); return 3;
            }
        case '/': 
            i++;
            if(test[i]!='/'){
                i--;
                printf(">> /\t(36,-)\n"); return 3;
            }

            else{

                while(1){
                    if(test[i++]=='\n')
                        return -1;
                }
                printf(">> //\t(37,-)\n");return 3;
            }
        case ':': printf(">> :\t(38,-)\n"); return 3;
        case ';': printf(">> ;\t(39,-)\n"); return 3;
        case '(': printf(">> (\t(40,-)\n"); return 3;
        case ')': printf(">> )\t(41,-)\n"); return 3;
        case '{': printf(">> {\t(42,-)\n"); return 3;
        case '}': printf(">> }\t(43,-)\n"); return 3;
        case '[': printf(">> [\t(44,-)\n"); return 3;
        case ']': printf(">> ]\t(45,-)\n"); return 3;
        case '|': printf(">> |\t(46,-)\n"); return 3;
        case '"': printf(">> \"\t(47,-)\n"); return 3;
        case ',': printf(">> ,\t(48,-)\n"); return 3;
        case '\'': printf(">> '\t(49,-)\n"); return 3;//单引号
        case '%': printf(">> %\t(54,-)\n"); return 3;
        case '.': printf(">> .\t(55,-)\n"); return 3;//小数点 
        case '&': 
            i++;
            if(test[i]!='&'){
                i--;
                printf(">> &\t(50,-)\n"); return 3;
            }   
            else{   
                printf(">> &&\t(51,-)\n");return 3;

            }
        case '\\': printf(">> \\\t(52,-)\n"); return 3;
    }

}

int main()
{

    int c = 0;
    int m;
    i = 0;
    FILE *fp;
    fp=fopen("test.txt","r");
    if (fp == NULL)
    {
        printf("can't open file!\n");
        exit(0);
    }

    while (!feof(fp))
    {
        test[c++] = fgetc(fp);
    }
    test[c] = '#'; //词法分析结束标志
    do
    {
        m = wordanalysis();

        switch (m)
        {
        case -1:i++; break; //对于一行的分析结束
        case 0: i++; break; //结束符号 
        case 3: i++; break; //运算符 or 分界符号
        }
    } while (m != 0);


    return 0;
}
