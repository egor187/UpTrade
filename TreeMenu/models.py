from django.db import models


class TreeMenu(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True, unique=True)

    def __str__(self):
        return self.name

    def children(self):
        return self.treemenu_set.all()

    def get_node_ids(self):
        if self.parent:
            return self.parent.get_node_ids() + [self.parent.id]
        else:
            return []


