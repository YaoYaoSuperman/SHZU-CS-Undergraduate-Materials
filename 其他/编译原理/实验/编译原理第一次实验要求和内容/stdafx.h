// stdafx.h : 标准系统包含文件的包含文件,
// 或是常用但不常更改的项目特定的包含文件
//

#pragma once


#include <iostream>
#include <tchar.h>

// TODO: 在此处引用程序要求的附加头文件

#define		OK			1
#define		ERROR		-1
#define		SPACE		32
#define		RETURN		10
#define		TABLE		9
#define		NULL		0

enum	WORD_TYPE_ENUM{//单词类型枚举值
				INVALID_WORD,
				IDENTIFIER,
				NUMBER,
				CONST,
				VAR,
				PROCEDURE,
				BEGIN,
				END,
				IF,
				THEN,
				WHILE,
				DO,
				WRITE,
				READ,
				CALL,
				LEFT_PARENTHESIS,
				RIGHT_PARENTHESIS,
				COMMA,
				SEMICOLON,
				PERIOD,
				PLUS,
				MINUS,
				MULTIPLY,
				DIVIDE,
				ODD,
				EQL,
				NEQ,
				LES,
				LEQ,
				GTR,
				GEQ,
				ASSIGN
};

/*struct	WORD_STRUCT{//一个单词的数据结构
				char szName[MAX_LENGTH_OF_A_WORD];//单词名字的字符串
				enum WORD_TYPE_ENUM		eType;//单词类型枚举值
				int	nNumberValue;//数单词的值
				int	nLineNo;//在源代码文件中单词所在的行数
};*/
