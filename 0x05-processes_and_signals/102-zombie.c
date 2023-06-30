#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
/**
 * infinite_while - entry
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - entry
 * Return: 0
 */
int main(void)
{
	int i;
	pid_t zombie;

	i = 0;
	while (i < 5)
	{
		zombie = fork();
		if (!zombie)
			return (0);
		printf("Zombie process created, PID: %d\n", zombie);
		i++;
	}

	infinite_while();
	return (0);
}
