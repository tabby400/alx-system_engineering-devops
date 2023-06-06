#include "lists.h"

/**
 * insert_node - function inserts a number in a singly linked list 
 *               that has been sorted
 * @head: points to the head of the singly linked list
 * @number: number to insert in the list
 *
 * Return: a pointer to inserted node otherwise NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *added;

	added = malloc(sizeof(listint_t));
	if (added == NULL)
	{
		return (NULL);
	}
	added->n = number;

	if (node == NULL || node->n >= number)
	{
		added->next = node;
		*head = added;
		return (added);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	added->next = node->next;
	node->next = added;

	return (added);
}
