#include <stdio.h>

// program for factorial calculating

int main(void) {
	long res = 1;
	int end;

	scanf("%d", &end);
	for (int i = 2; i <= end; ++i)
		res *= i;

	printf("Result: %ld\n", res);
	return 0;
}