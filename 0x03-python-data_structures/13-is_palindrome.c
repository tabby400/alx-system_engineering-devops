#include "lists.h"
#include <stddef.h>

void reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - function used to reverse a linked list
 *
 * @head: points to the first element in the list
 *
 * Return : points to the first node in the linked list
 */

void reverse_listint(listint_t **head)
{
	listint_t *now = *head;
	listint_t *tempnxt = NULL;
	listint_t *b4 = NULL;

	while (now)
	{
		tempnxt = now->next;
		now->next = b4;
		b4 = now;
		now = tempnxt;
	}

	*head = b4;
}

/**
 * is_palindrome - function that checks for a palindrome
 *                in a singly linked list
 * @head: points to the first element in the list
 *
 * Return: 1 if it is a palindrome, otherwise 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *behind = *head;
	listint_t *ahead = *head;
	listint_t *p = *head;
	listint_t *aftermid = NULL;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1); /*empty list is a palindrome*/
	}

	while (1)
	{
		ahead = ahead->next->next; /*twice as fast*/
		if (!ahead)
		{
			aftermid = behind->next;
			break;
		}
	if (!ahead->next)
	{
		aftermid = behind->next->next;
		break;
	}
	behind = behind->next;
	}
	reverse_listint(&aftermid);
	while (aftermid && p)
	{
		if (p->n == aftermid->n)
		{
			aftermid = aftermid->next;
			p = p->next;
		}
		else
			return (0);
	}
	if (!aftermid)
		return (1);

	return (0);
}
