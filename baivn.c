#include<stdio.h>
int main() {
	int a;
	printf("nhap vao so giay la:");
	scanf("%d", &a);
	printf("%d giay = %d gio %d phut %d giay",a, a / 3600, a % 3600 / 60, a % 3600 % 60);
 


}
