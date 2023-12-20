# C#基础知识  
### 数据类型 
- sbyte(System.sbyte):signed char
- byte:unsigned char
- short
- ushort
- int
- uint
- long
- ulong  
- char:0-65535之间的整数  

### 基本数据类型的使用以及格式化输出  
```csharp
static void main(String[] args){
	int a;
	string b;
	a = 17;
	b = "hello";
	Console.WriteLine($"{a},oops,{b}");//格式化输出
}
```  

### 运算符
- 若要一字不变得使用字符串,则需要在最前面加一个@。如以下两者是等价的:  
```Csharp
@"C:\windows\cmd.exe"  
"C:\\windows\\cmd.exe"
```  

C#可以使用++运算符。  

C#和py类似,读入的是字符串而不是数字  

### 名称空间  
默认情况下,C#代码在全局名称空间中。  

### C#类型转换  
- 显式转换  
- 隐式转换
```C#
byte a;
short b = 9;
a = (byte)b;//显式转换方法之一  
Convert.ToDouble("123");//方法之二,适用于字符串
```  

### 其他变量类型  
- 枚举  
```C#
//定义了一个枚举
enum Gender{
	male,
	female
}

Gender a;//声明了这个类型的变量  
a = Gender.male;//赋值
```

- 结构struct
与C的结构体相同  

- 数组  
```C#
int [] myArray;
myArray[10] = 5;

int[] myIntArray = new int[5] {1,2,3,4,5};//元素的个数必须与数组大小相匹配
```
和C一样,C#数组的大小不能动态定义。

访问数组所有成员:  
```C#
String[] friends = {"Tom","Jerry"};
foreach(string friendname in friends){
	Console.WriteLine(friendname);
}
```  
- 多维数组  
```C#
double[,] a = {
	{1,2,3,4},
	{5,6,7,8},
	{9,10,11,12}
}
```

###  字符串的处理  
```C#
string a = "Hello";
char[] b = a.ToCharArray;
string c = user.ToLower(a);//转小写
```

# 面向对象
- seal类:类似于final  
```C#
//继承语法
public class MyClass : MyBase{
	...
}
```
派生类的访问性不能高于基类。  
在继承树中,所有类的基类是System.Object  
