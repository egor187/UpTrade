from django import template
from django.shortcuts import get_object_or_404
from ..models import TreeMenu
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


@register.inclusion_tag('TreeMenu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    local_context = {'menu_item': get_object_or_404(TreeMenu, name=menu_name, parent=None)}
    try:
        active_menu_item = TreeMenu.objects.get(url=context['request'].path)
    except ObjectDoesNotExist:
        pass
    else:
        local_context['unwrapped_menu_item_ids'] = active_menu_item.get_node_ids() + [active_menu_item.id]
    return local_context


@register.inclusion_tag('TreeMenu/menu.html', takes_context=True)
def draw_menu_item_children(context, menu_item_id):
    local_context = {'menu_item': get_object_or_404(TreeMenu, pk=menu_item_id)}
    if 'unwrapped_menu_item_ids' in context:
        local_context['unwrapped_menu_item_ids'] = context['unwrapped_menu_item_ids']
    return local_context
