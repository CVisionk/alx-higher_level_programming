#include "lists.h"

int check_cycle(listint_t *list)
{
        listint_t* current = list;
        listint_t* faster = list;
	if(!list) return 0;
	while(current != NULL && faster != NULL)
	{
		current = current->next;
		faster = faster->next->next;
		if(current == faster)
		{
			return (1);
		}
	}
	return (0);
}
