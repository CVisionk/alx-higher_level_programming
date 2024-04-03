#include "lists.h"
/**
 * palindrome - check if is palindrome with recursion
 * @left: left
 * @right: right
 *
 * Return: 1 palindrome, 0 not palindrome
 */
int palindrome(listint_t **left, listint_t *right)
{
	int response;

	if (right != NULL)
	{
		response = palindrome(left, right->next);
		if (response != 0)
		{
			response = (right->n == (*left)->n);
			*left = (*left)->next;
			return (response);
		}
		return (0);

	}
	return (1);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head of linked list
 *
 * Return: 1 palindrome, 0 not palindrome
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL)
	{
		return (0);
	}
	return (palindrome(head, *head));
}
