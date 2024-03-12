#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
 * listint_s *insert_node - insert number in sorted singly linked list
 * @head: head of linked list
 * @number: number to insert
 *
 * Description: singly linked list node structure
 *
 * Return: pointer to new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current;

	if (head == NULL)
		return (NULL);
	current = *head;

	while (current->next != NULL && current->next->n < number)
	{
		current = current->next;
	}

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = current->next;
	current->next = new;

	return (new);
}
