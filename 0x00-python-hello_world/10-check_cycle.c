#include  "lists.h"

/**
 * check_cycle - function that checks if a singly linked
 *                list has a cycle in it
 * @list: the singly linked list to be looked at
 *
 * Return: 0 if there is no cycle otherwise 1 if it exists
 */

int check_cycle(listint_t *list)
{

	listint_t *snail = list;
	listint_t *mouse = list;

	if (list == NULL)
	{
		return (0);
	}

	while (snail && mouse && mouse->next)
	{
		snail = snail->next;
		mouse = mouse->next->next;
		if (snail == mouse)
			return (1);
	}

	return (0);
}
