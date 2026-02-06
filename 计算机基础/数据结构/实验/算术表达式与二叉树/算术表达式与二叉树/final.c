	#include<stdio.h>
	#include<stdlib.h>
	#include<string.h>
	#define TRUE 1
	#define FALSE 0
	#define OK 1
	#define ERROR 0
	#define OVERFLOW 0

	typedef int Status;
	/*二叉树结点类型*/
	typedef enum{INT,CHAR}ElemTag;/*INT为整型数据num，CHAR为字符型数据c*/
	typedef struct TElemType
	{
		ElemTag tag;/*{INT,CHAR}指示是整型还是字符型*/
		union
		{
			int num;/*tag=INT时，为整型*/
			char c;/*tag=CHAR时，为字符型*/
		};
	} TElemType;

	/*二叉树的二叉链表存储表示 */
	typedef struct BiTNode
	 {
	   TElemType data;
	   struct BiTNode *lchild,*rchild; /* 左右孩子指针 */
	 }BiTNode,*BiTree;
	typedef BiTree SElemType;/*栈SqStack的元素*/
	typedef char SElemType1; /*栈SqStack1的元素*/

	/*栈的顺序存储表示 */
	#define STACK_INIT_SIZE 10 /* 存储空间初始分配量 */
	#define STACKINCREMENT 2 /* 存储空间分配增量 */

	/*两个顺序栈*/
	typedef struct SqStack
	{
	   SElemType *base; /* 在栈构造之前和销毁之后，base的值为NULL */
	   SElemType *top; /* 栈顶指针 */
	   int stacksize; /* 当前已分配的存储空间，以元素为单位 */
	 }SqStack; /* 顺序栈 */

	typedef struct SqStack1
	{
	   SElemType1 *base; /* 在栈构造之前和销毁之后，base的值为NULL */
	   SElemType1 *top; /* 栈顶指针 */
	   int stacksize; /* 当前已分配的存储空间，以元素为单位 */
	 }SqStack1; /* 顺序栈 */

	/*顺序栈的基本操作*/
	Status InitStack(SqStack *S)
	{ /* 构造一个空栈S */
	  (*S).base=(SElemType *)malloc(STACK_INIT_SIZE*sizeof(SElemType));
	  if(!(*S).base)
	    exit(OVERFLOW); /* 存储分配失败 */
	  (*S).top=(*S).base;
	  (*S).stacksize=STACK_INIT_SIZE;
	  return OK;
	 }

	 Status StackEmpty(SqStack S)
	 { /* 若栈S为空栈，则返回TRUE，否则返回FALSE */
	   if(S.top==S.base)    return TRUE;
	   else   return FALSE;
	}

	Status Push(SqStack *S,SElemType e)
	{ /* 插入元素e为新的栈顶元素 */
	  if((*S).top-(*S).base>=(*S).stacksize) /* 栈满，追加存储空间 */
	  {
	    (*S).base=(SElemType *)realloc((*S).base,((*S).stacksize+STACKINCREMENT)*sizeof(SElemType));
	    if(!(*S).base)   exit(OVERFLOW); /* 存储分配失败 */
	    (*S).top=(*S).base+(*S).stacksize;
	    (*S).stacksize+=STACKINCREMENT;
	  }
	  *((*S).top)++=e;
	  return OK;
	}

	Status Pop(SqStack *S,SElemType *e)
	{ /* 若栈不空，则删除S的栈顶元素，用e返回其值，并返回OK；否则返回ERROR */
	  if((*S).top==(*S).base)    return ERROR;
	  *e=*--(*S).top;
	   return OK;
	}

	 Status GetTop(SqStack S,SElemType *e)
	 { /* 若栈不空，则用e返回S的栈顶元素，并返回OK；否则返回ERROR */
	   if(S.top>S.base)
	   {
		 *e=*(S.top-1);
		 return OK;
	   }
	   else
		 return ERROR;
	 }
	
	/*顺序栈的基本操作*/
	Status InitStack1(SqStack1 *S)
	{ /* 构造一个空栈S */
	  (*S).base=(SElemType1 *)malloc(STACK_INIT_SIZE*sizeof(SElemType1));
	  if(!(*S).base)
	    exit(OVERFLOW); /* 存储分配失败 */
	  (*S).top=(*S).base;
	  (*S).stacksize=STACK_INIT_SIZE;
	  return OK;
	 }

	 Status StackEmpty1(SqStack1 S)
	 { /* 若栈S为空栈，则返回TRUE，否则返回FALSE */
	   if(S.top==S.base)    return TRUE;
	   else   return FALSE;
	}

	Status Push1(SqStack1 *S,SElemType1 e)
	{ /* 插入元素e为新的栈顶元素 */
	  if((*S).top-(*S).base>=(*S).stacksize) /* 栈满，追加存储空间 */
	  {
	    (*S).base=(SElemType1 *)realloc((*S).base,((*S).stacksize+STACKINCREMENT)*sizeof(SElemType1));
	    if(!(*S).base)   exit(OVERFLOW); /* 存储分配失败 */
	    (*S).top=(*S).base+(*S).stacksize;
	    (*S).stacksize+=STACKINCREMENT;
	  }
	  *((*S).top)++=e;
	  return OK;
	}

	Status Pop1(SqStack1 *S,SElemType1 *e)
	{ /* 若栈不空，则删除S的栈顶元素，用e返回其值，并返回OK；否则返回ERROR */
	  if((*S).top==(*S).base)    return ERROR;
	  *e=*--(*S).top;
	   return OK;
	}

	 Status GetTop1(SqStack1 S,SElemType1 *e)
	 { /* 若栈不空，则用e返回S的栈顶元素，并返回OK；否则返回ERROR */
	   if(S.top>S.base)
	   {
		 *e=*(S.top-1);
		 return OK;
	   }
	   else
		 return ERROR;
	 }

	/*全局变量*/
	int save_number[51];/*在按原表达式输入形式中，输入的常量保存到数组save_number中，常量最多为50个，0单元不用*/
	char Expr_String[50];/*存放表达式的字符串*/
	
	/*以字符序列的形式输入语法正确的前缀表达式，保存到字符串string*/
	/*参数flag=0表示输出的提示信息是"请输入正确的前缀表示式："*/
	/*flag=1表示输出的提示信息为"请以表达式的原书写形式输入正确表示式："*/
	Status Input_Expr(char *string,int flag)
	{
		if(flag==0)printf("\n请输入正确的前缀表示式：");
		else printf("\n请以表达式的原书写形式输入正确表示式：");
		fflush(stdin);/*清理缓冲区*/
		gets(string);//从键盘输入一串字符串作为表达式
		if(strlen(string)==1)/*输入的表达式字符串长度为1*/
			if(string[0]=='+'||string[0]=='-'||string[0]=='*'||string[0]=='/'||string[0]=='^')/*输入的表达式只有一个运算符*/
				{ printf("\n表达式只有一个字符，为运算符，错误！");return ERROR;}
			else if((string[0]>='0'&&string[0]<'9')||(string[0]>='a'&&string[0]<='z')||(string[0]>='A'&&string[0]<='Z'))
				/*输入的表达式只有一个数字或字符*/
				{ printf("\n表达式只有一个字符！");return OK;}
			else {printf("\n输入的字符不是运算符也不是变量常量，错误！");return ERROR;}
		return OK;
	}

	/*判断字符string[i]，如果是'0'-'9'常量之间，二叉树结点存为整型；否则，存为字符型*/
	void judge_value(BiTree *E,char *string,int i)
	{
			if(string[i]>='0'&&string[i]<='9')/*为常量*/
				{(*E)->data.tag=INT;(*E)->data.num=string[i]-48;}
			else if(string[i]>=1&&string[i]<=20)/*为常量，常量存于数组save_number中*/
				{(*E)->data.tag=INT;(*E)->data.num=save_number[string[i]];}
			else/*为变量*/
				{(*E)->data.tag=CHAR;(*E)->data.c=string[i];}
	}

	/*以正确的前缀表示式并构造表达式E*/
	Status ReadExpr(BiTree *E,char *exprstring)
	{
		SqStack S;//定义顺序栈S
		int i,len;/*len为表达式的长度*/
		BiTree p,q;
		(*E)=(BiTree)malloc(sizeof(BiTNode));/*申请二叉树的根结点的空间*/
		(*E)->lchild=NULL;
		(*E)->rchild=NULL;
		len=strlen(exprstring);/*len赋值为表达式的长度*/
		if(len==1)/*表达式长度为1时，二叉树只有根结点*/	
			judge_value(E,exprstring,0);/*将exprstring[0]存入二叉树的结点中*/
		else 
		{
			judge_value(E,exprstring,0);/*将exprstring[0]存入二叉树的结点中*/
			InitStack(&S);/*初始化栈*/
			q=(*E);
			Push(&S,q);/*入栈*/
			Push(&S,q);/*入栈，根结点入栈两次是为判断先序输入的表达式是不是正确的表达式*/
			for(i=1;i<len&&!StackEmpty(S);i++)//
			{
				p=(BiTree)malloc(sizeof(BiTNode));
				judge_value(&p,exprstring,i);/*将exprstring[i]存入二叉树的结点中*/
				p->lchild=NULL;
				p->rchild=NULL;
				if(exprstring[i]=='+'||exprstring[i]=='-'||exprstring[i]=='*'||exprstring[i]=='/'||exprstring[i]=='^')
				{/*为运算符，运算符入栈，左孩子不空，向左孩子走，否则，如果右孩子不空，向右孩子走*/
					if(!q->lchild)	{q->lchild=p;Push(&S,p);q=p;}
					else	{q->rchild=p;Push(&S,p);q=p;}
				}
				else/*不是运算符，运算符出栈*/
				{
					if(!q->lchild)	{q->lchild=p;Pop(&S,&q);}
					else	{q->rchild=p;Pop(&S,&q);}
				}
			}
			if(StackEmpty(S)&&i>=len)	return OK;/*栈空且i>=len，说明输入的表达式是正确的*/
			else	/*输入的表达式是错误的*/
			{
				printf("\n输入的表达式有误！");
				return ERROR;
			}
		}
	}

	/*如果两个字符是运算符，比较两个运算符的优先级，c1比c2优先，返回OK，否则返回ERROR*/
	Status Pri_Compare(char c1,char c2)
	{
		if((c1=='^'||c1=='*'||c1=='-'||c1=='+'||c1=='/')&&(c2=='^'||c2=='*'||c2=='-'||c2=='+'||c2=='/'))
		{/*c1和c2为运算符*/
			if(c1=='^')/*c1为指数运算符，则当c2不为'^'时，c1比c2优先*/
			{
				if(c2!='^') return OK;
				else return ERROR;
			}
			else if(c1=='*'||c1=='/')/*c1为乘法或除法运算符，则当c2为'+'或'-'，c1比c2优先*/
			{
				if(c2=='^'||c2=='*'||c2=='/') return ERROR;
				else return OK;
			}
			else return ERROR;/*其余，c1不比c2优先*/
		}
		else return ERROR;/*c1和c2不是运算符*/
	}
	
	/*用带括弧的中缀表达式输出表达式*/
	void WriteExpr(BiTree E)
	{
		if(E)/*树不为空*/
		{	/*先递归左子树*/
			if(E->lchild&&E->lchild->data.tag==CHAR)/*E的左孩子不为空，且左孩子为字符*/
			{
				if(Pri_Compare(E->data.c,E->lchild->data.c))/*E->data.c比E->lchild->data.c优先*/
						{printf("(");
				         WriteExpr(E->lchild);
				         printf(")");}/*带括弧输出左子树*/
				else WriteExpr(E->lchild);/*否则，不带括弧输出左子树*/
			}
			else WriteExpr(E->lchild);/*否则，输出左子树*/
			/*访问输出根结点的值*/
			if(E->data.tag==INT){printf("%d",E->data.num);}
			else  printf("%c",E->data.c);
			/*后递归右子树*/
			if(E->rchild&&E->rchild->data.tag==CHAR)/*E的右孩子不为空，且右孩子为字符*/
			{
				if(Pri_Compare(E->data.c,E->rchild->data.c))/*E->data.c比E->rchild->data.c优先*/
						{printf("(");WriteExpr(E->rchild);printf(")");}/*带括弧输出右子树*/
				else WriteExpr(E->rchild);/*否则，不带括弧输出右子树*/
			}
			else WriteExpr(E->rchild);/*否则，输出右子树*/
		}
	}

	/*实现对表达式中的所有变量V的赋值(V=c)，参数flag为表示是否赋值过的标志*/
	void Assign(BiTree *E,char V,int c,int *flag)
	{
		if(*E)
		{
			if((*E)->data.tag==CHAR&&(*E)->data.c==V)/*如果找到要赋值的变量，赋值*/
				{(*E)->data.tag=INT;(*E)->data.num=c;*flag=1;}
			Assign(&((*E)->lchild),V,c,flag);/*递归左子树*/
			Assign(&((*E)->rchild),V,c,flag);/*递归左子树*/
		}
	}

	/*指数运算函数，底数为x，指数为exp*/
	long power(int x,int exp)
	{
		long result;
		int i;
		for(i=1,result=1;i<=exp;i++)
			result*=x;
		return result;
	}

	/*运算符运算求值，参数opr1,opr2为常量，opr为运算符，根据不同的运算符，实现不同的运算，返回运算结果*/
	long Operate(int opr1,char opr,int opr2)
	{
		long result;
		switch(opr)
		{
			case '+':/*加法*/
				result=opr1+opr2;
				return result;break;
			case '-':/*减法*/
				result=opr1-opr2;
				return result;break;
			case '*':/*乘法*/
				result=opr1*opr2;
				return result;break;
			case '/':/*除法，除法是在整型类型上的除法*/
				result=opr1/opr2;
				return result;break;
            
			case '^':/*指数运算*/
				result=power(opr1,opr2);
				return result;break;
			default:break;
		}
	}
	
	/*检查表达式是否还存在没有赋值的变量，以便求算数表达式的值*/
	Status Check(BiTree E)
	{
		if(E&&E->data.tag==CHAR)/*树不为空*/
		{			
			if(E->data.c!='*'&&E->data.c!='^'&&E->data.c!='-'&&E->data.c!='+'&&E->data.c!='/')
				{printf("\n表达式中仍存在变量没有赋值！没法求出表达式的值！");return ERROR;}
				/*存在变量，提示信息，后返回ERROR*/
			if(Check(E->lchild))/*递归左子树*/
				Check(E->rchild);/*递归右子树*/	
		}
	}

	/*对算术表达式求值*/
	long Value(BiTree E)
	{
		if(E)/*树不为空*/
		{
			if(!E->lchild&&!E->rchild&&E->data.tag==INT) return (E->data.num);
			/*结点的左孩子和右孩子为空，为叶子结点，返回结点的值*/
			return Operate(Value(E->lchild),E->data.c,Value(E->rchild));
			/*运算求值，后根遍历的次序对表达式求值，其中参数递归调用了Value()函数求左子树的值和右子树的值*/
		}
	}
	
	/*构造一个新的复合表达式*/
	void CompoundExpr(char P,BiTree *E1,BiTree E2)
	{
		BiTree E;
		E=(BiTree)malloc(sizeof(BiTNode));/*申请一个结点存放运算符P*/
		E->data.tag=CHAR;
		E->data.c=P;/*申请到的结点值为P*/
		E->lchild=(*E1);/*结点的左孩子为E1*/
		E->rchild=E2;/*结点的右孩子为E2*/
		(*E1)=E;/*(*E1)为根结点*/
		printf("\n表达式E复合成功！其表达式变为：\n");
		WriteExpr(E);/*输出复合好的表达式*/
	}

	/*以表达式的原书写形式输入，表达式的原书写形式字符串string变为字符串pre_expr*/
	/*后调用reversal_string()函数反转得到前缀表达式pre_expr*/
	Status Read_Inorder_Expr(char *string,char *pre_expr)
	{
		
		int i,j,len,char_number=1;/*len表示字符串string的长度，char_number是记录数组save_number[]的个数*/
		int number;/*保存大于9的常量*/
		char c,c1;
		SqStack1 S;/*栈定义*/
		InitStack1(&S);/*初始栈*/
		Push1(&S,'#');/*先将字符'#'入栈，用来表示作为栈的最底一个元素*/
		len=strlen(string);/*len为字符串string的长度*/
		c=string[len-1];/*从字符串的最后一个字符开始向前扫描*/
		i=len-1;
		while(!StackEmpty1(S)&&i>=0)/*栈不为空且i大于等于0*/
		{
			if(c=='(')/*字符为'('*/
			{
				Pop1(&S,&c);/*出栈，赋值给c*/
				while(c!=')')/*假如c不为')',出栈*/
				{
					*pre_expr++=c;
					if(!StackEmpty1(S)&&GetTop1(S,&c1)&&c1!='#') Pop1(&S,&c);
					else {printf("\n输入的表达式有误!");return ERROR;}
				}
			}
			else if(c==')')/*字符为')'，入栈*/
			{
				Push1(&S,c);
			}
			else if(c>='0'&&c<='9')/*字符为'0'-'9'之间，循环扫描string前一个字符，后确定常量的大小*/
			{
				number=c-48;/*number为第一个常量字符的ASCII码-48*/
				for(c1=string[i-1],j=1;(c1>='0'&&c1<='9')&&i>=0;j++,i--)/*循环扫描string前一个字符，求出常量后

赋给number*/
				{
					number=(c1-48)*power(10,j)+number;/*number为扫描到的常量*/
					c1=string[i-2];
				}
				save_number[char_number]=number;/*将number存入到数组save_number中，下标为

char_number*/
				*pre_expr++=char_number++;
			}
			else if((c>='a'&&c<='z')||(c>='A'&&c<='Z'))/*字符为'a'-'z'或'A'-'Z'之间的变量*/
			{/*string下一个字符不能为常量或变量，否则，出错*/
				if((string[i-1]>='0'&&string[i-1]<='9')||(string[i-1]>='A'&&string[i-1]<='Z')||(string[i-1]>='a'&&string[i-1]<='z'))
					{printf("\n输入的表达式有误！");return ERROR;}
				else	*pre_expr++=c;
			}
			else if(c=='*'||c=='/')/*字符为运算符'*'或'/'*/
			{
				while(GetTop1(S,&c1)&&(c1=='^'))/*将c与栈顶的字符c1比较优先级*/
					{Pop1(&S,&c1);*pre_expr++=c1;}/*如果c1比c优先，出栈*/
				Push1(&S,c);/*入栈字符c*/
			}
			else if(c=='+'||c=='-')/*字符为运算符'+'或'-'*/
			{
				while(GetTop1(S,&c1)&&(c1=='^'||c1=='*'||c1=='/'))/*将c与栈顶的字符c1比较优先级*/
					{Pop1(&S,&c1);*pre_expr++=c1;}/*如果c1比c优先，出栈*/
				Push1(&S,c);/*入栈运算符c*/
			}
			else if(c=='^')/*字符为运算符'^'*/
			{
				Push1(&S,c);/*入栈运算符'^'*/
			}
			else {printf("\n输入的表达式有误！");return ERROR;}/*其他字符，错误，返回ERROR*/
			i--;/*下一个字符*/
			if(i>=0) c=string[i];/*i不小于0，c=string[i]循环下一个字符*/
			else /*否则，将清空栈*/
				while(!StackEmpty1(S)&&GetTop1(S,&c1)&&c1!='#')	{Pop1(&S,&c);*pre_expr++=c;}
		}
		Pop1(&S,&c);/*将'#'出栈*/
		*pre_expr='\0';/*字符串结束符*/
		if(i<0&&StackEmpty1(S))return OK;
		else return ERROR;
	}
	
	/*将字符串exprstring反转过来*/
	void reversal_string(char *exprstring)
	{
		int len,i,j;
		char temp;
		len=strlen(exprstring);/*len为exprstring的长度*/
		for(i=0,j=len-1;i<j;i++,j--)/*字符串前后两个字符对换*/
		{
			temp=exprstring[i];
			exprstring[i]=exprstring[j];
			exprstring[j]=temp;
		}
	}
	
//判断是否操作符   
int isoperator(char c)  
{  
    switch(c)  
    {  
        case '+': return TRUE;
        case '-': return TRUE;
        case '*': return TRUE;
        case '/': return TRUE; 
        case '^': return TRUE;  
        default: return FALSE;  
    }  
}	

	/*主菜单*/
	char menu()
	{
		char choice;
		printf("\n\t****************************************");
		printf("\n\t***********请选择要进行的操作***********");
		printf("\n\t     1 >>>输入正确的前缀表达式");
		printf("\n\t     2 >>>带括弧的中缀表示式输出");
		printf("\n\t     3 >>>对变量进行赋值");
		printf("\n\t     4 >>>对算数表达式求值");
		printf("\n\t     5 >>>构造一个新的复合表达式（输入中缀表达式即可）");
		printf("\n\t     0 >>>退出");
		printf("\n\t****************************************");
		printf("\n\t请输入你的选择(数字)>>>>>");
		choice=getchar();
		return choice;
	}
	/*主函数*/
	int main()
	{
		
		BiTree E,E1;/*两个表达式E和E1*/
		int flag=0;/*表达式E构造标志，为0表示未构造，为1表示已构造*/
		long result;/*保存算数表达式运算结果*/
		char V,P;//V被赋值，P为符合表达式运算符
		int c;//C要赋值
		char string[30];//字符串
		while(1)
		{	system("cls");//清屏
			switch(menu())		
			{
				case '1':/*1 >>>输入正确的前缀表达式*/
					printf("\n\t*************************输入提示信息************************");
					printf("\n\t输入正确的前缀表达式的要求：");
					printf("\n\t\t【变量】  a-z或A-Z");
					printf("\n\t\t【常量】  0-9，不能超过9");
					printf("\n\t\t【运算符】  +,-,*,/,^(乘幂)");
	                printf("\n\t\t例0;5;+a*53");
					printf("\n\t请输入正确的前缀表达式，后按回车键存入缓冲区，否则可能会出错！");
					printf("\n\t*************************************************************");
					if(Input_Expr(Expr_String,0))//在flag=0时，初始输入
						if(ReadExpr(&E,Expr_String))//前缀读入并构造E
							{flag=1;
						     printf("\n表达式构造成功！\n输入的带括弧的中缀表达式：");
						     WriteExpr(E);}/*带括弧的中缀表示式输出 ，递归实现*/
					getchar();
					break;
				case '2':/*2 >>>带括弧的中缀表示式输出*/
					printf("\n\t********************输出说明信息***********************************");
					printf("\n\t输出带括弧的中缀表达式：");
					printf("\n\t【1】如果表达式已经构造成功的，输出表达式；");
					printf("\n\t【2】如果表达式还未构造成功的，请返回主菜单选择构造表达式；");
					printf("\n\t【注】其中要注意的是，可能有一些表达式构造时没有办法判断为有误，");
					printf("\n\t      如果输出不是你想得到的，说明你之前输入的表达式有误，请重新构造！");
					printf("\n\t********************************************************************");
					if(flag==1)
					{printf("\n带括弧的中缀表达式为：");
					  WriteExpr(E);
					}
					else printf("\n表达式未构造成功！请重新构造成功的表达式！");
					getchar();
					break;
				case '3':/*3 >>>对变量进行赋值*/
					printf("\n\t********************赋值操作说明信息***********************************");
					printf("\n\t赋值操作：实现对表达式中的某一个变量V的赋值，即使V=C，C为一整数");
					printf("\n\t  【1】根据输出的表达式，输入要赋值的变量V，只能输入一个字符，否则出错");
					printf("\n\t  【2】输入要将变量V赋值为的整数C，只能是整数，否则出错");
					printf("\n\t  【注】如果表达式未构造，请回到主菜单选择构造表达式");
					printf("\n\t***********************************************************************");
					if(flag==1)
					{
						int Assign_flag=0;
						printf("\n表达式E为：");
						WriteExpr(E);
						fflush(stdin);/*清理缓冲区*/
						printf("\n请输入要赋值的字符：");		
						V=getchar();
						printf("请输入要将赋值为：");	
						scanf("%d",&c);
						Assign(&E,V,c,&Assign_flag);//赋值并改变标志
						if(Assign_flag)
						{printf("\n赋值成功！\n赋值后的表达式为：");WriteExpr(E);}
						else printf("\n表达式里没有%c这个变量！",V);
					}
					else printf("\n表达式未构造成功！请构造成功的表达式！");
					getchar();
					break;
				case '4':/*4 >>>对算数表达式求值*/
					printf("\n\t********************算数表达式求值说明信息************************");
					printf("\n\t 【注】如果表达式还有变量未赋值，即表达式不是算数表达式");
					printf("\n\t       不能求出表达式的值，请回到主菜单选择赋值操作，后再求值");
					printf("\n\t******************************************************************");
					if(flag==1)
						{
							printf("\n算数表达式：");WriteExpr(E);
							if(Check(E)) //检查是否全赋值
							{result=Value(E);printf("\n求算数表达式的值:\t");WriteExpr(E);printf("=%ld",result);}
						}
					else printf("\n表达式未构造成功！请构造成功的表达式！");
					getchar();
					break;
				case '5':/*5 >>>构造一个新的复合表达式*/
					printf("\n\t*****************构造新的复合表达式说明信息***************************");
					printf("\n\t  【1】构造一个新的表达式E1，采用表达式的原书写形式输入");
					printf("\n\t  【2】构造表达式E1成功后，输入要复合表达式E和E1的操作运算符(+,-,*,/,^)");
					printf("\n\t  【注】如表达式E未构造，不能复合表达式；如构造表达式E1错误，复合失败");
					printf("\n\t***********************************************************************");
					if(flag==1)
					{
						printf("\n表达式E1为：");
						WriteExpr(E);
						printf("\n请构造新的表达式E2:");
						fflush(stdin);/*清理缓冲区*/
						if(Input_Expr(string,1))//标志为1，输入字符串
						{
						 	if(Read_Inorder_Expr(string,Expr_String))//入栈
							{
								reversal_string(Expr_String);//反转
								if(ReadExpr(&E1,Expr_String))
								{
									flag=1;printf("\n表达式E2构造成功！");WriteExpr(E1);
									printf("\n请输入要构造新的复合表达式的操作运算符>>>");
									P=getchar();
									while(P!='*'&&P!='/'&&P!='+'&&P!='-'&&P!='^')
									{
										fflush(stdin);/*清理缓冲区*/
										printf("\n输入的操作运算符有误！请重新输入>>>");
										P=getchar();
									}
									CompoundExpr(P,&E,E1);
								}
								else printf("\n复合新的表达式失败！请按任意键返回主菜单！");
							}
						}
					}
					else printf("\n表达式未构造成功！请构造成功的表达式！");
					getchar();
					break;
		
				case '0':/*0 >>>退出*/
					printf("\n请按任意键退出！");
					getchar();
					exit(0);
				default :
					printf("\n输入有误！请按任意键回到主菜单重新选择！");
					getchar();
					break;
			}
		}
	}
