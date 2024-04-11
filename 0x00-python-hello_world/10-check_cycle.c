#include "lists.h"
/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t *faster = list;

	if (!list)
		return (0);
	while (current != NULL && faster != NULL)
	{
		current = current->next;
		faster = faster->next->next;
		if (current == faster)
		{
			return (1);
		}
	}
	return (0);
}
