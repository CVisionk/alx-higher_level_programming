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
	listint_t *current = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (current == NULL || current->n >= number)
	{
		new->next = current;
		*head = new;
		return (new);

	}

	while (current->next != NULL && current->next->n < number)
		current = current->next;

	new->next = current->next;
	current->next = new;

	return (new);
}
